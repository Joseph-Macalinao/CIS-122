'''
Joseph Macaliao
CIS 122 - Spring 2021
Credit: Lab
Description: Get the stats from a file
'''
def num_letters(fil, letter):
    '''
    this function will open a file and get it ready for its stats to be taken

    this function will take a list argument and take open it. it will then strip all of its lines
    and make them lower to be able to get the stats of each individual line

    arg -
    fil(file) - file that will be opened
    letter(str) - checking first char of each line

    return -
    count(int) - how many lines there are in a file
    '''
    count = 0
    for line in fil:
        line = line.strip()
        line = line.lower()
        if line[0] == letter:
            count += 1
        print(count)
    return count


#open file
fin = open('../words_alpha.txt')



# Search for word by looping over file
count = 0
longest = ''
num_a = 0
num_b = 0
num_c = 0
num_d = 0
num_e = 0
num_f = 0
num_g = 0
num_h = 0
num_i = 0
num_j = 0
num_k = 0
num_l = 0
num_m = 0
num_n = 0
num_o = 0
num_p = 0
num_q = 0
num_r = 0
num_s = 0
num_t = 0
num_u = 0
num_v = 0
num_w = 0
num_x = 0
num_y = 0
num_z = 0
palindrom = 0

for line in fin:
    line = line.strip()
    line = line.lower()

    count += 1

    if len(line) > len(longest):
        longest = line


    if line[0] == 'a':
        num_a += 1
    if line[0] == 'b':
        num_b += 1
    if line[0] == 'c':
        num_c += 1
    if line[0] == 'd':
        num_d += 1
    if line[0] == 'e':
        num_e += 1
    if line[0] == 'f':
        num_f += 1
    if line[0] == 'g':
        num_g += 1
    if line[0] == 'h':
        num_h += 1
    if line[0] == 'i':
        num_i += 1
    if line[0] == 'j':
        num_j += 1
    if line[0] == 'k':
        num_k += 1
    if line[0] == 'l':
        num_l += 1
    if line[0] == 'm':
        num_m += 1
    if line[0] == 'n':
        num_n += 1
    if line[0] == 'o':
        num_o += 1
    if line[0] == 'p':
        num_p += 1
    if line[0] == 'q':
        num_q += 1
    if line[0] == 'r':
        num_r += 1
    if line[0] == 's':
        num_s += 1
    if line[0] == 't':
        num_t += 1
    if line[0] == 'u':
        num_u += 1
    if line[0] == 'v':
        num_v += 1
    if line[0] == 'w':
        num_w += 1
    if line[0] == 'x':
        num_x += 1
    if line[0] == 'y':
        num_y += 1
    if line[0] == 'z':
        num_z += 1


    if line == line[::-1]:
        palindrom +=1



co = num_letters(fin, 'a')
print(co)


# Close file
fin.close()

print(f'Count: {count}')
print(f'Lonest: {longest} ({len(longest)})')
print(f'A: {num_a} ({round((num_a / count) * 100, 2)}%)')
print(f'B: {num_b} ({round((num_b / count) * 100, 2)}%)')
print(f'C: {num_c} ({round((num_c / count) * 100, 2)}%)')
print(f'D: {num_d} ({round((num_d / count) * 100, 2)}%)')
print(f'E: {num_e} ({round((num_e / count) * 100, 2)}%)')
print(f'F: {num_f} ({round((num_f / count) * 100, 2)}%)')
print(f'G: {num_g} ({round((num_g / count) * 100, 2)}%)')
print(f'H: {num_h} ({round((num_h / count) * 100, 2)}%)')
print(f'I: {num_i} ({round((num_i / count) * 100, 2)}%)')
print(f'J: {num_j} ({round((num_j / count) * 100, 2)}%)')
print(f'K: {num_k} ({round((num_k / count) * 100, 2)}%)')
print(f'L: {num_l} ({round((num_l / count) * 100, 2)}%)')
print(f'M: {num_m} ({round((num_m / count) * 100, 2)}%)')
print(f'N: {num_n} ({round((num_n / count) * 100, 2)}%)')
print(f'O: {num_o} ({round((num_o / count) * 100, 2)}%)')
print(f'P: {num_p} ({round((num_p / count) * 100, 2)}%)')
print(f'Q: {num_q} ({round((num_q / count) * 100, 2)}%)')
print(f'R: {num_r} ({round((num_r / count) * 100, 2)}%)')
print(f'S: {num_s} ({round((num_s / count) * 100, 2)}%)')
print(f'T: {num_t} ({round((num_t / count) * 100, 2)}%)')
print(f'U: {num_u} ({round((num_u / count) * 100, 2)}%)')
print(f'V: {num_v} ({round((num_v / count) * 100, 2)}%)')
print(f'W: {num_w} ({round((num_w / count) * 100, 2)}%)')
print(f'X: {num_x} ({round((num_x / count) * 100, 2)}%)')
print(f'Y: {num_y} ({round((num_y / count) * 100, 2)}%)')
print(f'Z: {num_z} ({round((num_z / count) * 100, 2)}%)')
print(f'Palindromes: {palindrom}')

