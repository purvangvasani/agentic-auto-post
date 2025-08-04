import datetime

def should_post_today():
    return datetime.datetime.today().day % 2 == 0
