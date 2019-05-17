import pymongo

client = pymongo.MongoClient("mongodb://vinnybanshiwal:vinny@cluster0-shard-00-00-fogac.mongodb.net:27017,cluster0-shard-00-01-fogac.mongodb.net:27017,cluster0-shard-00-02-fogac.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.vb_db

def add_employee(idd, first, last, pay):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.vb_col.insert_one(
            {
            "id" : idd,
            "first" : first,
            "last" : last,
            "pay" : pay
            })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.vb_col.find()
    for i in user:
        print (i)




add_employee(1,'Sylvester', 'Fernandes', '50000')
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)

fetch_all_employee()