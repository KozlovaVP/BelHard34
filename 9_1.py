# Класс Time
# __init__ - принимает 2 аргумента: start_time: str (10:00). end_time: str (19:00), delta: str (0:30)
# get_timeline — возвращает график в виде списка от start_time до end_time с шагом delta
# 10:00
# 10:30
# 11:00
# ….
# 16:00
# 16:30
# 19:00
# если все временные промежутки заняты, должно быдавать строку «СВОБОДНОГО ВРЕМЕНИ НЕТ»
# reserve_time — принимает аргумент _time: str (11:30), данное время, если оно есть в timeline,
# должно быть от туда вычеркнуто (то есть вызывая get_timeline еще раз, там его не должно быть)

# Класс ReverveDateTime
# __init__ - принимает аргумент dates: list[int] — список дней месяца, а так же times: list[Time]
# — список объектов Time для каждого элемента из списка dates
# get_timeline — принимает день месяца и выводит timeline этого дня
# reserve_time — принимает день месяца и аргумент _time, данный метод должен
# резервировать указанное время в данный день месяца
from datetime import datetime, timedelta


class Timeline(object):

    def __init__(self, start_time: str, end_time: str, delta: str) -> None:
        start_time = datetime(
            hour=int(start_time.split(':')[0]),
            minute=int(start_time.split(':')[1]),
            year=1,
            month=1,
            day=1
        )
        end_time = datetime(
            hour=int(end_time.split(':')[0]),
            minute=int(end_time.split(':')[1]),
            year=1,
            month=1,
            day=1
        )
        delta = timedelta(
            hours=int(delta.split(':')[0]),
            minutes=int(delta.split(':')[0])
        )
        self.__timeline = []
        while start_time <= end_time:
            start_time += delta
            self.__timeline.append(start_time)

    @property
    def timeline(self):
        return self.__timeline


timeline = Timeline(start_time='10:00', end_time='17:00', delta='00:30')
print(timeline.timeline)
