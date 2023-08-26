from persiantools.jdatetime import JalaliDate, JalaliDateTime
import pytz

now = JalaliDateTime(1402, 6, 4, 17, 34, 0, 0, pytz.utc).strftime("%A")
print(now)
