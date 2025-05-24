import random
from otp_manager import add_key, get_client_ip
from email_notify import send_email

def generate_key():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))

def main():
    user_ip = input("Enter client IP for key lock: ").strip()
    key = generate_key()
    add_key(key, user_ip)
    print(f"Generated Key: {key}")

    # Gmail setting
    from_email = "yourgmail@gmail.com"
    from_password = "your_app_password"
    to_email = "yourgmail@gmail.com"

    subject = "New GPT5AII Key Generated"
    body = f"New key: {key}\nClient IP: {user_ip}\n"

    send_email(subject, body, to_email, from_email, from_password)
    print("Notification sent to Gmail.")

if _name_ == "_main_":
    main()
