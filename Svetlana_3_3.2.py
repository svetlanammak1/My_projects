## Step 1:
beatles = []
print("Beatles: ",beatles)
## Step 2:
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Beatles: ",beatles)
## Step 3:
for i in range(2):
    New1 = input("Enter new person: ")
    beatles.append(New1)
print(beatles)    
## Step 4:
del beatles[-1]
del beatles[-1]
print("Beatles: ",beatles)
## Step 5:
beatles.insert(2,"Ringo Starr")
print("Beatles: ",beatles)