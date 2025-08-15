#!/usr/bin/env python3

import psutil       # For checking system resource usage
import socket       # For DNS resolution check
import emails       # script emails.py to generate and send emails


def cpu_check():
    """Check if CPU usage is below 80%."""
    cpu_percent = psutil.cpu_percent(
        interval=1)  # Measure CPU usage over 1 second
    return cpu_percent < 80


def disk_check():
    """Check if available disk space is more than 20%."""
    disk_usage = psutil.disk_usage(
        '/')  # Get disk usage statistics for root directory
    return disk_usage.percent < 80


def mem_check():
    """Check if available memory is greater than 100 MB."""
    mem = psutil.virtual_memory()
    # Convert available bytes to megabytes and check threshold
    return (mem.available / 1024**2) > 100


def is_resolved():
    """
    Check if 'localhost' resolves to an IP address.
    Returns True if resolution is successful, False otherwise.
    """
    try:
        ip = socket.gethostbyname("localhost")
        return ip == "127.0.0.1"  # Ensure localhost resolves correctly
    except socket.gaierror:
        return False


def main():
    """
    Run all system checks and send email alerts if any check fails.
    """
    sender = "automation@example.com"
    recipient = "student@example.com"
    body = "Please check your system and resolve the issue as soon as possible"

    # Check CPU usage and send alert email if over 80%
    if not cpu_check():
        email = emails.generate_email(
            sender, recipient, "Error - CPU usage is over 80%", body)
        emails.send_email(email)

    # Check disk usage and send alert email if less than 20% space available
    if not disk_check():
        email = emails.generate_email(
            sender, recipient, "Error - Available disk space is less than 20%", body)
        emails.send_email(email)

    # Check memory availability and send alert email if less than 100MB available
    if not mem_check():
        email = emails.generate_email(
            sender, recipient, "Error - Available memory is less than 100MB", body)
        emails.send_email(email)

    # Check if 'localhost' resolves correctly, send alert if not
    if not is_resolved():
        email = emails.generate_email(
            sender, recipient, "Error - localhost cannot be resolved to 127.0.0.1", body)
        emails.send_email(email)


if __name__ == "__main__":
    main()
