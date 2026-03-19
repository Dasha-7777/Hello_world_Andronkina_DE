total_volume = float(input("Введите нужный объем раствора (мл):"))
nacl_mass = total_volume * 0.009
water_volume = total_volume
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
file.write("-----------------------------------------\n")
    file.write(f"Общий объем: {total_volume} мл\n")
    file.write(f"Масса соли: {nacl_mass:.2f} г\n")
    file.write(f"Объем воды: {water_volume} мл\n")
print("\nРасчеты выполнены. Результат записан в файл 'recipe.txt'.")