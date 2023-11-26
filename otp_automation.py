from gsmmodem.modem import GsmModem, SentSms
from gsmmodem.exceptions import GsmModemException
import logging
import time
import json

# Defining Constants
port = "/dev/ttyUSB0"
defBaudRate = 460800
pin = "0000"
networkCoverageTimeout = 30


def establish_modem_connection():
    try:
        modem = GsmModem(port, defBaudRate)
        modem.connect(pin)
        modem.waitForNetworkCoverage(networkCoverageTimeout)
        print("Connection with modem established")
        return modem
    except GsmModemException as e:
        print("Couldn't connect")
        return None


def main():
    logging.basicConfig(format='%(levelname)s: %(message)s',
                        level=logging.DEBUG)
    modem = establish_modem_connection()

    print("Modem check: ", isinstance(modem, GsmModem))

    while True:
        if (modem.alive):
            with open("control.json", "r") as file:
                user = json.load(file)
            if user["status"] == "sent":
                continue
            elif user['status'] == "pending":

                receiver = user['receiver']
                message = user['message']

                response = modem.sendSms(receiver, message)
                if response.status == 0:
                    status = "sent"
                else:
                    status = "pending"
                user['status'] = status
                print(receiver, message, "Status - ", status)

                with open("control.json", "w") as file:
                    file.write(json.dumps(user, indent=2))

                print("Waiting 4 sec..")
                time.sleep(4)
        if not modem.alive:
            try:
                modem.connect(pin)
                modem.waitForNetworkCoverage(networkCoverageTimeout)
                time.sleep(3)
            except GsmModemException as e:
                print("GSM Exception", e)
                print("Closing connection...")
                modem.close()


if __name__ == "__main__":
    main()
