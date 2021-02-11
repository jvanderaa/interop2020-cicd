import requests
import sys


def main():
    session = requests.Session()
    session.get("https://www.networktocode.com")
    session.get("https://josh-v.com")

    print(session.headers)


if __name__ == "__main__":
    main()