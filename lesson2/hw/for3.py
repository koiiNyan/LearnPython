grades = [
{'school_class1': '4a', 'scores' : [3,4,4,5,2]},
{'school_class2': '4b', 'scores' : [4,4,5,5,3]},
{'school_class3': '5a', 'scores' : [4,5,5,5,5]},
{'school_class4': '5b', 'scores' : [3,3,4,5,3]}]

#poluchit' znachenie scores !!

#sredniy ball po klassu1 = (3+4+4+5+2)/5 = 3,6
#sb klass2 = (4+4+5+5+3)/5 = 4,2
#sb klass3 = (4+5+5+5+5)/5 = 4,8
#sb klass4 = (3+3+4+5+3)/5 = 3,6
#sb shkola = ((sb klass1)+(sb klass2)+ (sbklass3) + (sbklass4))/4 = 4,05


print(grades [0] ['scores']) #pechataet tolko scores iz 0 elementa spiska

print(sum(grades [0] ['scores'])) #sum of scores of sc1

grades1 = (sum(grades [0] ['scores']))/5
grades2 = (sum(grades [1] ['scores']))/5
grades3 = (sum(grades [2] ['scores']))/5
grades4 = (sum(grades [3] ['scores']))/5
grades5 = (grades1 + grades2 + grades3 + grades4)/4

print('4a average grade: ', grades1)
print('4b average grade: ', grades2)
print('5a average grade: ', grades3)
print('5b average grade: ', grades4)
print('School average grade: ', round(grades5))

#Class grades using for loop:

for scores in (grades [0] ['scores'],
    grades [1] ['scores'], 
    grades [2] ['scores'], 
    grades [3] ['scores']):
    print("Class average grade: ", ((sum(scores))/5))
