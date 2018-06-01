price = 100
vat_rate = 18

vat = price / 100 * vat_rate

print(vat)
price_no_vat = price - vat
print(price_no_vat)