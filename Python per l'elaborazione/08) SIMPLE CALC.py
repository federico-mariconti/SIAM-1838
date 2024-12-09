print("Super calc!")
a=int(input("primo numero: "))
b=int(input("secondo numero: "))
somma=a+b
prod=a*b
diff=a-b
div1=a/b
div2=a//b
modulo=a%b
potenza=a**b

print(f"{a}+{b}={somma}")
print(f"{a}*{b}={prod}")
print(f"{a}-{b}={diff}")
print(f"{a}/{b}={div1}")
print(f"{a}/{b}={div2} divisione intera senza virgola")
print(f"{a}%{b}={modulo} resto della divisione")
print(f"{a}**{b}={potenza}")