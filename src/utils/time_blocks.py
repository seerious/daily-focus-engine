import json

def get_today_schedule():
    with open("schedule.json", "r") as f:
        return json.load(f)

def notify_block_start(block):
    print(f"\nStarting: {block['name']} ({block['start']}-{block['end']})")

def notify_block_end(block):
    print(f"Finished: {block['name']}")

