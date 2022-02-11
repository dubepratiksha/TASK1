#to Accept Student Details-Rollno,Name,percent and display 
dict ={}
 
dict1 = {1: [1,'pratiksha', 60],
     2: [2, 'neha', 70],
     3: [3, 'riddhi', 80],
     }

print ("{:<10} {:<10} {:<10}".format('rollno', 'name', 'percantage'))

for key, value in dict1.items():
    rollno, name, percentage = value
    print ("{:<10} {:<10} {:<10}".format(rollno, name, percentage))