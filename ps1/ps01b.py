# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-4-machine-interpretation-of-a-program/MIT6_00SCS11_ps1.pdf



INITIAL_PURCHASE = 999999
MIN_PAYMENT_RATE = .04
INTEREST_RATE = .18


def cc_pay(balance, payment, amount_paid = 0, month = 1, stop = 12):
    if month <= stop:
        #print("for month ", month)
        
        min_payment = payment
        amount_paid = round(amount_paid + min_payment,2)
        interest_paid = round(INTEREST_RATE/12 * balance,2)
        principal_paid = round(min_payment - interest_paid,2)
        remaining_balance = round(balance - principal_paid,2)
        #print("remaining balance ", remaining_balance)
        #print("total paid ", amount_paid)
        balance = remaining_balance
        month = month + 1
        return cc_pay(balance, payment, amount_paid, month, stop)
    else:
        return balance
        

x_min = INITIAL_PURCHASE/12
x_max = (INITIAL_PURCHASE*(1+(INTEREST_RATE/12))**12)/12

def biscect(x_min, x_max):
    x_test = (x_min+x_max)/2
    balance = cc_pay(INITIAL_PURCHASE, x_test)
    if balance > .01:
        x_min = x_test
        biscect(x_min, x_max)
    elif balance < -.01:
        x_max = x_test
        biscect(x_min, x_max)
    else:
        print(x_test)

biscect(x_min, x_max)



