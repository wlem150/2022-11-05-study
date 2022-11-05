from datetime import timedelta
import datetime


def tommorow(text):
    
    text = text.replace(' ', '-')
    g = datetime.datetime.strptime(text, "%Y-%m-%d")
    get_tommorow = g + timedelta(days=1)
    print(get_tommorow)
    
tommorow('2018 1 1')
