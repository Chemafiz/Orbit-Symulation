import matplotlib.pyplot as plt
import math

def error(tekst):
    while True:
        x = input(tekst)
        try:
            float(x)
            return float(x)           
            break
        except:
            print("\nBłąd podczas wprowadzania danych, spróbuj jeszcze raz\n")        
            continue


class Planeta:
    def __init__(self, first_velocity, angle, coor_x, coor_y):
        self.first_velocity = first_velocity
        self.angle = angle
        self.coor_x = float(coor_x)
        self.coor_y = float(coor_y)

        self.first_velocity_x = first_velocity * math.sin(math.radians(self.angle)) 
        self.first_velocity_y = first_velocity * math.cos(math.radians(self.angle)) 




print('Program do obliczania numerycznego orbit\n '.center(80, ' '))   
i = 1
planet_list = []
while True:
    print(''.center(100, '_'))
    print("Dodaj planetę nr %s".center(80, ' ') %(str(i)))
    velocity = error('Podaj prędkość początkową planety w km/s ') * 1000
    angle = error('Podaj kąt natarcia planety (w stopniach; od pionu) ')
    while True:
        try:
            coor_x, coor_y = input('Podaj współrzędne początkowe [x, y] ').split(' ')
            break
        except:
            print("\nBłąd podczas wprowadzania danych, spróbuj jeszcze raz\n")
            continue
    planeta = Planeta(velocity, angle, coor_x, coor_y)
    planet_list.append(planeta)
    print('Czy chcesz dodać kolejną planetę? Jeśli tak napisz TAK, jeśli nie naciśnij dowolony przycisk')
    operant = input()
    if operant.lower() == 'tak':
        i += 1
        continue
    else:
        break



mass = error("Podaj masę gwiazdy w środku układu (w masach Słońca) ")
iteration = int(error('Podaj ilość iteracji jaką ma wykonać program podczas symulacji '))
skala = error('Podaj skalę programu (w AU): ') * 150 * 10**9                                                                        #zmienne globalne dal każdej planety
czas = error('Podaj krok czasowy programu (w dniach): ') * 86400 





def slonce():
    barycentrum = [0, 0]
    plt.plot(barycentrum[0], barycentrum[1], marker='.', markersize=10, color="y")
    plt.text(barycentrum[0], barycentrum[1], 'Słońce')

                   

def orbit(list, iteracja, skala, czas, mass):
    GM = float(1.989 * 10**30 * 6.67 * 10**(-11) * mass)

    def colors(number):
        color_list = ['k', 'g', 'b', 'r', 'm', 'c']
        return color_list[number]

    for number_of_planet, planet in enumerate(list):

        for i in range(iteracja):
            if i == 0:
                plt.plot(planet.coor_x, planet.coor_y, marker='o', markersize=3, color="red")
                text = ('Planeta nr ' + str(number_of_planet + 1))
                plt.text(planet.coor_x, planet.coor_y, (str(text)))
                c_x = float(planet.coor_x)
                c_y = float(planet.coor_y)
                v_x = float(planet.first_velocity_x)
                v_y = float(planet.first_velocity_y)
            else:
                plt.plot(((c_x) + (((v_x * czas)) / skala)), (c_y) + ((((v_y * czas)) / skala)), marker='.', markersize=1, color=colors(number_of_planet))
           
                r3 = (math.sqrt(float(c_x * skala)**2 + float(c_y * skala)**2))**3
                a_x = (-GM * float(c_x * skala) )/ r3
                a_y = (-GM * float(c_y * skala) )/ r3
                v_x = (v_x + a_x * czas)
                v_y = (v_y + a_y * czas)
                c_x = (float(c_x) + (((v_x * czas)) / skala))
                c_y = (float(c_y) + (((v_y * czas)) / skala))
    

def wykres(x):
    plt.axvline(color="black", linewidth=0.1)
    plt.axhline(color="black", linewidth=0.1)
    plt.title('Program numeryczny')
    plt.xlabel('1 jednostka odpowiada %s AU' %(str(x/(150 * 10**9))))
    
        
def main():     
                
    slonce()
    wykres(skala)
    orbit(planet_list, iteration, skala, czas, mass)
    plt.show()
main()