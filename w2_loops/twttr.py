def main():
    vowels = ["a", "e", "i", "o","u"]
    string = input("Input: ")
    output = ""

    for c in string:
        if c.lower() in vowels:
            continue
        output += c
    
    print(f"Output: {output}")

if __name__ == "__main__":
    main()