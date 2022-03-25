import csv;
f= open("C:/Users/33622/Documents/Auchan/Integration/GIT/Pyhton/monFichier.csv")
myReader = csv.reader(f)
for row in myReader:
    print(row)
