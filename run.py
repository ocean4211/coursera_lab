#!/usr/bin/env python3

import os
import requests


def main(url, descr_dir):
    descriptions = []
    for file in os.listdir(descr_dir):
        file_dir = os.path.join(descr_dir, file)
        if file.lower().endswith(".txt"):
            with open(file_dir, 'r') as f:
                lines = [line.strip() for line in f.readlines()]
                descriptions.append({
                    "name": lines[0],
                    "weight": int(lines[1].replace("lbs", "")),
                    "description": lines[2],
                    "image_name": file.replace(".txt", ".jpeg")
                })
    for item in descriptions:
        try:
            r = requests.post(url, json=item)
            print(f"Posted {item["name"]} - Status: {r.status_code}")
            if r.status_code != 201:
                print(f"Server response: {r.text}")
        except Exception as e:
            print(f"Failed to post {item['name']}: {e}")


if __name__ == "__main__":
    url = "http://[external-IP-address]/fruits/"
    descr_dir = "./supplier-data/descriptions/"
    main(url, descr_dir)
