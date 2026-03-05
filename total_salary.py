def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        average = total / count
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено")
        return (0, 0)


# перевірка роботи функції
total, average = total_salary("salary.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")