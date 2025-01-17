# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

data_str_data = '2024-01-16 15:32:45'
data_str_format = '%Y-%m-%d %H:%M:%S'

atual = datetime.now(timezone('America/Sao_Paulo'))
print(atual)

# data = datetime(2024, 12, 1, 22, 49, 8, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_format)
data = datetime.now()
print(data)
print(datetime.fromtimestamp(1))