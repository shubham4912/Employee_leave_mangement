#Assign employee under manger

from emp1 import*
class manger():
    def __init__(self):
        self.mang_data={}
    def  assign_emp_under_mang(self,data):
        if not self.mang_data:
            print("check employee data")
            mang=[]
            emp=[]
            for k in data.keys():
                if data[k]["position"]=="manger":
                    mang.append(k)
                else:
                    emp.append(k)
            print("Manger are{}".format(mang))
            print("Employees are{}".format(emp))
            if len(mang)==0:
                print("Manger is not avilable fist add manger")
            else:
                print("Enter the manger id want to assign employee")
                mang_id=int(input())
                if mang_id in mang:
                    mang.remove(mang_id)
                    print("Enter employee id want to assign under manger ({})".format(mang_id)) 
                    emp_id=int(input())
                    if emp_id in emp:
                        emp.remove(emp_id)
                        d1=data.get(emp_id)
                        self.mang_data[mang_id]=[{emp_id:d1}] 
                while True:
                    if len(emp)!=0:
                        print("Do you want to assign more employee under same manger press y else assign employee under another manger press o ")
                        op=input()
                        if op=="y":
                            print("avilable employee: ",emp)
                            emp_id=int(input("Enter employee id want to assign  under manger({mang_id}) : ").format(mang_id))
                            if emp_id in emp:
                                emp.remove(emp_id)
                                d1=data.get(emp_id)
                                l=self.mang_data.get(mang_id)
                                l.append({emp_id:d1})
                                if len(emp)!=0:
                                    continue
                                else:
                                    break
                            else:
                                print("enter the wrong employee id please try again")
                                break
                        elif op =="o":
                            print("avilable employee: ",emp)
                            print("Enter the manger id want to assign employee")
                            mang_id2=int(input())
                            if mang_id2 in mang :  
                                mang.remove(mang_id2) 
                                print("Enter employee id want to assign under manger ({})".format(mang_id2)) 
                                emp_id=int(input())
                                if emp_id in emp:
                                    emp.remove(emp_id)
                                    d1=data.get(emp_id)
                                    self.mang_data[mang_id2]=[{emp_id:d1}]
                                    
                                    while True:
                                        if len(emp)!=0:
                                            print("Do you want to assign more employee under same manger press y else press n")
                                            op=input()
                                            if op=="y":
                                                print("avilable employee: ",emp)
                                                emp_id=int(input("Enter employee id want to assign  under manger({}}) : ").format(mang_id2))
                                                if emp_id in emp:
                                                    emp.remove(emp_id)
                                                    d1=data.get(emp_id)
                                                    l=self.mang_data.get(mang_id2)
                                                    l.append({emp_id:d1})
                                                    if len(emp)!=0:
                                                        continue
                                                    else:
                                                        break
                                                    
                                            else:
                                                break
                                        else:
                                            break
                            else:
                                print("Enter the wrong manger id")
                                break
                        else:
                            print("Enter the wrong option")
                            break
                    
                    else:
                        print("employee is assign undr RA manger")
                        break
                return self.mang_data
        else:
            self.s=self.assign_emp(data)
            return self.s

    def assign_emp(self,data):
        
        mang=[]
        emp=[]
        for k in data.keys():
            if data[k]["position"]=="manger":
                mang.append(k)
            else:
                emp.append(int(k))
       # print("check employee data",emp)
        print(" manger is",mang)
        mang1=[]
        emp1=[]
        for k,v in self.mang_data.items():
            mang1.append(k)
            for i in v:
                for j in i:
                    emp1.append(int(j))
        #print("check employee data",emp1)
        #print("check manger data",mang1)
                
        emp2=[]
        for ele in emp:
            if ele not in emp1:
                emp2.append(ele)

        print("employee remening to assign under manger is ",emp2)

        print("enter manger id want to assing employee")
        man_id=int(input())
        if man_id in mang1 :
            print("enter the employee id")
            emp_id=int(input())
            if emp_id in emp2:
                emp2.remove(emp_id)
                d1=data.get(emp_id)
                l=self.mang_data.get(man_id)
                l.append({emp_id:d1})
                
        elif man_id in mang :
            print("enter the employee id")
            emp_id=int(input())
            if emp_id in emp2:
                emp2.remove(emp_id)
                d1=data.get(emp_id)
                self.mang_data[man_id]=[{emp_id:d1}]
        else:
            print("Enter the wrong id" )
        return self.mang_data

    def approve_leave(self,id,res,l,data):
      #  print(f"Employee {id} is apply for {res}")
        mang=[]
        emp=[]
        for k,v in data.items():
            if data[k]["position"]=="manger":
                mang.append(k)
            else:
                emp.append(k)
   
        mang1=[]
        emp1=[]
        for k,v in self.mang_data.items():
            mang1.append(k)
            for i in v:
                for j in i:
                    emp1.append(int(j))
        if id in emp1:
           # print(f"Employee {id} is apply for {res}")
            print(f"Employee {id} apply for {l} day of {res}")
            c=0
            for k,v in self.mang_data.items():
                for i in v:
                    e=self.mang_data[k][c]
                    c+=1
                    for j in i:
                        if id ==int(j):
                            print(f"Employee {id} working under {k} manger")
                            #check employee leave
                            print("Employee avilable leave are",e[id]["leave"])
                            l2=e[id]["leave"]
                            if l2>=l:
                                print(f"manger({k}) approve or reject a leave")
                                dec=input()
                                if dec=="yes":
                                    l3=l2-l
                                    e[id]["leave"]=l3
                                   # print("Manger data: ",self.mang_data)
                                    return "yes"
                                elif dec =="no":
                                    return "no"
                c=0       
        elif id in mang:
            print(f"Manger ({id}) apply for {l} day of {res}")
            print("manger avilable leave are",data[id]["leave"])
            l2=data[id]["leave"]
            if l2>=l:
                print("Enter approve or reject a leave")
                dec=input()
                if dec=="yes":
                    l3=l2-l
                    data[id]["leave"]=l3
                    # print("Manger data: ",self.mang_data)
                    return "yes"
                elif dec =="no":
                    return "no"
   
        elif id in emp:
            print("Employee is not assign under manger first assign Ra manger")
            return "no"

    def remove_emp(self,id):
        mang1=[]
        emp1=[]
        for k,v in self.mang_data.items():
            mang1.append(k)
            for i in v:
                for j in i:
                    emp1.append(int(j))
        if id in emp1:
            #print(f"Employee {id} is removed")
            c=0
            for k,v in self.mang_data.items():
                for i in v:
                    e=self.mang_data[k][c]
                    c+=1
                    for j in i:
                        if id ==int(j):
                            del e[j]
                            return self.mang_data
                c=0            


        elif id in mang1:
            del self.mang_data[id] 
            return self.mang_data
        else:
            pass

    def rem_mang(self,id):
        if id in self.mang_data:
            del self.mang_data[id]
            return self.mang_data

    def print_info(self):
        if not self.mang_data:
            print("Not add any employee under manger")
        else:
            c=0
            for k,v1 in self.mang_data.items():
                print("Employee Working under manger {} is: ".format(k))
                das="-"*63
                print(das)
                print("{:<15}|  {:<10}|  {:<18}|  {:<10}".format("Employee Id","Name","position","leave"))
                das="-"*63
                print(das)
                for i in v1:
                    d=self.mang_data[k][c]
                    c=c+1
                    for j in i:
                        s=int(j)
                        name=d[s]["name"]
                        position=d[s]["position"]
                        leave=d[s]["leave"]
                        
                        print ("{:<15}|  {:<10}|  {:<18}|  {:<10}".format(s, name,position,leave))
                das="-"*60
                print(das)

            c=0
