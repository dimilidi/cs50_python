def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (s[0:2].isalpha()
            and 2 <= len(s) <= 6
            and s.isalnum()
            and numbers_at_end(s)):
        return True
    return False


def numbers_at_end(s):
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            if not s[i:].isdigit():
                return False
            break
    return True

main()

