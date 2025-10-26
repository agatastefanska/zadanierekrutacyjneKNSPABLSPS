

Hej, nie znam sie kompletnie na tym i zdaje sobie sprawę że zadanie nie jest w pełni dobrze wykonane 😅

🐢 Zadanie: żółw chodzący po trajektorii będącej tworem ósemko-podobnym 🐢

Wymagania
- ROS 2 Humble
- Python 3
- Zainstalowany `colcon` (do budowania pakietów)
- Zainstalowany symulator `turtlesim`

---

Instalacja
1. Przejdź do swojego workspace’a ROS 2:
cd ~/ros2_ws/src


Sklonuj lub skopiuj folder TURTLE_EIGHT do katalogu src:
git clone <adres> TURTLE_EIGHT


Zbuduj pakiet:
cd ~/ros2_ws
colcon build --packages-select turtle_eight

Załaduj środowisko:
source install/setup.bash


Uruchamianie node'a:
uruchom turtlesim:
ros2 run turtlesim turtlesim_node

2. Uruchom node turtle_eight:
ros2 run turtle_eight turtle_controller


🐢 SPRAWOZDANIE 🐢

Pierwszym problemem jest fakt iż komputer z systemem linux mam w Gdańsku, a do warszawy wzięłam jedynie laptopa z windowsem, więc instalowałąm przez WSL linuxa na podstawie poradnika jakiegoś na yutube.
Później instalowałam ros2 również z poradnika na youtbe i z oficjalnej strony kopiując do terminala wymagane komendy.

Później jak juz zainstalowałam wszytsko to utowrzyłam wymagane pliki i napisałam kod przy pomocy chatu GPT.
Umiem jedynie podstawy pythona i nie programowałam nigdy nic w ros2, więc w zasadzie CHAT GPT mnie uratował. hehe
Ja jedynie mówiłam mu co ma pozmieniać lub po prosru pisałam że coś nie działa

I teraz sytuacja się tak prezentuje, że nie miałam specjalnie dużo czasu na zrobienie tego zadania, więc jest bardzo niedopracowane a ja w sumie odsyłam to co udało mi się zrobić bo stwierdziłam że nie mam nic do stracenia😅😅


<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/042b4304-0736-40b0-b9cc-6d5065ad5080" />







