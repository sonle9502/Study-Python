from module1 import C_DataFromG ,C_HandleDataFromSql 
from module2 import fetch_data
from module2 import fetch_data_fweb
debug = 0
def main():
    if debug == 1:
        data_handler = C_DataFromG.DataFromG()
        data_handler.handlewithData("country_food")
        data_handler.handlewithData("vietnam_food")
        data_handler.handlewithData("language")
    
    if debug == 1:
        createChart_handler =C_HandleDataFromSql.HandleDataFromSql()
        data = createChart_handler.get_data_from_sqlserver("language")
        if data is not None:
            createChart_handler.plot_data(data,"Vietnam food","China food","title2","X_asix","Y_asix")

    job_listings = fetch_data.fetch_job_listings('data scientist', 'New York', 1)
    
    print(job_listings)

    fetch_data_fweb.get_hmtlFileFromWeb()
    
    # SQLserver.WriteToSQLserver(
    #     serverName = 'C116\SQLEXPRESS',DBname ='TestDB',TBname = 'TableTest',dataPath = SwitchCase("country_food_filepath").filePath())
    # SQLserver.WriteToSQLserver(
    #     serverName ='C116\SQLEXPRESS',DBname ='TestDB1',TBname = 'TableTest1',dataPath = SwitchCase("vietnam_food_filepath").filePath())
    # SQLserver.WriteToSQLserver(
    #     serverName ='C116\SQLEXPRESS',DBname ='TestDB1',TBname = 'TableTest2',dataPath = SwitchCase("language").filePath())

if __name__ == "__main__":
    main()

