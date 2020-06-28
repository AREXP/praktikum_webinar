def main():
    fn = 'text'
    with open(fn) as filestream:
        for line in filestream:
            print(line)


if __name__ == '__main__':
    main()
