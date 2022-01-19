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

a= int(input("write your first number: "))
b= int(input("write your sec number:"))
op = input("what do you want to do: ")

# results

if op=="+":
    add (a,b)
elif op=="-":
    sub (a,b)
elif op=="*":
    mult (a,b)
elif op=="/":
    div (a,b)
else:
    print("invalid user input")
