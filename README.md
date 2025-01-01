# ASCII Art Creator

Bu proje, kullanıcıya özel isim ve renk girerek terminalde ASCII art oluşturan bir Python scriptidir


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
echo 'cat ~/ascii-art-creator/ascii_art_output.txt' >> ~/.bashrc
```
### Python Scriptini Çalıştırın
```sh
python ascii_art_creator.py
```

## nano ~/.bashrc yazdıktan sonra içine şunu yazın
```sh
/data/data/com.termux/files/home/Termux-tags/ascii_art_output.txt
