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

    def get_timeline(self) -> list:
        lst = [self.start_time,]
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
        if not lst:
            print('There is no time available!')
        return lst

    def reserve_time(self, _time: str, lst: list):
        result = []
        for i in self.get_timeline():
            if i != _time:
                result.append(i)
        return result


time = Time('10:00', '19:00', '0:30')
print(time.get_timeline())
time1 = time.reserve_time('16:00', time)
print(time1)



