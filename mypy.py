""" my python, not done yet.  """

def decor(func):
    def wrap():
        print("===========================================================================")
        func()
        print("===========================================================================")
    return wrap

def greet():
    print("Hello!!!")
    print("keep trying, you still suck...")
    print("keep trying, you still suck...".replace("suck", "stink"))

#@decor
def end():
        print("end app")

#renamed the ver decorated, to greet
#greet = decor(greet)
greet()

@decor
def mytext()
try:
    filename = input("Enter filename: ")
   # print(text)
    with open(filename, "r") as f:
    #print(mytext)
        text = f.read()
    print(text)
except:
    print("error")
finally:
    f.close()

mytext()
end()



""" Gibson, S. Ghost... 8-8-2016 """
