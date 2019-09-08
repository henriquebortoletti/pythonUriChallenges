def greatest(a,b):
    return (a+b+abs(a-b))/2

a,b,c = input().split()

maior = greatest(int(a),int(b))
maior = int(greatest(maior,int(c)))


print(str(maior)+' eh o maior')

