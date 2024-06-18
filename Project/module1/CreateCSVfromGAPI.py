from pytrends.request import TrendReq
from utils.dataPath import SwitchCase

def test():
    # Initialize pytrends request object
    print("hello")

def CreateCSVfile(nameInput):
    
    name = nameInput

    # Initialize pytrends request object
    pytrends = TrendReq(hl='ja-JP', tz=360)
    # Define the keywords to get trends for
    vietname_food = ["Phở", "Bánh mì", "Gỏi cuốn", "Bún chả", "Cà phê sữa đá"]
    country_food_List = ["Vietnam food", "China food"]
    language_list = ['Python', 'JavaScript', 'Java']

    if name == "country_food_filepath":
        # Build the payload
        pytrends.build_payload(country_food_List, cat=0, timeframe='2020-01-01 2024-06-01', geo='JP', gprop='')
    elif name == "vietnam_food_filepath":
        pytrends.build_payload(vietname_food, cat=0, timeframe='2020-01-01 2024-06-01', geo='JP', gprop='')
    elif name == "language":
        pytrends.build_payload(language_list, cat=0, timeframe='2020-01-01 2024-06-01', geo='JP', gprop='')


    # Get the interest over time for the keywords
    interest_over_time_df = pytrends.interest_over_time()

    # Save the data to a CSV file
    interest_over_time_df.to_csv(SwitchCase(name).filePath())