import requests

response = requests.get('http://localhost:5000/')
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")

response = requests.get("http://localhost:5000/about")
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")

response = requests.get("http://localhost:5000/greet/chana")
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")

response = requests.get("http://localhost:5000/calculate?num1=10&num2=5&operation=add")
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

response = requests.get("http://localhost:5000/calculate?num1=10&num2=5&operation=divide")
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

response = requests.get("http://localhost:5000/echo", json={"message": "Hello World"})
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

response = requests.get("http://localhost:5000/status/200")
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

response = requests.get("http://localhost:5000/status/400")
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

response = requests.get('http://localhost:5000/')
custom_header = response.headers.get('X-Custom-Header')
print(f"Custom Header: {custom_header}")

response = requests.get('http://localhost:5000/calculate?num1=10&num2=0&operation=divide')
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")