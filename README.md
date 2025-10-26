

Hej, nie znam sie kompletnie na tym i zdaje sobie sprawę że zadanie nie jest w pełni dobrze wykonane 😅

🐢 Zadanie: żółw chodzący po trajektorii będącej tworem ósemko-podobnym 🐢

Wymagania
- ROS 2 Humble
- Python 3
- Zainstalowany `colcon` (do budowania pakietów)
- Zainstalowany symulator `turtlesim`

---

Jak uruchomić?
uruchom turtlesim:
ros2 run turtlesim turtlesim_node

2. Uruchom node turtle_eight:
ros2 run turtle_eight turtle_controller


---

🐢 SPRAWOZDANIE 🐢

Pierwszym problemem jest fakt iż komputer z systemem linux mam w Gdańsku, a do warszawy wzięłam jedynie laptopa z windowsem, więc instalowałąm przez WSL linuxa na podstawie poradnika jakiegoś na yutube.
Później instalowałam ros2 również z poradnika na youtbe i z oficjalnej strony kopiując do terminala wymagane komendy.

Później jak juz zainstalowałam wszytsko to utowrzyłam wymagane pliki i napisałam kod przy pomocy chatu GPT.
Umiem jedynie podstawy pythona i nie programowałam nigdy nic w ros2, więc w zasadzie CHAT GPT mnie uratował. hehe

Ja jedynie mówiłam mu co ma pozmieniać lub po prosru pisałam że coś nie działa i on mi podawał przykładowe przyczyny i szukałam w czym problem.

Algorytm jest taki że żółw cały czas idzie do przodu (linear.x)
Jednocześnie skręca sinusoidalnie (angular.z)
Sinus zmienia znak → żółw skręca raz w prawo, raz w lewo
tak powstaje ósemka :)



zdjęcie na dowód:
---
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/042b4304-0736-40b0-b9cc-6d5065ad5080" />







