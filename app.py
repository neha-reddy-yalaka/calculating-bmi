from flask import Flask, render_template
import mysql.connector
conn = mysql.connector.connect(user="root",password="root",host="127.0.0.1",database="my_guitar_shop",port ='3306')
mycursor = conn.cursor()
query = "SELECT * FROM customers"
mycursor.execute(query)
data = mycursor.fetchall()
print(data)
for (customer_id,email_address) in mycursor:
    print("{} id and {} title".format(customer_id,email_address))
mycursor.close()
conn.close()


app = Flask(__name__)@app.route('/')
def index():return render_template('index.html')@app.route('/v_timestamp')
def v_timestamp():
    mycursor.execute("SELECT * FROM customers")
    data = mycursor.fetchall()
    return render_template('v_timestamp.html', data=data)




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')@app.route('/v_timestamp')
def v_timestamp():
    mycursor.execute("SELECT * FROM customers")
    data = mycursor.fetchall()
    return render_template('v_timestamp.html', data=data)


if __name__ == '__main__':
    app.run()
