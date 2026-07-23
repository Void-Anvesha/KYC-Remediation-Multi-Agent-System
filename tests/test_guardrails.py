from workflows.workflow_runner import WorkflowRunner


def test_workflow_runner_runs() -> None:
    runner = WorkflowRunner()
    result = runner.run({"risk_score": 0.2, "evidence": ["document"]})
    assert result["payload"]["risk_score"] == 0.2
