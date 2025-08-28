# main.py
import datetime

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Script runned successfully!")

    # Também escreve em um arquivo de log (opcional)
    with open("script.log", "a") as log_file:
        log_file.write(f"[{now}] Script runned successfully!\n")

if __name__ == "__main__":
    main()
