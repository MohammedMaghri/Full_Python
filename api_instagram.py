from instagrapi import Client

with open("credentials.txt", "r") as f:
    username, password = f.read().splitlines()