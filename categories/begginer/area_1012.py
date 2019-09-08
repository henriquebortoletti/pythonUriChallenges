line = input()
line = line.split()
a = float(line[0])
b = float(line[1])
c = float(line[2])

triangulo = a*c/2
circulo = 3.14159*c**2
trapezio =  (a+b)*c/2
quadrado = b**2
retangulo = a*b

print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))



