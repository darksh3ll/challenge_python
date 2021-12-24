import requests
from time import sleep


while True:
  url = "https://service.ecojoko.com/gateway/7426/device/55643/realtime_conso"
  cookies = {'LKS': 'e16dd4e08a4ff78a777b043cc8641b27'}
  response = requests.get(url, cookies=cookies)
  print(response.json().get("real_time")['value'])
  sleep(2)
