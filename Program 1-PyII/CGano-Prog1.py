#Cara Gano
#CIT 244 Program 1

class contactClass(object):
    
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def getContactList(self):
        self.fullName = self.fname + " " + self.lname
        return(self.fullName, self.email)


def displayContacts(contacts):
    if len(contacts) > 0:
        print()
        print("%-15s %15s" % ("Name", "E-mail"))
        for c in contacts:
            print("%-15s %15s" % c.getContactList())
    else:
        print()
        print("No contacts have been added yet.")
        
def addContact(contacts):
    try:
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        email = input("Enter e-mail address: ")
        contacts.append(contactClass(fname, lname, email))
    except ValueError:
        print('Data entered is invalid.')

    return contacts

#def deleteContact(contacts, lname):
    #try:
        #for c in contacts:
            #if lname == lname:
                #contacts.remove(c)
                #print('Contact removed from list.')
                #print()
    #except:
        #print("Something went wrong, check spelling.")
    #return contacts

def main():
    contacts = []

    while True:
        print("""
        Menu options.  Choose 1, 2 or 3
            1. Display all contacts
            2. Add new contact
            3. Save and quit
        """)

        opt = input("Enter option 1, 2 or 3: ")

        if opt == "1":
            displayContacts(contacts)

        elif opt == "2":
            contacts = addContact(contacts)

        #elif opt == "3":
            #print
            #lname = input("Enter last name of contact to delete: ")
            #contacts = deleteContact(contacts, lname)

        elif opt == "3":
            print("Goodbye")
            print()
            break

        else:
            print("Invalid entry, please re-enter you choice")
            print()
main()

    
