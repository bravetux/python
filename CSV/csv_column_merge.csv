import csv

# Open the CSV file Data 1 and Data 2
reader = csv.reader(open("D:\Data1.csv", "r"))
writer = csv.reader(open("D:\Data2.csv", "r"))

# Convert the CSV file to List
rdata, wdata = list(reader), list(writer)

for i in range(1, len(rdata)):
    for j in range(1, len(wdata)):
        if (rdata[i][0] == wdata[j][0]):
            # Columns of SVIDs.csv
            # 0-ID	3-contents	5-contents	7-contents
            #print (rdata[j][0], rdata[j][3], rdata[j][5], rdata[j][7])
            #print (wdata[j][0], wdata[j][3], wdata[j][5], wdata[j][7])
            wdata[j][3] = rdata[i][3]  #Column 3
            wdata[j][5] = rdata[i][5]  #Column 5
            wdata[j][7] = rdata[i][7]  #Column 7

#Creates the Merged File Replacing Data2.csv with contents of Data1.csv
with open("D:\Merged.csv", "w", newline='') as newfile:
    wr = csv.writer(newfile, quoting=csv.QUOTE_ALL)
    wr.writerows(wdata)

exit(0)
