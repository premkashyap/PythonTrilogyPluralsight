def sequence_class(immutable):
    return tuple if immutable else list

seq = sequence_class(immutable=True)
t = seq("ABCDEFG")
print(t)
print(type(t))
seq = sequence_class(immutable=False)
t = seq("ABCDEFG")
print(t)
print(type(t))