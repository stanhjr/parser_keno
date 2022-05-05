import json

import pandas
from pandas import DataFrame

from models.tabs import KenoRaw, session


class DataApi:
    def __init__(self):
        self.session = session

    def check_row(self, keno_label):
        with self.session() as s:
            return s.query(KenoRaw).filter(KenoRaw.keno__label == keno_label).first()

    def set_raw(self, raw: list):
        with self.session() as s:
            for row in raw:
                keno = KenoRaw()
                keno.keno_label = row[0]
                keno.balls = json.dumps(row)
                s.add(keno)
                s.commit()

    def render_excel_file(self):
        with self.session() as s:
            result = s.query(KenoRaw).all()
            keno_label = []
            ball_1 = []
            ball_2 = []
            ball_3 = []
            ball_4 = []
            ball_5 = []
            ball_6 = []
            ball_7 = []
            ball_8 = []
            ball_9 = []
            ball_10 = []
            ball_11 = []
            ball_12 = []
            ball_13 = []
            ball_14 = []
            ball_15 = []
            ball_16 = []
            ball_17 = []
            ball_18 = []
            ball_19 = []
            ball_20 = []
            for model in result:

                model = model.get_row()
                keno_label.append(model[0])
                ball_1.append(model[1])
                ball_2.append(model[2])
                ball_3.append(model[3])
                ball_4.append(model[4])
                ball_5.append(model[5])
                ball_6.append(model[6])
                ball_7.append(model[7])
                ball_8.append(model[8])
                ball_9.append(model[9])
                ball_10.append(model[10])
                ball_11.append(model[11])
                ball_12.append(model[12])
                ball_13.append(model[13])
                ball_14.append(model[14])
                ball_15.append(model[15])
                ball_16.append(model[16])
                ball_17.append(model[17])
                ball_18.append(model[18])
                ball_19.append(model[19])
                ball_20.append(model[20])

            df = DataFrame({"keno_label": keno_label,
                            "ball_1": ball_1,
                            "ball_2": ball_2,
                            "ball_3": ball_3,
                            "ball_4": ball_4,
                            "ball_5": ball_5,
                            "ball_6": ball_6,
                            "ball_7": ball_7,
                            "ball_8": ball_8,
                            "ball_9": ball_9,
                            "ball_10": ball_10,
                            "ball_11": ball_11,
                            "ball_12": ball_12,
                            "ball_13": ball_13,
                            "ball_14": ball_14,
                            "ball_15": ball_15,
                            "ball_16": ball_16,
                            "ball_17": ball_17,
                            "ball_18": ball_18,
                            "ball_19": ball_19,
                            "ball_20": ball_20,
                            })

            with pandas.ExcelWriter('report.xlsx', engine='xlsxwriter') as wb:
                df.to_excel(wb, sheet_name='report', index=False)
                sheet = wb.sheets['report']
                sheet.set_column('A:A', 10)
            return True


db_api = DataApi()
