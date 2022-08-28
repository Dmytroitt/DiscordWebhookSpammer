import requests
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')
i=0
def payload():
    result = requests.post(url, json = data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload realized, code {}.".format(result.status_code))

os.system('color a' if os.name == 'nt' else 'tput setaf  1')

print("""
▌ ▌   ▌  ▌        ▌
▌▖▌▞▀▖▛▀▖▛▀▖▞▀▖▞▀▖▌▗▘ ▞▀▘▛▀▖▝▀▖▛▚▀▖▛▚▀▖▞▀▖▙▀▖
▙▚▌▛▀ ▌ ▌▌ ▌▌ ▌▌ ▌▛▚  ▝▀▖▙▄▘▞▀▌▌▐ ▌▌▐ ▌▛▀ ▌
▘ ▘▝▀▘▀▀ ▘ ▘▝▀ ▝▀ ▘ ▘ ▀▀ ▌  ▝▀▘▘▝ ▘▘▝ ▘▝▀▘▘
By: github.com/Dmytroit
""")

url = str(input("Webhook url: "))
avatar = str(input("Webhook avatar: "))
name = str(input("Webhook name: "))
message = str(input("Message for spam: "))
cooldown = int(input("Cooldown between messages: "))
messages_limit = int(input("Limit of requests [0 for Unlimited]: "))



data = {
    "content" : message,
    "username" : name,
    "avatar_url": avatar
}

if messages_limit == 0:
    while True:
        payload()
        i = i + 1
        print(f">> {i} requests sent.")
        time.sleep(cooldown)
elif messages_limit < 0:
    print(">> invalid messages limit!")
elif messages_limit > 0:
    for i in range(0,messages_limit):
        payload()
        i = i + 1
        print(f">> {i} requests sent.")
        time.sleep(cooldown)
