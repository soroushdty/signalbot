#Loop 'n' Log Function
def loopnlog(wrapper_function,sleep_time):
    global fullfilledl
    global fullfilleds
    while True:
        try:
            now = datetime.datetime.now(tz=tz)
            print(f'*Started at {now.strftime("%d %b %H:%M:%S")}*')
            wrapper_function()
        except Exception as exception:
            now = datetime.datetime.now(tz=tz)
            print(f'--Error: {type(exception).__name__} at {now.strftime("%d %b %H:%M:%S")}--')
            #fullfilled global variables reset
            fullfilledl = []
            fullfilleds = []
            time.sleep(sleep_time)
            pass
        else:
            now = datetime.datetime.now(tz=tz)
            print(f'*Completed at {now.strftime("%d %b %H:%M:%S")}*')
            time.sleep(sleep_time)
            pass