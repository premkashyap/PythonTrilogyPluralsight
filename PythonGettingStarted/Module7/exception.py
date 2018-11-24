import sys
import os

def convert_to_int(x):
    try:
        i = int(x)
        return i
    except (ValueError, TypeError) as e:
        print("Conversion Failed {}.".format(str(e)), file=sys.stderr)
        #raise #to re raise the exception

def sqrt(x):
    if x < 0:
        raise ValueError("Can't find the square root of negative number {}".format(x))
    guess = x
    i = 0
    while guess*guess !=x and i< 20:
        guess = (guess + x/guess)/2.0
        i+=1
    return guess

def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print("Operation Failed: {}", e)
    finally:
        os.chdir(original_path)

def main():
    print(convert_to_int("10"))
    print(convert_to_int("prem"))
    print(convert_to_int([1,2,3]))
    print(sqrt(25))
    try:
        print(sqrt(-1))
    except ValueError as e:
        print(e, file = sys.stderr)

if __name__ == '__main__':
    main()