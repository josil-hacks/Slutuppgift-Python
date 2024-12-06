# Detta program ska larm användaren vid specfik användning av CPU, RAM och/eller DISK

import psutil
import time 

from larm import cpu_lista, ram_lista, disk_lista


# Övervakningsprogrammet ska vara inaktivt vid start
alarm_active = False

def activate_alarm():
    global alarm_active
    if not cpu_lista and not ram_lista and not disk_lista: #Kontrollerar att det finns några larm att övervaka.
        print("Inga larm är aktiva. Vänligen ställ in larm för att kunna aktivera övervakningsläget.")
    else:
        alarm_active = True
        monitoring()


# Funktion för när övervakningsläget/larmen ska vara aktiva
def monitoring():
    try:
        while True: 
            # Hämtar information om användningen
            global cpu_usage
            global ram_usage
            global disk_usage
            cpu_usage = psutil.cpu_percent(interval=1)
            ram_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage('/').percent

            print("Övervakningsläge aktivt. Avsluta med 'CTRL + C'.") #Meddelande till användaren om hur man avslutar övervakningsläget
            print()

            #För att larmet ska reagera:
            if any(cpu_usage >= x for x in cpu_lista):
                print(f"\033[31m VARNING LARM AKTIVERAT: CPU-ANVÄNDNINGEN ÄR JUST NU: {cpu_usage}%!\033[0m")
                print()
            if any(ram_usage >= x for x in ram_lista):
                print(f"\033[31m VARNING LARM AKTIVERAT: RAM-ANVÄNDNINGEN ÄR JUST NU: {ram_usage}%!\033[0m")
                print()
            if any(disk_usage >= x for x in disk_lista):
                print(f"\033[31m VARNING LARM AKTIVERAT: DISK-ANVÄNDNINGEN ÄR JUST NU: {disk_usage}%!\033[0m")
                print()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Övervakningsläge inaktiverat.")
        pass 
