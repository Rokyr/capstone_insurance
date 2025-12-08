import pandas as pd
import pytest
from src.transform.transform import transform_data


@pytest.fixture
def sample_unclean_transactions():
    """Fixture: load sample unclean transaction data
    (medical insurance CSV)."""
    df = pd.read_csv("data/raw/medical_insurance.csv")
    return df


def test_transform_data_pipeline_integration(sample_unclean_transactions):
    """
    Test that transform_data runs the full pipeline on
    medical_insurance.csv
    and produces both cleaned customers and a correlation
    table with the expected structure.
    """
    cleaned_customers, correlation_table = transform_data(
        sample_unclean_transactions
    )

    assert (
        "person_id" in cleaned_customers.columns
    ), f"Missing 'person_id' column, got {cleaned_customers.columns}"
    assert (
        "income" in cleaned_customers.columns
    ), f"Missing 'income' column, got {cleaned_customers.columns}"
    assert (
        "age" in cleaned_customers.columns
    ), f"Missing 'age' column, got {cleaned_customers.columns}"

    # Assert correlation table DataFrame
    assert isinstance(correlation_table, pd.DataFrame)
    assert not correlation_table.empty
