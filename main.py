from attack_setting import attack_data

#공격 대상 페이지 설정
url = "http://elms1.skinfosec.co.kr:8082/community6/free"
cookies = {
    "JSESSIONID":"0119FF32DD8F8D49072123ADE57C39F7"
}


page = attack_data()
page.set_url(url)
page.set_cookies(cookies)
page.set_query("틀린쿼리")
page.send_post_request()

page.show()