import requests

url = 'http://0.0.0.0:80/'
upload_url = url+'upload/'
battle_url = url+'battle/'

def file_to_string(filename):
    with open(filename, 'r') as f:
        s = f.read()
    return s

def register(filename, name):
    f = file_to_string(filename)
    payload = {'file':f, 'name':name}
    r = requests.post(upload_url, data= payload)
    return r.text

def play(player1,player2):
    r = requests.get(battle_url + player1 + '/' + player2 + '/')
    return r.text
