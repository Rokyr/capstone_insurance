import os
import sys
import subprocess

LOCATION_STREAMLIT = os.path.join(
    os.path.dirname(__file__), "..", "src", "streamlit", "home.py"
)


def main():
    try:
        subprocess.run(
            [sys.executable, "-m", "streamlit", "run", LOCATION_STREAMLIT],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: Streamlit exited with code {e.returncode}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
