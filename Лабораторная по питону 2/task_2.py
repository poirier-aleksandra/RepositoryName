salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
for month in range(months):
    if month == 0:
        spend = spend
    else:
        spend *= (1 + increase)

    minus = spend - salary
    if minus > 0:
        money_capital += minus

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
