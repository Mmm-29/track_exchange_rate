import subprocess

TASK_NAME = "ExchangeRateFetchingTaskDaily"
PYTHON_PATH = r"D:\exchange_rate\virtual_env\Scripts\python.exe"
PROJECT_DIR = r"D:\exchange_rate"
SCRIPT_NAME = "main.py"

SCHEDULE_TIME = "11:06"

command = (
    f'schtasks /create /sc DAILY /tn "{TASK_NAME}" '
    f'/tr "cmd /c cd /d {PROJECT_DIR} && {PYTHON_PATH} {SCRIPT_NAME}" '
    f'/st {SCHEDULE_TIME} /f'
)

subprocess.run(command, shell=True)

print("Task Scheduled Successfully!")