import time


def main():
    fn = 'text'
    count = 0
    start_time = time.time()
    with open(fn) as filestream:
        for line in filestream:
            print(line)
            count += 1

    print('-' * 10)
    print(f'Total lines count: {count}')
    print(f'Total time: {time.time() - start_time}')


if __name__ == '__main__':
    main()
