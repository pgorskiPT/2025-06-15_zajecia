from idlelib.colorizer import prog_group_name_to_tag

generator_1=[x for x in range(5)]
print(generator_1)
print(type(generator_1))


generator_2=(x for x in [1,2,3,4,5])
print(generator_2)
print(type(generator_2))


print(next(generator_2))
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))

def generator_3():
    for x in [1, 2, 3 , 4, 5]:
        yield x
print(10*"=")
g3=generator_3()
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))

print(10*"=4")
def gen4():
    i=1
    while True:
        yield i *1
        i +=1

g4 =gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))

print(10*"=Fibo")
def fibo():
    a,b=0,1
    while True:
        yield b
        a,b = b, a+b
fib1=fibo()
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))


print(10*"=FiboIn")
# for i,n in fibo_with_index(10):
#     print(f"Pozycja{i},element{n}")
#
# fibo3=fibo_with_index(10)
# print(list(fibo3))
#
#
# for i in fibo3:
#     print(i)


def counter(start=0):
    n=start
    while True:
        result = yield n
        print(result)
        if result =="stop":
            break
        n+=1

c=counter(20)
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(c.send("Ok"))

try:
    print (c.send("stop"))
except StopIteration:
    print("Koniec")