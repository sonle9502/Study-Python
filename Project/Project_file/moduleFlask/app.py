from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
from module1 import C_HandleDataFromSql

def flask_app():
    app = Flask(__name__)

    # ホームページのルート
    @app.route('/')
    def home():
        query = f'SELECT * FROM [indeedDB].[dbo].[indeedTB]'
        handle = C_HandleDataFromSql.HandleDataFromSql()
        df = handle.get_data_from_sqlserver(server='C116\\SQLEXPRESS', database='indeedDB', query=query)
        
        if df is not None:
            table_html = df.to_html(classes='table table-striped')
            return render_template('index.html', table=table_html)
        else:
            return "No data found"

    app.run(debug=True)
