import requests
from time import sleep


def check_internet_connection():
    url = "https://www.google.com"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False


def get_todo_to_api():
    if check_internet_connection():
        response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
        print(response.json())
    else:
        print('No internet connection')


def app():
    try:
        while True:
            get_todo_to_api()
            sleep(5)
    except KeyboardInterrupt:
        print("End of the programme")


app()
