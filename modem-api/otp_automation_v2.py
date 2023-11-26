import requests
import time
import asyncio

# Where the OTP authentification comes from
baseUrl = '' # "http://example.com/api/sms-receiver/1/"
# Where you have to store OTP Status
API_ENDPOINT = "" # example "http://example.com/api/sms/sms-update"


async def send_to_api_endpoint(phone, message, status):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "phone": phone,
        "message": message,
        "status": status
    }
    response = requests.post(API_ENDPOINT, json=data, headers=headers)
    response.raise_for_status()

async def socket_checker():
    while True:
        data = requests.get(baseUrl)
        if data.status_code == 200:
            user = data.json()
            # receiver = user['receiver']
            # message = user['message']
            # status = user['status']
        # Cheking needed
        if user['status'] == "sent":
            await send_to_api_endpoint(user['receiver'], user['message'], True)
        else:
            await send_to_api_endpoint(user['receiver'], user['message'], False)
        time.sleep(5)

def main():
    # logging.basicConfig(format='%(levelname)s: %(message)s',
    #                     level=logging.DEBUG)

    while True:
        try:
            asyncio.run(socket_checker())
        except Exception as e:
            print(f"An error occurred: {e}")
            continue


if __name__ == "__main__":
    main()

