# Automated OTP Console Application

## Overview

This Python console application utilizes the `gsmmodem` library to automate the OTP (One-Time Password) process, particularly catering to countries with limited access to services for OTP authentication. The application interacts with a GSM modem to send and receive SMS messages, facilitating the automated retrieval and processing of OTPs.

## Features

- **Automated OTP Retrieval:** The application automates the process of retrieving OTPs via SMS, making it suitable for scenarios where internet-based OTP services may be restricted.

- **GSM Modem Integration:** Utilizes the `gsmmodem` library to interact with a GSM modem, allowing seamless communication for SMS operations.

- **Country Compatibility:** Designed with a focus on countries with limited access to internet-based OTP services, providing an alternative solution for OTP authentication.

## Requirements

- Python 3.x
- `gsmmodem` library (`pip install gsmmodem`)
- `requests` library (`pip install requests`)
- `asyncio` library (`pip install asyncio`)

## Usage

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Connect GSM Modem:**

   - Ensure that your GSM modem is properly connected to the computer.

3. **Run the application:**
   ```bash
   python otp_automation.py
   ```
4. **Follow-on Screen Prompts:**
   - The application will guide you through the process of sending and receiving OTPs via SMS.

## Configuration

- Modify the `otp_automation.py` script to customize settings such as SMS destination number, message format, and other parameters.

## Contributions

Contributions are welcome! If you encounter issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
