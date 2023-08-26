def show_jalali_age(birth):
    import jdatetime
    # now = str(jdatetime.datetime.now()).split()[0]
    # thisyear = int(now.split("-")[0])
    thisyear = jdatetime.datetime.now().year
    age = thisyear - birth
    print(age)


def show_gregorian_age(birth):
    import datetime
    thisyear = datetime.datetime.now().year
    age = thisyear - birth
    print(age)


birth = int(input("Enter your birth year : "))

show_jalali_age(birth)
# show_gregorian_age(birth)
