# Ten sub-processes mode
import multiprocessing
import time


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


def main():
    start = time.perf_counter()

    processes = []

    for _ in range(10):

        # defining/starting processes
        p = multiprocessing.Process(target=do_something, args=[1])

        # starting off processes
        p.start()
        processes.append(p)

    for process in processes:
        # waiting for processes
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')


if __name__ == '__main__':
    main()
