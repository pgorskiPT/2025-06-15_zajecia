import time


def kwadrat2(n):
    for x in range (n):
        yield x ** 2


kwa = kwadrat2(5)
print (kwa)
print(next(kwa))
print(next(kwa))
print(next(kwa))


print("zrob cokollwiek")
lista=[]
lista.append("123456")
print(lista)

print(next(kwa))
print(next(kwa))

kwa2 =kwadrat2(10)
kwa3=kwadrat2(20)

print(next(kwa2))
print(next(kwa3))
print(next(kwa2))
print(next(kwa2))
print(next(kwa3))
print(next(kwa2))


print(list(kwa3))


for i in kwadrat2(10):
    print(i)
    time.sleep(1)