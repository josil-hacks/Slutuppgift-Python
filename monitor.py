# Detta program ska övervaka CPU- disk- och RAM-användningen

import psutil 
import time 

# CPU-användning
def cpu_monitor(interval=0.5):
    # Hämta CPU-användning i procent
    global cpu_usage # För att variablen ska global, användas i flera funktioner
    cpu_usage = psutil.cpu_percent(interval=interval)
    print(f"CPU-användning: {cpu_usage}%")


# Minnesanvändning
def ram_monitor(interval=0.5):
    # Hämta Minnesanvändning i procent
    ram_info = psutil.virtual_memory()
    ram_usage = ram_info.used / (1024 ** 3) # 1024 ** 3 är 1024 upphöjt i 3 för att få GB istället för byte!
    total_ram = ram_info.total / (1024 ** 3)
    global ram_percentage # För att variablen ska global, användas i flera funktioner
    ram_percentage = ram_info.percent
    print(f"RAM-användning: {ram_usage:.2f} GB / {total_ram:.2f} GB ({ram_percentage}%)")
    time.sleep(interval)


# Diskanvändning
def disk_monitor(interval=0.5):
    # Hämtar diskanvändningsstatistik för den primära partitionen
    disk_usage = psutil.disk_usage('/')
    # Skriv ut aktuell diskanvändning
    print(f"Total disk: {disk_usage.total // (1024 ** 3)} GB | Använder: {disk_usage.percent}%")
    print(f"")
          

# Öveervakningen skall vara inaktiv när programmet startas
monitor_active = False

# I menyval 1, så skall övervakningen startas
def activate_monitor():
    global monitor_active
    monitor_active = True

# I menyval 2, så hämtar programmet uppgifterna om CPU, RAM & diskanvändning
def check_active_status():
    if monitor_active == True:
        print("Övervakning är aktiverat.")
        print()
        cpu_monitor()
        ram_monitor()
        disk_monitor()
    else: #Om övervakningen är inaktiv
        print("Övervakning är inaktiv.")
        print()
 
