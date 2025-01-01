import os
import pyfiglet
from termcolor import colored

# Terminali temizler ve gerekli mesajı gösterir
def clear_terminal():
    os.system('clear')  # clear komutunu çalıştırır
    print("@zwwac")  # Üst köşede yazılacak kullanıcı adı

# Menü seçeneklerini gösterir
def display_menu():
    print(colored("===== ASCII Art Oluşturucu =====", 'magenta'))
    print(colored("1. İsim gir", 'magenta'))
    print(colored("2. Renk seç", 'magenta'))
    print(colored("3. ASCII art oluştur", 'magenta'))
    print(colored("4. Çıkış", 'magenta'))
    print(colored("===============================", 'magenta'))

# Kullanıcıdan isim alır
def get_name():
    name = input(colored("İsminizi girin: ", 'magenta'))
    return name

# Kullanıcıdan renk seçmesini ister
def get_color():
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    print(colored("Mevcut renkler: " + ", ".join(colors), 'magenta'))
    color = input(colored("Bir renk seçin: ", 'magenta')).lower()
    while color not in colors:
        print(colored("Geçersiz renk! Lütfen tekrar seçin.", 'magenta'))
        color = input(colored("Bir renk seçin: ", 'magenta')).lower()
    return color

# ASCII art oluşturur ve kalıcı olarak dosyaya yazar
def create_ascii_art(name, color):
    ascii_art = pyfiglet.figlet_format(name)
    colored_ascii_art = colored(ascii_art, color)
    
    # ASCII art'ı ekrana yazdır
    print(colored_ascii_art)
    
    # ASCII art'ı dosyaya yazdır
    with open("ascii_art_output.txt", "a") as f:
        f.write(colored_ascii_art + "\n")

def main():
    clear_terminal()  # Terminali temizler
    name = ""
    color = ""
    while True:
        display_menu()
        choice = input(colored("Bir seçenek girin (1-4): ", 'magenta'))
        
        if choice == "1":
            name = get_name()
        elif choice == "2":
            color = get_color()
        elif choice == "3":
            if name and color:
                create_ascii_art(name, color)
            else:
                print(colored("Lütfen önce isim ve renk girin.", 'magenta'))
        elif choice == "4":
            print(colored("Çıkılıyor...", 'magenta'))
            break
        else:
            print(colored("Geçersiz seçenek! Lütfen tekrar deneyin.", 'magenta'))

if __name__ == "__main__":
    main()
