from Customer import Customer
from Talking import Talking
from Lines import Line
from cRoute import Croute
import pyodbc

database = "pythonDB"
server = "DESKTOP-T3AHI49"
print("Connecting to SQL SERVER...")
print("Loading...")
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';')
print("Connection Succeed")
cursor = connection.cursor()
connection.autocommit = False

'''add customer to db by input from user'''
def addCustomerByInput():
    customer = Customer(
        input("Enter your Id: "),
        input("Enter your first name: "),
        input("Enter your last name: "),
        input("Enter your address: "),
        input("Enter your country: ")
    )
    countRow = cursor.execute("INSERT INTO Customer(CustomerId,CustomerName,CustomerLast,CustomerAddress,CustomerCountry) "
                              "VALUES('" + customer.CustomerId + "','" + customer.CustomerName + "','" + customer.CustomerLast + "','" + customer.CustomerAddress + "','" + customer.CustomerCountry + "')").rowcount
    print(str(countRow) + " row effected")
    # def updateRoute():
    connection.commit()
    cursor.close()
    connection.close()

'''add customer by const data'''
def addCustomer():
    countRow = cursor.execute(
        "INSERT INTO Customer (CustomerId,CustomerName,CustomerLast,CustomerAddress,CustomerCountry) values ('111','gal','levi','sha','IL')").rowcount
    print(str(countRow) +" row effected")
    connection.commit()
    cursor.close()
    connection.close()

'''update cost '''
def updateCost():
    countRow = cursor.execute("UPDATE cRoute set Cost=Cost*102/100 where Cost<30").rowcount
    print(str(countRow) + " row effected")
    connection.commit()
    cursor.close()
    connection.close()

def deleteTalking():
    phoneToDelete = input("Enter your phone to delete the talks: ")
    countRow = cursor.execute("DELETE FROM talking WHERE FromPhone =" + phoneToDelete).rowcount
    print(str(countRow) + " row effected")
    connection.commit()
    cursor.close()
    connection.close()

# addCustomerByInput()
# addCustomer()
# updateCost()
# deleteTalking()
'''add talking by input from user'''
def addTalking():
    talking = Talking(
        input("enter StartDate: "),
        input("enter EndDate: "),
        input("enter your phone: "),
        input("enter memeber phone: ")
    )
    countRow=cursor.execute("INSERT INTO Talking(StartDate,EndDate,FromPhone,ToPhone)VALUES('" + talking.StartDate + "','" + talking.EndDate + "','" + talking.FromPhone + "','" + talking.ToPhone +"')").rowcount
    print(str(countRow) +" row effected")
    connection.commit()
    cursor.close()
    connection.close()
# addTalking()
'''get all talks of customer by phone'''
def getTalkingByPhone(YourPhone):
    cursor.execute("SELECT StartDate,EndDate,FromPhone,ToPhone from Talking where FromPhone="+ YourPhone)
    all = cursor.fetchall()
    talkingList = []
    for i in all:
        talkingList.append(Talking(i[0], i[1], i[2], i[3]))
    for i in talkingList:
       print(i)
    connection.commit()
    cursor.close()
    connection.close()
# getTalkingByPhone('0548466119')
'''get cost of all talks by customer ID'''

def getcost(yourCode):
    cursor.execute("select SUM(DATEDIFF(MINUTE,StartDate, EndDate))*c.Cost s from talking t  join lines l  on t.FromPhone =l.Phone join cRoute c on l.CrouteCode= c.CrouteCode where  FromPhone like (select Phone l from lines where CustomerCode={})group by c.Cost".format(yourCode))
    result = 0
    all = cursor.fetchall()
    for i in all:
        result = i[0]
    print(result)
    connection.commit()
    cursor.close()
    connection.close()
# getcost(60)
'''get num of lines to any route '''
def getCountLinesOfAnyRoute():
    cursor.execute("select COUNT(Phone),c.WaysName from lines l join cRoute c on l.CrouteCode=c.CrouteCode group by c.WaysName")
    all = cursor.fetchall()
    for i in all:
        print("route: "+i[1]+" ,count lines: " +str(i[0]))
    connection.commit()
    cursor.close()
    connection.close()
# getCountLinesOfAnyRoute()
'''check if was an exception from the correct minutes'''
def exceptionCheck(PhoneT):
    cursor.execute("select c.MinuteHere -SUM(DATEDIFF(MINUTE,StartDate, EndDate)) from talking t join lines l on t.FromPhone=l.Phone join cRoute c on l.CrouteCode= c.CrouteCode where FromPhone = {} group by c.MinuteHere".format(PhoneT))
    result=0
    all=cursor.fetchall()
    for i in all:
        result=i[0]
    if result<0:
        print("Was exception")
    else:
        print("Wasn't exception")
# exceptionCheck('0548466119')