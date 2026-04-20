from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import subprocess

def retrain():
    print(f"Retraining started: {datetime.now()}")
    subprocess.run(["jupyter", "nbconvert", "--to", "notebook", 
                   "--execute", "train.ipynb"])
    print(f"Retraining complete: {datetime.now()}")

def main():
    scheduler = BlockingScheduler(timezone="UTC")
    scheduler.add_job(retrain, "cron", day_of_week="sat", hour=12, minute=0)
    print("Scheduler running — fires every Saturday at 12:00 UTC")
    scheduler.start()

if __name__ == "__main__":
    main()
