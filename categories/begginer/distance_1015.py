import math
x_1,y_1 = input().split()
x_2,y_2 = input().split()
x_dif = (float(x_1)-float(x_2))**2
y_dif = (float(y_1)-float(y_2))**2
dist = math.sqrt(x_dif+y_dif)

print('{:.4f}'.format(dist))



