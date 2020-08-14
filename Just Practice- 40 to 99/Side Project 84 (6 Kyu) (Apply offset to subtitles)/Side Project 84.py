import datetime
def subs_offset_apply(string, offset):
    if offset <0:
        if int(abs(offset)/1000/60/60) > int(string[0:2]) or int(abs(offset)/1000/60/60) == int(string[0:2]) and int(abs(offset)/1000/60%60) > int(string[3:5]) or int(abs(offset)/1000/60/60) == int(string[0:2]) and int(abs(offset)/1000/60%60) == int(string[3:5]) and int(abs(offset)/1000%60) > int(string[6:8]):
            return "Invalid offset"
    haiz = datetime.datetime(1,1,1 if int(string[0:2]) < 24 else 1 + int(int(string[0:2])/ 24),int(string[0:2]) if int(string[0:2]) <24 else int(string[0:2])% 24,int(string[3:5]),int(string[6:8])) + datetime.timedelta(seconds = (int(string[9:13]) + offset)/1000)
    crime = datetime.datetime(1,1,1 if int(string[17:19]) < 24 else 1 + int(int(string[17:19])/ 24),int(string[17:19]) if int(string[17:19]) <24 else int(string[17:19])% 24,int(string[20:22]),int(string[23:25])) + datetime.timedelta(seconds = (int(string[26:29]) + offset)/1000)
    return '{}:{}:{},{} --> {}:{}:{},{}{}'.format((haiz.day - 1) * 24 + haiz.hour if haiz.day > 1 else haiz.hour if haiz.hour>9 else '0'+str(haiz.hour),haiz.minute if haiz.minute>9 else '0'+str(haiz.minute),haiz.second if haiz.second>9 else '0'+str(haiz.second),(int(string[9:13]) + offset)%1000 if (int(string[9:13]) + offset)%1000 > 99 else '0' + str((int(string[9:13]) + offset)%1000) if (int(string[9:13]) + offset)%1000 > 9 else '00' + str((int(string[9:13]) + offset)%1000),(crime.day - 1) * 24 + crime.hour if crime.day > 1 else crime.hour if crime.hour>9 else '0'+str(crime.hour),crime.minute if crime.minute>9 else '0'+str(crime.minute) ,crime.second if crime.second>9 else '0'+str(crime.second) ,(int(string[26:29]) + offset)%1000 if (int(string[26:29]) + offset)%1000 > 99 else '0' + str((int(string[26:29]) + offset)%1000) if (int(string[26:29]) + offset)%1000 > 9 else '00' + str((int(string[26:29]) + offset)%1000),string[29:])