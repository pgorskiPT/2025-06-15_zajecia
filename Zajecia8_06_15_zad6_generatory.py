import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        stat_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - stat_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper

def genertor_danych(dane):
    for element in dane:
        yield element
def przetworz_dane(dane):
    return [element for element in dane if element %2 ==0 ]

@measure_time
def stworz_raport(dane):
    for element in genertor_danych(dane):
        print(f"Raport dla systemu {element}")

dane= range(100_000)
prz_dane=przetworz_dane(dane)
stworz_raport(dane)
