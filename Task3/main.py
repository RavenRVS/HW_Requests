import requests
from datetime import timedelta, datetime

def get_questions(tag, for_last_days):
    now = datetime.today() - timedelta(days=for_last_days)
    dt = int(now.timestamp())
    resp = requests.get(f"https://api.stackexchange.com/2.3/questions?fromdate={dt}&tagged={tag}&site=stackoverflow")
    return resp.json()

questions = get_questions('python', 2)