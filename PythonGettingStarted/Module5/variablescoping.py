count = 5

def show_count():
    print('count ', count)

def set_count(c):
    count = c

def set_count_global(c):
    global count
    count= c

show_count()
set_count(10)
show_count()
set_count_global(10)
show_count()