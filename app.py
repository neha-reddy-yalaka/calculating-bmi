import json
from flask import Flask, render_template
import mysql.connector

conn = mysql.connector.connect(user="root",password="root",host="127.0.0.1",database="my_guitar_shop",port ='3306')
mycursor = conn.cursor()
query = "SELECT * FROM customers"
mycursor.execute(query)
data = mycursor.fetchall()
resp = []
for list_item in (data):
    json_data = {"id":list_item[0],"email":list_item[1],"hash":list_item[2],"first_name":list_item[3],"last_name":list_item[4]}
    resp.append(json_data)

mycursor.close()
conn.close()

app = Flask(__name__)


@app.route('/')
def main():
    return str(resp)


if __name__ == '__main__':
    app.run()
