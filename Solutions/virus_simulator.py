#!/usr/bin/env python3
# MOCK VIRUS - FOR TESTING PURPOSES ONLY

import os
import time
import random

def fake_payload():
    print("[*] Initializing payload...")
    time.sleep(1)
    files = ["data1.txt", "img2.jpg", "system32.dll", "config.sys"]
    for file in files:
        print(f"[!] Encrypting {file}...")
        time.sleep(0.5)

def show_fake_warning():
    print("\n!!! YOUR SYSTEM HAS BEEN INFECTED !!!")
    print("All your files have been encrypted.")
    print("Send 1 BTC to 1FAKEADDRESS999XYZ to recover your data.")
    print("This is just a test. No files were harmed.")

def main():
    fake_payload()
    show_fake_warning()

if __name__ == "__main__":
    main()
