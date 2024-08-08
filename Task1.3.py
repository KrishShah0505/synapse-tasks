def total_spending(request_spending, account_id: str, category: str) -> float:
    account = request_spending.get(account_id)
    if account:
        transactions = account.get("transactions", [])
        total = sum(transaction["amount"] for transaction in transactions if transaction["category"] == category and transaction["amount"] < 0)
        return -total
    return 0.0

def account_balance(request_spending, account_id: str) -> float:
    account = request_spending.get(account_id)
    if account:
        initial_balance = account.get("balance", 0.0)
        transactions = account.get("transactions", [])
        total_transactions = sum(transaction["amount"] for transaction in transactions)
        return initial_balance + total_transactions
    return 0.0

def money_owed(request_spending, account_id: str) -> float:
    account = request_spending.get(account_id)
    if account:
        initial_balance = account.get("balance", 0.0)
        transactions = account.get("transactions", [])
        total_transactions = sum(transaction["amount"] for transaction in transactions)
        final_balance = initial_balance + total_transactions
        if final_balance < 0:
            return -final_balance
        return 0.0
    return 0.0
request_spending = {
    "Mahek": {
        "balance": 3000.00,
        "transactions": [
            {"amount": -9000.00, "category": "Creatives"},
            {"amount": 7000.00, "category": "Sponsor"},
            {"amount": -2000.00, "category": "Prize-Money"}
        ]
    },
    
}

print(total_spending(request_spending, "Mahek", "Creatives"))  
print(account_balance(request_spending, "Mahek"))  
print(money_owed(request_spending, "Mahek"))  