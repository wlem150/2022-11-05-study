# 사용자로부터 날짜를 나타내는 세 개의 숫자를 입력받습니다. 첫 번째 숫자는 연도를 나타내는 네 자리 숫자이고, 두 번째 숫자는 월을, 세 번째 숫자는 일을 나타냅니다.

# 입력받은 날짜를 mm/dd/yyyy 형식으로 출력합니다. 월을 두 자리 숫자(01, 02, 03, ..., 12)로, 일을 두 자리 숫자(01, 02, 03, ..., 31)로, 연도를 네 자리 숫자로 나타냅니다.

# 입력받은 날짜의 다음 날에 해당하는 날짜도 같은 형식으로 출력합니다. 단, 윤년은 무시합니다(2월은 항상 28일까지 있다고 가정합니다).

from datetime import timedelta
import datetime

def tommorow(text):
    
    text = text.replace(' ', '-')
    get_time = datetime.datetime.strptime(text, "%Y-%m-%d")
    get_tommorow = get_time + timedelta(days=1)
    print(get_time)
    print(get_tommorow)
    


if __name__=="__main__":
    print(tommorow('2018 2 28'))

#---------------------------------------------------------
# 정답으로 올라온 답안

def read_date():
    year, month, day = tuple(map(int, input().split()))
    return year, month, day

def print_date(date):
    year, month, day = date
    print("%02d/%02d/%04d" % (month, day, year))

def advance_day(date):
    year, month, day = date
    
    # end_of_month = (month == 1 and day == 31) or \
               # (month == 2 and day == 28) or \
               # (month == 3 and day == 31) or \
               # (month == 4 and day == 30) or \
               # (month == 5 and day == 31) or \
               # (month == 6 and day == 30) or \
               # (month == 7 and day == 31) or \
               # (month == 8 and day == 31) or \
               # (month == 9 and day == 30) or \
               # (month == 10 and day == 31) or \
               # (month == 11 and day == 30) or \
               # (month == 12 and day == 31)
    
    #end_of_month = (month in [1, 3, 5, 7, 8, 10, 12] and day == 31) or \
    #                     (month in [4, 6, 9, 11] and day == 30) or \
    #                     (month == 2 and day == 28)
    
    end_of_month = (month, day) in [(1, 31), (2, 28), (3, 31), (4, 30), (5,
        31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
    
    end_of_year = month == 12 and day == 31
    
    if end_of_month:
        if end_of_year:
            year += 1
            month = 1
            day = 1
        else:
            month += 1
            day = 1
    else:
        day += 1
    
    return year, month, day
    
if __name__ == "__main__":
    today = read_date()
    print_date(today)
    tomorrow = advance_day(today)
    print_date(tomorrow)