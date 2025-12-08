import pandas as pd
import pytest
from unittest.mock import patch
from src.extract.extract import extract_data


def normalise_nulls(df):
    """Normalise null values to avoid None vs NaN warnings in DataFrame comparisons."""
    return df.fillna(pd.NA).replace({pd.NA: None})


@pytest.fixture
def expected_customers():
    df = pd.read_csv("data/raw/medical_insurance.csv")
    return normalise_nulls(df)


@patch("src.extract.extract_all.extract_all")
def test_extract_data_returns_expected_customers(
    mock_extract_all, expected_customers
):
    """Test that extract_data returns the customers DataFrame correctly."""
    # Arrange: mock extract_all to return the expected customers
    mock_extract_all.return_value = expected_customers

    # Act
    result = extract_data()
    result = normalise_nulls(result)

    # Assert
    assert isinstance(result, pd.DataFrame)
    pd.testing.assert_frame_equal(
        result, expected_customers, check_dtype=False
    )
