import time

def stream_data(strText):
    for word in strText:
        yield word
        time.sleep(0.02)
