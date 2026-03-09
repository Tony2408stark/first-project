# Ohm's Law Calculator
# V = I * R

print("Ohm's Law Calculator")
print("--------------------")

print("Choose what you want to calculate:")
print("1. Voltage (V)")
print("2. Current (I)")
print("3. Resistance (R)")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    I = float(input("Enter Current (I) in Amps: "))
    R = float(input("Enter Resistance (R) in Ohms: "))
    V = I * R
    print("Voltage =", V, "Volts")

elif choice == 2:
    V = float(input("Enter Voltage (V) in Volts: "))
    R = float(input("Enter Resistance (R) in Ohms: "))
    I = V / R
    print("Current =", I, "Amps")

elif choice == 3:
    V = float(input("Enter Voltage (V) in Volts: "))
    I = float(input("Enter Current (I) in Amps: "))
    R = V / I
    print("Resistance =", R, "Ohms")

else:
    print("Invalid choice")
