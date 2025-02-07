# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# - Исходные данные:
# - Количество элементов:
# - Произведение элементов:
# - Количество пар, для которых произведение элементов делится на 3 (элементы пары в
# последовательности являются соседними):

a = [-100, -50, -43, -4, 1, 21, 5, 63]

with open('data.txt', 'w') as file:
    for num in a:
        file.writelines(str(num) + ' ')


file1 = open('data.txt', 'r')

nums_data_str = file1.readline()
print(nums_data_str)

nums_data_str1 = nums_data_str.split(' ')
nums_data_list = []
for el in nums_data_str1:
    if el:
        nums_data_list.append(int(el))
print(nums_data_list)

len_of_ndl = len(nums_data_list)
print(len_of_ndl)

multiply_of_ndl = 1
for i in nums_data_list:
    multiply_of_ndl *= i
print(multiply_of_ndl)

para_del_3 = []
for g in range(len(nums_data_list)):
    i = nums_data_list[g]
    j = g + 1
    if j < len(nums_data_list):
        cur_el = [i, nums_data_list[j]]
        if (i * nums_data_list[j]) % 3 == 0:
            para_del_3.append(cur_el)
    else:
        break

print(para_del_3)




with open('data2.txt', 'w') as file2:
    file2.write(f'Исходные данные: {nums_data_str}\n')
    file2.write(f'Количество элементов: {len_of_ndl}\n')
    file2.write(f'Произведение элементов: {multiply_of_ndl}\n')
    file2.write(f'Количество пар: {para_del_3}\n')

