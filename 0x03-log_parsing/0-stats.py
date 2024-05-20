#!/usr/bin/python3
"""
Logs parsing with pattern matching
"""
import sys
import re
import signal


def match_second_last_element(input_string, pattern):
    """
    Pattern matching the second last element
    """
    elements = input_string.split()

    if len(elements) < 2:
        return None

    second_last = elements[-2]

    match = re.match(pattern, second_last)

    return match


def match_last_element(input_string, pattern):
    """
    Pattern matching the last element
    """
    elements = input_string.split()

    if len(elements) < 1:
        return None

    last_element = elements[-1]

    match = re.match(pattern, last_element)

    return match


def stats():
    """
    Handling the pattern matching
    Extracting bytes and status code
    Printing every 10 lines
    """
    re_template_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - ' \
        r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] ' \
        r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'

    code_pattern = r'^(\d{3})$'
    size_pattern = r'^(\d+)$'

    codes = [200, 301, 400, 401, 403, 404, 405, 500]
    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    counter = 0
    total_count = 0

    for line in sys.stdin:
        counter += 1
        total_count += 1

        if match_second_last_element(line, code_pattern) is not None:
            match = match_second_last_element(line, code_pattern)
            if int(match.group(0)) in codes:
                status_codes[int(match.group(0))] += 1

        if match_last_element(line, size_pattern) is not None:
            match = match_last_element(line, size_pattern)
            file_size += int(match.group(0))

        if counter == 10:
            print(f"File size: {file_size}", flush=True)
            for key, value in status_codes.items():
                if value > 0:
                    print(f"{key}: {value}", flush=True)
            counter = 0

        def signal_handler(sig, frame):
            """
            Handling the Ctrl+C signal
            """
            print(f"File size: {file_size}")
            for key, value in status_codes.items():
                if value > 0:
                    print(f"{key}: {value}")
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)

    if counter > 0:
        print(f"File size: {file_size}", flush=True)
        for key, value in status_codes.items():
            if value > 0:
                print(f"{key}: {value}", flush=True)

    if total_count == 0:
        print("File size: 0")


if __name__ == '__main__':
    stats()
