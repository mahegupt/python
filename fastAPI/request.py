import requests


url = "http://127.0.0.1:8000/items/"
data = {
    "id": 1,
    "name": "Laptop",
    "price": 999.99,
    "in_stock": True
}

response = requests.post(url, json=data)  # Note the `json=` keyword
print(response.status_code)
print(response.json())

url = "http://127.0.0.1:8000/"
print(requests.get(url).json())

url = "http://127.0.0.1:8000/items/ 1"
print(requests.get(url).json())
