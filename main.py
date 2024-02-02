"""
    In this project, you'll create a program that that tells
    you when the value of your Bitcoin falls below $30,000.

    You will need to:
    - Create a function to convert Bitcoin to USD
    - If your Bitcoin falls below $30,000, print a message.

    You can assume that 1 Bitcoin is worth $40,000

"""

investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000
#Objective 
# 1) write a function to calculate bitcoin to usd
# 2) use function to calculate if the investment is below $30,000
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    usd_value = bitcoin_amount * bitcoin_value_usd
    return usd_value

bitcoin_amount = 1.2
bitcoin_value_usd = 40000

investment_in_usd = bitcoinToUSD(bitcoin_amount, bitcoin_value_usd)

if investment_in_usd < 30000:
    print("Alert: The value of your Bitcoin has fallen below $30,000.")
