import argparse
from scan import scan_web_app
from payload_injection import inject_payload
from response_analysis import analyze_response

def main():
    parser = argparse.ArgumentParser(description="Web Application Fuzzer")
    parser.add_argument('url', help="Target URL to scan")
    parser.add_argument('--payload', help="Payload to inject")
    args = parser.parse_args()

    scan_web_app(args.url)
    
    if args.payload:
        response = inject_payload(args.url, "email", args.payload)
        print("Injection Response:", response.text)
        analyze_response(args.url, args.payload)

if __name__ == "__main__":
    main()
