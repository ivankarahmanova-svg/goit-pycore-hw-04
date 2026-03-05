import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def show_directory_structure(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + item.name + "/" + Style.RESET_ALL)
            show_directory_structure(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + item.name + Style.RESET_ALL)

def main():
    if len(sys.argv) != 2:
        print("Використання: python script.py /шлях/до/директорії")
        return

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(Fore.RED + "Помилка: шлях не існує" + Style.RESET_ALL)
        return

    if not directory.is_dir():
        print(Fore.RED + "Помилка: це не директорія" + Style.RESET_ALL)
        return

    print(Fore.BLUE + directory.name + "/" + Style.RESET_ALL)
    show_directory_structure(directory)


if __name__ == "__main__":
    main()