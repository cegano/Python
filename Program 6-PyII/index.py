import sqlite3 as db
from bottle import route, run, request, template

@route('/', method = 'GET')
def index():
    data = {'title': 'Welcome!'}
    return template('welcome', data)



@route('/byDepartment', method = ['GET', 'POST'])
def department():
    if request.method == 'GET':
        return template('deptForm')
    else:
        dept = request.forms.get("dept")
        conn = db.connect("payroll.db")
        cur = conn.cursor()

        sql = '''SELECT pay_data.emp_id, emp_name, wage, hrs_worked FROM employees
                JOIN pay_data
                WHERE pay_data.emp_id = employees.emp_id AND employees.department = ?'''
        cur.execute(sql, (dept,))

        rows = cur.fetchall()
        cur.close()
        hrs = 0
        wage = 0

        if rows:
            dataList = []
            for row in rows:
                eid, name, wage, hrs = row
                if hrs <= 40:
                    pay = wage * hrs
                else:
                    ot_pay = (hrs - 40) * 1.5 * wage
                    pay = (wage * 40) + ot_pay

                emp = (eid, name, wage, hrs, pay)
                dataList.append(emp)

            data = {'rows': dataList, 'dept': dept}
            return template('show_department', data)
        else:
            msg = 'No such employee'

@route('/editHours', method = ['GET', 'POST'])
def editHours():
    if request.method == 'GET':
        return template('editHours')
    else:
        hrs = request.forms.get('hrs')
        eid = request.forms.get('eid')

        try:
            conn = db.connect('payroll.db')
            cur = conn.cursor()

            sql = '''UPDATE pay_data
                    SET hrs_worked = ?
                    WHERE emp_id = ?'''
            cur.execute(sql, (hrs, eid))
            
            conn.commit()
            cur.close()
            m = {'status': "successful"}
            return template('status', m)
        except:
            m = {'status': "not successful"}
            return template('status', m)

                        
        finally:
            cur.close
        
run(host='localhost', port=8080)
