name = [
    {"global_id":37750254,"Number":1,"Cells":{"global_id":37750254,"Name":"Мария","Year":2015,"NumberOfPersons":252,"Month":"январь"}},
    {"global_id":37750255,"Number":2,"Cells":{"global_id":37750255,"Name":"Анастасия","Year":2015,"NumberOfPersons":224,"Month":"январь"}},
    {"global_id":37750256,"Number":3,"Cells":{"global_id":37750256,"Name":"Анна","Year":2015,"NumberOfPersons":190,"Month":"январь"}},
    {"global_id":37750257,"Number":4,"Cells":{"global_id":37750257,"Name":"Варвара","Year":2015,"NumberOfPersons":190,"Month":"январь"}}
    ]


yearslist = ''

for y in name:
    years = y['Cells']['Year']
    yearslist += str(years) + '\n'

print(yearslist)