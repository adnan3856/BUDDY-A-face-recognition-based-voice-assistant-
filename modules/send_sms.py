import requests
url = "https://www.fast2sms.com/dev/bulk"

def send_sms():
    message = "BUDDY >> Unauthorized User tried to access your data."
    number = '9162945996'
    payload = "sender_id=FSTSMS&message=" + message +"&language=english&route=p&numbers="+ number
    headers = {
        'authorization': 'DAtOwPdYhy9nxNQbus5B6a38zc70I4vFGolHfXEJZCrUWMKemRpBqLVveU3DmKlcCTNnYdaErHZhS62O',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

