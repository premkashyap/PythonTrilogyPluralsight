file = open('file.txt', mode = 'wt', encoding='utf-8')
file.write('Notepad++ v7.5.6 enhancements & bug-fixes:\n\n')
file.write('1.  Fix macro playing back crash issue on new added "find previous" and "find next" buttons.')
file.write('2.  Function List enhancement: Highlight the current function based on cursor position.')
file.write('3.  Fix crash on styler dialog of User Defined Language dialog.')
file.write('4.  Fix file status detection issue under Windows XP.')
file.close()
file = open('file.txt', mode = 'rt', encoding='utf-8')
print(file.readline()) #Read line by line
print(file.read(10)) #Read 10 strings
file.seek(0)
print(file.readlines())

file = open('file.txt', mode = 'at', encoding='utf-8')
file.writelines([
    '5.  Ghost typing enhancement: Unicode, syntax highlighting and speed support.\n(check the url for the usage of ghost typing on command line: https://notepad-plus-plus.org/features/ghost-typing.html )\n',
    '6.  Add a message from outer space.'
])
file.close()
def readfile():
    file =  open('file.txt', mode = 'rt', encoding='utf-8')
    try:
        [print(line) for line in file]
    finally:
        file.close()
def readfilewith():
    with open('file.txt', mode = 'rt', encoding='utf-8') as f:
        [print(line) for line in f]

readfilewith()
