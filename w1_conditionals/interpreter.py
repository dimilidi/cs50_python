def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split(" ")
    #result = int(x) int(z)
    print(calculate(x, z, y))
   
def calculate(int1, int2, operator):
    int1 = float(int1)
    int2 = float(int2)
    match operator:
        case "+":
            return int1 + int2
        case "-":
            return int1 - int2
        case "*":
            return int1 * int2
        case "/":
            return int1 / int2

main()