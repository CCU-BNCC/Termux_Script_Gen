import os
import sys
import socket
from gpt4all_engine import ask_gpt
from voice_module import speak_text, listen_voice
from payment_lock import is_payment_done
from otp_manager import validate_key, get_client_ip

print("\n[+] TarmuxScriptGen (Offline ChatGPT in Termux)")
print("[i] Type 'exit' to quit or 'voice' for voice mode.")
print("\033[91m[NOTICE]\033[0m Only send money to your personal bKash: +8801337411771 (Do NOT use agent)")

if not is_payment_done():
    print("\033[91m[ERROR]\033[0m Payment required to use this tool. Please send payment to +8801337411771")
    sys.exit(1)

client_ip = get_client_ip()
print(f"[i] Your IP: {client_ip}")

user_key = input("Enter your access key: ").strip()
if not validate_key(user_key, client_ip):
    print("\033[91m[ERROR]\033[0m Invalid or IP mismatched key. Access denied.")
    sys.exit(1)

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    elif user_input.lower() == 'voice':
        user_input = listen_voice()
        print(f"You (via voice): {user_input}")

    response = ask_gpt(user_input)
    print(f"Bot: {response}\n")
    speak_text(response)
