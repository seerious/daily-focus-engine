import datetime
from utils.time_blocks import get_today_schedule, notify_block_start, notify_block_end
from utils.logger import log_block_result, start_daily_log, daily_review_prompt

def run_assistant():
    today = datetime.date.today().isoformat()
    print(f"Welcome Matthew, here's your schedule for today.\n")

    start_daily_log(today)

    schedule = get_today_schedule()
    for block in schedule:
        notify_block_start(block)
        input(">> Press ENTER when your are done this block...")
        notify_block_end(block)
        log_block_result(block)
    
    daily_review_prompt(today)

if __name__ == "__main__":
    run_assistant()
