# creating a calculator in python
# defining functions

def add (a,b):
    res = (a+b)
    print (res)

def sub (a,b):
    res = (a-b)
    print (res)

def mult (a,b):
    res = (a*b)
    print (res)

def div (a,b):
    res = (a/b)
    print (res)

# user inputs
try :
     a = float(input("write your first number: "))
     op = input("what do you want to do: ")
     b = float(input("write your sec number:"))

except ZeroDivisionError :
        print ("division by zero is not possible")
except ValueError :
        print ("try to use numbers")
except Exception :
        print ("something went wrong...")

    #a= int(input("write your first number: "))
    #b= int(input("write your sec number:"))
    #op = input("what do you want to do: ")


# results
try :
    if op=="+":
        add (a,b)
    elif op=="-":
        sub (a,b)
    elif op=="*":
        mult (a,b)
    elif op=="/":
        div (a,b)
    else :
          print ("something went wrong")

except ZeroDivisionError :
    print ("division by zero is not possible")
except ValueError :
    print ("try to use numbers")
except Exception :
    print ("something went wrong...")

finally :
    print ("end")

