import os
from datetime import date

def start_daily_log(today):
    log_path = f"logs/{today}.txt"
    with open(log_path, "w") as f:
        f.write(f"Daily log: {today}\n\n")

def log_block_result(block):
    notes = input(f"\nWhat did you do during {block['name']}?\n> ")
    today = date.today().isoformat()
    log_path = f"logs/{today}.txt"
    with open(log_path, "a") as f:
        f.write(f"\n[{block['start']}-{block['end']}] {block['name']}\n")
        f.write(f"-> Notes: {notes.strip()}\n")

def daily_review_prompt(today):
    print("\nEnd of Day Review:")
    worked = input("\nWhat worked today?\n> ")
    blocked = input("\nWhat didn't work today?\n> ")
    priority = input("\nTop priority for tomorrow?\n> ")

    log_path = f"logs/{today}.txt"
    with open(log_path, "a") as f:
        f.write("\n--- Daily Review ---\n")
        f.write(f"What worked: {worked.strip()}\n")
        f.write(f"What didn't: {blocked.strip()}\n")
        f.write(f"Priority for tomorrow: {priority.strip()}\n")