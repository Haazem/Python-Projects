
#To store patients     

patients = []

#To store status
#Normal = 0 , urgent = 1 , Super_urgent = 2 
type_status = ['Normal' , 'urgent' , 'super urgent']
status = {0 : 0 , 1 : 0 , 2 : 0 }

#To store Specialization
speializations = {}
for i in range(1 , 21):
    speializations[i] = 0 


#check user_choice
def chcek_user_choice(num):
    #if value not a digit
    if (str(num).isdigit() == False):
        return 1
    else:
        #if value valid 
        if int(num) >= 1 and int(num) <= 5 :
            return 2
        #if value not valid
        return 3
        
#create menu
def menu():
    print("Program optiens:")
    print("1) Add New Patient")
    print("2) Print all patients")
    print("3) Get Next Patient")
    print("4) Remove a leaving atient")
    print("5) End the program")
    
    user_choice = "" 
    while True:
        user_choice = input("Enter your choice[1 : 5] :")
        if (chcek_user_choice(user_choice) == 1 or chcek_user_choice(user_choice) == 3):
            print("Please Enter a valid value")
        else :
            break
            
    return int(user_choice)
            
def dummy():
    #specialization , name , status
    #l = [sp , name , st]
    patients.append(['1' , 'shady' , '1'])
    speializations[1]+=1
    status[1]+=1
    patients.append(['1' , 'asim' , '0'])
    speializations[1]+=1
    status[0]+=1
    patients.append(['1' , 'islam' , '1'])
    speializations[1]+=1
    status[1]+=1
    patients.append(['1' , 'sayed' , '2'])
    speializations[1]+=1
    status[2]+=1
    patients.append(['1' , 'hazem' , '0'])
    speializations[1]+=1
    status[0]+=1
    patients.append(['1' , 'mohamed' ,'1'])
    speializations[1]+=1
    status[1]+=1
    patients.append(['2' , 'ahmed' , '0'])
    speializations[2]+=1
    status[0]+=1
    patients.append(['2' , 'omar' , '1'])
    speializations[2]+=1
    status[1]+=1
    patients.append(['3' , 'zizo' , '2'])
    speializations[3]+=1
    status[2]+=1
    patients.append(['4' , 'tarek' , '2'])
    speializations[4]+=1
    status[2]+=1
    patients.append(['5' , 'hamed' , '1'])
    speializations[5]+=1
    status[1]+=1
    patients.append(['6' , 'ali' , '2'])
    speializations[6]+=1
    status[2]+=1
    patients.append(['7' , 'hazem' , '0'])
    speializations[7]+=1
    status[0]+=1
    patients.append(['7' , 'mona' , '2'])
    speializations[7]+=1
    status[2]+=1
    patients.append(['7' , 'alaa' , '1'])
    speializations[7]+=1
    status[1]+=1
    patients.append(['8' , 'emam' , '2'])
    speializations[8]+=1
    status[2]+=1
    patients.append(['8' , 'sasy' , '0'])
    speializations[8]+=1
    status[0]+=1
    patients.append(['8' , 'gaber' , '1'])
    speializations[8]+=1
    status[1]+=1
    
        
        
#Func To take patient input
def patient_input():
    sp =  name  =  st = ""
    #patient_info
    pat = []
    while True: 
        sp = (input("Enter Specialization [1:20]: "))
        name = input("Enter Your Name: ")
        st = (input("Enter Status Number [Normal = 0 , urgent = 1  , super urgent = 2]: "))
        if (is_valid(sp , st)):
            break
        else :
            print("Wrong Value in  specialization or name or status.")
            print("Please Enter Valid Values")
          
    sp = int(sp)
    st = int(st)
    
    if speializations[sp] == 10 :
        print("Sorry we can't accpet more patients")
    else :
        l = [sp , name , st]
        return l
        
#to check  specialization , status 
def is_valid(sp , st):
    ok = True
    if (str(sp).isdigit() == False or str(st).isdigit() == False):
        ok = False
    if int(sp) < 1 or int(sp) > 20:
        ok = False
    if (int(st) < 0 or int(st) > 2 ):
        ok = False
    return ok 
    
    
#Func to add patients
def Add_patient():
    ans = patient_input()
    st = int(ans[2])
    status[st] +=1
    sp = int(ans[0])
    speializations[sp]+=1
    patients.append(ans)


#func to print patient name , specialization , status
def patient_info(l):
    # pat = [name , sp , st]
    print("Specialization: " +  str(l[0]))
    print("Name: " + l[1])
    print("Status: "+ type_status[int(l[2])])
    
    
#func to update specialization & status  
def update_status_specialization(num1 , num2):
    speializations[num1] -=1 
    status[num2] -= 1
    
    
#print Next patient based on  specialization num 
def Get_Next_patient_based_on_status(num):
    
    #type_status = ['Normal' , 'urgent' , 'super urgent']
    #l = [sp , name , st]
    ok = False
    for i in patients:
        if int(i[0]) == num and int(i[2]) == 2 :
            print(i[1] + " go with Dr.")
            patients.remove(i)
            update_status_specialization(int(i[0]) , int(i[2]))
            ok = True
            break
    if ok == False:
        for i in patients:
            if int(i[0]) == num and int(i[2]) == 1 :
                print(i[1] + " go with Dr.")
                patients.remove(i)
                update_status_specialization(int(i[0]) , int(i[2]))
                ok = True
                break
            
    if ok == False:
        for i in patients:
            if int(i[0]) == num and int(i[2]) == 0 :
                print(i[1] + " go with Dr.")
                patients.remove(i)
                update_status_specialization(int(i[0]) , int(i[2]))
                ok = True
                break

  
def Get_Next_Patient():
    num = ""
    while True:
        num = (input("Enter Specialization Number [1:20]: "))
        if num.isdigit():
            if int(num) >= 1 and int(num) <= 20 :
                break
            else :
                print("Please enter valid value")
        else :
            print("Please enter valid value")
            
    if speializations[int(num)] > 0 :
        Get_Next_patient_based_on_status(int(num))
    
    else  :
        print("There are not patients in this specialization.")
    
    
def  Remove_Patient():
    patient_specialization = ""
    patient_name = ""
    #Take specialization&name 
    while True:
        patient_specialization = input("Enter Your Specialization Number: ")
        patient_name = input("Enter Your Name: ").lower()
        if patient_specialization.isdigit():
            if int(patient_specialization) >= 1 and int(patient_specialization) <= 20:
                break
            else:
                print("Enter Valid Value")
        else:
            print("Enter Valid Value")
             
    #l = [sp , name , st]
    ok = False
    for i in patients:
        if int(i[0]) == int(patient_specialization) and str(i[1]).lower() == patient_name:
            #remove patient with specialization , name
            print("Patient Removed Sucessfully")
            patients.remove(i)
            ok = True
            break
    if ok == False:
        print("No Patient with this name in this Specialization.")
            
    


#func to print patients based on specialization num & status_type    
def print_patients():
    #to store count of status
    status2_count = status1_count = status0_count = 0
    status_2 = int(status[2])
    status_1 = int(status[1])
    status_0 = int(status[0])
    for i in range(1 , 21):
        #l = [sp , name , st]
        #type_status = ['Normal' , 'urgent' , 'super urgent']

        if speializations[i] > 0:
            print("Specialization " + str(i) + " has " + str(speializations[i]) + " patients.")
            for j in patients:
                if int(j[0]) == i and int(j[2]) == 2 :
                    patient_info(j)
                    
            for j in patients:
                if int(j[0]) == i and int(j[2]) == 1 :
                    patient_info(j)
                    
            for j in patients:
                if int(j[0]) == i and int(j[2]) == 0 :
                    patient_info(j)
                    
                    
            print(" ")
           
        else :
            print("There are not patients in specialization "+ str(i)+'.')
    
    
def show():
    while True:
        choice = menu()
        if (choice == 1 ):
            Add_patient()
        elif (choice == 2 ):
            print_patients()
        elif (choice == 3 ):
            Get_Next_Patient()
        elif (choice == 4):
            Remove_Patient()
        else :
            print("End of the program")
            break
        

dummy()
show()
















