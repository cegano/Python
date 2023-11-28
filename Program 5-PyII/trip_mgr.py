import sqlite3 as db
from bottle import route, run, request, response, template

@route('/', method = "GET")
def index():
    return template('index')

@route('/login', method = "POST")
def login():
    user = request.forms.get('username')
    pswd = request.forms.get('password')

    conn = db.connect("travel_expenses.db")
    cur = conn.cursor()
    sql = "SELECT * FROM members WHERE username = ? AND password = ?"

    cur.execute(sql, (user, pswd))
    result = cur.fetchone()
    cur.close()

    if (result):
        return template('tech_menu')
    else:
        m = {'msg': "Login failed"}
        return template('status', m)


@route('/showTrips', method=['GET', 'POST'])
def table():
    if request.method == 'GET':
        return template('tripForm')
    else:
        user = request.forms.get("user")

        conn = db.connect("travel_expenses.db")
        cur = conn.cursor()
        sql = "SELECT * FROM trips WHERE username = ?"

        cur.execute(sql, (user,))
        result = cur.fetchall()
        cur.close()

        #if username[0] == user:

        return template('displayTrips', rows=result)
        #else:
           # msg = 'Incorrect username entered'


@route('/enterTrip', method = ['GET', 'POST'])
def add_trip():
    if request.method == 'GET':
        return template('add_trip')
    else:
        user = request.forms.get("user")
        date = request.forms.get("date")
        dest = request.forms.get("dest")
        miles = request.forms.get("miles")
        gallons = request.forms.get("gallons")


        try:
            conn = db.connect("travel_expenses.db")
            cur = conn.cursor()

            data = (None, user, date, dest, miles, gallons)

            sql = "INSERT INTO trips VALUES (?, ?, ?, ?, ?, ?)"

            cur.execute(sql, data)
            conn.commit()
            cur.close()

            m = {'msg': "Trip successfully entered"}
            return template('status', m)
            
        except:
            m = {'msg': "Trip not entered successfully"}
            return template('status', m)
    
        
run(host = 'localhost', port = 8080)


#add_trip.tpl -
#login_page -
#show_trips -
#status
#tech_menu -
#trips_form -
