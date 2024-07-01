from module1.HandleDataFromG import handlewithData

def main():
    handlewithData ("country_food")
    handlewithData("vietnam_food")
    handlewithData("language")
    
    # SQLserver.WriteToSQLserver(
    #     serverName = 'C116\SQLEXPRESS',DBname ='TestDB',TBname = 'TableTest',dataPath = SwitchCase("country_food_filepath").filePath())
    # SQLserver.WriteToSQLserver(
    #     serverName ='C116\SQLEXPRESS',DBname ='TestDB1',TBname = 'TableTest1',dataPath = SwitchCase("vietnam_food_filepath").filePath())
    # SQLserver.WriteToSQLserver(
    #     serverName ='C116\SQLEXPRESS',DBname ='TestDB1',TBname = 'TableTest2',dataPath = SwitchCase("language").filePath())

if __name__ == "__main__":
    main()

