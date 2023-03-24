# Write a python program to merge two python dictionaries into one dictionary.

bank = {
    "employee_name": "Tiwari",
    "id": 231324,
    "position": "Accountant",
    "salary": "1.25 lacs"
}

customer = {
    "customer_name": "Ankit sharma",
    "account_no": 2313214424,
    "balance": 67787

}

bank.update(customer)

print(bank)