import os
import json
import socket

KEY_FILE = "key_store.txt"
KEY_IP_MAP_FILE = "key_ip_map.json"

def get_client_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def validate_key(key, ip):
    if not os.path.exists(KEY_FILE) or not os.path.exists(KEY_IP_MAP_FILE):
        return False
    with open(KEY_FILE, "r") as f:
        keys = f.read().splitlines()
    if key not in keys:
        return False
    with open(KEY_IP_MAP_FILE, "r") as f:
        ip_map = json.load(f)
    if ip_map.get(key) != ip:
        return False
    return True

def add_key(key, ip):
    if not os.path.exists(KEY_FILE):
        open(KEY_FILE, "w").close()
    with open(KEY_FILE, "a") as f:
        f.write(key + "\n")
    ip_map = {}
    if os.path.exists(KEY_IP_MAP_FILE):
        with open(KEY_IP_MAP_FILE, "r") as f:
            ip_map = json.load(f)
    ip_map[key] = ip
    with open(KEY_IP_MAP_FILE, "w") as f:
        json.dump(ip_map, f)
