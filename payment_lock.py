import os

def is_payment_done():
    return os.path.exists(".paid")
