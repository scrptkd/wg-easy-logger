import requests
import datetime
import pytz
import json
import time

url = 'http://0.0.0.0:51821/api/wireguard/client'

headers = {
    'Host': '0.0.0.0:51821',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.98 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Referer': 'http://0.0.0.0:51821/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'connect.sid=PLACE_COOCKIE_HERE'
}
                  
while True:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        for record in data:
            if record['latestHandshakeAt'] is None:
                continue
            latest_handshake_utc = datetime.datetime.strptime(record['latestHandshakeAt'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.UTC)
            now_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
            if abs(now_utc - latest_handshake_utc) < datetime.timedelta(seconds=30):
                with open('/var/www/html/index.nginx-debian.html', 'a') as f:
                    f.write('Name: ' + record['name'] + ', OPENED: ' + now_utc.strftime('%Y-%m-%dT%H:%M:%S.%fZ') + '\n')
                    f.close()
                print('ACTIVITY FOUND! Time is UTC. client name is ' + record['name'] + ' on ' + record['latestHandshakeAt'])
    else:
        print('Request failed with status code:', response.status_code)
    time.sleep(3)
