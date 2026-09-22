def simple_generator():
    yield 10
    yield 20
    yield 30


gen = simple_generator()


print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
