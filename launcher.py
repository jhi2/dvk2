from pytermgui import tim
import time
import sys
from pathlib import Path
import os
tim.print("[inverse]Dad vs. kaiser version 2.0.0[/inverse]")
tim.print("[blue bold]1. Single-player\n2.Multi-player")
tim.print("[blue bold]3. Quit")
tim.print("[red bold]Enter an option:", end="")
try:
    option = int(input())
except:
    tim.print("[red bold]Invalid input.")
    time.sleep(4)
    sys.exit()
if option not in (1,2,3,4):
    tim.print("[red bold]Invalid input.")
    time.sleep(4)
    sys.exit()
if option == 1:
    tim.print("[inverse]Single-player mode[/inverse]")
    os.system(f"python {Path.cwd()}\\sp.py")
if option == 2:
    tim.print("[inverse]Multi-player mode[/inverse]")
    os.system(f"python {Path.cwd()}\\mp.py")
if option == 3:
    tim.print("Thank you for playing=[inverse]Dad vs. kaiser[/inverse].")
    time.sleep(4)
    sys.exit()
