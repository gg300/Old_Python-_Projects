class lol:
    def __init__(self, name: str, price: float, quant=0):
        #run validation
        assert price >0,f"Price {price} should be greater than zero"
        assert quant >0,f"Quantity {quant} should be greater than zero"
        #assign to self object
        self.name = name
        self.price = price
        self.quant = quant
    def calc_price(self):
        return self.price * self.quant
# item=input("ITEM : ")
# price = float(input("PRICE : "))
# quant = int(input("QUANTITY : "))
# item=lol(item,price,quant)
# 

class time : 
    def __init__(self,days=0,hours=0,minutes=0,seconds=0,milisec=0) :
        #run errors
        assert days >= 0 , f"Days {days} should be greater than 0"
        assert hours >= 0 , f"Days {hours} should be greater than 0"
        assert minutes >= 0 , f"Days {minutes} should be greater than 0"
        assert seconds >= 0 , f"Days {seconds} should be greater than 0"
        assert milisec >= 0 , f"Days {milisec} should be greater than 0"
        # assing to object
        time.days = days
        time.hours = hours
        time.minutes = minutes
        time.seconds = seconds
        time.milisec = milisec
    def calc_days(self):
        return self.days
    def calc_hours(self):
        if self.days>0:
            hours=self.hours+(self.days*24)
        else:
            hours = self.hours
        return hours    
    def calc_minutes(self):
        if self.days>0:
            hours=self.hours+self.days*24
        else:
            hours=self.hours
        if self.hours>0 or hours > 0:
            minutes = self.minutes + hours*60
        else:
            minutes = self.minutes
        return minutes
    def calc_seconds(self):
        if self.days>0:
            hours=self.hours+self.days*24
        else:
            hours=self.hours

        if self.hours>0 or hours > 0:
            minutes = self.minutes + hours*60
        else:
            minutes = self.minutes
        if self.minutes>0 or minutes > 0:
            seconds = self.seconds + minutes*60
        else:
            seconds = self.seconds       
        return seconds
    def calc_milisec(self):
        if self.days>0:
            hours=self.hours+self.days*24
        else:
            hours=self.hours
        if self.hours>0 or hours > 0:
            minutes = self.minutes + hours*60
        else:
            minutes = self.minutes
        if self.minutes>0 or minutes > 0:
            seconds = self.seconds + minutes*60
        else:
            seconds = self.seconds 
        if self.seconds>0 or seconds>0:
            milisec= self.milisec + seconds * 1000
        else:
            milisec=self.milisec
        return milisec
# 
# days = int(input("days: "))
# hours=int(input("hours: "))
# minutes=int(input("minutes: "))
# seconds=int(input("seconds: "))
# milisec=int(input("milisec: "))
# 
# time1 = time(days,hours,minutes,seconds,milisec)
