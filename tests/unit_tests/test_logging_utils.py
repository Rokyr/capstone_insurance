import logging
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

from src.utils.logging_utils import (
    _ensure_log_directory,
    _create_formatter,
    _create_handlers,
    setup_logger,
    log_extract_success,
    log_load_success,
)


def test_ensure_log_directory_creates_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        base_path = Path(temp_dir) / "test_project"
        log_dir = _ensure_log_directory(base_path)

        assert log_dir.exists()
        assert log_dir.name == "logs"


def test_create_formatter_returns_correct_format():
    formatter = _create_formatter()

    assert isinstance(formatter, logging.Formatter)
    fmt_str = formatter._fmt or ""
    assert "%(asctime)s" in fmt_str
    assert "%(name)s" in fmt_str
    assert "%(levelname)s" in fmt_str


def test_create_handlers_returns_both_handlers():
    with tempfile.TemporaryDirectory() as temp_dir:
        log_dir = Path(temp_dir)
        file_handler, console_handler = _create_handlers(
            log_dir, "test.log", logging.INFO
        )

        assert isinstance(file_handler, logging.FileHandler)
        assert isinstance(console_handler, logging.StreamHandler)
        assert file_handler.level == logging.INFO
        assert console_handler.level == logging.INFO

        file_handler.close()
        console_handler.close()


@patch("src.utils.logging_utils.logging.getLogger")
def test_setup_logger_creates_logger_with_handlers(mock_get_logger):
    mock_logger = MagicMock()
    mock_logger.handlers = []
    mock_get_logger.return_value = mock_logger

    with tempfile.TemporaryDirectory() as temp_dir:
        setup_logger("test", "test.log", base_path=temp_dir)

        mock_logger.setLevel.assert_called_once_with(logging.DEBUG)
        assert mock_logger.addHandler.call_count == 2


@patch("src.utils.logging_utils.logging.getLogger")
def test_setup_logger_skips_handlers_if_already_exist(mock_get_logger):
    mock_logger = MagicMock()
    mock_logger.handlers = [MagicMock()]  # Already has handlers
    mock_get_logger.return_value = mock_logger

    setup_logger("test", "test.log")

    mock_logger.addHandler.assert_not_called()


@patch("src.utils.logging_utils.logging.getLogger")
def test_setup_logger_skips_handlers_if_already_exist(mock_get_logger):
    mock_logger = MagicMock()
    mock_logger.handlers = [MagicMock()]  # Already has handlers
    mock_get_logger.return_value = mock_logger

    setup_logger("test", "test.log")

    mock_logger.addHandler.assert_not_called()


def test_log_extract_success_exceeds_expected_rate():
    mock_logger = MagicMock()

    log_extract_success(mock_logger, "slow_data", (100, 3), 5.0, 0.01)

    assert mock_logger.info.call_count == 3
    mock_logger.warning.assert_called_once_with(
        "Execution time per row exceeds 0.01: 0.05 seconds"
    )


def test_log_load_success_logs_info_for_nonempty_data():
    mock_logger = MagicMock()

    log_load_success(mock_logger, "slow_data", (100, 3), 5.0)

    # Should log 4 info messages (success, loaded, execution time, per-row time)
    assert mock_logger.info.call_count == 4
    mock_logger.warning.assert_not_called()
