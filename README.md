# Automated OSINT Script

This script automates the process of pulling open-source information.

This can also serve as a template for your own custom reconnaissance needs. 

The script has placeholders for API keys from Shodan, WHOIS, and haveibeenpwned.

Unfortunatley, you will need paid memberships to generate the Shodan and haveibeenpwned API keys.

You do not need a membership for a WHOIS key at the time of writting this.

As stated, customize this script for whatever you need it for.

With the right APIs, you can likely make turn this into a very powerful and versitile information gathering tool.

## Features
- Generates an OSINT report text file and places in on your desktop
- The template on its own can target any domain name, but a tool like Sherlock could allow for social media usernames and email addresses to be targeted as well (currently working on this)

## Requirements

1. Python 3.10 or newer installed on the system
2. Shelock if you want to do some username scraping

---

## Setup

### 1. Clone the Repository

Open **Command Prompt**, then run:

```powershell
git clone <url>
cd osint-recon

```

### 2. Temporarily bypass script policy
```powershell
powershell -ExecutionPolicy Bypass -File ./setup.ps1
```

### 3. Install dependencies
```powershell
pip install -r requirements.txt
```

### 4. Edit the script
The script should appear in your desktop.
Right click and open in any python text editor

![Screenshot 2024-12-18 at 17 41 02](https://github.com/user-attachments/assets/ed6d5c61-457b-4be1-814c-5bece1f3e10e)

The script has designated placeholders for Shodan, WHOIS, and haveibeenpwned API keys.

But feel free to modify to use with whatever APIs you would like.

![Screenshot 2024-12-18 at 17 41 24](https://github.com/user-attachments/assets/13c86c8f-bd10-489c-95c5-545e5f54c15c)

File -> save

### 5. Change to your Desktop directory (Still in command prompt)
```powershell
cd ..
cd Desktop
```
### 6. Set your target
````powershell
python osint_recon.py -t <target URL>
````
Example with Youtube:

![Screenshot 2024-12-18 at 17 04 34](https://github.com/user-attachments/assets/9d6af2aa-53b2-43f7-8966-105b992d7519)


A text file should appear on your desktop with the report output

![Screenshot 2024-12-18 at 18 08 22](https://github.com/user-attachments/assets/21e16f7f-53b1-4711-ab01-a3b1490f740d)


-----

### Troubleshooting
 Script failed to run? Ensure you’ve adjusted the execution policy to allow scripts:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
---
Feel free to submit issues or pull requests to improve functionality or documentation

This project is licensed under the MIT License
