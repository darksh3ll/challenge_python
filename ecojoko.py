import requests
from selenium import webdriver
from time import sleep

"""
Recuperer le cookies de la session
"""

lks = ''
PRICE_KWH = 0.1193


def get_cookies_session():
    print("Wait cookies LKS ....")
    global lks
    driver = webdriver.Firefox(executable_path="./geckodriver")
    driver.get("https://service.ecojoko.com/")
    email = driver.find_element_by_id("login_l")
    email.send_keys('')
    password = driver.find_element_by_id("login_p")
    password.send_keys('')
    valide_button = driver.find_element_by_id("btn-login")
    sleep(3)
    valide_button.click()
    lks = driver.get_cookies()[0].get('value')
    sleep(10)
    driver.close()


def get_recovering_power_consumption(cook):
    url = "https://service.ecojoko.com/gateway/7426/device/55643/realtime_conso"
    cookies = {'LKS': cook}
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        consumption_watt = response.json().get("real_time")['value']
        return consumption_watt
    else:
        get_cookies_session()


def get_total_kwh(cook):
    url = "https://service.ecojoko.com/gateway/7426/device/55643/powerstat/d4/2021-12-28"
    cookies = {'LKS': cook}
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        kwh = response.json().get("stat")['period']['kwh']
        price_ht = round(PRICE_KWH * kwh, 2)
        price_ttc = round(price_ht + price_ht * 0.20, 2)
        return f"{price_ht} Euros HT /{price_ttc} Euros TTC / {kwh} kwh"
    else:
        get_cookies_session()


def app():
    try:
        while True:
            print(get_total_kwh("487dbc2b17125b79948b033e1b98712d"))
            # print(f"{get_recovering_power_consumption(lks)} W")
            sleep(60)
    except KeyboardInterrupt:
        print('Good bye')


app()
