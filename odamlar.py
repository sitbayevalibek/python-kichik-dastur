# Foydalanuvchidan bugun nechta odam bilan gaplashganini so'raydigan kichik dastur
n_odam = int(input("Bugun nechta odam bilan gaplashdingiz? Ularning ismini yozing!\n>>> "))
odamlar = []
for n in range(n_odam):
    odamlar.append(input(f"{n+1} - odam ismi: "))
odamlar_str = ", ".join([odam.title() for odam in odamlar[:-1]]) + f" va {odamlar[-1].title()}"
print(f"Bugun siz {odamlar_str} lar  bilan gaplashdingiz.")