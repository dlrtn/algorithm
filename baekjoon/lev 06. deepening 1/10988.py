string = input()

origin = list(string)
reverse = list(string)
reverse.reverse()

if origin == reverse:
    print(1)
else:
    print(0)