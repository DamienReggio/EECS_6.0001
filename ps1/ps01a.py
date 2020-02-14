#https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/MIT6_0001F16_ps1.pdf




total_cost = 1000000
sami_anual_raise = .07

portion_down_payment = .25
current_savings = 0
r = .04
down_payment = total_cost * portion_down_payment




port_min = .1
port_max = .5
i = 0


end = False

while end == False:
    portion_saved = (port_min+port_max)/2
    i += 1;
    print("pass ", i, " portion saved ", portion_saved)
    month = 0
    current_savings = 0
    annual_salary = 300000

    while month < 36:
        if (month + 1) % 6 == 0:
            annual_salary = annual_salary * (1 + sami_anual_raise)
        current_savings = round(current_savings * (1 + r/12) + annual_salary / 12\
                          * portion_saved,2)
        month += 1

    print(current_savings)
    if (down_payment - current_savings) < -100:
        port_max = portion_saved
    elif (down_payment - current_savings) > 100:
        port_min = portion_saved
    else:
        print("all done:", portion_saved)
        end = True


print("Number of moneths: ", month)
