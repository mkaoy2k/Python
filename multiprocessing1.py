# multiple-process mode
import multiprocessing
import time


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == '__main__':
    start = time.perf_counter()

    # defining processes
    p1 = multiprocessing.Process(target=do_something, args=[1])
    p2 = multiprocessing.Process(target=do_something, args=[1])

    # starting off processes
    p1.start()
    p2.start()

    # waiting for processes
    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
