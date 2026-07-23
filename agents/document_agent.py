class DocumentAgent(BaseAgent):

    def execute(self, case):

        docs = DocumentTool.verify(case)

        return case