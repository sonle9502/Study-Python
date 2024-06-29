from module1 import SQLserver 
from module1 import CreateCSVfromGAPI
from utils.dataPath import SwitchCase

def main():
    CreateCSVfromGAPI.CreateCSVfile("country_food")
    CreateCSVfromGAPI.CreateCSVfile("vietnam_food")
    CreateCSVfromGAPI.CreateCSVfile("language")
    
    # SQLserver.WriteToSQLserver(
    #     serverName = 'C116\SQLEXPRESS',DBname ='TestDB',TBname = 'TableTest',dataPath = SwitchCase("country_food_filepath").filePath())
    # SQLserver.WriteToSQLserver(
    #     serverName ='C116\SQLEXPRESS',DBname ='TestDB1',TBname = 'TableTest1',dataPath = SwitchCase("vietnam_food_filepath").filePath())
    # SQLserver.WriteToSQLserver(
    #     serverName ='C116\SQLEXPRESS',DBname ='TestDB1',TBname = 'TableTest2',dataPath = SwitchCase("language").filePath())

if __name__ == "__main__":
    main()

