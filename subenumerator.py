import subprocess
import threading
import time
import os

# Prerequrisits
'''
Tools to install
- assetfinder
- subfider
- sublist3r
- Download certsh.py and add execute permissions
'''


# Commands to run each tool
commands = {
    "assetfinder": "assetfinder -subs-only {domain} > assetfinder_enumerated.subs",
    "subfinder": "subfinder -d {domain} -o subfinder_enumerated.subs",
    "sublist3r": "sublist3r -n -d {domain} -o sublist3r_enumerated.subs",
    "certsh": "/opt/certsh.py -d {domain} > certsh_enumerated.subs"
}

# Function to run a command
def run_command(name, command, domain):
    print(f"[INFO] Running {name}...")
    subprocess.run(command.format(domain=domain), shell=True)
    print(f"[INFO] {name} completed.")

# Function to display live progress
def live_progress(tools_status):
    while not all(tools_status.values()):
        for tool, status in tools_status.items():
            print(f"{tool}: {'Completed' if status else 'Running'}")
        time.sleep(1)
        print("\033[F" * len(tools_status))  # Move cursor up to overwrite the lines

def main(domain):
    # Dictionary to track the status of each tool
    tools_status = {name: False for name in commands}

    # Create and start threads for each command
    threads = []
    for name, command in commands.items():
        thread = threading.Thread(target=lambda n=name, c=command: (run_command(n, c, domain), tools_status.update({n: True})))
        threads.append(thread)
        thread.start()

    # Start live progress thread
    progress_thread = threading.Thread(target=live_progress, args=(tools_status,))
    progress_thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Stop the live progress thread
    progress_thread.join()

    # Collect and merge unique subdomains
    unique_subdomains = set()
    output_files = [
        "assetfinder_enumerated.subs",
        "subfinder_enumerated.subs",
        "sublist3r_enumerated.subs",
        "certsh_enumerated.subs"
    ]

    for file in output_files:
        try:
            with open(file, "r") as f:
                for line in f:
                    unique_subdomains.add(line.strip())
        except FileNotFoundError:
            print(f"[WARNING] {file} not found. Skipping...")

    # Write unique subdomains to a file
    with open("unique_subdomains.txt", "w") as f:
        for subdomain in sorted(unique_subdomains):
            f.write(subdomain + "\n")

    print("[INFO] Subdomain enumeration completed. Unique subdomains written to unique_subdomains.txt")

if __name__ == "__main__":
    domain = input("Enter the root domain (e.g., google.com): ")
    main(domain)
