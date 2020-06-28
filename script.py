def main():
    fn = 'text'
    count = 0
    with open(fn) as filestream:
        for line in filestream:
            print(line)
            count += 1

    print('-' * 10)
    print(f'Total lines count: {count}')


if __name__ == '__main__':
    main()
