import os

# Sample database of malware signatures (hash values or patterns)
malware_signatures = {
    "malware1": "5d41402abc4b2a76b9719d911017c592",
    "malware2": "7d793037a0760186574b0282f2f435e7",
}

# Function to calculate a simple hash of a file
def calculate_hash(file_path):
    import hashlib
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Function to scan a directory for malware
def scan_directory(directory):
    infected_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            if file_hash in malware_signatures.values():
                infected_files.append(file_path)
    return infected_files

# Function to remove infected files
def remove_infected_files(infected_files):
    for file in infected_files:
        try:
            os.remove(file)
            print(f"Removed infected file: {file}")
        except Exception as e:
            print(f"Failed to remove file {file}: {e}")

# Example usage
directory_to_scan = "/path/to/scan"
infected_files = scan_directory(directory_to_scan)
if infected_files:
    print("Infected files found:")
    for file in infected_files:
        print(file)
    remove_infected_files(infected_files)
else:
    print("No infected files found.")
