import random
import time

roboter_name = "Lemon"
sorted_packages_count = 0 
total_weight = 0

print("Roboter startet die Schicht am Fließband!")
print("-----------------------------------------")

while True:
    package_weight = random.randint(1, 25)
    sorted_packages_count += 1
    total_weight += package_weight

   
    print(f"{roboter_name} hat Paket {sorted_packages_count} mit Gewicht"
        f" {package_weight} kg sortiert. (Gesamt: {total_weight} kg)")
    if sorted_packages_count >= 5:
        break
    time.sleep(2)