import logging
from src.utils.logging_utils import setup_logger
import sqlalchemy as sq

# Reference: SQLAlchemy inspection API
# https://docs.sqlalchemy.org/en/20/core/inspection.html#module-sqlalchemy.inspection

# Set up a logger
logger = setup_logger(
    __name__, "database_table_check.log", level=logging.DEBUG
)


# Check whether a given table exists in the specified schema
def log_table_action(connection, table_name: str, schema: str) -> bool:
    # Create an inspector object to examine the database schema
    inspector = sq.inspect(connection)

    # Check if the table exists in the given schema
    if inspector.has_table(table_name, schema=schema):
        logger.info(
            f"Table {schema}.{table_name} exists. Data will be appended."
        )
    else:
        logger.info(
            f"Table {schema}.{table_name} does not exist. "
            "A new table will be created."
        )

    # Return True if table exists, otherwise False
    return inspector.has_table(table_name, schema=schema)
