from pprint import pprint as pp
def hyper_volume(*lengths):
    print(lengths)
    print(type(lengths))
    seq = iter(lengths)
    v= next(seq)
    for len in seq:
        v*=len
    print(v)

def hyper_volume(length, *lengths):
    v= length
    for len in iter(lengths):
        v*=len
    return v

def tag(name, **attributes):
    print(attributes)
    print(type(attributes))
    result = '<' + name
    for key, val in attributes.items():
        result += ' {k} = "{v}" '.format(k = key, v= str(val))
    result +='>'
    return result

def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)

def print_args_from_itr(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

def print_args_from_dict(kwarg1, kwarg2, **kwargs):
    print(kwarg1)
    print(kwarg2)
    print(kwargs)

seq = (1,2,3,4,5)
print_args_from_itr(*seq)
dic = {'kwarg1':"red", 'kwarg2' :'blue', 'kwarg3':"yellow"}
print_args_from_dict(**dic)
    

hyper_volume(10,20)
hyper_volume(10)
hyper_volume(2,3,5)

print(tag('img', src="prem.jpg", border =1, alt = "Prem Kashyap"))
print_args(1,2,3,4,5, kwarg1 ="Prem", kwarg2="Anita", kwarg3="Raghu", kwarg4="Mili")


sunday = [20,21,22,23,22,21]
monday = [22,23,34,24,23,21]
tuesday =[21,21,22,24,23,22]
days =[sunday, monday, tuesday]

for item in zip(*days):
    pp(item)