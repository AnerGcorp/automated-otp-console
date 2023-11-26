import asyncio
import websockets
import json
import requests

# OTP authentification server URL
WEBSOCKET_URL = '' # example "ws://example.com/app/websocketkey?protocol=7&client=js&version=4.3.1&flash=false"
# OTP user authentication status
API_ENDPOINT = '' # example "http://example.com/api/sms/sms-update"


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


async def websocket_client():
    while True:
        try:
            async with websockets.connect(WEBSOCKET_URL) as websocket:
                await websocket.send(json.dumps({
                    "event": "pusher:subscribe",
                    "data": {
                        "channel": "verifications"
                    }
                }))
                while True:
                    message = await websocket.recv()
                    data = json.loads(message)
                    if "data" in data:
                        data = json.loads(data['data'])
                    print(data)
                    if data.get("phone") is not None:
                        user = {}
                        user["receiver"] = data.get("phone")
                        user['message'] = data.get("message")
                        user["status"] = "pending"
                        with open("control.json", "w") as file:
                            file.write(json.dumps(user, indent=2))
                        # await send_to_api_endpoint(data.get("phone"), data.get("message"), True)
                        # await send_to_api_endpoint(data.get("phone"), data.get("message"), False)
                        print(json.dumps(user, indent=2))
        except (websockets.exceptions.ConnectionClosed, ConnectionRefusedError):
            print("WebSocket connection closed or refused. Retrying...")
            # Wait for 5 seconds before attempting to reconnect
            await asyncio.sleep(5)


def main():
    # logging.basicConfig(format='%(levelname)s: %(message)s',
    #                     level=logging.DEBUG)

    while True:
        try:
            asyncio.run(websocket_client())
        except Exception as e:
            print(f"An error occurred: {e}")
            continue


if __name__ == "__main__":
    main()
