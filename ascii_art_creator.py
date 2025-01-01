import pyfiglet
from termcolor import colored

def display_menu():
    print("===== ASCII Art Oluşturucu =====")
    print("1. İsim gir")
    print("2. Renk seç")
    print("3. ASCII art oluştur")
    print("4. Çıkış")
    print("===============================")

def get_name():
    name = input("İsminizi girin: ")
    return name

def get_color():
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    print("Mevcut renkler:", ", ".join(colors))
    color = input("Bir renk seçin: ").lower()
    while color not in colors:
        print("Geçersiz renk! Lütfen tekrar seçin.")
        color = input("Bir renk seçin: ").lower()
    return color

def create_ascii_art(name, color):
    ascii_art = pyfiglet.figlet_format(name)
    colored_ascii_art = colored(ascii_art, color)
    print(colored_ascii_art)

def main():
    name = ""
    color = ""
    while True:
        display_menu()
        choice = input("Bir seçenek girin (1-4): ")
        
        if choice == "1":
            name = get_name()
        elif choice == "2":
            color = get_color()
        elif choice == "3":
            if name and color:
                create_ascii_art(name, color)
            else:
                print("Lütfen önce isim ve renk girin.")
        elif choice == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
