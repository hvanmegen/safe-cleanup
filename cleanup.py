#!/usr/bin/python3
import os
import sys
import time
import argparse

try:
    from tqdm import tqdm
except ImportError:
    print("tqdm module not found. Please install it using 'pip install tqdm'")
    sys.exit(1)

def numerize(n):
    if isinstance(n, int):
        return '{:,}'.format(n)
    elif isinstance(n, float):
        return '{:,.2f}'.format(n)
    else:
        return str(n)

try:
    from numerize import numerize
except ImportError:
    pass

MAX_ERRORS = 3
MAX_WAIT_TIME = 30

def main(args):
    dir_path, num_items, verbose = args.directory, args.number, args.verbose
    items = []
    error_count = 0
    wait_time = 1

    total_start_time = time.time()

    print(f"Scanning {dir_path} and compiling list of {numerize(num_items)} items to delete.")

    for root, _, files in os.walk(dir_path):
        for f in files:
            items.append(os.path.join(root, f))
            if len(items) >= num_items:
                break
        else:
            continue
        break

    print(f"List of {numerize(num_items)} items compiled. Proceding with deletion.")

    with tqdm(total=num_items, disable=not verbose) as pbar:
        start_time = time.time()
        for item in items:
            try:
                deletion_start = time.time()
                os.remove(item)
                deletion_time = time.time() - deletion_start

                if deletion_time > wait_time:
                    wait_time *= 2 if wait_time < MAX_WAIT_TIME // 2 else MAX_WAIT_TIME
                    time.sleep(wait_time)
                    if wait_time >= MAX_WAIT_TIME:
                        print(f"File deletion exceeded {MAX_WAIT_TIME}s. Exiting.")
                        sys.exit(1)

                pbar.update(1)
            except Exception as e:
                error_count += 1
                if error_count > MAX_ERRORS:
                    print(f"Error: {e}. Took {time.time() - start_time:.2f} seconds.")
                    sys.exit(1)
                time.sleep(wait_time * (2 ** (error_count - 1)))
                pbar.refresh()

    print(f"Deleted {numerize(num_items)} items in {time.time() - total_start_time:.2f} seconds at {num_items / (time.time() - total_start_time):.2f} it/s.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script to delete a limited number of files and directories from a given directory. It accepts a directory path, number of items to delete, and an optional verbose flag (-v) for detailed output.")
    parser.add_argument("directory")
    parser.add_argument("number", type=int)
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    try:
        main(args)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user (CTRL-C). Exiting.")
        sys.exit(1)
