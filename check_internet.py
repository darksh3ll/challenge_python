import requests
from time import sleep


def check_internet():
    url = "https://www.google.com"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False


def get_datas():
    if check_internet():
        r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
        print(r.json())
    else:
        print('Pas de connexion internet')


def main():
    try:
        while True:
            get_datas()
            sleep(5)
    except KeyboardInterrupt:
        print("fin du programme")


main()
