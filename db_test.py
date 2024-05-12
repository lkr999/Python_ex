import plotly.express as px
import pandas as pd
import pymysql
# import mariadb
import dash_pivottable
import datetime

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from dash_iconify import DashIconify
from datetime import date
from dash import Dash, Input, Output, ctx, dcc, html, dash_table
from sqlalchemy import create_engine
from pymsgbox import alert, confirm, password, prompt

HOST     = 'localhost'
DB       = 'android_db'
USER = 'root'
PASSWORD = 'tncjf5180'

try:
    # self.conn = pymysql.connect(host='192.168.1.95', user=USER, password=PASSWORD, db='zeitgypsumdb', charset='utf8')
    pymysql.install_as_MySQLdb()
    engine = create_engine("mysql://{user}:{password}@{host}/{db}".format(user=USER, password=PASSWORD, host=HOST, db=DB))
    # conn = mysql.connector.connect(**config)
    conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, charset='utf8')

    cur = conn.cursor()
    df = pd.read_sql("select * from scanner;", con=engine)  # Board Inventory DB

    # data = {'name':['lee','kim','kang','choi','moon'], 'lot':['addfa','dada','adfasd','qeq','qead'],'wh':['g1','g2','g3','g4','g5']}
    # df_data = pd.DataFrame(data)
    # df_data.to_sql('scanner', con=engine, if_exists='append', index=False)

    print(df, )
    conn.close()
except Exception as e: alert(e)
