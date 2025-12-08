import pandas as pd
import pytest
from src.extract.extract_all import (
    extract_all,
    TYPE,
    FILE_PATH,
    EXPECTED_PERFORMANCE,
)


@pytest.fixture
def mock_log_extract_success(mocker):
    return mocker.patch("src.extract.extract_all.log_extract_success")


@pytest.fixture
def mock_logger(mocker):
    return mocker.patch("src.extract.extract_all.logger")


def test_extract_all_csv_to_dataframe(
    mocker, mock_log_extract_success, mock_logger
):
    # Mock the extract_all function to return a DataFrame
    mock_df = pd.DataFrame(
        {"id": [1, 2, 3], "name": ["Rokas", "Rokas1", "Rokas2"]}
    )
    mocker.patch("src.extract.extract_all.pd.read_csv", return_value=mock_df)

    # Patch timeit.default_timer to simulate execution time
    mock_start_time = 100.0
    mock_end_time = 100.5
    mocker.patch(
        "src.extract.extract_all.timeit.default_timer",
        side_effect=[mock_start_time, mock_end_time],
    )

    # Act
    df = extract_all()

    # Assert
    mock_log_extract_success.assert_called_once_with(
        mock_logger,
        TYPE,
        df.shape,
        mock_end_time - mock_start_time,
        EXPECTED_PERFORMANCE,
    )


def test_log_extract_all_error(mocker, mock_logger):
    # Patch pd.read_csv to raise an exception
    mocker.patch(
        "src.extract.extract_all.pd.read_csv",
        side_effect=Exception("Exception message"),
    )

    # Test that the exception is raised
    with pytest.raises(Exception) as exc_info:
        extract_all()

    # Assert the raised exception message matches exactly
    assert str(exc_info.value) == f"Failed to load CSV file: {FILE_PATH}"

    # Verify that the error was logged
    mock_logger.error.assert_called_once_with(
        f"Error loading {FILE_PATH}: Exception message"
    )
