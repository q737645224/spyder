import multiprocessing

def f():
    while True:
        pass

if __name__ == "__main__":
    p = multiprocessing.Process(target=f)
    p.start()

    while True:
        pass