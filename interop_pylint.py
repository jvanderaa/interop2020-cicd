import requests
import os


def main():
    """Main code execution."""
    session = requests.Session()
    session.get("https://www.networktocode.com")

    print(session.headers)

if __name__ == "__main__":
    main()