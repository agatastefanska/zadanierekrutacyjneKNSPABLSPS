

Hejka, nie znam sie kompletnie na tym, więc zdaje sobie sprawę że prawdopodobnie zadanie nie jest do końca dobrze wykonane 😅


🐢 Turtle Eight 🐢

Pakiet **turtle_eight** zawiera prosty node ROS 2 napisany w Pythonie, który steruje żółwiem (np. w symulatorze turtlesim) tak, aby poruszał się po kształcie cyfry **8**.

---

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
ros2 run turtle_eight turtle_eight_node


🐢 SPRAWOZDANIE 🐢

Pierwszym problemem jest fakt iż komputer z systemem linux mam w Gdańsku, a do warszawy wzięłam jedynie laptopa z windowsem, więc instalowałąm przez WSL linuxa na podstawie poradnika jakiegoś na yutube.
Później instalowałam ros2 również z poradnika na youtbe i z oficjalnej strony kopiując do terminala wymagane komendy.

Później jak juz zainstalowałam wszytsko to utowrzyłam wymagane pliki i napisałam kod przy pomocy chatu GPT.

algorytm działania kodu:
W każdej iteracji (co 0.05 sekundy):

Żółw dostaje stałą prędkość liniową:
v=2.0
dzięki temu zawsze idzie naprzód.

Prędkość kątowa (skręt) zmienia się sinusoidalnie:
ω=1.5⋅sin(t)
to powoduje, że żółw najpierw skręca w jedną stronę, potem w drugą — cyklicznie.




