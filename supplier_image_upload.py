#!/usr/bin/env python3

import requests
import os


def main(url, images_dir):
    for image in os.listdir(images_dir):
        image_dir = os.path.join(images_dir, image)
        if os.path.isfile(image_dir) and image.lower().endswith(".jpeg"):
            try:
                with open(image_dir, 'rb') as opened:
                    response = requests.post(url, files={'file': opened})
                    print(f"{image} uploaded with status: {response.status_code}")
            except Exception as e:
                print(f"failed to upload {image}: {e}")


if __name__ == "__main__":
    url = "http://[external-IP-address]/upload/"
    images_dir = "./supplier-data/images/"
    main(url, images_dir)
