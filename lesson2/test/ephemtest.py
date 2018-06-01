import ephem
mars = ephem.Mars ('2018/05/17')

print(ephem.constellation(mars))

print(ephem.next_full_moon ('2018/05/17'))