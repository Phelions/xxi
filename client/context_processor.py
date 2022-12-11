from math import trunc
def total_carrito(request):
    total = 0
    iva = 0
    propina = 0
    if 'carrito' in request.session:
        for key, value in request.session['carrito'].items():
            iva += int(value['acumulado']) * 0.19
            total += int(value['acumulado']) + iva + propina
            propina += total * 0.10
    return {'total_carrito': trunc(round(total,0)), 'iva_carrito': trunc(round(iva,0)), 'propina_carrito': trunc(round(propina,0))}