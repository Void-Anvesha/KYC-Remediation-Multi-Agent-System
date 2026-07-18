# KYC Remediation Multi-Agent

This project implements a multi-agent workflow for KYC remediation and case review. It combines specialized agents for document review, sanctions screening, registry checks, ownership analysis, auditing, and decision-making to support end-to-end case handling.

## Project Structure

```text
.
├── app.py
├── README.md
├── requirements.txt
├── agents/
│   ├── action_agent.py
│   ├── audit_agent.py
│   ├── decision_agent.py
│   ├── document_agent.py
│   ├── evidence_fusion_agent.py
│   ├── gap_detection_agent.py
│   ├── ingress_agent.py
│   ├── orchestrator_agent.py
│   ├── ownership_agent.py
│   ├── registry_agent.py
│   └── sanctions_agent.py
├── app/
├── data/
│   ├── audit_log.csv
│   ├── beneficial_owners.csv
│   ├── customer_master.csv
│   ├── documents.csv
│   ├── kyc_profile.csv
│   ├── outreach_history.csv
│   ├── policy_rules.csv
│   ├── registry.csv
│   ├── sanctions.csv
│   └── triggers.csv
├── kyc_multiagent_datasets/
│   ├── audit_log.csv
│   ├── beneficial_owners.csv
│   ├── customer_master.csv
│   ├── documents.csv
│   ├── kyc_profile.csv
│   ├── outreach_history.csv
│   ├── policy_rules.csv
│   ├── registry.csv
│   ├── sanctions.csv
│   └── triggers.csv
├── models/
│   ├── case.py
│   ├── decision.py
│   └── evidence.py
├── services/
│   ├── case_manager.py
│   ├── csv_loader.py
│   └── logger.py
├── tools/
│   ├── document_tool.py
│   ├── ownership_tool.py
│   ├── registry_tool.py
│   └── sanctions_tool.py
└── workflows/
    └── kyc_graph.py
```

## Overview

The application is organized around:

- Agents for specialized KYC tasks
- Models for case, evidence, and decision objects
- Services for data loading, case management, and logging
- Tools for interacting with document, ownership, registry, and sanctions data
- Workflows that define the overall KYC graph/process

## Getting Started

1. Create a Python environment
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

- The dataset files under the data and kyc_multiagent_datasets folders are used as sample inputs for the workflow.
- Update the dependency list in requirements.txt as more libraries are introduced.
