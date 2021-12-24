import requests
from selenium import webdriver
from time import sleep

"""
Recuperer le cookies de la session
"""


def get_cookies_session():
    driver = webdriver.Firefox(executable_path="./geckodriver")
    driver.get("https://service.ecojoko.com/")
    email = driver.find_element_by_id("login_l")
    email.send_keys('')
    password = driver.find_element_by_id("login_p")
    password.send_keys('')
    valide_button = driver.find_element_by_id("btn-login")
    sleep(3)
    valide_button.click()
    return driver.get_cookies()[0].get('value')


def get_recovering_power_consumption():
    url = "https://service.ecojoko.com/gateway/7426/device/55643/realtime_conso"
    cookies = {'LKS': '1660bdf60fcb2924da65a3224fe0735c'}
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        consumption_watt = response.json().get("real_time")['value']
        return consumption_watt
    return "Cookies session no valide"


def app():
    try:
        while True:
            print(get_recovering_power_consumption())
            sleep(2)
    except KeyboardInterrupt:
        print('Good bye')


get_cookies_session()
