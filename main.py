from src.application.domain.entities.transactions_response import diary_balance
from src.application.app import make_transaction_list


if __name__=='__main__':
    json_file = make_transaction_list()
    balance_resume = diary_balance(json_file)
    print(balance_resume)
