import pandas as pd
from sqlalchemy import create_engine
import urllib

def WriteToSQLserver(serverName,DBname,TBname,dataPath):

    file_path = dataPath
    
    # Replace with your actual database connection details
    server = serverName
    database = DBname
    table_name = TBname
    # username = 'your_username'
    # password = 'your_password'
    driver = 'ODBC Driver 17 for SQL Server'

    # Replace 'your_file.csv' with your CSV file path
    df = pd.read_csv(file_path)

    # Connection string
    connection_string = (
        f'DRIVER={{{driver}}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
        # f'UID={username};'
        # f'PWD={password}'
    )

    # Create a SQLAlchemy engine
    params = urllib.parse.quote_plus(connection_string)
    engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')

    # Replace 'your_table' with your table name

    df.to_sql(table_name, engine, if_exists='replace', index=False)


    print("Data has been successfully written to the database.")
