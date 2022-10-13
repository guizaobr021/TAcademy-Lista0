def show_daily_balance(daily_balance: list) -> None:
    print('')
    for i in daily_balance:
        print(i)

def show_daily_balance2(daily_balance: list) -> None:
    print(daily_balance)

def show_total_transactions(transactions: list) -> None:
    print('')
    print(transactions)

def show_ordered_transactions(transactions: list) -> None:
    print('')
    for i in transactions:
        print(f'Cost: {i.cost} | Price: U${i.price} | Quantity: {i.qty} | Date: {i.date}')

def show_days_diference(days_diference: int) -> None:
    print('')
    print(f'Dias de diferença entre as datas: {days_diference} dias')
