def get_cats_info(path: str) -> list[dict[str, str]]:
    cats: list[dict[str, str]] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                cat: dict[str, str] = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat)

        return cats

    except FileNotFoundError:
        return []


if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)