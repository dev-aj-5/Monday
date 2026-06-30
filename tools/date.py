from datetime import datetime


def get_date():

    today = datetime.now()

    return today.strftime("%d %B %Y")