# Create a generator to produce first n even natural numbers

def even_produce(n):
    for num in range(2, 2*n+1, 2):
        yield num


for e in even_produce(int(input("Enter a number: "))):
    print(e)