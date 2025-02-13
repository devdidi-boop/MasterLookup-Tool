import requests
import json

# Fonction de recherche IP (utilise l'API ipinfo.io)
def lookup_ip(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        return f"Error occurred while looking up the IP: {e}"

# Fonction de recherche d'un ID Discord
def lookup_discord_id(discord_id, bot_token):
    url = f"https://discord.com/api/v10/users/{discord_id}"
    headers = {
        "Authorization": f"Bot {bot_token}"
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
    except Exception as e:
        return f"Error occurred while looking up the Discord ID: {e}"

# Fonction d'envoi de message via un webhook Discord
def send_webhook_message(webhook_url, message):
    data = {
        "content": message
    }
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            return "Message sent successfully!"
        else:
            return f"Failed to send message. Status Code: {response.status_code}"
    except Exception as e:
        return f"Error occurred while sending the message: {e}"

# Interface en ligne de commande
def run_tool():
    print("Welcome to MasterLookup Tool!")
    while True:
        print("\nChoose an option:")
        print("1. Lookup IP address")
        print("2. Lookup Discord ID")
        print("3. Send message via Webhook")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ip_address = input("Enter the IP address to lookup: ")
            result = lookup_ip(ip_address)
            print(json.dumps(result, indent=4))

        elif choice == "2":
            discord_id = input("Enter the Discord ID to lookup: ")
            bot_token = input("Enter your Discord bot token: ")
            result = lookup_discord_id(discord_id, bot_token)
            print(json.dumps(result, indent=4))

        elif choice == "3":
            webhook_url = input("Enter the Webhook URL: ")
            message = input("Enter the message to send: ")
            result = send_webhook_message(webhook_url, message)
            print(result)

        elif choice == "4":
            print("Exiting MasterLookup Tool...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_tool()