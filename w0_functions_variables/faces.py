def convert(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")

def main():
    string = input()
    print(convert(string))

main()