# Advent of Code 2018 - day 1


def checklist(freq, f_list):
    found = False
    for f in f_list:
        if f == freq:
            found = True
    return found


file_obj = open('d1_input.txt')

freq_list = list()
freq = 0
freq_list.append(freq)
is_found = False
part_two = 0
for row in file_obj:
    method = row[0]
    val = row[1:]
    if method == '+' or method == '-':
        if method == '+':
            freq += int(val)
        elif method == '-':
            freq -= int(val)
        if not is_found:
            is_found = checklist(freq, freq_list)
            if is_found:
                part_two = freq
        freq_list.append(freq)
    else:
        pass


print(' Part one - The frequency is shifted by: ' + str(freq))
print(' Part two - The first frequency that is found twice is: ' + str(part_two))

print(freq_list)

file_obj.close()

