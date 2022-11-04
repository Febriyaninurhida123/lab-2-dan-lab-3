print ("bilangan acak yang lebih kecil dari o.5")
import random
n = int ( input ("masukan nilai:"))
a = 0
for c in range (n) :
    a+= 1
    b = random.uniform(.0, .5)
    print("data ke:", a, "==>", b)

print ("selesai")
