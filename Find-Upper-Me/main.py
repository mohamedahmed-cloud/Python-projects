import tabula,csv,sys
from collections import defaultdict
# Convert pdf file to csv
# Read a PDF File
df = tabula.read_pdf("main.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("main.pdf", "main.csv", output_format="csv", pages='all')
print(df)

# Read from CSV File 
with open("main.csv") as f:
        reader = csv.DictReader(f)
        grades = [line1['Total'] for line1 in reader]
n=0
yourGrade=int(input())
myDict=defaultdict(int)
for i in grades:
    if float(i)>=yourGrade:
        n+=1
    myDict[i]+=1
myDict=sorted(myDict.items())
# print(myDict)
print(myDict)
print(n)