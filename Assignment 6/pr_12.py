# Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part

# Accept a complex number from user
complex_num = complex(input("Enter a complex number: "))

# Check if real part is greater than imaginary part
if complex_num.real > complex_num.imag:
    print("Real part is greater")
else:
    print("Imaginary part is greater")