# Create a generator to produce first n odd natural numbers

def odd_produce(n):
   for num in range(1, 2*n+1, 2):
       yield num

for e in odd_produce(int(input("Enter a number: "))):
    print(e)