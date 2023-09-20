import os.path
import datetime
import csv
import pandas as pd


def write_excel():
    a = os.path.realpath(__file__)
    date = datetime.date.today()
    current_working_name = os.path.dirname(os.path.dirname(a))
    file = current_working_name + '\\output_files' + '\\' + str(date) + '.csv'
    excel_file = current_working_name + '\\output_files' + '\\' + str(date)+'.xlsx'
    df_new = pd.read_csv(file)
    GFG = pd.ExcelWriter(excel_file)
    df_new.to_excel(GFG, index=False)


def write_csv(data):
    try:
        header = ["server", "command", "output"]
        a = os.path.realpath(__file__)
        current_working_name = os.path.dirname(os.path.dirname(a))
        date = datetime.date.today()
        file = current_working_name+'\\output_files'+'\\'+str(date)+'.csv'
        with open(file, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        return True, None
    except Exception as e:
        print("Not able to write a file please check logs for more details")
        return False, e










