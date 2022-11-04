from types import MappingProxyType


print("======Latihan 2======")
print("menampilkan bilangan, berhenti ketika bilangan 0, dan menampilkan bilangan terbesar")

max = 0
while True:
    angka = int(input("masukan bilangan : "))
    if max < angka:
        max = angka
    if angka==0:
        break
print ("bilangan terbesarnya adalah = ", max)
print ("======selesai======")
