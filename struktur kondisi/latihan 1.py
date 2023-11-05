bilangan1 = float(input("masukkan bilangan pertama:"))
bilangan2 = float(input("masukkan bilangan kedua:"))


if bilangan1 > bilangan2:
    print(f"bilangan terbesar adalah: {bilangan1}")
elif bilangan2 > bilangan1:
    print(f"bilangan terbesar adalah:{bilangan2}")
else:
    print("kedua bilangan sama besar.")
    