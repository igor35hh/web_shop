import datetime
import os

def writeLog(kw):
    DirPostLog = "static/{}.log".format(datetime.date.today())
    if os.path.exists(DirPostLog):
        PostLog = open(DirPostLog, "a")
    else:
        PostLog = open(DirPostLog, "w")
    PostLog.write(str(kw['slug']+":"+kw['id'])+"\n")
    PostLog.close

    
