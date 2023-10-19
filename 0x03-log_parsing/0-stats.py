#!/usr/bin/python3
"""stats module"""
import sys
import re


# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_statistics():
    """print stats"""
    print(f"Total file size: {total_file_size}")
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")


try:
    for line in sys.stdin:
        line = line.strip()
        line_count += 1

        # Use a regular expression to match the specified input format
        match = re.match(
            r'^(\d+\.\d+\.\d+\.\d+) .* "GET .+ (\d+) (\d+)$',
            line
        )
        if match:
            ip_address, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            # Update metrics
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    # Handle Ctrl + C interruption
    print_statistics()
