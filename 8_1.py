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

class Time(object):

    def __init__(self, start_time: str, end_time: str, delta: str) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.delta = delta
        self.booked = []

    def reserve_time(self, _time: str) -> list:
        self.booked.append(_time)
        return self.booked

    @property
    def get_timeline(self) -> list:
        lst = [self.start_time, ]
        k = 1
        i = self.start_time
        if self.delta == '0:30':
            while i != self.end_time:
                if i[3] == '0':
                    lst.append(f'{i[0:3]}' + '30')
                else:
                    lst.append(f'{i[0]}' + f'{int(i[1]) + 1}' + f'{i[2]}' + '00')
                i = lst[k]
                k += 1

        for l in self.booked:
            for j in lst:
                if j == l:
                    lst.remove(j)
        if not lst:
            raise ValueError('There is no time available!')
        return lst


class ReverveDateTime(Time):

    def __init__(self, dates: list, times: list) -> None:
        if not isinstance(dates, list):
            raise TypeError('argument `dates` must be a list')
        for date in dates:
            if not isinstance(date, int):
                raise TypeError('date must be a int')

        if not isinstance(times, list):
            raise TypeError('argument `times` must be a list')
        for time in times:
            if not isinstance(time, Time):
                raise TypeError('time must be a Time')

        self.dates = dates
        self.times = times

    def get_timeline(self, day: int) -> list:
        if not isinstance(day, int):
            raise TypeError('day must be a int')
        for i in range(len(self.dates)):
            if self.dates[i] == day:
                return self.times[i].get_timeline

    def reserve_time(self, day: int, _time: str):
        if not isinstance(day, int):
            raise TypeError('day must be a int')
        if not isinstance(_time, str):
            raise TypeError('time must be a string')

        for i in range(len(self.dates)):
            if self.dates[i] == day:
                return self.times[i].reserve_time(_time)


time = Time('10:00', '12:00', '0:30')
print(time.get_timeline)
time.reserve_time('12:00')
print(time.get_timeline)
time.reserve_time('10:30')
print(time.get_timeline)
print('\n')

reserve = ReverveDateTime([1, 8, 12], [Time('10:00', '12:00', '0:30'), Time('10:00', '11:00', '0:30'),
                                       Time('11:00', '12:00', '0:30')])
print(reserve.get_timeline(8))
reserve.reserve_time(8, '10:30')
print(reserve.get_timeline(8))
reserve.reserve_time(8, '10:00')
print(reserve.get_timeline(8))
