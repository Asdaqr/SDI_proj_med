import datetime as dt
import calendar


def notification_times(start, delta):
    """returns list containing the times at which medicine should be taken - object is a datetime obj"""
    end = start
    med_day_list = list()

    while end - start < dt.timedelta(days=14):
        end = end + delta
        med_day_list.append(end)

    return med_day_list


