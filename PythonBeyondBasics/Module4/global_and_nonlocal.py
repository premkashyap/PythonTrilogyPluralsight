global_msg = 'Message Global hai'
global_msg_for_change = "Global"

def enclosing():
    global_msg = 'Message ka naam global hai lekin yeh local hai'
    enclosing_msg = 'Message enclosed hai'
    enclosing_msg_for_change = 'enclosing_msg_for_change'
    global global_msg_for_change
    global_msg_for_change = "Local"
    def inner():
        global_msg = "Message ka naam global hai lekin yeh inner hai"
        enclosing_msg = "Message ka naam enclosing hai lekin yeh inner hai"
        nonlocal enclosing_msg_for_change
        enclosing_msg_for_change= "Inner"
    print(global_msg) 
    print(enclosing_msg)
    print(global_msg_for_change)
    print(enclosing_msg_for_change)
    inner()
    print(global_msg) 
    print(enclosing_msg)
    print(global_msg_for_change)
    print(enclosing_msg_for_change)

print(global_msg) 
print(global_msg_for_change)
enclosing()
print(global_msg) 
print(global_msg_for_change)


import time

def make_timer():
    last_called = None
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now-last_called
        last_called = now
        return result

