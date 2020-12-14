import json
from multiprocessing.pool import ThreadPool
# from concurrent.futures import ThreadPoolExecuter
import os

from rich.console import Console

console = Console()


def display_progress(iteration, total):
    bar_max_width = 45 # char
    bar_current_width = bar_max_width * iteration // total
    bar = "█" * bar_current_width + "-" * (bar_max_width - bar_current_width)
    progress = "%.1f" % (iteration / total * 100)
    console.print(f"|{bar}| {progress} %", end="\r", style="bold green")
    if iteration == total:
        print()


def extract_json_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def threadpool_executer(function, iterable, iterable_length):
    number_of_workers = os.cpu_count()
    print(f"\nRunning using {number_of_workers} workers.\n")
    with ThreadPool(number_of_workers) as pool:
        for loop_index, _ in enumerate(pool.imap(function, iterable), 1):
            display_progress(loop_index, iterable_length)