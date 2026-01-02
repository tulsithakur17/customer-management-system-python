#BLL
import pickle
import pymysql
import json

class Customer:
    cus_list=[]     
    con=pymysql.connect(host="localhost",user="root",password="1723@july",database="cusdb")
    cur=con.cursor()
    def __init__(self):
        self.id=0       
        self.name=0     
        self.age=0      
        self.mob=0      
    def addCustomer(self):  
        Customer.cus_list.append(self)
        qry=f"insert into custb values('{self.id}','{self.name}','{self.age}','{self.mob}')"
        Customer.cur.execute(qry)
        Customer.con.commit()
    def searchCustomer(self):   
        qry=f"select * from custb where id={self.id}"
        Customer.cur.execute(qry)
        data=Customer.cur.fetchone()
        self.name=data[1]
        self.age=data[2]
        self.mob=data[3]
        # for e in Customer.cus_list:
        #     if(e.id==self.id):
        #         self.name=e.name    
        #         self.age=e.age
        #         self.mob=e.mob
        #         return1
        # else:
        #     raise ValueError("ID Not Found")

    def deleteCustomer(self):   
        qry=f"delete from custb where id={self.id}"
        Customer.cur.execute(qry)
        Customer.con.commit()
        # for e in Customer.cus_list:
        #     if(e.id==self.id):
        #         Customer.cus_list.remove(e)
        #         return
    def modifyCustomer(self):    
        qry=f"update custb set name='{self.name}',age='{self.age}',mob='{self.mob}' where id={self.id}"
        Customer.cur.execute(qry)
        Customer.con.commit()
        # for e in Customer.cus_list:
        #     if(e.id==self.id):
        #         e.name=self.name
        #         e.age=self.age
        #         e.mob=self.mob
        #         return
    @staticmethod
    def saveToPickle():
        f=open("C:\\Tulsi\\cmspickle.txt","wb")
        pickle.dump(Customer.cus_list,f)
        f.close()

    @staticmethod
    def loadFromPickle():
        f = open("C:\\Tulsi\\cmspickle.txt", "rb")
        Customer.cus_list=pickle.load(f)
        f.close()
    @staticmethod
    def convertToDict(obj):
        return obj.__dict__
    @staticmethod
    def saveToJSON():
        f = open("C:\\Tulsi\\cmsjson.txt", "w")
        json.dump(Customer.cus_list, f,default=Customer.convertToDict)
        f.close()
    @staticmethod
    def convToCust(d):     
        cus=Customer()
        cus.id=d["id"]
        cus.name=d["name"]
        cus.age=d["age"]
        cus.mob=d["mob"]
        return cus
    @staticmethod
    def loadFromJSON():
        f = open("C:\\Tulsi\\cmsjson.txt", "r")
        Customer.cus_list = json.load(f,object_hook=Customer.convToCust)
        f.close()

#PL
if(__name__=="__main__"):
    def showCustomer(cus):      
        print("Cust ID:",cus.id,"Cust Name:",cus.name,"Cust Age:",cus.age,"Cust Mob:",cus.mob)
    def showCus_tuple(e):
        print("Cust ID:", e[0], "Cust Name:", e[1], "Cust Age:", e[2], "Cust Mob:", e[3])
    print("Welcome to Tulsi's CMS")

    while(1):
            choice=input("Enter Choice:1 for Add Cust,"
                         "2 for Search Cust, 3 for Delete Cust,"
                         "4 for Modify Cust, 5 Display All, "
                         "6 for Exit, 7 Write Data in Pickle,"
                         "8 Load data from pickle, 9 Write Data in JSON,"
                         "10 Load data from JSON:")
            if(choice=="1"):    #Customer Add
                try:
                    cus=Customer()  
                    cus.id=input("Enter Cust Id:")  
                    cus.name=input("Enter Cust Name:")  
                    cus.age=input("Enter Cust Age:")    
                    cus.mob=input("Enter Cust Mob:")    
                    cus.addCustomer()   
                    print("Customer Added Successfully")
                except Exception as err:
                    print("Error!",err)
            elif(choice=="2"):   #Search Customer
                try:
                    cus=Customer()  
                    cus.id=input("Enter Customer ID:")  
                    cus.searchCustomer()
                    showCustomer(cus)       
                except Exception as err:
                    print("Error!",err)
            elif(choice=="3"):  #Delete Customer
                try:
                    cus=Customer()      
                    cus.id=input("Enter cust id to delete:")    
                    cus.deleteCustomer()
                    print("Customer Deleted Successfully")
                except Exception as err:
                    print("Error!",err)
            elif (choice == "4"):  # Modify Customer
                cus = Customer()  
                cus.id = input("Enter cust id to modify:")  
                cus.name=input("Enter Cust Updated Name:") 
                cus.age = input("Enter Cust Updated Age:")  
                cus.mob = input("Enter Cust Updated Mob:")  
                cus.modifyCustomer()
                print("Customer Modified Successfully")
            elif (choice == "5"):  # Display All Customers
                qry="select * from custb"
                Customer.cur.execute(qry)
                data=Customer.cur.fetchall()
                for e in data:
                    showCus_tuple(e)

                # for e in Customer.cus_list:
                #     showCustomer(e)
            elif (choice == "6"):  # Exit
                print("Thanks for using Tulsi's CMS")
                break
            elif(choice=="7"):      #Write Data in a Pickle Format file
                Customer.saveToPickle()
                print("Data Saved in Pickle Format Successfully")
            elif (choice == "8"):  # Load Data from Pickle Format file
                Customer.loadFromPickle()
                print("Data Retrieved from Pickle Format Successfully")
            elif(choice=="9"):      #Write Data in a JSON Format file
                Customer.saveToJSON()
                print("Data Saved in JSON Format Successfully")
            elif (choice == "10"):  # Load Data from JSON Format file
                Customer.loadFromJSON()
                print("Data Retrieved from JSON Format Successfully")

            else:
                print("Incorrect Choice")
