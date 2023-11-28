#Program 4- Cara Gano

import csv

def readData():
    fields = ("name", "race1", "race2", "race3")
    f = open("runners.txt", "r")
    runners = []
    dReader = csv.DictReader(f, fieldnames = fields, delimiter = ",")

    for row in dReader:
        runners.append(row)
                             
    f.close()
    return runners

def displayData(racers):
    fs = "%-8s %-16s %7s %s"
    print(fs % ("Name", "Boston Marathon", "Chicago Marathon", "New York Marathon"))
    for r in racers:
        fs = "%-8s %-16s %-8s %5s"
        print(fs % (r['name'], r['race1'], r['race2'], r['race3']))

def getAvg(runners):
    race1 = 0
    race2 = 0
    race3 = 0
    name = input("Enter a racers name: ")

    for runner in runners:
        if name == runner['name']:
            bos = int(runner['race1'])
            chi = int(runner['race2'])
            ny = int(runner['race3'])

            avg = (bos + chi + ny) / 3
            print("The average of %s's marathon times is %d minutes" %(name, avg))
            break
        else:
            print("Name entered is not in list.")

def addRacer(racers):
    nom = input("Enter your name: ")
    rc1 = input("Enter time(in minutes) it took to finish Boston marathon: ")
    rc2 = input("Enter time(in minutes) it took to finish Chicago marathon: ")
    rc3 = input("Enter time(in minutes) it took to finish New York marathon: ")

    record = {'name': nom, 'race1': rc1, 'race2': rc2, 'race3': rc3}
    racers.append(record)
    return racers

def storeData(racers):
    fields = ("name", "race1", "race2", "race3")
    f = open("runners.txt", "w")
    dWriter = csv.DictWriter(f, fieldnames = fields, delimiter = ",", lineterminator = "\n")
    dWriter.writerows(racers)
    f.close()

def main():
    runner_log = readData()

    while True:
        print("""
            Menu options. Choose 1, 2, 3, or 4
            1. Display all data for all racers.
            2. Display a runners individual race average in minutes.
            3. Add a new runner and race data.
            4. Save and exit
            """)
        opt = input("Enter your choice, 1, 2, 3, or 4: ")

        if opt == "1":
            print()
            displayData(runner_log)
        elif opt == "2":
            getAvg(runner_log)
        elif opt == "3":
            runner_log = addRacer(runner_log)
        elif opt == "4":
            storeData(runner_log)
            print("Goodbye")
            print()
            break
        else:
            print("Invalid entry, please re-enter your choice")
            print()

main()





        

        
