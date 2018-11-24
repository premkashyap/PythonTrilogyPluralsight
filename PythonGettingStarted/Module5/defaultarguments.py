import time
def banner(string, upperborder = "-", lowerborder= "#"):
    print(upperborder*len(string))
    print(string)
    print(lowerborder*len(string))

banner("Prem")
banner("Prem Kashyap", "*")
banner("Prem", lowerborder="!", upperborder="~") #named arguements. Can be called in any order. but should be after the sequential arguments

def show_default(default=time.ctime()):
    print(default)

# time.sleep(2)
# print(time.ctime())
# time.sleep(2)
# show_default() # default is evaluated at the time of definition
# show_default()
# time.sleep(2)
# print(time.ctime())

def add_menu(menu=[]):
    menu.append("sausages")
    print(menu)

add_menu() #sausage once
add_menu() #sausage twice
add_menu(["bread", "bacon"]) #sausage once
add_menu(["biryani"]) #sausage once

#so only use immutable object as default arguements. Else follow below pattern
def add_menu_correctly(menu=None):
    if(menu is None):
        menu = []
    menu.append("sausage")
    print(menu)

add_menu_correctly() #sausage once
add_menu_correctly() #sausage twice
add_menu_correctly(["bread", "bacon"]) #sausage once
add_menu_correctly(["biryani"]) #sausage once
