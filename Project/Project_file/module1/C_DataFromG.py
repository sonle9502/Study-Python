from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError ,TooManyRequestsError
import pyodbc
from sqlalchemy import create_engine


class DataFromG:
    def handlewithData(self,nameInput):
        m_name = nameInput
        try:
            if m_name == "country_food":
                m_dataFromG = self.getDataFromG(m_name)
                self.writeDF_toSQL(m_dataFromG,m_name)

            elif m_name == "vietnam_food":
                m_dataFromG = self.getDataFromG(m_name)
                self.writeDF_toSQL(m_dataFromG,m_name)

            elif m_name == "language":
                m_dataFromG = self.getDataFromG(m_name)
                self.writeDF_toSQL(m_dataFromG,m_name)
        except TooManyRequestsError as e:
            print(f"Too many requests error: {e}")
            # Handle the exception (e.g., retry logic, wait and retry, etc.)
            
    def getDataFromG(self,m_name):
        # Initialize pytrends request object
        pytrends = TrendReq(hl='ja-JP', tz=360)
        try:
            if m_name == "country_food":
                # Define the keywords to get trends for
                country_food_List = ["Vietnam food", "China food"]
                # Build the payload
                pytrends.build_payload(country_food_List, cat=0, timeframe='2020-01-01 2024-06-01', geo='JP', gprop='')
                # Get the interest over time for the keywords
                interest_over_time_df = pytrends.interest_over_time()
                return interest_over_time_df

            elif m_name == "vietnam_food":
                vietname_food = ["Phở", "Bánh mì", "Gỏi cuốn", "Bún chả", "Cà phê sữa đá"]
                pytrends.build_payload(vietname_food, cat=0, timeframe='2020-01-01 2024-06-01', geo='JP', gprop='')
                # Get the interest over time for the keywords
                interest_over_time_df = pytrends.interest_over_time()
                return interest_over_time_df
            
            elif m_name == "language":
                language_list = ['Python', 'JavaScript', 'Java']
                pytrends.build_payload(language_list, cat=0, timeframe='2020-01-01 2024-06-01', geo='JP', gprop='')
                # Get the interest over time for the keywords
                interest_over_time_df = pytrends.interest_over_time()
                return interest_over_time_df

        except TooManyRequestsError as e:
            print(f"Too many requests error: {e}")
            # Handle the exception (e.g., retry logic, wait and retry, etc.)

    
    def writeDF_toSQL(self,df,table):
        # Database connection details
        server = 'C116\\SQLEXPRESS'  # Replace with your SQL Server instance name
        database = 'master'  # Connect to the master database to create a new database
        new_database = "newDB"  # Name of the new database
        new_tabel = table
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
                    df.to_sql(name=new_tabel, con=engine, if_exists='replace', index=False)
                    print("DataFrame successfully written to SQL Server!")
                except Exception as e:
                    print("Error writing DataFrame to SQL Server:", e)
            except Exception as ex:
                print("Error connecting to the new database:", ex)

        except pyodbc.Error as ex:
            print("Error connecting to SQL Server:", ex)