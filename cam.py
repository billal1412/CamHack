#_*_coding=UTF-8_*_
import requests,re,os,sys
prompt = "\33[33;1m[\033[37;1mOPTIONS\033[33;1m]: \033[32;1m"
def show(type,msg):
        if type=="error":
                print ("\033[33;1m{\033[31;1mERROR\033[33;1m}> \033[31;1m%s\033[0m"%(msg))
#               sys.exit()
        elif type=="sukses":
                print ("\033[33;1m{\033[32;1mSUCCESS\033[33;1m}> \033[32;1m%s\033[0m"%(msg))
        elif type=="warning":
                print ("\033[33;1m{WARNINGS}> \033[37;1m%s\033[0m"%(msg))

def get(code,page):
	try:
		show("warning","Getting page: "+str(page))
		hulu = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1; A1603) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36"}
		r = ""
		try:
			r = requests.get("https://www.insecam.org/en/bycountry/%s/?page=%s"%(code,page),headers=hulu)
		except requests.exceptions.ConnectionError:
			show("error","Connection Error, \033[32;1mPlease check your signal")
			sys.exit()
		f = re.findall('http://\d+.\d+.\d+.\d+:\d+', r.text)
		c = 0
		for _ in f:
			ip = f[c]
			show("sukses",str(ip))
			c+=1
	except (KeyboardInterrupt,EOFError):
		print ("")
		show("error","Exit? OK!")
		sys.exit()
def banner():
	print ("""\033[31;1m                  _________-----_____
       _____------           __      ----_
___----             ___------              \\
   ----________        ----                 \\
               -----__    |             _____)
                    __-                /     \\
        _______-----    ___--          \    /)\\
  ------_______      ---____            \__/  /
               -----__    \ --    _          /\\
                      --__--__     \_____/   \_/\\
\033[32;1m    ╔═╗┌─┐┌┬┐\033[33;1mAuthor\033[31;1m:\033[32;1m Billal \033[31;1m  ----|   /          |
\033[32;1m    ║  ├─┤│││\033[33;1mVersion\033[31;1m:\033[32;1m0.1\033[31;1m |  |___________|
\033[32;1m    ╚═╝┴ ┴┴ ┴\033[34;1m  Woll Cyber Team  \033[31;1m  |  | ((_(_)| )_)
\033[34;1m  Black \033[32;1m   ╦ ╦┌─┐┌─┐┬┌─┌─┐┬─┐  \033[31;1m   |  \_((_(_)|/(_)
\033[34;1m  Coder \033[32;1m   ╠═╣├─┤│  ├┴┐├┤ ├┬┘  \033[31;1m   \             (
\033[34;1m  Crush  \033[32;1m  ╩ ╩┴ ┴└─┘┴ ┴└─┘┴└─     \033[31;1m \_____________)\033[0m""")

def menu2(code,max):
	print ("""
\033[31;1m[\033[32;1m1\033[31;1m]: Default Page
\033[31;1m[\033[32;1m2\033[31;1m]: Custom Page
""")
	p = raw_input(prompt)
	if p in ["01","1"]:
		for page in range(max):
			if page == 0: pass
			else: get(code,page)
	elif p in ["02","2"]:
		page = raw_input("\033[33;1m[\033[32;1mPAGE\033[33;1m]: \033[32;1m")
		if max > page or page == 0:
			show("error","Max page: "+str(max))
			sys.exit()
		else:
#			for page in range(1,max):
			get(code,page)

def menu():
	print ("""
\033[31;1m[\033[32;1m1\033[31;1m]: Albania
\033[31;1m[\033[32;1m2\033[31;1m]: Argentina
\033[31;1m[\033[32;1m3\033[31;1m]: Australia
\033[31;1m[\033[32;1m4\033[31;1m]: Austria
\033[31;1m[\033[32;1m5\033[31;1m]: Bangladesh
\033[31;1m[\033[32;1m6\033[31;1m]: Belgium
\033[31;1m[\033[32;1m7\033[31;1m]: Bosnia
\033[31;1m[\033[32;1m8\033[31;1m]: Brazil
\033[31;1m[\033[32;1m9\033[31;1m]: Bulgaria
\033[31;1m[\033[32;1m10\033[31;1m]: Canada
\033[31;1m[\033[32;1m11\033[31;1m]: China
\033[31;1m[\033[32;1m12\033[31;1m]: Denmark
\033[31;1m[\033[32;1m13\033[31;1m]: Egypt""")
def main():
	os.system("clear")
	banner()
	menu()
	op = raw_input(prompt)
	if op in ["01","1"]:
		code = "AL"
		menu2(code,2)
	elif op in ["02","2"]:
		code = "AR"
		menu2(code,19)
	elif op in ["03","3"]:
		code = "AU"
		menu2(code,15)
	elif op in ["04","4"]:
		code = "AT"
		menu2(code,49)
	elif op in ["05","5"]:
		code = "BD"
		menu2(code,4)
	elif op in ["06","6"]:
		code = "BE"
		menu2(code,26)
	elif op in ["07","7"]:
		code = "BA"
		menu2(code,2)
	elif op in ["08","8"]:
		code = "BR"
		menu2(code,30)
	elif op in ["09","9"]:
		code = "BG"
		menu2(code,20)
	elif op in ["10"]:
		code = "CA"
		menu2(code,40)
	elif op in ["11"]:
		code = "CN"
		menu2(code,9)
	elif op in ["12"]:
		code = "DK"
		menu2(code,14)
	elif op in ["13"]:
		code = "EG"
		menu2(code,15)
	elif op in ["14"]:
		code = ""
		menu2(code,4)
	elif op in ["15"]:
		code = ""
		menu2(code,10)
main()
