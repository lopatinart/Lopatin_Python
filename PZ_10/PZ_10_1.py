# Даны имена девочек. Определить, какие из этих имен встречаются в группах на всех вторых
# курсах, какие есть только в некоторых группах и какие не встречаются ни в одной из групп.

names = {'Sophie', 'Alice', 'Maria'}

group_1 = {'Sophie', 'Maria', 'Vadim'}
group_2 = {'Oleg', 'Nastya', 'Sophie'}
group_3 = {'Maria', 'Sophie', 'Bogdan'}

all_names = []
rare_names = []
solo_names = []

for name in names:
    if name in group_1 and name in group_2 and name in group_1:
        all_names.append(name)
    elif name in names&group_1&group_2 or name in names&group_2&group_3 or name in names&group_1&group_3:
        rare_names.append(name)
    elif name not in names&group_1 or name not in names&group_2 or name not in names&group_3:
        solo_names.append(name)

print(f'Имена, которые есть во всех группах>> {all_names}')
print(f'Имена, которые есть в некоторых группах>> {rare_names}')
print(f'Имена, которых нет в группах>> {solo_names}')
