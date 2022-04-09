import urllib.request, json, ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
with urllib.request.urlopen("https://api.resrobot.se/v2/departureBoard?key=4c810d6f-7775-438a-a3e8-dee84dd931fe&id=740059681&maxJourneys=5&format=json&direction=740000002&passlist=0", context=ctx) as url:
    data = json.loads(url.read().decode())

for result in data['Departure']:
    print(result['name'], result['time'])
