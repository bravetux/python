import csv

rlist=csv.reader(open("D:\\Data1.csv", "r"))
fp = open("D:\\Data.txt",'a')

#Convert the CSV file to List
rlist =list(rlist)

for i in range(1, len(rlist)):
    print("ID: ", rlist[i][0], "\nOld Number: ", rlist[i][1], "\nNew Number: ", rlist[i][2], "\nOld Temp: ", rlist[i][3], "\nNew Temp: ", rlist[i][4], "\n")

fp.close()

exit(0)
