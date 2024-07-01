from pytrends.request import TrendReq
from . import WriteDFtoSQL
from pytrends.exceptions import TooManyRequestsError

def CreateCSVfile(nameInput):
    
    m_name = nameInput
    # Initialize pytrends request object
    pytrends = TrendReq(hl='ja-JP', tz=360)
    # Define the keywords to get trends for
    vietname_food = ["Phở", "Bánh mì", "Gỏi cuốn", "Bún chả", "Cà phê sữa đá"]
    country_food_List = ["Vietnam food", "China food"]
    language_list = ['Python', 'JavaScript', 'Java']
    try:
        if m_name == "country_food":
            # Build the payload
            pytrends.build_payload(country_food_List, cat=0, timeframe='2020-01-01 2024-06-01', geo='JP', gprop='')
            # Get the interest over time for the keywords
            interest_over_time_df = pytrends.interest_over_time()
            WriteDFtoSQL.WriteDF_toSQL(interest_over_time_df,m_name)
        elif m_name == "vietnam_food":
            pytrends.build_payload(vietname_food, cat=0, timeframe='2020-01-01 2024-06-01', geo='JP', gprop='')
            # Get the interest over time for the keywords
            interest_over_time_df = pytrends.interest_over_time()
            WriteDFtoSQL.WriteDF_toSQL(interest_over_time_df,m_name)
        elif m_name == "language":
            pytrends.build_payload(language_list, cat=0, timeframe='2020-01-01 2024-06-01', geo='JP', gprop='')
            # Get the interest over time for the keywords
            interest_over_time_df = pytrends.interest_over_time()
            WriteDFtoSQL.WriteDF_toSQL(interest_over_time_df,m_name)

        

        # Save the data to a CSV file
        #interest_over_time_df.to_csv(SwitchCase(m_name).filePath())

    except TooManyRequestsError as e:
        print(f"Too many requests error: {e}")
        # Handle the exception (e.g., retry logic, wait and retry, etc.)


    

    