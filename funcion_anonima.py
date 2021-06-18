def main():
    # def palindrome(string):
    #     string == string[::-1]
    #     return
    palindrome = lambda string: string == string[::-1]

    print(palindrome('ana'))


if __name__ == '__main__':
    main()