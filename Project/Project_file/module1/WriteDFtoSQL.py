import pandas as pd
import pyodbc
from sqlalchemy import create_engine



def WriteDF_toSQL(df):
    # Database connection details
    server = 'C116\\SQLEXPRESS'  # Replace with your SQL Server instance name
    database = 'master'  # Connect to the master database to create a new database
    new_database = 'newDB'  # Name of the new database
    df = df
    # Step 1: Connect to SQL Server
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
        print("Connected to SQL Server successfully!")

        # Step 2: Create a new database if it doesn't exist
        try:
            conn.autocommit = True  # Ensure autocommit mode is enabled
            cursor = conn.cursor()
            cursor.execute(f"IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = '{new_database}') CREATE DATABASE {new_database}")
            print(f"Database '{new_database}' created successfully (if it didn't already exist).")
        except pyodbc.Error as ex:
            print("Error creating database:", ex)
        finally:
            cursor.close()
            conn.close()  # Close the connection to the master database

        # Step 3: Reconnect to the new database
        try:
            engine = create_engine(f'mssql+pyodbc://{server}/{new_database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes')
            print(f"Connected to the new database '{new_database}' successfully!")

            # Write DataFrame to SQL Server
            try:
                df.to_sql(name='People', con=engine, if_exists='replace', index=False)
                print("DataFrame successfully written to SQL Server!")
            except Exception as e:
                print("Error writing DataFrame to SQL Server:", e)
        except Exception as ex:
            print("Error connecting to the new database:", ex)

    except pyodbc.Error as ex:
        print("Error connecting to SQL Server:", ex)
