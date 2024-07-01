from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError

def getDataFromG(m_name):
    
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

    