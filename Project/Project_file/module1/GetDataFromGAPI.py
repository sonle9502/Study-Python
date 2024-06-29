import pandas as pd
from sqlalchemy import create_engine
import urllib

try:
    from pytrends.request import TrendReq
    print("pytrends is installed correctly.")
except ImportError as e:
    print("ImportError:", e)

# Initialize pytrends request object
pytrends = TrendReq(hl='ja-JP', tz=360)

# Define the keywords to get trends for
keywords = ["Phở", "Bánh mì", "Gỏi cuốn", "Bún chả", "Cà phê sữa đá"]

country_food_List = ["Vietnam food", "China food"]

# Build the payload
pytrends.build_payload(country_food_List, cat=0, timeframe='2020-01-01 2024-06-01', geo='JP', gprop='')

# Get the interest over time for the keywords
interest_over_time_df = pytrends.interest_over_time()




