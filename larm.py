# Funktion för att visa undermenyn för larm
def larm_menu():
    print()
    print("=============================")
    print("Konfigurera larm:")
    print("1. CPU-användning")
    print("2. RAM-användning")
    print("3. Disk-användning")
    print("4. Tillbaka till huvudmenyn")
    print()
    print()

cpu_level = 0 # Nollställer nivån för larm vid programstart
ram_level = 0 # Nollställer nivån för larm vid programstart
disk_level = 0 # Nollställer nivån för larm vid programstart

cpu_lista = [] # Lista för CPU-larm
ram_lista = [] # Lista för RAM-larm
disk_lista = [] # Lista för Disk-larm

def cpu_larm():
    while True:
        try:
            cpu_level = int(input("Ställ in nivå för alarm mellan 0-100: "))
            if cpu_level >= 1 and cpu_level <= 100:
                cpu_lista.append(cpu_level) # Lägger till satt larmnivå i en lista
                print(f"Larm för CPU-använding satt till {cpu_level}%")
                return
            else:
                print(f"Du måste ange ett tal som är större än 1 och mindre än 100. Försök igen.")
        except ValueError:
            print("Fel: Du måste mata in ett giltigt tal. Försök igen.")
        print()

def ram_larm():
    while True:
        try:
            ram_level = int(input("Ställ in nivå för alarm mellan 0-100: "))
            if ram_level >= 1 and ram_level <= 100:
                ram_lista.append(ram_level) # Lägger till satt larmnivå i en lista
                print(f"Larm för RAM-använding satt till {ram_level}%")
                return
            else:
                print(f"Du måste ange ett tal som är större än 1 och mindre än 100. Försök igen.")
        except ValueError:
            print("Fel: Du måste mata in ett giltigt tal. Försök igen.")
        print()

def disk_larm():
    while True:
        try:
            disk_level = int(input("Ställ in nivå för alarm mellan 0-100: "))
            if disk_level >= 1 and disk_level <= 100:
                disk_lista.append(disk_level) # Lägger till satt larmnivå i en lista
                print(f"Larm för CPU-använding satt till {disk_level}%")
                return
            else:
                print(f"Du måste ange ett tal som är större än 1 och mindre än 100. Försök igen.")
        except ValueError:
            print("Fel: Du måste mata in ett giltigt tal. Försök igen.")
        print()

# Loop för menyn
def larm_menu_choice():
    while True:
        larm_menu()
        userChoice = input("Välj ett alternativ i menyn: ")
        if userChoice == "1":
            cpu_larm()
            print()
            input("Tryck på 'enter' för att gå tillbaka till menyn.")
            print()

        elif userChoice == "2":
            ram_larm()
            print()
            input("Tryck på 'enter' för att gå tillbaka till menyn.")
            print()

        elif userChoice == "3":
            disk_larm()
            print()
            input("Tryck på 'enter' för att gå tillbaka till menyn.")
            print()

        elif userChoice == "4":
            return # Gör så att användaren kommer tillbaka till huvudmenyn
        
        else:
            print("Felaktig inmatning. Försök igen")
            print()
            print()
