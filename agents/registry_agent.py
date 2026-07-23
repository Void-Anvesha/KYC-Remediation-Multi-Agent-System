class RegistryAgent(BaseAgent):

    def execute(self, case):

        registry = RegistryTool.search(case)

        case.evidence.append(...)

        return case