from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import dataPath
import os
import pyodbc

class HandleDataFromSql:
    def write_df_to_sqlserver(self,server, database_master, new_database, new_table,df):
        # Step 1: Connect to SQL Server
        try:
            conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database_master + ';Trusted_Connection=yes;')
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
                    df.to_sql(name=new_table, con=engine, if_exists='replace', index=False)
                    print("DataFrame successfully written to SQL Server!")
                except Exception as e:
                    print("Error writing DataFrame to SQL Server:", e)
            except Exception as ex:
                print("Error connecting to the new database:", ex)

        except pyodbc.Error as ex:
            print("Error connecting to SQL Server:", ex)

    def get_data_from_sqlserver(self,server,database,query):
        
        conn_str = f'mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
        engine = create_engine(conn_str)

        try:
            with engine.connect() as conn:
                data = pd.read_sql(query, conn)
            print("Data retrieved successfully!")
            return data
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return None

    def plot_data(self,data, x_col, y_col, title, x_label, y_label):
        title = "title"
        x_col = x_col
        y_col = y_col
        x_label = x_label
        y_label = y_label

        data = pd.DataFrame(data)
        data['date'] = pd.to_datetime(data['date'])  # Convert date column to datetime format
        # Iterate over each date and create a pie chart
        for i, date in enumerate(data['date']):
            # Prepare data for the current date
            labels = ['Python', 'JavaScript', 'Java']
            sizes = [data['Python'][100], data['JavaScript'][100], data['Java'][100]]
            
            # Plotting
            plt.figure(figsize=(9, 6))  # Optional: Adjust figure size
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title(f'Programming Language Interest on {date}')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
            
            # Display the plot
            plt.tight_layout()  # Optional: Adjust layout
            plt.show()