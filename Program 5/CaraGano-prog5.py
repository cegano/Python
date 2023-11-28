import sqlite3


def addTicket(cur, conn):
    act_spd = int(input('Speed recorded: '))
    post_spd = int(input('Speed limit: '))
    age = int(input('Age: '))
    vio_sx = input('Sex(Enter Male or Female): ')

    data = (None, act_spd, post_spd, age, vio_sx)
    sql = "INSERT INTO tickets VALUES (?, ?, ?, ?, ?)"

    cur.execute(sql, data)

    conn.commit()


def displayAllTickets(cur):
    sql = "SELECT * FROM tickets"
    cur.execute(sql)

    results = cur.fetchall()

    if results:
        printResults(results)
    else:
        print('Data not found')
        print()


def displayTicketsBySex(cur):
    vio_sx = input("Search by offender sex as 'Female' or 'Male': ")
    if vio_sx != "Female":
        vio_sx = "Male"

    try:
        sql = "SELECT * FROM tickets WHERE violator_sex = ?"

        cur.execute(sql, (vio_sx,))
        results = cur.fetchall()

        if results:
            printResults(results)
        else:
            print('Sex of offender not found')
            print()


    except sqlite3.Error as error:
        print(str(error), 'Error occured')
        print("No data found.")

def printResults(data):
    
    print("%-6s %-13s %-10s %-9s %11s" % ('Ticket ID', 'Posted MPH', 'MPH Over', 'Age', 'Violator Sex'))
    
    for row in data:
            if row[2] != 0:
                mphOver = row[1] - row[2]
            else:
                mphOver = 0

            print(" %-10s %-8s %-15s %-7s %-2s " % (row[0], row[1], mphOver, row[3], row[4]))  

def main():
    conn = sqlite3.connect('tickets5.db')
    cur = conn.cursor()

    while True:

        print("""
            Menu options.  Choose 1, 2, 3 or 4
            1. Display all Tickets
            2. Add a Ticket
            3. Filter by Offender Sex
            4. Save & Exit
        """)

        opt= input("Enter your choice, 1, 2, 3 or 4: ")

        if opt == "1":
            displayAllTickets(cur)

        elif opt == "2":
            addTicket(cur, conn)

        elif opt == "3":
            displayTicketsBySex(cur)

        elif opt == "4":
            print()
            print("Goodbye")

            if conn:
                conn.close
            break
        else:
            print("Invalid entry, please choose from option 1-4.")
            print()


main()

        
