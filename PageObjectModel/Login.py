import json
class LoginPOM:
    username_css="[value='admin@yourstore.com']"
    passward_css="[id='Password']"
    login_button_css="[type='submit']"
    file=open('TestData/Jsonfile.json')
    data=json.load(file)
    url=data['url']
    username=data['username']
    passward=data['passward']

