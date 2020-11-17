import subprocess
import sys

cml = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifiInfo = [wifi.split(':')[1][1:-1] for wifi in cml if "All User Profile" in wifi]

for wifi in wifiInfo:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [key.split(':')[1][1:-1] for key in results if "Key Content" in key]
    try:
        sys.stdout = open("wifiInfo.txt", "a")
        print(f'WIFI Name: {wifi}, WIFI Password: {results[0]}')
        sys.stdout.close()
    except IndexError:
        sys.stdout = open("wifiInfo.txt", "a")
        print(f'WIFI Name: {wifi}, WIFI Password: Either no password or cannot be read')
        sys.stdout.close()

