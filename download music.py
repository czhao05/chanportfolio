import requests
res = requests.get('https://freelistenonline.com/artist/Israel+Kamakawiwo%27ole')
music = res.content
listen = open('Israel.mp3','wb')
listen.write(music)
listen.close()