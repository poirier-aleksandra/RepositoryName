def find_common_participants(group1, group2, delimiter=','):
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    common_participants = participants1.intersection(participants2)

    return sorted(common_participants)


group_1 = "Иванов,Петров,Сидоров"
group_2 = "Сидоров,Кузнецов,Петров"
common = find_common_participants(group_1, group_2)
print(common)
