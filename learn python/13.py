#                                                Variable-Length Arguments

def adf (a,b):
    return a + b
x = adf(2,2) # 2,2 is called arguments   and 2 argumentnu kodlebeku

print(x) 


def ading(*num):            #                            * >>> args
    print(num)
    print(type(num)) # gives tuple

ading(5,4,3,2,1)  


def adition (*w):

    return sum(w)

print(adition(5,5,10))




# notes copy 

def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total_sum(1, 2, 3, 4)) 



numbe = [1,2,3,4]
print(*numbe)  # output : 1 2 3 4   *numbe unpack the list



#                                                 **kwargs  (keyword arguments)

def bros_info(**detail):
    print(detail)

    for key, value in detail.items():
        print(f"{key} : {value}")

bros_info(name = "tejas", age = 20, car = "BMW \\\M4 cs" ,love = "none")
bros_info(name = "RAJu", age = 22, car = "ROLS_ROYCE",)

                 # kwargs gives dictionary   




#                                                  lambda Functions
# A lambda function is a small anonymous function that can take any number of arguments but has only one expression.


adnum = lambda a,b : a+b # performing one simple task
print(adnum(5,5))

mark  = lambda m : 2*m # performing one simple task
print(mark(100)) 

#  

stud = [ 
    {"name" : "tejas" , "marks" : 40 },
    {"name" : "chidu" , "marks" : 80},
    {"name" : "sharath", "marks" : 90}
] 

stud.sort(key= lambda x: x["marks"] , reverse= True)

print(stud)  
 


#v                                                          Recursion

# a funtion call itself calld recurtion 

#   Recursion occurs when a function calls itself. It's used to solve problems that can be broken down into smaller, similar problems.


def fact (n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(4))


#                                                             Nested Functions

def bro_car (a,b):
    
    def bro1(a):
        print(f"BRO CHIDU HAve {a}")
    def bro2(b):
        print(f"bro raju have {b}")

    bro1("Supra")
    bro2("RR")

print(bro_car(2,2))