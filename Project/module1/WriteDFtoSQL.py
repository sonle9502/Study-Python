import pandas as pd
from sqlalchemy import create_engine

# Sample DataFrame
data = {
    'column1': [1, 2, 3],
    'column2': ['a', 'b', 'c']
}
df = pd.DataFrame(data)

# Define your SQL Server connection string
# Example for SQL Server authentication
conn_str = 'mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server'

# Example for Windows authentication
# conn_str = 'mssql+pyodbc://server/database?driver=ODBC+Driver+17+for+SQL+Server;Trusted_Connection=yes'

# Create an engine
engine = create_engine(conn_str)

# Write the DataFrame to a SQL table named 'table_name'
# if_exists='replace' will drop the table if it exists and create a new one
# if_exists='append' will insert the data without dropping the table
df.to_sql('table_name', engine, if_exists='replace', index=False)

print("DataFrame written to SQL Server successfully.")
