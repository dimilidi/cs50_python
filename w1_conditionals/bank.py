def main():
    greeting = input("Greeting: ").strip().lower()

    def evaluate(input):
        if greeting[0:5] == "hello":
            return "$0"
        elif greeting[0] == "h":
            return "$20"
        else:
            return "$100"

    print(evaluate(greeting))

main()