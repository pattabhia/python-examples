import requests
try:
    response = requests.get("http://localhost:50002/user/10")
    print(response.json())
except requests.exceptions.HTTPError as error:
    print(error)