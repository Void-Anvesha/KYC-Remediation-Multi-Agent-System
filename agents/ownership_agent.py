class OwnershipAgent(BaseAgent):

    def execute(self, case):

        owners = OwnershipTool.get(case)

        return case