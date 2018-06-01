def get_vat(payment, percent = 18):
    try:
        payment = float(payment)
        percent = int(percent)
        vat = payment / 100 * percent
        vat = round(vat, 2)
        return 'VAT: {}'.format(vat)
    except(TypeError, ValueError):
        return "Error! Use numbers, please!"

payment=input('Payment: ')
result = get_vat(payment, 20)
print(result)