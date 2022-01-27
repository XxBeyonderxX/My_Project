import mysql.connector as a

con = a.connect(host="localhost",user="root",passwd="12345678",database="school")
c=con.cursor() 
def scr():
   n=input("Student Name :")
   c = input("Class : ")
   r = input("Roll No : ")
   m = input("Marks : ")
   s = input("Status : ")
   data=(n,c,r,m,s)
   ad='insert into scorecard values(%s,%s,%s,%s,%s)'
   c=con.cursor()
   c.execute(ad,data)
   con.commit()
   print("Data Entered Successfully")
   print(">——————————————————————————————————–<")
   main()
def sct():
    c = input("Class Name : ")
    r = input("Roll No : ")
    data = (c,r)
    sql = 'delete from scorecard where Class = %s and Roll_no = %s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data Updated')
    print('>——————————————————————————————————–<')
    main()
def dscr():
    cl = input("Class : ")
    data = (cl,)
    sql = "select * from scorecard where class = %s"
    c = con.cursor()
    c.execute(sql,data)  
    d = c.fetchall()           
    for i in d:
        print("NAME : ",i[0])
        print("CLASS : ",i[1])
        print("ROLL NO: ",i[2])
        print("MARKS: ",i[3])
        print("STATUS : ",i[4])
        print(">————————————–<")
    print(">——————————————————————————————————–<")
    main()
    
def ast():
   n = input("Student Name : ")
   c = input("Class : ")
   r = input("Roll No : ")
   a = input("City : ")
   p = input("Phone : ")
   data = (n,c,r,a,p)
   sql = 'insert into student values(%s,%s,%s,%s,%s)'
   c=con.cursor()
   c.execute(sql,data)
   con.commit()
   print("Data Entered Successfully")
   print(">——————————————————————————————————–<")
   main()
   
def rst():
    c = input("Class Name : ")
    r = input("Roll No : ")
    data = (c,r)
    sql = 'delete from student where Class = %s and Roll_no = %s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data Updated')
    print('>——————————————————————————————————–<')
    main()

def addt():
    n = input("Teacher : ")
    p = input("Post : ")
    s = input("Salary : ")
    a = input("City : ")
    ph = input("Phone : ")
    ac = input("Account : ")
    data = (n,p,s,a,ph,ac)
    sql = 'insert into teacher values(%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">——————————————————————————————————–<")
    main()

def remt():
    n = input("Teacher Name : ")
    ac = input("Account No : ")
    data = (n,ac)
    sql = 'delete from teacher where Name = %s and Account = %s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">——————————————————————————————————–<")
    main()

def abclass():
    d = input("Date : ")
    cl = input("Class : ")
    ab = input("Names of Absent Students : ")
    data = (d,cl,ab)
    sql = "insert into cattendance values(%s,%s,%s)"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">——————————————————————————————————–<")
    main()

def abteacher():
    d = input("Date : ")
    ab = input("Names of Absent Teacher : ")
    data = (d,ab)
    sql = "insert into tattendance values(%s,%s)"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">——————————————————————————————————–<")
    main()

def submitf():
    n = input("Student Name : ")
    c = input("Class Name : ")
    r = input("Roll No : ")
    m = input("Month and Year : ")
    f = input("Fees : ")
    d = input("Date : ")
    data = (n,c,r,m,f,d)
    sql = 'insert into fees values(%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">——————————————————————————————————–<")
    main()

def pays():
    n = input("Teacher Name : ")
    m = input("Month : ")
    p = input("Yes / No : ")
    data = (n,m,p)
    sql = 'insert into salary values(%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">——————————————————————————————————–<")
    main()

def dclass():
    cl = input("Class : ")
    data = (cl,)
    sql = "select * from student where class = %s"
    c = con.cursor()
    c.execute(sql,data)  
    d = c.fetchall()           
    for i in d:
        print("NAME : ",i[0])
        print("CLASS : ",i[1])
        print("ROLL : ",i[2])
        print("ADDRESS : ",i[3])
        print("PHONE : ",i[4])
        print(">————————————–<")
    print(">——————————————————————————————————–<")
    main()

def dteacher():
    sql = "select * from teacher"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("NAME : ",i[0])
        print("POST : ",i[1])
        print("SALARY : ",i[2])
        print("ADDRESS : ",i[3])
        print("PHONE : ",i[4])
        print("ACNO : ",i[5])
        print(">————————————–<")
    print(">——————————————————————————————————–<")
    main()
try:
   c.execute('create table student(Name char(40),Class varchar(3),Roll_no int primary key not null,City char(20),Phone int)')
   c.execute('create table teacher(Name char(40),Post char(30),Salary int,City char(20),Phone int,Account int primary key not null)')
   c.execute('create table cattendence(Date varchar(50),Class varchar(30),Absentees char(20))')
   c.execute('create table tattendence(Date varchar(50),Absentees char(20))')
   c.execute('create table fees(Name char(40),Class varchar(3),Roll_no int primary key not null,Month varchar(30),Fees int)')
   c.execute('create table salary(Name char(40),Month varchar(30),Paid char(4))')
   c.execute('create table scorecard(Name char(40),Class varchar(3),Roll_no int primary key not null,Marks_in_percentage int,Status char(15))')
   def main():
      print("""                                   St.John's Academy

                            1.  ADD STUDENT                 2.  REMOVE STUDENT

                            3.  ADD SCORECARD               4.  REMOVE SCORECARD
                            
                            5.  ADD TEACHER                 6.  REMOVE TEACHER

                            7. CLASS ATTENDANCE             8.  TEACHER ATTENDANCE

                            9. SUBMIT FEES                  10.  PAY SALARY

                            11. DISPLAY CLASS               12. TEACHERS LIST

                                           13. DISPLAY SCORECARD
                            
      """)

      choice = input("Enter Task No : ")
      print(">————————————–<")
      if (choice == '1'):
           ast()
      elif (choice=='2'):
           rst()
      elif (choice=='5'):
           addt()
      elif (choice=='6'):
           remt()
      elif (choice=='7'):
           abclass()
      elif (choice == '8'):
           abteacher()
      elif (choice=='9'):
           submitf()
      elif (choice =='10'):
           pays()
      elif (choice == '11'):
           dclass()
      elif (choice == '12'):
           dteacher()
      elif (choice == '13'):
           dscr()    
      elif (choice == '3'):
           scr()
      elif (choice == '4'):
           sct()
      else:
          print(" Wrong choice")
          main()
   def pswd():
      p=input("Password : ")
      if p=="qwerty":
            main()
      else:
            print("Wrong Password  ")
            pswd()
   pswd()
   
except:
   def main():
      print("""                                   St.John's Academy

                            1.  ADD STUDENT                 2.  REMOVE STUDENT

                            3.  ADD SCORECARD               4.  REMOVE SCORECARD
                            
                            5.  ADD TEACHER                 6.  REMOVE TEACHER

                            7. CLASS ATTENDANCE             8.  TEACHER ATTENDANCE

                            9. SUBMIT FEES                  10.  PAY SALARY

                            11. DISPLAY CLASS               12. TEACHERS LIST

                                           13. DISPLAY SCORECARD
                            
      """)

      choice = input("Enter Task No : ")
      print(">————————————–<")
      if (choice == '1'):
           ast()
      elif (choice=='2'):
           rst()
      elif (choice=='5'):
           addt()
      elif (choice=='6'):
           remt()
      elif (choice=='7'):
           abclass()
      elif (choice == '8'):
           abteacher()
      elif (choice=='9'):
           submitf()
      elif (choice =='10'):
           pays()
      elif (choice == '11'):
           dclass()
      elif (choice == '12'):
           dteacher()
      elif (choice == '13'):
           dscr()    
      elif (choice == '3'):
           scr()
      elif (choice == '4'):
           sct()
      else:
          print(" Wrong choice")
          main()
   def pswd():
      p=input("Password : ")
      if p=="qwerty":
           main()
      else:
           print("Wrong Password  ")
      pswd()
   pswd()
