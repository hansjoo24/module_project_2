import requests
from attack_setting import attack_data

page = attack_data()

cookies = {
    "PHPSESSID":"ed931cfa102411d13fc699826d0870f5",
    "JSESSIONID":"09F1AB6C662C22453B021F9CB2D29AD3"
}

page.set_url("https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=61")
page.set_cookies(cookies)

page.send_get_request("https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=61")