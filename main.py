import subprocess
import time

scripts = [
        "pabloxo.py",
"back666ws.py",
        "thuggpint.py",
        "evilgiane.py",
    "roddyg.py",
  "joshu.py",
  "zai.py",
  "major.py",
  "2cool.py",
  "fuckzaza.py",
  "aeter.py",
  "death.py",
  "elijxhwtf.py",
    "mikebroke.py",
    "jefesito.py",
    "angel.py",
    "kkk.py",
    "uney.py",
    "night.py",
    "cash.py",
    "VAHEL.py",
    "suhkumi.py",
    "nightlight.py",
    "1okktubre.py",
    "2slimey.py",
    "christ_blunt.py",
    "corpsekyo.py",
    "elek.py",
    "giuliano.py",
    "helabrokeangel.py",
    "hellsing_glock_boyz.py",
    "knsevenkay.py",
    "moneynumb.py",
    "my_little_pony.py",
    "naxowo.py",
    "nekkropsy.py",
    "ocelot.py",
    "pistolero2k.py",
    "putrid.py",
    "sexadlibs.py",
    "slattuhs.py",
    "suban.py",
    "tnnn.py",
    "unixzo.py",
    "vampireosamagang666.py",
    "vritni.py",
    "war6aw.py",
    "xartinreligion.py",
    "xoly.py",
    "xtendo.py",
    "yoi.py",
    "young_piri.py",
    "zatru.py"
]

processes = {}

def start_script(script):
    return subprocess.Popen(["python3", script])

print("Iniciando todos los scrobblers...")

for script in scripts:
    processes[script] = start_script(script)
    print("Iniciado:", script)
    time.sleep(10)

while True:
    for script, process in processes.items():
        if process.poll() is not None:
            print("Reiniciando:", script)
            processes[script] = start_script(script)
            time.sleep(5)
    time.sleep(20)
