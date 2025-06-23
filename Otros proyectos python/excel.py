import pandas
import openpyxl

import pandas as pd

datos = pd.DataFrame({
    'Columna1': [1,2,3],
    'Columna2': [4,5,6]
})

excel_writer = pd.ExcelWriter('reporte.xlsx')
datos.to_excel(excel_writer, sheet_name='Hola1')
excel_writer._save()

print('Reporte generado')

