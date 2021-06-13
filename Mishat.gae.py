print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")

Select = input("Please select any one of the above operators from 1 to 5: ")

x = float(input("Enter your number(base number for power): "))
y = float(input("Enter your number again(power for the power operator): "))

if Select == "1":
    Add = x + y
    print("Answer is", Add)

elif Select == "2":
    Subtract = x - y
    print("Answer is", Subtract)

elif Select == "3":
    Multiply = x * y
    print("Answer is", Multiply)

elif Select == "4":
    Divide = x / y
    print("Answer is", Divide)

elif Select == "5":
    Power = x ** y
    print("Answer is", Power)

else:
    print("Invalid number")
print("Hameem gay fuck")
