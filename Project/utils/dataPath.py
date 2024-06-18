# utils/dataPath.py
class SwitchCase:
    def __init__(self, name):
        self.name = name

    def filePath(self):
        if self.name == "country_food_filepath":
            return r"C:\Users\s-le\Desktop\study\Python\Python-study\Project\data\country_food_overTime_df.csv"
        elif self.name == "vietnam_food_filepath":
            return r"C:\Users\s-le\Desktop\study\Python\Python-study\Project\data\vietnam_food_overTime_df.csv"
        elif self.name == "language":
            return r"C:\Users\s-le\Desktop\study\Python\Python-study\Project\data\language.csv"
        # else:
        #     return "C:/path/to/daughter_file.csv"
