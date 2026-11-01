import requests

def ping_service():
    # This will ping your website endpoint to prevent Render from sleeping
    url = "https://namnalam-oils.onrender.com/health"
    try:
        res = requests.get(url)
        print(f"Ping successful! Status: {res.status_code}")
    except Exception as e:
        print(f"Ping failed: {e}")

if __name__ == "__main__":
    ping_service()
  
