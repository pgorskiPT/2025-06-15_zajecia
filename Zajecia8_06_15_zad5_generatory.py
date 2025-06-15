def count_down(min):
    count =min
    while count>0:
        yield count
        count -=1

def count_up_to(max):
    count =1
    while count<=max:
        yield count
        count +=1



c_u = count_up_to(3)
c_d= count_down(3)


# for n in c_u:
#     print(n)
# for n in c_d:
#     print(n)

def combine(gen1, gen2):
    yield from gen1
    yield from gen2
# najpierw przeiteruje od 1 do 3 wg gen1 rosnaca o potem od wartosci max w dół wg gen2.
c = combine(c_u, c_d)

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))






