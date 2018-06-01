with open ('myfile.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.upper()
        line = line.replace("\n", "") #zamenyaem "\n", chotby ne bylo stroky mezhdu 1 i 2 slovom
        print(line)