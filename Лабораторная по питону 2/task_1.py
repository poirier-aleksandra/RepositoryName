money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.03  # Ежемесячный рост цен

months = 0

while money_capital > spend:
    money_capital += salary
    money_capital -= spend
    spend *= 1 + increase
    months += 1
print("Количество месяцев, которое можно протянуть без долгов:",  months)


