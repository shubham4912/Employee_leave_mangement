import mang
class emp:
    def __init__(self):
        self.emp_info={}
        self.emp_leave=10
        self.mang_data={}
    def emp_id(self):
        while True:          
            try:
                emp_id=int(input("Enter the employee id: "))
                l=str(emp_id)
                if len(l)<5:
                    break
                else:
                    print("Enter employee id less than 5 digit")
            except ValueError:
                print("Plese enter valid Employee Id accept only digit")
        return emp_id
    def emp_name(self):
        while True:
            emp_name=input("Enter the employee name : ")
            if emp_name.isalpha():
                break
            else:
                print("please enter the valid name")
        return emp_name
    def emp_post(self):
        print("Enter the employee position :\n 1.manger\n 2.Softer Engineer\n 3.Hardware Engineer\n 4.Trainee Engineer")
        while True:
            try:
                op=int(input("Enter above option: "))
                if op==1:
                    emp_position="manger"
                    break
                elif op ==2:
                    emp_position="software engineer"
                    break
                elif op ==3:
                    emp_position="Hardware engineer"
                    break
                elif op==4:
                    emp_position="Trainee engineer"
                    break
            except ValueError:
                print("plase enter valid option")

        return emp_position
       

    # Add employ information into dictionery
    def add_emp(self):
        id=self.emp_id()                     # get employee id
        name=self.emp_name()                 # get employee name
        emp_position=self.emp_post()         # get employee position
        if not self.emp_info:
            self.emp_info.update({id:{"name":name,"position":emp_position,"leave":self.emp_leave}})  #add information into dictionery according to employee Id
        else:
            if  id in self.emp_info.keys():
                print("Enter employee id alredy exist")
            else:
                self.emp_info.update({id:{"name":name,"position":emp_position,"leave":self.emp_leave}})
      #  print("Add employee successfully")
        return self.emp_info
    
    #add employee as manger
    def add_manger(self):
        if not self.emp_info:
            print("First add employee")
        else:
            print("Enter the ID of employee want to make as manger")
            id=int(input())
            if id in self.emp_info:
                m1=self.emp_info.get(id)
                m2=m1.get("position")
                if m2 != "manger":
                    m1["position"]="manger"
                    #print(m1)
                    return self.emp_info
                else:
                    print("{} he is alradey manger".format(id))
            
            else:
                print("Employee ID is invalid")
    
    #Assign employee under Manger 
    def assingn_emp_under_mang(self):
        if not self.emp_info:
            print("First add employee")
        else:
            d=m.assign_emp_under_mang(self.emp_info)
       #print(d)
            return d
    
    # Remove employee
    def rem_emp(self):
        if not self.emp_info:
            print("First add employee")
        else:
            print("Enter the employee id to remove: ")
            id=int(input())
            if id in self.emp_info:
                del self.emp_info[id]
                print("Remove employee Success")
            else:
                print("Id of employee in invalid")
            
            r=m.remove_emp(id)
            return self.emp_info
    #Remove employee as manger
    def rem_manger(self):
        if not self.emp_info:
            print("First add employee")
        else:
            print("Enter the ID of employee want to remove as manger")
            id=int(input())
            if id in self.emp_info:
                m1=self.emp_info[id]["position"]
                if m1 == "manger":
                    self.emp_info[id]["position"]="Senior Engineer"
                    #return self.emp_info
                else:
                    print("he is not a manger")
                    #return self.emp_info
            else:
                print("Employee ID is invalid")
            r=m.rem_mang(id)
            return self.emp_info
    #Apply leave employee
    def apply_leave(self):
        if not self.emp_info:
            print("First add employee")
        else:
            print("Enter Id which employee want leave")
            id=int(input())
            if id in self.emp_info:
                l1=self.emp_info[id]["leave"]
                c=0
                while c<3:
                    try:
                        c +=1
                        print("Avilable leave is: ",l1)
                        print("How many day want to leave")
                        l=int(input( ))
                        if l>0:
                            if l<=l1:
                                print("resone want to leave\n 1. Sick leave\n 2. Casual Leave\n 3. optional leave\n")
                                op=int(input( ))
                                if op ==1:
                                    a=m.approve_leave(id,"sick leave",l,self.emp_info)
                                    #print(f"Employee {id} is apply for sick leave")
                                    if a=="yes":
                                        print("Leave is approved")
                                        ave_l=l1-l
                                        self.emp_info[id]["leave"]=ave_l
                                        print("remening leave is: ",ave_l)
                                        break
                                       
                                    elif a=="no":
                                        print("Sorry,Leave is not approve")
                                        break

                                elif op==2:
                                    a=m.approve_leave(id,"casual leave",l,self.emp_info)
                                    if a=="yes":
                                        print("Leave is approved")
                                        ave_l=l1-l
                                        self.emp_info[id]["leave"]=ave_l
                                        print("remening leave is: ",ave_l)
                                        break
                                    
                                    elif a=="no":
                                        print("Sorry,Leave is not approve")
                                        break

                                elif op==3:
                                    a=m.approve_leave(id,"optional leave",l,self.emp_info)
                                    if a=="yes":
                                        print("Leave is approved")
                                        ave_l=l1-l
                                        self.emp_info[id]["leave"]=ave_l
                                        print("remening leave is: ",ave_l)
                                        break
                                    elif a=="no":
                                        print("Sorry,Leave is not approve")
                                        break
                            else:
                                print("you don't have that much leave ")
                        else:
                            print("please Apply for more than 1 leave ")
                    except ValueError:
                        print("please try again")
                return self.emp_info
            else:
                print("You Enter wrong Employee Id")
    #see information of employee
    def print_info(self):
        if not self.emp_info:
            print("First add employee")
        else:
            das="-"*70
            print(das)
            print("{:<15}|  {:<15}|  {:<20}|  {:<10}|".format("Employee Id","Name","position","leave"))
            das="-"*70
            print(das)
            for k,v in self.emp_info.items():
                name=v["name"]
                position=v["position"]
                leave=v["leave"]
            #  print(name,position,leave)
                print ("{:<15}|  {:<15}|  {:<20}|  {:<10}|".format(k, name,position,leave))
            das="-"*70
            print(das)

if __name__=="__main__":
    e=emp()
    m=mang.manger()
    while True:
        print("Enter the option\n 1. add employee\n 2. remove employee\n 3. make employee as manger\n 4. remove employee from manger\n 5. Assingn employee under RA manger\n 6. apply leave\n 7. see information employee data\n 8. see employee assign info\n 9. End program ")  
        try:
            option=int(input("Enter option "))
            if option == 1:
                e1=e.add_emp()
                #print(e1)
                e.print_info()
            elif option ==2:
                e1=e.rem_emp()
                #print(e1)
                e.print_info()
            elif option ==3:
                e1=e.add_manger()
                e.print_info()
                #print(e1)
            elif option ==4:
                e5=e.rem_manger()
                e.print_info()
               # print(e5)
            elif option==5:
                e6=e.assingn_emp_under_mang()
                m.print_info()
            elif option ==6:    
                e1=e.apply_leave()
                e.print_info()
                #print(e1)
            elif option ==7:
                e.print_info()
            elif option ==8:
                m.print_info()
            elif option ==9:
                break
            else :
                print("Enter the valid option")
        except ValueError:
            print("Enter the valid option option")