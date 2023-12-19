import datetime as dt

def test():
    print('hello world!!')
    print(dt.datetime.utcnow().strftime('%Y/%m/%d %H:%M'))

test()