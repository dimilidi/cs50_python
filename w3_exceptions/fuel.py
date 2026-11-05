def main():

    while True:
        try: 
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)

            if x < 0 or y < 0 or x > y:
                raise ValueError
            frac = round((x / y) * 100)

            if frac <= 1:
                print("E")
            elif frac >= 99:
                print("F")
            else:
                print(f"{frac}%")
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    main()