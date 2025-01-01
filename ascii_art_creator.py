import os
import pyfiglet
from termcolor import colored

# Instagram sayfası
INSTAGRAM_URL = "https://www.instagram.com/zwwac/"

# Mevcut tüm fontlar
FONTS = pyfiglet.FigletFont.getFonts()

# Terminali temizler ve gerekli mesajı gösterir
def clear_terminal():
    os.system('clear')
    # Üst köşede büyük boyutta ASCII art yazısı
    zwac_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⠖⠀⠀⠲⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣇⣤⠶⠛⣛⣉⣙⡛⠛⢶⣄⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣿⣿⣿⡟⢁⣴⣿⣿⣿⣿⣿⣿⣦⡈⢿⣿⣿⣿⣀⡀⠀⠀⠀⠀
⠀⠀⢠⣴⣿⣿⣿⣿⡟⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣿⣿⣦⡄⠀⠀
⠀⣴⣿⣿⡿⠿⢛⣻⡇⢸⡟⠻⣿⣿⣿⣿⣿⡿⠟⢻⡇⣸⣛⡛⠿⣿⣿⣿⣦⠀
⢸⣿⡿⠋⠀⠀⢸⣿⣿⡜⢧⣄⣀⣉⡿⣿⣉⣀⣠⣼⢁⣿⣿⡇⠀⠀⠙⢿⣿⡆
⣿⣿⠁⠀⠀⠀⠈⣿⣿⡇⣿⡿⠛⣿⣵⣮⣿⡟⢻⡿⢨⣿⣿⠀⠀⠀⠀⠈⣿⣿
⢿⡟⠀⠀⠀⠀⠀⠘⣿⣷⣤⣄⡀⣿⣿⣿⣿⢁⣤⣶⣿⣿⠃⠀⠀⠀⠀⠀⣿⡟
⠘⠇⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⢿⣿⣿⣿⢸⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠻⠃
⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⢩⣦⣘⡘⠋⣛⣸⡍⠁⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀
⠀⠀⠘⢿⣷⣤⣤⣄⣤⣤⣶⣿⣿⣿⡿⢿⣿⣿⣿⣷⣤⣤⣠⣤⣴⣾⡿⠁⠀⠀
⠀⠀⠀⠀⠉⠛⠿⠿⠿⡿⠿⠿⠛⠉⠀⠀⠉⠛⠿⠿⣿⠿⠿⠿⠛⠉⠀⠀⠀⠀
"""
    terminal_width = os.get_terminal_size().columns
    for line in zwac_art.split("\n"):
        print(colored(line.center(terminal_width), 'green'))
    print(f"Instagram: {colored(INSTAGRAM_URL, 'blue', attrs=['underline'])}\n")

# Menü seçeneklerini gösterir
def display_menu():
    print(colored("===== ASCII Art Oluşturucu =====", 'magenta', attrs=['bold']))
    print(colored("1. İsim gir", 'yellow', attrs=['bold']))
    print(colored("2. Renk seç", 'yellow', attrs=['bold']))
    print(colored("3. Font seç", 'yellow', attrs=['bold']))
    print(colored("4. ASCII art oluştur", 'yellow', attrs=['bold']))
    print(colored("5. Çıkış", 'red', attrs=['bold']))
    print(colored("===============================", 'magenta', attrs=['bold']))

# Kullanıcıdan isim alır
def get_name():
    return input(colored("İsminizi girin: ", 'cyan', attrs=['bold'])).strip()

# Kullanıcıdan renk seçmesini ister
def get_color():
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    print(colored("Mevcut renkler: " + ", ".join(colors), 'cyan', attrs=['bold']))
    while True:
        color = input(colored("Bir renk seçin: ", 'cyan', attrs=['bold'])).strip().lower()
        if color in colors:
            return color
        print(colored("Geçersiz renk! Lütfen tekrar seçin.", 'red', attrs=['bold']))

# Kullanıcıdan font seçmesini ister
def get_font():
    print(colored("Mevcut fontlar: " + ", ".join(FONTS), 'cyan', attrs=['bold']))
    while True:
        font = input(colored("Bir font seçin: ", 'cyan', attrs=['bold'])).strip().lower()
        if font in FONTS:
            return font
        print(colored("Geçersiz font! Lütfen tekrar seçin.", 'red', attrs=['bold']))

# ASCII art oluşturur ve kalıcı olarak dosyaya yazar
def create_ascii_art(name, color, font):
    ascii_art = pyfiglet.figlet_format(name, font=font)
    colored_ascii_art = colored(ascii_art, color)
    # ASCII art'ı ekrana yazdır
    print(colored_ascii_art)
    # ASCII art'ı dosyaya yazdır
    with open("ascii_art_output.txt", "a") as f:
        f.write(colored_ascii_art + "\n")

def main():
    clear_terminal()
    name, color, font = "", "", "standard"
    while True:
        display_menu()
        choice = input(colored("Bir seçenek girin (1-5): ", 'cyan', attrs=['bold'])).strip()
        if choice == "1":
            name = get_name()
        elif choice == "2":
            color = get_color()
        elif choice == "3":
            font = get_font()
        elif choice == "4":
            if name and color and font:
                create_ascii_art(name, color, font)
            else:
                print(colored("Lütfen önce isim, renk ve font girin.", 'red', attrs=['bold']))
        elif choice == "5":
            print(colored("Çıkılıyor...", 'red', attrs=['bold']))
            break
        else:
            print(colored("Geçersiz seçenek! Lütfen tekrar deneyin.", 'red', attrs=['bold']))

if __name__ == "__main__":
    main()
