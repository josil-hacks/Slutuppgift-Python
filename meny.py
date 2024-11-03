
from monitor import activate_monitor # För menyval 1
from monitor import check_active_status # För menyval 2

from larm import larm_menu_choice # För menyval 3
#from testyta import larm_menu_choice # För menyval 4
#from testyta import active_alarms

# Function to show menu
def show_menu():
    print()
    print("=============================")
    print()
    print("1. Starta övervakning")
    print("2. Lista aktiv övervakning")
    print("3. Skapa larm")
    print("4. Visa larm")
    print("5. Starta övervakningsläge")
    print("6. Stäng programmet")
    print()
    print()

def start_monitor():
    if check_active_status == True:
        print("Övervakning redan startad.")
    else:
        print("Övervakning startad.")
        activate_monitor()

def show_active_monitor():
    check_active_status()

def create_alarm():
    larm_menu_choice()

def show_alarm():
    active_alarms()
    #print(f"Funktionen är inte tillgänglig i denna version.")

def start_monitor_mode():
    print(f"Funktionen är inte tillgänglig i denna version.")

def close():
    print("Programmet avslutas.")
    exit()

# Loop för att visa och använda huvudmenyn
def main_menu():
    while True:
        show_menu()
        userChoice = input("Välj ett alternativ i menyn: ")
        if userChoice == "1":
            start_monitor()
            print()
            input("Tryck på 'enter' för att gå tillbaka till menyn.")
            print()

        elif userChoice == "2":
            show_active_monitor()
            print()
            input("Tryck på 'enter' för att gå tillbaka till huvudmenyn.")
            print()

        elif userChoice == "3":
            create_alarm()

        elif userChoice == "4":
            show_alarm()
            print()
            input("Tryck på 'enter' för att gå tillbaka till huvudmenyn.")
            print()
        
        elif userChoice == "5":
            start_monitor_mode()
            print()
            input("Tryck på 'enter' för att gå tillbaka till huvudmenyn.")
            print()

        elif userChoice == "6":
            close()
        
        else:
            print("Felaktig inmatning. Försök igen")
            print()
            print()

# Launch program
print("==== VÄLKOMMEN TILL PROGRAMMET ====")
print("Välj vad du vill göra genom att mata in ett nummer i menyn.")
print()
main_menu()