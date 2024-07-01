from . import WriteDFtoSQL 
from . import GetDataFromG
from pytrends.exceptions import TooManyRequestsError

def handlewithData(nameInput):
    
    m_name = nameInput

    try:
        if m_name == "country_food":
            m_dataFromG = GetDataFromG.getDataFromG(m_name)
            WriteDFtoSQL.writeDF_toSQL(m_dataFromG,m_name)

        elif m_name == "vietnam_food":
            m_dataFromG = GetDataFromG.getDataFromG(m_name)
            WriteDFtoSQL.writeDF_toSQL(m_dataFromG,m_name)

        elif m_name == "language":
            m_dataFromG = GetDataFromG.getDataFromG(m_name)
            WriteDFtoSQL.writeDF_toSQL(m_dataFromG,m_name)

        

        # Save the data to a CSV file
        #interest_over_time_df.to_csv(SwitchCase(m_name).filePath())

    except TooManyRequestsError as e:
        print(f"Too many requests error: {e}")
        # Handle the exception (e.g., retry logic, wait and retry, etc.)


    

    