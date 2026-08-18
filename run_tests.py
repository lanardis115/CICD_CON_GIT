import pytest
import sys

def main():
    print("🚀 Avvio della suite di test...")
    pytest_args = [
        "tests",
        "--html=report.html",
        "--self-contained-html",
        "-v"
    ]
    exit_code = pytest.main(pytest_args)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()