from aineko.core.node import AbstractNode
import tempfile
import bandit
import os


class CoolNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        """Optional; used to initialize node state."""
        self.state = params.get("initial_state", 0)

    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        # Implement cool functionality here
        pass

    def evaluate_python_code(self, python_code):
        issues_list = []
        try:
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w") as tmpfile:
                tmpfile.write(python_code)

            b_mgr = bandit.manager.BanditManager(bandit.config.BanditConfig(), 'file')
            b_mgr.discover_files([tmpfile.name], None)
            b_mgr.run_tests()

            results = b_mgr.get_issue_list(sev_level=bandit.constants.LOW, conf_level=bandit.constants.LOW)

            tmpfile.close()
            os.remove(tmpfile.name)

            return {'result': 'PASS', 'issues': results} if not results else {'result': 'FAIL', 'issues': results}
        except Exception as err:
            return {'result': 'ERROR', 'message': str(err)}