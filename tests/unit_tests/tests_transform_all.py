import os
import pandas as pd
import pytest
from src.transform.transform_all import clean_customers


# Paths
EXPECTED_CLEANED_CUSTOMER_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "test_data",
    "expected_customers_clean_results.csv",
)

UNCLEAN_CUSTOMER_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "raw",
    "medical_insurance.csv",
)


def normalize_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize nulls for consistent DataFrame comparison."""
    return df.where(pd.notnull(df), None)


@pytest.fixture
def expected_cleaned_customers():
    """Fixture to load expected cleaned customer data."""
    df = pd.read_csv(EXPECTED_CLEANED_CUSTOMER_DATA_PATH)
    return normalize_nulls(df)


@pytest.fixture
def unclean_customers():
    """Fixture to load unclean customer data."""
    df = pd.read_csv(UNCLEAN_CUSTOMER_DATA_PATH)
    return df


def test_clean_customers_transforms_data_correctly(
    unclean_customers, expected_cleaned_customers
):
    """Test that clean_customers transforms unclean data into the expected cleaned format."""
    # Act
    cleaned = clean_customers(unclean_customers)
    cleaned = normalize_nulls(cleaned)

    # Assert
    assert isinstance(cleaned, pd.DataFrame)
    pd.testing.assert_frame_equal(
        cleaned, expected_cleaned_customers, check_dtype=False
    )
