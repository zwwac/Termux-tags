
# ASCII Art Creator

Bu proje, kullanıcıya özel isim, renk ve font girerek terminalde ASCII art oluşturan bir Python scriptidir


![IMG_20250101_144810](https://github.com/user-attachments/assets/e248e4c8-c61d-4297-a4ac-bf0a85bb83a3)


## Kurulum

### 2. Python'u Kurun
```sh
pkg install python
```
### Gerekli Python Paketlerini Yükleyin
```sh
pip install pyfiglet termcolor
```
### Depoyu Klonlayın
```sh
git clone https://github.com/zwwac/Termux-tags.git
cd Termux-tags
```
### Termux Başlangıç Mesajını Kaldırın
```sh
touch ~/.hushlogin
```
### 6. ASCII Art'ı Başlangıçta Görüntüleyin
```sh
echo 'cat ~/Termux-tags/ascii_art_output.txt' >> ~/.bashrc
```
### Python Scriptini Çalıştırın
```sh
python ascii_art_creator.py
```

