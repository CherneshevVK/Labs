def find_common_participants(group1, group2, delimiter=","):
    set1 = set(group1.split(delimiter))
    set2 = set(group2.split(delimiter))
    common_participants = set1 & set2
    return sorted(list(common_participants))

group1 = "Дима,Андрей,Маша,Андрей"
group2 = "Алёна,Михаил,Дима,Маша,Андрей"
common_participants = find_common_participants(group1, group2)
print(common_participants)