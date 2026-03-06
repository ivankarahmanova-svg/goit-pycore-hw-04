def total_salary(path: str) -> tuple[int, float]:
    total: int = 0
    count: int = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return (0, 0.0)

        average: float = total / count
        return (total, average)

    except FileNotFoundError:
        return (0, 0.0)


if __name__ == "__main__":
    total, average = total_salary("salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")