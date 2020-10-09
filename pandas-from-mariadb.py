import pandas as pd
from sqlalchemy import create_engine

# pandas display settings
pd.set_option("display.max_columns", 999)

# credentials to create database connections
db_driver = 'mysql+mysqldb'
db_username = 'db_username'
db_password = 'db_password'
db_ipaddress = '1.2.3.4'
db_port = '3306'
db_dbname = 'db_dbname'

# database connection ... refresh last line before each dataframe read
str_mariadb_con = f'{db_driver}://{db_username}:{db_password}@{db_ipaddress}:{db_port}/{db_dbname}'
mariadb_engine = create_engine(str_mariadb_con)
mariadb_connection = mariadb_engine.connect()

def get_df_from_mariadb(db_dbname, str_table_name):
  '''
  Sample syntax to create pandas dataframe from MariaDB table. 
  '''

  # sql query 
  str_sql = f'''
  SELECT *
  FROM {db_dbname}.{str_table_name};
  '''
    
  # create dataframe from the SQL query against the database connection
  df = pd.read_sql_query(str_sql, mariadb_connection)
  
  return df
  
# run the function, refresh connection
mariadb_engine = create_engine(str_mariadb_con)
mariadb_connection = mariadb_engine.connect()
df_sample = get_df_from_mariadb(db_dbname='db_dbname', str_table_name='str_table_name')
