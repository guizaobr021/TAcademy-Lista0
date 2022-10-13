from src.application.app import calculate_daily_balance, generate_balance_json, make_transaction_list, calculate_total_transactions, calculate_days_diference
from src.application.output import show_daily_balance, show_total_transactions, show_ordered_transactions,show_days_diference


if __name__=='__main__':
    transaction_list = make_transaction_list()
    daily_balance = calculate_daily_balance(transaction_list)
    generate_json = generate_balance_json(daily_balance)
    total_transactions = calculate_total_transactions(transaction_list)
    days_diference = calculate_days_diference(transaction_list)

    show_daily_balance(daily_balance)
    show_total_transactions(total_transactions)
    show_ordered_transactions(sorted(transaction_list, key=lambda transaction: transaction.cost, reverse=False))
    show_days_diference(days_diference)
    print(generate_json)
