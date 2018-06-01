with open('referat.txt', 'r', encoding='utf-8') as ref:
    
    #chitaem file
    file = ref.read()

    #splitim slova, probel default, poluchaem spisok
    file = file.split()
    
    #podschet slov
    words = len(file)
    print(words)