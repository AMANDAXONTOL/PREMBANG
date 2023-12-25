import os
import datetime
os.system('pip install termcolor')
os.system('clear')
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	import pyfiglet
except ImportError:
	os.system('pip install pyfiglet')
from termcolor import colored
from rich.progress import track
from time import sleep
from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
from rich import print as rprint
#COLORS
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
m = '\33[31;1m' # MERAH

f = Figlet(font="banner3-D")
print(colored(f.renderText('krek FB'),'blue'))
print(u + "INI ADALAH SEBUAH TOOLS BERBAYAR BY AUTHOR : LUTHFI XD")

asu=Table()

asu.add_column('Author :',style='white')
asu.add_column('WA :',style='white')

asu.add_row('LUTHFI','083861251898')

console = Console()
console.print(asu,style='red')

print(colored("Waktu :",'blue'),colored(datetime.datetime.now(),'cyan'))
print (' ')
table = Table(title="HARGA LISENSI")

table.add_column("AKTIF", style="cyan", no_wrap=True)
table.add_column("HARGA", style="magenta")

table.add_row("2 MINGGU", "70k")
table.add_row("1 BULAN", "140k")

console = Console()
console.print(table)

def process_data():
    sleep(0.01)
aa=input(colored("KAMU INGIN BELI BERAPA HARI ? : ",'green'))
if aa in ['70','70 hari','70 MINGGU','2 MINGGU']:
	os.system("xdg-open https://wa.me/6283861251898?text=BANG%MAU%BELI%LISENSI%SC%CRACK%FB%2MINGGU")
elif aa in ['140','40 BULAN','1 BULAN']:
	os.system("xdg-open https://wa.me/6283861251898?text=BANG%MAU%BELI%LISENSI%SC%CRACK%FB%1BULAN")
else:
	print(u+'MASUKAN YANG BENAR')
	exit()
	
for _ in track(range(100), description='[green]Script sedang berjalan'):
    process_data()
print(colored("SELESAI, SILAHKAN TUNGGU LUTHFI YANG NGEJAWAB:b",'green'))
exit()