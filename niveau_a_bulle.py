# Programme de niveau à bulle
# (R) F6EQN 02/2021
#

#imporation des bibliotheques
from sense_emu import *
from time import sleep
from math import *

#définition des couleurs d'affichage
r = (255,0,0)
o = (255,200,0)
v = (0,255,0)

# matrice de couleur pour l'affichage (le centre de cible est en [4,4]car la matrice led n'est pas impaire)
couleur = [[r,r,r,r,r,r,r,r],
           [r,o,o,o,o,o,o,r],
           [r,o,o,o,o,o,o,r],
           [r,o,o,o,o,o,o,r],
           [r,o,o,o,v,o,o,r],
           [r,o,o,o,o,o,o,r],
           [r,o,o,o,o,o,o,r],
           [r,r,r,r,r,r,r,r]]

sense = SenseHat() #instanciation Sense-HAT
sense.set_imu_config(False, True, False)  # configuration de l'IMU, seulement les gyroscopes
sense.clear() # efface l'affichage

def lect_capt():
    global x,y,roul,tang
    
    o = sense.get_orientation_radians()
    tang = o["pitch"]
    roul = o["roll"]
        
    # formattage des données
    
    x = int((pi + roul)*8/(2*pi))
    y = int((pi + tang)*8/(2*pi))
    
    print (x,y)
    print("Roulis:",roul,"Tangage:",tang) #affiche les valeurs de roulis/tanguage en radians
    
    tang_deg = tang * 360/(2*pi)
    roul_deg = roul *360/(2*pi)
    
    print('Roulis:%5.2f'%roul_deg,'Tangage:%5.2f'%tang_deg) #affiche les valeurs de roulis/tanguage en degres
    
    return x, y

try:
    
    while True: # Bouble principale
        
        lect_capt() #appelle la routine de lecture des capteurs
        sense.clear()
        sense.set_pixel(x,y,couleur[x][y]) #allume la led sur le sense-hat, la couleur est indexee dans la matrice de couleur
        
       
        #sleep(0.04)
        sleep(0.1)
    
except KeyboardInterrupt: #sortie de prgm si ctrl C
    print("Termine")
    sense.clear()
