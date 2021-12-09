## Example from CW: Svetlana
## Date: 08/12/2021 
## Task: The program  reads phone book from contacts.csv file  and writes out data into 
##        exported_contact.csv, exported_contact1.csv   files

import csv

class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Phone():
    def __init__(self):
        self.contacts = []

    def load_contacts_from_csv(self, file):
        with open(file, newline='') as csvfile:
            fieldnames =['Name', 'Phone'] 
            reader = csv.DictReader(csvfile, fieldnames) 

            for row in reader:
               #print(row) 
                self.contacts.append(PhoneContact(row['Name'], row['Phone']))  
         

    def search_contacts(self, phrase):
        count = 0
        for contact in self.contacts:
            if phrase.lower() in contact.name.lower()\
                or phrase in contact.phone:
                print('{0} {1}'.format(contact.name, contact.phone)) 
                count +=1
        if count ==0:
            print("No contact found!")        

phone = Phone()
phone.load_contacts_from_csv('contacts.csv')


phrase = input("Search contacts: ")
phone.search_contacts(phrase)

with open("exported_contact.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        
    writer.writerow(['Name', 'Phone'])
    writer.writerow(['mother','222-555-101'])
    writer.writerow(['father','222-555-102'])
    writer.writerow(['wife','222-555-103'])
    writer.writerow(['mother-in-law','222-555-104'])


with open("exported_contact1.csv", 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerow({'Name' : 'mother','Phone' : '222-555-101'})
    writer.writerow({'Name' : 'father', 'Phone' : '222-555-102'})
    writer.writerow({'Name' : 'wife', 'Phone' : '222-555-103'})
    writer.writerow({'Name' : 'mother-in-law', 'Phone' : '222-555-104'})
    writer.writerow({'Name' : 'grandmother, grandfather', 'Phone' : '222-555-104'})
                   