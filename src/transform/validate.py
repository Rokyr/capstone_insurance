import os
import pandas as pd
from datetime import datetime


FOLDER_PATH = "./data/raw"
LOG_FILE = "data_quality_log.txt"


def analyze_csv(file_path: str) -> str:
    """Run basic data quality checks on a single CSV."""
    report_lines = [f"File: {file_path}"]

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        report_lines.append(f"  ERROR: Could not read file: {e}\n")
        return "\n".join(report_lines)

    report_lines.append(f"  Rows: {len(df)}")
    report_lines.append(f"  Columns: {len(df.columns)}")

    # Check duplicates
    num_duplicates = df.duplicated().sum()
    report_lines.append(f"  Duplicate rows: {num_duplicates}")

    # Check missing values
    report_lines.append("  Missing values per column:")
    for col, cnt in df.isna().sum().items():
        report_lines.append(f"    - {col}: {cnt}")

    # Check date columns
    date_cols = [col for col in df.columns if "date" in col.lower()]
    if date_cols:
        report_lines.append("  Date column checks:")
        for col in date_cols:
            parsed = pd.to_datetime(df[col], errors="coerce")
            invalid_count = parsed.isna().sum()
            valid_count = len(parsed) - invalid_count
            report_lines.append(
                f"    - Column '{col}': valid={valid_count}"
                f", invalid={invalid_count}"
            )
    else:
        report_lines.append("  (No date columns detected)")

    report_lines.append("")
    return "\n".join(report_lines)


def main():
    all_reports = [f"Data quality check started at: {datetime.now()}\n"]

    for file_name in os.listdir(FOLDER_PATH):
        if file_name.lower().endswith(".csv"):
            file_path = os.path.join(FOLDER_PATH, file_name)
            all_reports.append(analyze_csv(file_path))

    all_reports.append(f"Data quality check finished at: {datetime.now()}")

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(all_reports))

    print(f"Done. Log written to: {LOG_FILE}")


if __name__ == "__main__":
    main()
