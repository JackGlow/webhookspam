import time
import random
import os
import requests
from colorama import *

init(autoreset=True)

class jg:
	names = ["Миша", "Аимбет", "Хакеры из ананимус", "Дова", "Клайд", "Влад гей","когда миксед", "я люблю сосать член","пуська", "бля", "твоя мама гей", "сука", "бля"]
	def helloWorld():
		print(Fore.CYAN + 'WEBHOOK FLOOD')
		print("github.com/jackglow/webhookspam")
	def run(urmsg):
		hf = open("hooks.txt", "r")
		hooks = hf.read()
		hf.close()
		totalhooks = 0
		hooks = hooks.split('\n')
		for hook in hooks:
			totalhooks += 1
			print(Fore.YELLOW+"Loaded "+str(totalhooks)+" webhook in total...")
		print(Fore.GREEN + "Webhooks loaded.")
		print(Fore.YELLOW + "Running message (30) send...")
		for x in range(0,30):
			for hook in hooks:
				r = requests.post(hook, data={'username': random.choice(jg.names), 'content': urmsg, "avatar_url": "https://avatars3.githubusercontent.com/u/13962537?s=460&v=4"})

jg.helloWorld()
print(Fore.YELLOW + "Enter message> ", end="")
f = input()
jg.run(f)