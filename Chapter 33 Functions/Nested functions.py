#Nested functions:

def disp():
    def show():
        print("show function")
    print("Disp function")
    show()

disp()
print("------------------")

#2nd ex:
def disp():
    def show():
        return "show function"
    result=show()+"Disp function"
    return result

print(disp())
