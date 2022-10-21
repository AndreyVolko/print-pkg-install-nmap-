print('Как у вас настроение?')
a = input()
if '1/100' or '1/200' in a:
    print("apt install nmap")
elif '' in a:
    print('Ничего, скоро всё наладится')
elif 'не' in a:
    print('Извините, но я вас не понимаю')
elif '?' in a:
    print('Извините, но я вас не понимаю')
else:
    print('Извините, но я вас не понимаю')
