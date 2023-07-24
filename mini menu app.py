import pymysql


#global varibale

db=None
cur=None

def connectDB():
    global db,cur
    db= pymysql.connect(host='localhost',
                        user='root',
                        password='',
                        database='python')

    cur=db.cursor()

def disconnectDB():
    cur.close()
    db.close()

def readallDB():
    connectDB()
    query='select * from student' # all the data will be fetched and get stor
    cur.execute(query)
    result=cur.fetchall()      #this fetch all function will gives u all the data 
##    cur.execute(result)
    for i in result:
        print(f'ID : {i[0]} Name : {i[1]} Marks : {i[2]}')
    disconnectDB()



def search(id):
    connectDB()
    cur.execute(f'select * from student where Id={id}')
    result=cur.fetchone()
    print(f'ID:{result[0]} Name :{result[1]} Marks:{result[2]}')
    disconnectDB()


def insertDB(id,name,marks):
    connectDB()
    cur.execute(f'insert into student values ({ID}, "{name}", {marks})')
    db.commit()
    disconnectDB()


def deleteDB(id):
    connectDB()
    cur.execute(f'delete from student where ID={id}')
    db.commit()
    disconnectDB()

def updatename(id,name):
    connectDB()
    cur.execute(f'update student set Sname="{name}" where ID={id} ')
    db.commit()
    disconnectDB()

def updatemarks(id,marks):
    connectDB()
    cur.execute(f'update student set Marks="{marks}" where ID={id} ')
    db.commit()
    disconnectDB()

while True:
    print('''Select your operation to perform:
            1. Display all records
            2. Search record
            3. Inser a record
            4. Delete a record
            5. Update record
            0. Exxit ''')
    choice=int(input('Enter the operation of your '))
    if choice==0:
        break
    elif choice==1:
        readallDB()

    elif choice==2:
        ID=int(input('enter the id : '))
        search(ID)

    elif choice==3:
        ID=int(input('enter the id : '))
        Name=input('enter the name : ')
        Marks=float(input('enter the marks : '))
        insertDB(ID,Name,Marks)
        
    elif choice==4:
        ID=int(input('enter the id : '))
        deleteDB(ID)
    elif choice==5:
        ID=int(input('enter the id : '))
        print('''What do you want to update?
                        1.Name
                        2.Marks ''')

        ch=int(input('Enter Your choice: '))
        if ch==1:
            Name=input('Enter New Name to Update: ')
            updatename(ID,Name)
        elif ch==2:
            Marks=input('Enter your New Marks : ')
            updatemarks(ID,Marks)
        else:
            print('Enter Correct Option')


    else:
        print('Invalid Decision')
            
        
    

              
        
            
            
            



