#!/usr/bin/python3
"""
Log parsing script
Reads stdin line by line and computes metrics
"""
import sys

# Initialize variables
total_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """Prints the accumulated statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Validate line length and parts to avoid index errors
        if len(parts) < 7:
            continue

        # Extract and add file size
        try:
            file_size = int(parts[-1])
            total_size += file_size
        except ValueError:
            continue

        # Extract and count status code
        status_code = parts[-2]
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        # Print metrics after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Final print after reading all lines
print_stats()

