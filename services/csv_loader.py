"""
CSV Loader Service

Responsible for loading all datasets used in the KYC Remediation workflow.
"""

from pathlib import Path
import pandas as pd

from config import DATA_DIR


class CSVLoader:
    """Loads CSV datasets from the data directory."""

    @staticmethod
    def load(filename: str) -> pd.DataFrame:
        """
        Generic CSV loader.

        Args:
            filename: Name of CSV file

        Returns:
            pandas.DataFrame
        """
        filepath = DATA_DIR / filename

        if not filepath.exists():
            raise FileNotFoundError(f"{filename} not found in {DATA_DIR}")

        return pd.read_csv(filepath)

    # ----------------------------
    # Dataset-specific loaders
    # ----------------------------

    @staticmethod
    def load_customers():
        return CSVLoader.load("customer_master.csv")

    @staticmethod
    def load_kyc_profiles():
        return CSVLoader.load("kyc_profile.csv")

    @staticmethod
    def load_documents():
        return CSVLoader.load("documents.csv")

    @staticmethod
    def load_registry():
        return CSVLoader.load("registry.csv")

    @staticmethod
    def load_beneficial_owners():
        return CSVLoader.load("beneficial_owners.csv")

    @staticmethod
    def load_sanctions():
        return CSVLoader.load("sanctions.csv")

    @staticmethod
    def load_policy_rules():
        return CSVLoader.load("policy_rules.csv")

    @staticmethod
    def load_triggers():
        return CSVLoader.load("triggers.csv")

    @staticmethod
    def load_outreach_history():
        return CSVLoader.load("outreach_history.csv")

    @staticmethod
    def load_audit_log():
        return CSVLoader.load("audit_log.csv")