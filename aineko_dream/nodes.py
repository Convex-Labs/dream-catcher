from aineko.core.node import AbstractNode
import os
import openai
import tempfile
import bandit
from github import Github, Auth
import pandas as pd


class GitHubDocFetcher(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.access_token = os.environ.get("GITHUB_ACCESS_TOKEN")
        self.organization = params.get("organization")
        self.repo = params.get("repo")
        self.branch = params.get("branch")
        self.file_path = params.get("file_path")
        auth = Auth.Token(token=self.access_token)
        self.github_client = Github(auth=auth)
        self.emit_new_document()

    def _execute(self, params: Optional[dict] = None) -> Optional[bool]:
        message = self.consumers["github_event"].consume()
        if message is None:
            return
        self.log("Received event from GitHub, fetching latest document.")
        self.emit_new_document()

    def emit_new_document(self) -> None:
        repo = self.github_client.get_repo(f"{self.organization}/{self.repo}")
        contents = repo.get_contents(self.file_path, ref=self.branch)
        github_contents = {f.path: f.decoded_content.decode("utf-8") for f in contents}
        self.producers["document"].produce(github_contents)
        self.log(f"Fetched documents for {self.organization}/{self.repo} branch {self.branch}")


class OpenAIClient(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.model = params.get("model")
        self.max_tokens = params.get("max_tokens")
        self.temperature = params.get("temperature")
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def _execute(self, params: Optional[dict] = None) -> Optional[bool]:
        message = self.consumers["generated_prompt"].consume()
        if message is None:
            return
        messages = message["message"]["chat_messages"]
        response = openai.ChatCompletion.create(
            messages=messages,
            stream=False,
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        message["message"]["chat_messages"].append({
            "role": "assistant",
            "content": response.choices[0].message.content,
        })
        self.producers["llm_response"].produce(
            message["message"]["chat_messages"]
        )


class SecurityEvaluation(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> None:
        message = self.consumers["llm_response"].consume()
        if message is None:
            return
        python_code = message["message"]
        issues_list = []
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w") as tmpfile:
            tmpfile.write(python_code)
        b_mgr = bandit.manager.BanditManager(bandit.config.BanditConfig(), 'file')
        b_mgr.discover_files([tmpfile.name], None)
        b_mgr.run_tests()
        results = b_mgr.get_issue_list(
            sev_level=bandit.constants.LOW,
            conf_level=bandit.constants.LOW,
        )
        tmpfile.close()
        os.remove(tmpfile.name)
        if results:
            self.producers["evaluation_result"].produce(results)
