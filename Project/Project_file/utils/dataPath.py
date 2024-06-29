# utils/dataPath.py
import os

class SwitchCase:
    def __init__(self, name):
        self.name = name

    def filePath(self):
        root = "C:\\Users\\s-le\\Desktop\\study-private\\Python\\Study-Python\\Project\\Project_file\\data"
        if self.name == "country_food_filepath":
            return  os.path.join(root,"datacountry_food_overTime_df.csv")
        elif self.name == "vietnam_food_filepath":
            return os.path.join(root,"vietnam_food_filepath.csv") 
        elif self.name == "language":
            return os.path.join(root,"language.csv") 
        # else:
        #     return "C:/path/to/daughter_file.csv"
