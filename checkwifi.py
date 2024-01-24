import requests

def internet_connection():
    try:
        response = requests.get("https://google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False    
if internet_connection():
    print("The Internet is connected.")
else:
    raise RuntimeError('no internet connecton')