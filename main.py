print("by Ab.5#9111")
import tls_client
import os
import base64
import requests
import threading
import random


class Joiner:
    def __init__(self):
        os.system("cls")
        self.session = tls_client.Session(client_identifier="chrome_108")
        invite_code = input("discord.gg/")
        with open("./tokens.txt") as f:
            tokens = f.read().split('\n')
        ts = [threading.Thread(target=self.join,args=[token,invite_code,self.proxy()]) for token in tokens]
        for t in ts:
            t.start()
        for t in ts:
            t.join()
    
    def proxy(self):
        return random.choice(open("./proxies.txt").read().splitlines())
    
    def join(self,token,invite,proxy):
        xconst, xprops = self.xheaders()
        headers = {
		"accept":               "*/*",
		"accept-encoding":      "gzip, deflate, br",
		"accept-language":      "en-US,en-NL;q=0.9,en-GB;q=0.8",
		"authorization":        token,
		"content-type":         "application/json",
		"cookie":               self.cookies(proxy),
		"origin":               "https://discord.com",
		"referer":              "https://discord.com/channels/@me/",
		"sec-fetch-dest":       "empty",
		"sec-fetch-mode":       "cors",
		"sec-fetch-site":       "same-origin",
		"user-agent":           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9006 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
		"x-context-properties": xconst.decode(),
		"x-debug-options":      "bugReporterEnabled",
		"x-discord-locale":     "en-US",
		"x-super-properties":   xprops.decode(),
	}
        req = self.session.post(f"https://discord.com/api/v9/invites/{invite}",json={},headers=headers,proxy=f"http://{proxy}")
        if req.status_code == 200:
            print("joined")
        else:
            print("failed")
    
    def cookies(self,proxy):
        c = requests.get("https://discord.com",proxies={"all":"http://"+proxy})
        return f"__dcfduid={c.cookies['__dcfduid']}; __sdcfduid={c.cookies['__sdcfduid']}; "
    
    def xheaders(self):
        xconst = '{"location":"Invite Button Embed","location_guild_id":null,"location_channel_id":"","location_channel_type":3,"location_message_id":""}'
        xprops = '{"os":"Windows","browser":"Discord Client","release_channel":"stable","client_version":"1.0.9006","os_version":"10.0.22000","os_arch":"x64","system_locale":"en-US","client_build_number":151638,"client_event_source":null}'
        return base64.b64encode(xconst.encode("utf-8")), base64.b64encode(xprops.encode("utf-8"))

Joiner()
