
# my_phone = Phone()

# from oop2 import Phone
from csv import DictReader

with open("file1.csv","r") as rf:
    csv_reader = DictReader(rf,delimiter=",")
    for i in csv_reader: # csv_reader will result the value row-wise
        print(i["name"])


from csv import DictWriter
# newline ="" --> is to remove the space
with open("file2.csv","w",newline="") as wf:
    csv_writer = DictWriter(wf,fieldnames=["name","contact","address","dob"])
    csv_writer.writeheader()
    # two ways to write data in csv file
    #1 --> writerow --> take single row at one time
    #2 --> writerows --> take multiple rows in list
    csv_writer.writerow(
        {"name":"write-row-Ram","contact":"9845","address":"ktm","dob":"7 july"}
        )

    csv_writer.writerows([
        {"name":"Kiran","contact":"9845","address":"ktm","dob":"7 july"},
        {"name":"Sita","contact":"9845","address":"ktm","dob":"7 july"},
        {"name":"Ram","contact":"9845","address":"ktm","dob":"7 july"},
        {"name":"Ram","contact":"9845","address":"ktm","dob":"7 july"},
        ])