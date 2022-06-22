def kinetic_energy(m, v):
    ke = (m * v**2) / 2
    return ke


m = float(input("Enter the mass of the object in kilograms : "))
v = float(input("Enter the velocity of the object in meters per second : "))
ke = kinetic_energy(m, v)
print(f"The kinetic energy of the object is {ke:.2f} joules.")
