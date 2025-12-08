import pandas as pd
import timeit
from config.db_config import load_db_config
from src.utils.db_utils import get_db_connection
from src.utils.logging_utils import setup_logger, log_load_success
from src.utils.db_table_check import log_table_action
from sqlalchemy.types import String, Float


# Configure the logger
logger = setup_logger(__name__, "load_data_correlation.log")

TYPE = "CORRELATION table moved to database"

TARGET_SCHEMA = "all_2509"
TARGET_TABLE = "rp_capstone_load"


logger.info("Running load_correlation module")


def load_correlation(transformed_data: pd.DataFrame) -> None:
    """
    Load transformed correlation data.

    Args:
        transformed_data (pd.DataFrame): DataFrame containing
        transformed correlations.

    Raises:
        Exception: If loading fails.
    """
    if transformed_data.empty:
        logger.warning(
            "No data provided to load. Skipping database operation."
        )
        return

    try:
        # Set up performance recording for transaction load
        start_time = timeit.default_timer()
        load_correlation_exec(transformed_data)
        load_transactions_execution_time = timeit.default_timer() - start_time

        log_load_success(
            logger,
            TYPE,
            transformed_data.shape,
            load_transactions_execution_time,
        )
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        raise Exception(f"Failed to load data: {e}")


logger.info("Running load_correlation exec")


def load_correlation_exec(transformed_data: pd.DataFrame) -> None:
    """
    Execute the transaction load into the target database.

    Args:
        transformed_data (pd.DataFrame): DataFrame containing
        transformed transaction records.

    """

    connection_details = load_db_config()["target_database"]
    connection = get_db_connection(connection_details)

    # Check if table exists and log action, create utils for this
    exists = log_table_action(connection, TARGET_TABLE, TARGET_SCHEMA)

    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
    # Load data into table

    # Define data types for each column
    cols = transformed_data.columns
    d = {}
    for i, col in enumerate(cols):
        if i == 0:
            d[col] = String(50)  # first column as string
        else:
            d[col] = Float()  # all other columns as float for simplicity

    try:
        transformed_data.to_sql(
            TARGET_TABLE,
            connection,
            schema=TARGET_SCHEMA,
            if_exists="append" if exists else "replace",
            dtype=d,
            index=False,
        )
    except Exception as e:
        logger.error(
            f"Failed to load {len(transformed_data)}"
            f"rows into {TARGET_SCHEMA}.{TARGET_TABLE}: {e}"
        )
        raise Exception(f"Failed to load into database: {e}")

    connection.close()
