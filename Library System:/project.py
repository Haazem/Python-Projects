
Books = []
Users = []
users_books = {10  : ["cpp" , "C#"], 20 :  ["SQL"]}       

def dummy_data_books():
    #book = [id , name , quantity , Number_of_borrowed]
    print('Books Loaded') 
    Books.append([10 , 'cpp' , 2 , 0 ])
    Books.append([20 , 'python' , 2 , 0])
    Books.append([30 , 'c#' , 2 , 0 ])
    Books.append([40 , 'SQL' , 2 , 0 ])
    Books.append([50 , 'Data' , 1 , 0])
    Books.append([60 , 'Data Analysis' , 1 , 0])   
    Books.append([70 , 'Data Science' , 1 , 0])   
   

def dummy_data_users():
    #user = [id , name , NoBorrow]
    print("Users Loaded")
    Users.append([10 , "Zezo" , 2 , False])
    Users.append([20 , "Omar" , 1 , False])
    Users.append([30 , 'Nour' , 0 , False])

    
class Book:
    
    def __init__(self , id , name , total_quantity):
        print("Book Class")
        self.id = id 
        self.name = name 
        self.total_quantity = total_quantity 
        book = [self.id , self.name , self.total_quantity , 0 ]
        Books.append(book)
        
    def get_name(self ):
        return self.name
    
    def set_name(self , name):
        self.name = name 
        
    def get_id(self):
        return self.id
    
    def set_id (self , id ):
        self.id = id 
        
    def get_quantity(self):
        return self.quantity
    
    def set_quantity(self , q):
        self.quantity = q 
        
    def get_total_borrowed(self):
        return self.total_borrow

    def set_total_borrowed(self , num):
        self.total_borrow += num 
        
    
class User:
    
    
    def __init__(self , id , name ):
        print("User Class")
        self.id = id 
        self.name = name
        #ID Name NoBorrow
        user= [self.id , self.name , 0] 
        Users.append(user) 
        
    def get_name(self ):
        return self.name
    
    def set_name(self , name):
        self.name = name
        
    def get_id(self):
        return self.id
        
    def set_id(self , id):
        self.id = id

    def user_profile(self):
        print("Your Name " + self.get_name())
        print("Your ID "+str(self.get_id()) )
        print("User Books are :" , end = ' ')
        self.get_user_books()
        
    def get_user_books(self , id):
        print("User Books: ")
        for i in range(len(self.user_list_book[id])):
            print("Book " + str(i + 1) + " " + self.user_list_book[id][i])
            
  
class Admin_View():
    
    #Add User 
    #Add Book
    #print profile
    #Borrow Books
    #Return Books
    def __inti__(self ):
        pass
        
    def Add_Book(self , id , name , total_quantity ):
        #book = [id , name , quantity , total_borrowed]
        Book(id , name , total_quantity)
      
    def Add_New_User(self , id , name ):
        #user = [id , name , NoBorrow]
        User(id , name  )
    
     
    def borrow_book(self):
        user_name  = input("Enter user Name : ").lower()
        user_id = int(input("Enter user Id (you should enter number ): "))
        Book_name = input("Enter Book Name: ").lower()
        #print(user_name , user_id , Book_name)
        
        ok = True
        #book = [id , name , quantity , 0]
        #user = [id , name , NoBorrow , ISUser]

        for i in range(len(Books)):
            if str(Books[i][1]).lower() == str(Book_name).lower() :
                #check Qantity > 0 
                if (Books[i][2] - Books[i][3] == 0 ):
                    ok = False
                    break
                else :
                    ok = True
                    #decrease Book Borrow with 1  
                    Books[i][3] += 1
                    break
        print(ok)                
        if ok :
            #Mark User Borrow Book
            #user = [id , name , NoBorrow , ISUser]  
            for i in range(len(Users)):
                if str(Users[i][1]).lower() == str(user_name).lower() :
                    #print("Yes: " + str(Users[i][0]) +  " " + Book_name)
                    if user_id not in users_books:
                        new_list = [Book_name]
                        users_books[user_id] = new_list
                        print("Book Borrowed")
                        break
                    else:
                        users_books[user_id].append(Book_name)
                        Users[i][2] += 1
                        print("Book Borrowed")
                        break
                    
                
            
    def return_book(self):
        #Inc Book Qunatity with 1 
        #Mark User Return Book
        user_name  = input("Enter user Name: ").lower()
        user_id = int(input("Enter user Id (you should enter number ): "))
        Book_name = input("Enter Book Name: ").lower()
        ok = True
        #book = [id , name , quantity , 0]
        #user = [id , name , NoBorrow , ISUser]

        for i in range(len(Books)):
            if str(Books[i][1]) == str(Book_name).lower() :
                #print(Books[i][1] , Book_name)
                #Dec Book Borrow with 1 
                Books[i][3] -=1
                break
            
        #Mark User returned Book
        #user = [id , name , NoBorrow , IsUser]
        #Remove Book from user Books
        ok = False
        for i in range(len(Users)):
            #Mark User returned Book
            if Users[i][0] == user_id and str(Users[i][1]).lower() == str(user_name).lower():
                #print(Users[i])
                Users[i][2] -=1
                ok = True
                break
            
        if ok :
            for j in users_books[user_id]:
                if str(j).lower() == str(Book_name).lower():
                    users_books[user_id].remove(j)
                    print("Book Returned")
                    break 
        
    
    def users_borrow_book(self):
        #Book_name
        #user naem 
        users_borrow_books =[]
        for i , j  in users_books.items():
            for k in Users:
                #users_books = {10  : ["cpp" , "C#"], 20 :  ["SQL"]}       
                #if user_id in useres_books = user_id in users
                if  k[0] == i :
                    j.insert(0 , str(k[1]).capitalize() )
                    print(j )
                    break 
                

    
class Library_System(Admin_View):
    
    #Borrow Book
    #Return Book
    #Books 
    def __inti__(self):
        print('Library system')
        
    def load_Book(self):
        return dummy_data_books()
    
    def load_User(self):
        return dummy_data_users()
    
    
    def print_options(self ):
        print("program options:")
        print("1) Add Book")
        print("2) Print Library Books")
        print("3) print Books By Prefix")
        print("4) Add User")
        print("5) Borrow Book")
        print("6) Return Book")
        print("7) Print users Borrowed Book")
        print("8) Print Users")
        #Need to check validation
        #Take user input
        user_input = int(input("Enter Your Choice from [1:8]: "))
        
        return user_input
    
    def run(self):
        while True:
            print(" ")
            user_choice = self.print_options()
            if user_choice == 1 :
                self.add_book()
            elif user_choice == 2 :
                self.Print_Library_Books()
            elif user_choice == 3 :
                pre = input("Enter Book Name Prefix: ").lower()
                self.print_books_by_prefix(pre)
            elif user_choice == 4 :
                self.Add_User()
            elif user_choice == 5 :
                self.Borrow_book()
            elif user_choice == 6 :
                self.Return_book()
            elif user_choice == 7 :
                self.Print_users_Borrowed_Book()
            elif user_choice == 8 :
                self.PrintUsers()
            else :
                break
            
    
    def add_book(self):
        print("Enter Book Info:")
        book_id = int(input("Enter Book ID: "))
        book_name = input("Enter Book Name: ")
        total_quantity = int(input("Enter Total Quantity: "))
        self.Add_Book(book_id , book_name , total_quantity)
    
    def Print_Library_Books(self):
        #book = [id , name , quantity , 0]
        for i in range(len(Books)):
            print(str(i + 1) + " Book name " + str(Books[i][1]).capitalize() , "Book ID " + str(Books[i][0]) + 
                  " Total Quantity " + str(Books[i][2]) + "   Total Borrowed " + str(Books[i][3]))
            print("-"*10)
    
    def print_books_by_prefix(self , pre):
        #book = [id , name , quantity , 0]
        for  i in Books:
            if str(i[1]).lower().startswith(pre):
                print(i[1])
            
    
    def Add_User(self):
        print("Enter User Info:")
        user_name = input("Enter Name: ")
        user_Id = int(input("Enter User ID: "))
        self.Add_New_User(user_Id , user_name)
        
    def Borrow_book(self):
        self.borrow_book()
    
    def Return_book(self):
        self.return_book()
    
    def Print_users_Borrowed_Book(self):
        self.users_borrow_book()
    
    def PrintUsers(self):
        for i in range(len(Users)):
            #user = [id , name , NoBorrow]
            print("User No " + str(i + 1) + " User Name " +Users[i][1] + " User ID " + str(Users[i][0])
                  + " Number of Books borrowed " + str(Users[i][2]))
            print("-"*10)
    
        
#System       
l1 = Library_System()

#To Load Data  
l1.load_Book()
l1.load_User()
print(" ")

#To Run program
l1.run()

