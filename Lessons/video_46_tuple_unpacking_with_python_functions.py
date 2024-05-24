stock_prices = [("APPL", 50), ('GOOG', 200), ("MSFT", 40)]

for ticker, price in stock_prices :
    print(ticker, price+(0.1*price))

# emplyoyee of the year
work_hours = [("Carsten", 800), ("Louis", 1000), ("Ankhi", 1200)]
def empl_of_yr(logbook):
    current_max = 0
    human_of_month = ''

    for person, hours in logbook :
        if hours > current_max :
            current_max = hours
            human_of_month = person
        else : pass

    return (human_of_month, current_max)

# Then some tuple unpacking
name, hours = empl_of_yr(work_hours)

print(name, hours)