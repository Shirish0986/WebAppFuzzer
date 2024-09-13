# ui.py
import argparse
from scan import scan_web_app

def main():
    parser = argparse.ArgumentParser(description="Web Application Fuzzer")
    parser.add_argument('url', help="Target URL")
    args = parser.parse_args()

    scan_web_app(args.url)

if __name__ == "__main__":
    main()
