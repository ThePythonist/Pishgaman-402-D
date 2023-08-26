import jdatetime

test = str(jdatetime.datetime.now()).split()
now = test[1]
# now = now.split(":")
# print(f"{now[0]}:{now[1]}")
now = now[:5]
print(now)
