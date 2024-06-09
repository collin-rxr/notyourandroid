import requests
import random
import re
import os

banner = """
  _   _       ___     __                               _           _     _ 
 | \ | |     | \ \   / /               /\             | |         (_)   | |
 |  \| | ___ | |\ \_/ /__  _   _ _ __ /  \   _ __   __| |_ __ ___  _  __| |
 | . ` |/ _ \| __\   / _ \| | | | '__/ /\ \ | '_ \ / _` | '__/ _ \| |/ _` |
 | |\  | (_) | |_ | | (_) | |_| | | / ____ \| | | | (_| | | | (_) | | (_| |
 |_| \_|\___/ \__||_|\___/ \__,_|_|/_/    \_\_| |_|\__,_|_|  \___/|_|\__,_|
                                             MyAndroid Server Finder (Beta)"""

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.myandroid.org/playonline/androidemulator.php',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
}

def get_server():
    username = "BN"+str(random.randint(11111,99999))
    r = requests.get('https://www.myandroid.org/community/user.php', params={ 'username': username }, headers=headers)
    service = r.text
    r = requests.get('https://www.myandroid.org/runapk/create-myandroid.php', params={ 'mobile': 'no', 'service': service, 'username': username, 'app': '', 'apk': 'org.telegram.messenger', }, headers=headers)
    return r.text.strip()

def print_loading(i):
    print(f"Fetching Busy Servers...")
    if i == 0:
        print(f"Progress: |█-----------| 5%")
    elif i == 1:
        print(f"Progress: |██----------| 15%")
    elif i == 2:
        print(f"Progress: |███---------| 30%")
    elif i == 3:
        print(f"Progress: |█████-------| 45%")
    elif i == 4:
        print(f"Progress: |███████-----| 60%")
    elif i == 5:
        print(f"Progress: |████████---|. 75%")
    elif i == 6:
        print(f"Progress: |███████████-| 90%")

busy = [
    "https://stream.myandroid.org/osessionx74/#/?username=guest01&password=server0101",
    "https://stream.myandroid.org/osessionx74/#/?username=guest02&password=server0102",
    "https://stream.myandroid.org/osessionx74/#/?username=guest03&password=server0103",
    "https://stream.myandroid.org/osessionx74/#/?username=guest04&password=server0104",
    "https://stream.myandroid.org/osessionx74/#/?username=guest05&password=server0105",
    "https://stream.myandroid.org/osessionx74/#/?username=guest06&password=server0106",
]

urls = []
if __name__ == "__main__":
    for i in range(5):
        os.system("cls")
        print(banner)
        print_loading(i)
        server = get_server()
        url = f"https://stream.myandroid.org/osessionx74/#/?username={server}&password=server01{re.sub('\\D', '', server)}"
        if not url in urls and not url == "https://stream.myandroid.org/osessionx74/#/?username=&password=server01":
            urls.append(url)
    os.system("cls")
    print(banner)
    print(f"Fetching Busy Servers... Done!")
    for _ in urls:
        busy.remove(_)
    print("")
    for x in busy:
        print(x)
