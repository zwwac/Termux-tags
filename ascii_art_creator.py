import os
import pyfiglet
from termcolor import colored

# Instagram sayfası
INSTAGRAM_URL = "https://www.instagram.com/zwwac/"

# Mevcut tüm fontlar
FONTS = pyfiglet.FigletFont.getFonts()

# Mevcut arka plan renkleri ve temalar
BACKGROUND_COLORS = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]

# Terminali temizler ve gerekli mesajı gösterir
def clear_terminal():
    os.system('clear')
    # Üst köşede büyük boyutta yazılacak kullanıcı adı
    zwac_art = """
███████╗
██╔════╝
█████╗  
██╔══╝  
███████╗
╚══════╝
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
    print(colored("4. Arka plan rengi seç", 'yellow', attrs=['bold']))
    print(colored("5. ASCII art oluştur", 'yellow', attrs=['bold']))
    print(colored("6. Çıkış", 'red', attrs=['bold']))
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

# Kullanıcıdan arka plan rengi seçmesini ister
def get_background_color():
    print(colored("Mevcut arka plan renkleri: " + ", ".join(BACKGROUND_COLORS), 'cyan', attrs=['bold']))
    while True:
        bg_color = input(colored("Bir arka plan rengi seçin: ", 'cyan', attrs=['bold'])).strip().lower()
        if bg_color in BACKGROUND_COLORS:
            os.system(f"termux-style color {bg_color}")
            return bg_color
        print(colored("Geçersiz arka plan rengi! Lütfen tekrar seçin.", 'red', attrs=['bold']))

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
    name, color, font, bg_color = "", "", "standard", "black"
    while True:
        display_menu()
        choice = input(colored("Bir seçenek girin (1-6): ", 'cyan', attrs=['bold'])).strip()
        if choice == "1":
            name = get_name()
        elif choice == "2":
            color = get_color()
        elif choice == "3":
            font = get_font()
        elif choice == "4":
            bg_color = get_background_color()
        elif choice == "5":
            if name and color and font:
                create_ascii_art(name, color, font)
            else:
                print(colored("Lütfen önce isim, renk, font ve arka plan rengi girin.", 'red', attrs=['bold']))
        elif choice == "6":
            print(colored("Çıkılıyor...", 'red', attrs=['bold']))
            break
        else:
            print(colored("Geçersiz seçenek! Lütfen tekrar deneyin.", 'red', attrs=['bold']))

if __name__ == "__main__":
    main()
