mean_radi_dict = {
    "Io": 1821.6,
    "Europa": 1560.8,
    "Ganymede": 2634.1,
    "Callisto": 2410.3,
}
spec_gravity_dict = {
    "Io": 1.796,
    "Europa": 1.314,
    "Ganymede": 1.428,
    "Callisto": 1.235,
}
mean_orb_peri_dict = {
    "Io": 1.769,
    "Europa": 3.551,
    "Ganymede": 7.154,
    "Callisto": 16.689,
}
moon_name = input("Enter the name of the moon of jupiter : ")
print(
    f"\n Mean radius = {mean_radi_dict[moon_name]}\n Specific gravity = {spec_gravity_dict[moon_name]} \n Orbital period={mean_orb_peri_dict[moon_name]}"
)
