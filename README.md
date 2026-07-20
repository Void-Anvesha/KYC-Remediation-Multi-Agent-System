# KYC Remediation Multi-Agent

This project implements a multi-agent workflow for KYC remediation and case review. It combines specialized agents for document review, sanctions screening, registry checks, ownership analysis, audit logging, outreach, escalation, and decision-making to support end-to-end case handling with checkpoints, guardrails, and workflow state tracking.

## Project Structure

```text
kyc-remediation-multi-agent/
├── app.py                          # Entry point
├── config.py                       # Global configuration
├── requirements.txt
├── README.md
│
├── agents/
│   ├── base_agent.py               # Base class inherited by every agent
│   ├── ingress_agent.py            # Validate & accept trigger
│   ├── ontology_agent.py           # Normalize data schema
│   ├── gap_detection_agent.py      # Detect KYC gaps
│   ├── orchestrator_agent.py       # Brain of the workflow
│   ├── enrichment_agent.py         # Coordinates enrichment agents
│   ├── registry_agent.py
│   ├── document_agent.py
│   ├── ownership_agent.py
│   ├── sanctions_agent.py
│   ├── evidence_fusion_agent.py
│   ├── decision_agent.py
│   ├── outreach_agent.py
│   ├── escalation_agent.py
│   ├── audit_agent.py
│   └── feedback_agent.py
│
├── core/
│   ├── guardrail_manager.py        # Retry + rollback + validation
│   ├── checkpoint_manager.py       # Creates checkpoints
│   ├── rollback_manager.py
│   ├── retry_manager.py
│   ├── validator.py
│   ├── state_manager.py            # Workflow state
│   ├── event_bus.py                # Simple event dispatcher
│   ├── exceptions.py
│   └── constants.py
│
├── models/
│   ├── case.py
│   ├── gap.py
│   ├── evidence.py
│   ├── decision.py
│   ├── audit.py
│   └── task.py
│
├── services/
│   ├── csv_loader.py
│   ├── logger.py
│   ├── case_repository.py
│   ├── policy_engine.py
│   ├── confidence_engine.py
│   └── metrics.py
│
├── tools/
│   ├── registry_tool.py
│   ├── document_tool.py
│   ├── ownership_tool.py
│   ├── sanctions_tool.py
│   └── communication_tool.py
│
├── workflows/
│   ├── kyc_graph.py
│   └── workflow_runner.py
│
├── data/
│   ├── customer_master.csv
│   ├── kyc_profile.csv
│   ├── registry.csv
│   ├── documents.csv
│   ├── beneficial_owners.csv
│   ├── sanctions.csv
│   ├── outreach_history.csv
│   ├── policy_rules.csv
│   ├── triggers.csv
│   └── audit_log.csv
│
├── logs/
│   ├── application.log
│   ├── audit.log
│   └── workflow.log
│
├── checkpoints/
│   ├── case_1001/
│   ├── case_1002/
│   └── ...
│
├── ui/
│   ├── dashboard.py
│   ├── pages/
│   │   ├── case_view.py
│   │   ├── audit_view.py
│   │   ├── workflow_view.py
│   │   └── analytics.py
│   └── assets/
│
├── tests/
│   ├── test_gap_detection.py
│   ├── test_registry.py
│   ├── test_document.py
│   ├── test_decision.py
│   └── test_guardrails.py
│
└── docs/
    ├── architecture.md
    ├── workflow.md
    ├── agent_catalogue.md
    ├── api.md
    └── screenshots/
```

## Overview

The application is organized around:

- Specialized agents for ingestion, enrichment, validation, decision-making, outreach, escalation, and audit review
- Core workflow components for state management, checkpointing, retries, rollback, validation, and event handling
- Models for cases, gaps, evidence, decisions, audits, and tasks
- Services for CSV loading, policy evaluation, confidence scoring, metrics, and case repositories
- Tools for interacting with registry, document, ownership, sanctions, and communication data
- Workflows and UI modules that support end-to-end remediation and monitoring

## Getting Started

1. Create a Python environment

   On Windows PowerShell:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS/Linux:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application
   ```bash
   python app.py
   ```

## Notes

- The sample dataset files under the data directory are used as inputs for the workflow.
- Logs, checkpoints, and UI/test artifacts are generated during execution.
- Update the dependency list in requirements.txt as more libraries are introduced.
