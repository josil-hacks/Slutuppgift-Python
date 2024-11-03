class active_alarms:
    def __init__(self):
       self.cpu_lista = [] # Lista för CPU-larm
       self.ram_lista = [] # Lista för RAM-larm
       self.disk_lista = [] # Lista för Disk-larm

    def cpu_larm(self, cpu_level):
        while True:
            try:
                cpu_level = int(input("Ställ in nivå för alarm mellan 0-100: "))
                if cpu_level >= 1 and cpu_level <= 100:
                    self.cpu_lista.append(cpu_level) # Lägger till satt larmnivå i en lista
                    print(f"Larm för CPU-använding satt till {cpu_level}%")
                    return
                else:
                    print(f"Du måste ange ett tal som är större än 1 och mindre än 100. Försök igen.")
            except ValueError:
                print("Fel: Du måste mata in ett giltigt tal. Försök igen.")
            print()

    def ram_larm(self, ram_level):
        while True:
            try:
                ram_level = int(input("Ställ in nivå för alarm mellan 0-100: "))
                if ram_level >= 1 and ram_level <= 100:
                    self.ram_lista.append(ram_level) # Lägger till satt larmnivå i en lista
                    print(f"Larm för RAM-använding satt till {ram_level}%")
                    return
                else:
                    print(f"Du måste ange ett tal som är större än 1 och mindre än 100. Försök igen.")
            except ValueError:
                print("Fel: Du måste mata in ett giltigt tal. Försök igen.")
            print()

    def disk_larm(self, disk_level):
        while True:
            try:
                disk_level = int(input("Ställ in nivå för alarm mellan 0-100: "))
                if disk_level >= 1 and disk_level <= 100:
                    self.disk_lista.append(disk_level) # Lägger till satt larmnivå i en lista
                    print(f"Larm för CPU-använding satt till {disk_level}%")
                    return
                else:
                    print(f"Du måste ange ett tal som är större än 1 och mindre än 100. Försök igen.")
            except ValueError:
                print("Fel: Du måste mata in ett giltigt tal. Försök igen.")
            print()