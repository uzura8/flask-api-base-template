import datetime as dt

def get_next_weekdate(weeknum, basedate='', is_next=True):
    if not basedate:
        basedt = dt.date.today()
    else:
        basedt = dt.datetime.strptime(basedate, '%Y-%m-%d')
    offset = (weeknum - basedt.weekday()) % 7
    if offset == 0:
        offset = 7
    if not is_next:
        offset = (7 - offset) * -1
    return basedt + dt.timedelta(days=offset)
