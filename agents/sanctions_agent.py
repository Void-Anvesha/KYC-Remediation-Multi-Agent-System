class SanctionsAgent(BaseAgent):

    def execute(self, case):

        sanctions = SanctionsTool.search(case)

        return case