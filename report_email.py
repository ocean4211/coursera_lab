#!/usr/bin/env python3

import os
import reports
import emails
from datetime import datetime

today = datetime.today().strftime("%B %d, %Y")
title = "Processed Update on " + today
rows = []
descr_dir = "./supplier-data/descriptions/"

for file in os.listdir(descr_dir):
    if file.lower().endswith(".txt"):
        with open(os.path.join(descr_dir, file), "r") as f:
            name = f.readline().strip()
            weight = f.readline().strip()
            rows.append(f"name: {name}<br/>weight: {weight}<br/>")

if __name__ == "__main__":
    reports.generate("/tmp/processed.pdf", title, "<br/>".join(rows))
    message = emails.generate_email(
        "automation@example.com",
        "student@example.com",
        "Upload Completed - Online Fruit Store",
        "All fruits are uploaded to our website successfully. A detailed list is attached to this email",
        "/tmp/processed.pdf",)
    emails.send_email(message)
