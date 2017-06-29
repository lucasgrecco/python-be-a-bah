from datetime import date
from datetime import time
from datetime import datetime

class ClassTesteDateTima():
    def __init__(self):
        self.today = datetime.now()
        self.data_hoje = date.today()
        self.tempo_agora = time(self.today.hour, self.today.minute, self.today.second, 0)
        self.data = date(2006, 10, 18)
        self.tempo = time(15, 30, 40, 0)

    def diff_datas(self, data_hoje, data):
        diff_data = data_hoje - data
        print(diff_data)


today = datetime.now()
data_hoje = date.today()
tempo_agora = today.time().
data = date(2006, 10, 18)
tempo = time(15, 30, 40, 0)
teste = ClassTesteDateTima()
teste.diff_datas(data_hoje, data)
teste.diff_tempo(tempo_agora, tempo)