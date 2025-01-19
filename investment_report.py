

tt_invested = 0
tt_current = 0

num = int(input("No of investments:"))
for _ in range(num):

    invested = float(input("Invested amount:"))
    current = float(input("Current amount:"))
    profit_loss = current - invested
    
    tt_invested += invested
    tt_current += current

    print("\n\tinvested\tcurrent\t\tProfit/Loss")
    print(f"\t{invested}\t\t{current}\t\t{profit_loss}")

    if profit_loss < 0:
        print("\n\t\t\t\t\tLOSS")
    elif profit_loss > 0:
        print("\n\t\t\t\t\t\tPROFIT")
    else:
        print("\n\t\t\t\t\t\tNO PROFIT OR LOSS")

    tt_profit_loss = tt_current - tt_invested
    print("\n")
    print(f"Total\t{tt_invested}\t\t{tt_current}\t\t{tt_profit_loss}")

    if tt_profit_loss < 0:
        print("\t\t\t\t\tLOSS")
    elif tt_profit_loss >0:
        print("\t\t\t\t\tPROFIT")
    else:
        print("\t\t\t\t\tNO PROFIT OR LOSS")
    
    
