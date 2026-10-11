def main():
    amount_due = 50
   
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        coin = int(input("Insert coin: "))
       
        if coin not in [25, 10, 5]:
            amount_due = amount_due
            continue
        
        amount_due = amount_due - coin
    
    print(f"Change Owed: {abs(amount_due)}")

if __name__ == "__main__":
    main()