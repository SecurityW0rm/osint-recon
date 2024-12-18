import requests
import argparse
import json
import os
import subprocess

# Shodan API Key
SHODAN_API_KEY = "your_shodan_api_key"

# HaveIBeenPwned API Key
HIBP_API_KEY = "your_haveibeenpwned_api_key"

# WHOIS API Key (optional, or use free tools like socket)
WHOIS_API_URL = "https://www.whoisxmlapi.com/whoisserver/WhoisService"
WHOIS_API_KEY = "your_whois_api_key"

def shodan_recon(target):
    """Query Shodan for target information."""
    url = f"https://api.shodan.io/shodan/host/{target}?key={SHODAN_API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "IP": data.get("ip_str", "N/A"),
                "Organization": data.get("org", "N/A"),
                "ISP": data.get("isp", "N/A"),
                "Open Ports": data.get("ports", []),
                "Location": f"{data.get('city', 'N/A')}, {data.get('country_name', 'N/A')}"
            }
        else:
            return {"error": f"Error fetching data from Shodan: {response.text}"}
    except Exception as e:
        return {"error": f"Shodan query failed: {str(e)}"}

def whois_recon(domain):
    """Query WHOIS API for domain information."""
    params = {
        "apiKey": WHOIS_API_KEY,
        "domainName": domain,
        "outputFormat": "JSON"
    }
    try:
        response = requests.get(WHOIS_API_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "Domain Name": data.get("WhoisRecord", {}).get("domainName", "N/A"),
                "Registrar": data.get("WhoisRecord", {}).get("registrarName", "N/A"),
                "Creation Date": data.get("WhoisRecord", {}).get("createdDate", "N/A"),
                "Expiration Date": data.get("WhoisRecord", {}).get("expiresDate", "N/A"),
                "Registrant": data.get("WhoisRecord", {}).get("registrant", {}).get("organization", "N/A")
            }
        else:
            return {"error": f"Error fetching data from WHOIS: {response.text}"}
    except Exception as e:
        return {"error": f"WHOIS query failed: {str(e)}"}

def hibp_recon(email):
    """Query HaveIBeenPwned for breach information."""
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": HIBP_API_KEY}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return {"Breaches": [breach["Name"] for breach in data]}
        elif response.status_code == 404:
            return {"Breaches": "No breaches found"}
        else:
            return {"error": f"Error fetching data from HIBP: {response.text}"}
    except Exception as e:
        return {"error": f"HIBP query failed: {str(e)}"}

def sherlock_recon(username):
    """Run Sherlock to scrape platforms for the username."""
    print(f"[INFO] Starting Sherlock for username: {username}")
    try:
        # Run Sherlock as a subprocess
        command = ["python", "-m", "sherlock", username, "--json", f"{username}_sherlock.json"]
        subprocess.run(command, check=True)
        # Load and return the Sherlock JSON results
        with open(f"{username}_sherlock.json", "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        return {"error": f"Sherlock query failed: {str(e)}"}

def save_report(target, data):
    """Save the gathered information into a JSON file."""
    filename = f"{target}_recon_report.json"
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"[INFO] Recon report saved as: {filename}")
    except Exception as e:
        print(f"[ERROR] Failed to save report: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Automated OSINT Recon Script")
    parser.add_argument("-t", "--target", required=True, help="Target IP, domain, or username for recon")
    parser.add_argument("--email", help="Target email for breach recon")
    parser.add_argument("--username", help="Username for Sherlock recon")
    args = parser.parse_args()

    target = args.target

    print(f"[INFO] Starting OSINT recon on: {target}")
    shodan_data = shodan_recon(target)
    whois_data = whois_recon(target)
    hibp_data = hibp_recon(args.email) if args.email else None
    sherlock_data = sherlock_recon(args.username) if args.username else None

    report = {
        "Target": target,
        "Shodan Data": shodan_data,
        "WHOIS Data": whois_data,
        "HaveIBeenPwned Data": hibp_data,
        "Sherlock Data": sherlock_data,
    }

    print(json.dumps(report, indent=4))
    save_report(target, report)

if __name__ == "__main__":
    main()
