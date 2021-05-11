
def num_letters(fil, letter):
    count = 0
    for line in fil:
        line = line.strip()
        line = line.lower()
        if line[0] == letter:
            count += 1
        print(count)
    return count


#open file
fin = open('words_alpha.txt')



# Search for word by looping over file
count = 0
longest = ''
num_a = 0
for line in fin:
    line = line.strip()
    line = line.lower()

    count += 1

    if len(line) > len(longest):
        longest = line


    if line[0] == 'a':
        num_a += 1


co = num_letters(fin, 'a')
print(co)


# Close file
fin.close()

print(f'Count: {count}')
print(f'Lonest: {longest} ({len(longest)})')
print(f'A: {num_a} ({round((num_a / count) * 100, 2)}%)')

