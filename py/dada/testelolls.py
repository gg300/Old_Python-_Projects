# lol = {'carte':["Moara cu noroc","Ion"],'minge':"de folbal",'harta':"politica"}

# lol.update({'minge':["de handbal","de fotbal","de basket"]})

# print(lol.values())

# def lolo(b,a=0):
#     return a*b

# print(lolo(2,6))

def is_year_leap(year):
    if year%100==0 and year%4==0:
        if year%400==0:
            return True
    elif year%4==0:
        return True
    return False

def days_in_month(year, month):
    list =[]    
    for i in range(1,13):
        list.append(i)
    if month==2:
        if is_year_leap(year):
            return 29
        return 28
    if month<13 and month>0:
        for i in range(1,8):
            if month == i:
                if i % 2 == 1:
                    return 31
                if i % 2 == 0:
                    return 30
        for i in range(8,13):
            if month == i:
                if i % 2 == 1:
                    return 30
                if i %2 == 0: 
                    return 31   

# august 23 

# 8  - > 23 
