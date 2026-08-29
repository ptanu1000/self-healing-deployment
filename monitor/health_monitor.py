import time
import requests

HEALTH_URL = "http://localhost:8000/health"
CHECK_INTERVAL = 10


def check_health():
    try:
        response = requests.get(HEALTH_URL, timeout=5)

        if response.status_code == 200:
            print("HEALTHY")
            return True

        print(f"UNHEALTHY - HTTP {response.status_code}")
        return False

    except requests.RequestException as exc:
        print(f"UNHEALTHY - {exc}")
        return False


while True:
    check_health()
    time.sleep(CHECK_INTERVAL)
