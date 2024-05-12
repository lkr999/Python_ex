
import dash
import flask
import numpy as np
import xlwings as xl
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import matplotlib.pyplot as plt

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
# from sqlalchemy import create_engine
from pymsgbox import alert, confirm, password, prompt
import sqlalchemy

HOST     = 'localhost'
DB       = 'android_db'
USER = 'root'
PASSWORD = 'tncjf5180'

# pymysql.install_as_MySQLdb()
engine = sqlalchemy.create_engine("mysql://{user}:{password}@{host}/{db}".format(user=USER, password=PASSWORD, host=HOST, db=DB))
# conn = mysql.connector.connect(**config)
# conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, charset='utf8')
# cur = conn.cursor()
df = pd.read_sql('select * from scanner;', con=engine)
# conn.close()

print(df)
