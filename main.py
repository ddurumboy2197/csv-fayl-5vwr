import csv

def csv_yozuvchi(fayl_ismi, ma'lumotlar):
    try:
        with open(fayl_ismi, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(ma'lumotlar)
        print("Ma'lumotlar yozildi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

# Misol:
ma'lumotlar = [
    ["Ism", "Familiya", "Yosh"],
    ["Ali", "Valiyev", 25],
    ["Vali", "Aliyev", 30],
    ["Hasan", "Murodov", 35]
]

fayl_ismi = "ma'lumotlar.csv"
csv_yozuvchi(fayl_ismi, ma'lumotlar)
