def ToggleCase(string):
    s=""
    for char in string:
        s+=chr((ord(char)^(1<<5)))
    return s
if __name__ == '__main__':
    string=input()
    print(ToggleCase(string))