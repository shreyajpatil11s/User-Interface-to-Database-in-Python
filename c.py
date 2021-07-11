import csv  
import pandas as pd 


fields = ['CollegeID','CollegeName','CourseType','City','Fees','PinCode']
    
#Part (a) entering user input into a csv file
x=1
print("enter number of entries\n")
y= int(input()) 
while(x<=y):
	CollegeID=[]
	num = input("enter college id\n")
	CollegeName=[]
	name = input("enter college name\n")
	CourseType=[]
	num1 = input("enter course type number\n")
	City=[]
	name1= input("enter your city\n")
	Fees=[]
	num2 = input("enter fee amount\n")
	PinCode=[]
	num3 = input("enter your pincode\n")
	x=x+1


rows = [num,name,num1,name1,num2,num3]

filename = "file.csv"
with open(filename, 'a') as csvfile:  
	 
    csvwriter = csv.writer(csvfile)  
        
    csvwriter.writerow(fields)  
   
    csvwriter.writerow(rows)

#Part (b) Finding colleges in Mumbai:

print("Do you want to check the colleges in mumbai??\n""Check the result file for colleges in Mumbai\n""Thank you")

with open("file.csv", "r") as input, open ("result.txt","w") as result:
     testfilereader = csv.DictReader(input) 
     City = 'mumbai'
     fieldnames = testfilereader.fieldnames
     testfilewriter = csv.DictWriter(result, fieldnames, delimiter=',',)
     testfilewriter.writeheader()      
     for row in testfilereader:
         if row['City'] == City:
            testfilewriter.writerow(row)

# Part (c) Delete a record based on CollegeID 
print("Deleting rows with CollegeID 555")
md = pd.read_csv('file.csv')
md = md.set_index("CollegeID")
md = md.drop("555",axis=0)