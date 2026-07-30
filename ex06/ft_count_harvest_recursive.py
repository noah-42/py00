def ft_count_harvest_helper(current_day, total_days):
    if current_day > total_days:
        print("Harvest time!")
        return
    print(f"Day {current_day}")
    ft_count_harvest_helper(current_day + 1, total_days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_count_harvest_helper(1, days)
