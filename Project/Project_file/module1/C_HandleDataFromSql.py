from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class HandleDataFromSql:
    
    def get_data_from_sqlserver(self,name):
        # Database connection details
        server = 'C116\\SQLEXPRESS'
        database = 'newDB'
        table = name  # Replace with your actual table name
        query = f'SELECT * FROM {database}.dbo.{table}'  # Correct SQL syntax
        """
        Retrieves data from SQL Server based on the provided query.
        """
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