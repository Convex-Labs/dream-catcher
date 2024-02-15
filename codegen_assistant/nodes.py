from aineko.core.node import AbstractNode
from typing import Optional
import openai
import os
import tempfile
import bandit

openai.api_key = os.getenv('OPENAI_API_KEY')


class PromptHandler(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        prompt = self.consumers['user_prompt'].next()
        response = openai.Completion.create(
            engine='davinci-codex',
            prompt=prompt,
            max_tokens=150
        )
        code = response.choices[0].text.strip()
        self.producers['generated_code'].produce(code)


class CodeValidator(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        code = self.consumers['generated_code'].next()
        with tempfile.NamedTemporaryFile(suffix='.py', mode='w') as tmp:
            tmp.write(code)
            tmp.flush()
            b_mgr = bandit.manager.BanditManager(bandit.config.BanditConfig(), 'file')
            b_mgr.discover_files([tmp.name], None)
            b_mgr.run_tests()
            issues = b_mgr.get_issue_list(sev_level=bandit.constants.LOW, conf_level=bandit.constants.LOW)
        if issues:
            self.producers['validation_result'].produce({'code': code, 'valid': False, 'issues': issues})
        else:
            self.producers['validation_result'].produce({'code': code, 'valid': True})