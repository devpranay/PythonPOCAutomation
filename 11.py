"""11. Update and format data in Excel spreadsheets of any size"""
import csv
def write():
    """this is write function"""
    with open("csv_file1.csv","w", newline="",encoding="utf8") as file:
        fieldnames=["emp_id","emp_name","emp_salary"]
        obj=csv.DictWriter(file,fieldnames=fieldnames)
        obj.writeheader()
        obj.writerow({"emp_id":21241,"emp_name":"srinitha","emp_salary":50000})
        obj.writerow({"emp_id":21251,"emp_name":"swathi","emp_salary":40000})
        obj.writerow({"emp_id":21261,"emp_name":"sailu","emp_salary":30000})
        def update():
            obj.writerow({"emp_id": 21271, "emp_name": "shiva", "emp_salary": 20000})
        update()

if __name__=="__main__":
    write()
