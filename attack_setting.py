import requests

class attack_data:
    def __init__(self):
        base_url = ""
        attack_url = ""
        cookies = {}
        headers = {}
        data = {}

    def set_url(self,new_url):
        self.base_url = new_url

    def set_cookies(self,cookie):
        self.cookies = cookie

    def send_get_request(self,url):
        #요청 보내기
        res = requests.get(url, cookies=self.cookies)
        if '권한' in res.text:
            print("세션 ID 교체") 
            return False
        elif 'SE' in res.text:
            print("true")
            #print(res.text)
            return True
        else:
            print("false")
            #print(res.text)
            return False


    

