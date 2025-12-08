import os
import logging
import pandas as pd
import timeit
from src.utils.logging_utils import setup_logger, log_extract_success

FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "raw",
    "medical_insurance.csv",
)

logger = setup_logger(__name__, "extract_data.log", level=logging.DEBUG)

EXPECTED_PERFORMANCE = 1  # s per 100k rows
TYPE = "ALL data from CSV"


def extract_all() -> pd.DataFrame:
    """
    Extract ALL data from CSV file with performance logging.

    Returns:
        DataFrame containing customer records from CSV file.

    Raises:
        Exception:  1.If CSV file cannot be loaded.
                    2....
    """
    start_time = timeit.default_timer()

    try:
        customers = pd.read_csv(FILE_PATH)
        extract_customers_execution_time = timeit.default_timer() - start_time
        log_extract_success(
            logger,
            TYPE,
            customers.shape,
            extract_customers_execution_time,
            EXPECTED_PERFORMANCE,
        )
        return customers

    except Exception as e:
        logger.error(f"Error loading {FILE_PATH}: {e}")
        raise Exception(f"Failed to load CSV file: {FILE_PATH}")
