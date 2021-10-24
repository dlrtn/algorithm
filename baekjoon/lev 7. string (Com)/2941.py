str = input()
sum = 0
sum = str.count('c=') + str.count('c-') + str.count('dz=') + str.count('d-') + str.count('lj') + str.count('nj') + str.count('s=') + str.count('z=')
print(len(str)-sum)