# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：ebay_1.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-30 오후 7:06 
'''


from itertools import  product

def solution(schedule):
    def divide_calculate(time):
        clear = "".join(time.split(":"))
        temp = time.split(":")
        if temp[1] == '30':
            hour = str(int(temp[0])+2)
            result = hour+"00"
            return [int(clear), int(result)]
        else:
            hour = str(int(temp[0]) + 1)
            result = hour + "30"
            return [int(clear), int(result)]

    def calculate(time):
        clear = "".join(time.split(":"))
        temp = time.split(":")
        hour = str(int(temp[0]) + 3)
        result = hour + temp[1]
        return [int(clear), int(result)]

    def time_table(day, time, week):
        if day == "MO":
            week[0].append(time)
        elif day == "TU":
            week[1].append(time)
        elif day == "WE":
            week[2].append(time)
        elif day == "TH":
            week[3].append(time)
        elif day == "FR":
            week[4].append(time)

    def check(list):
        flag = True
        temp = sorted(list)
        # print(temp)
        if len(temp) > 1:
            for i in range(len(temp)-1):
                if temp[i][1] > temp[i+1][0]:
                    flag =False
                    break
        return flag

    answer = 0
    week=[[] for _ in range(5)]

    prod = product(range(4),range(4),range(4),range(4),range(4))

    for case in prod:
        flag = True

        for idx, value in enumerate(case):
            # print(idx, schedule[idx][value])
            temp = schedule[idx][value].split()
            if len(temp) == 2:
                day, time = temp[0], temp[1]
                time_table(day,calculate(time),week)
            else:
                for i in range(2):
                    time_table(temp[i*2], divide_calculate(temp[i*2-1]), week)
        for i in week:
            flag = check(i)
            if not flag: #flag in false
                break

        if flag:
            answer+=1

        # break
        week = [[] for _ in range(5)]

    # print(week)

    return answer

schedule = [["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"],
            ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"],
            ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"],
            ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"],
            ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]
print(solution(schedule))