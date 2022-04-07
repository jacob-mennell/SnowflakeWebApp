from flask import Flask, render_template, request
from snowflake import connector
import pandas as pd
import os

app = Flask("my website")

@app.route('/')
def homepage():
    return render_template('index.html', dfhtml=dfhtml)

@app.route('/submit')
def submitpage():
    return render_template('submit.html')

@app.route('/thanks4submit', methods=["POST"])
def thanks4submit():
    colorname = request.form.get("cname")
    username = request.form.get("uname")
    return render_template('thanks4submit.html',
                           colorname=colorname,
                           username=username)

#define env variables
password = os.getenv('password')
username = os.getenv('username')

#snowflake
cnx = connector.connect(
    account='ia83659.europe-west2.gcp',
    user=username,
    password=password,
    warehouse='COMPUTE_WH',
    database='DEMO_DB',
    schema='PUBLIC',
    role='SYSADMIN'
)

cur = cnx.cursor()
cur.execute("SELECT * FROM COLORS")
rows = pd.DataFrame(cur.fetchall(),columns=['COLOR_UID', 'COLOR_NAME'])
#print(rows)

#test dataframe as html
dfhtml = rows.to_html()
print(dfhtml)

app.run()