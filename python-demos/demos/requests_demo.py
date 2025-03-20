import time

import requests


def check_api_health(url: str) -> bool:
    max_retries = 4
    for i in range(max_retries):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return True
            else:
                print(f"Attempt {i + 1}: Status code {r.status_code} - Retrying ...")
        except requests.RequestException as e:
            print(f"Attempt {i + 1}: Error {e} - Retrying ...")
        time.sleep(0.5)
    return False


def main() -> None:  # pragma: no cover
    url = "https://www.google.com/"
    print(check_api_health(url))
    url = "https://www.google.com/wrongapi"
    print(check_api_health(url))


if __name__ == "__main__":
    main()
