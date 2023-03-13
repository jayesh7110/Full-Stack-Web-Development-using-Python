# There are three dictionary with keys and values
Bank_1 = {"Saving rate":2.70,"Fixed Deposit rate":5.40}
Bank_2 = {"Saving rate":3.00,"Fixed Deposit rate":5.50}
Bank_3 = {"Saving rate":3.50,"Fixed Deposit rate":5.70}

# nested dictionary for data from another dictionary
bank_data = {"SBI":Bank_1,"HDFC":Bank_2,"Kotal":Bank_3}

# Loop through get the key, value 
for key,value in bank_data.items():
    # Print the keys and value
    print(f"{key} : {value}")
