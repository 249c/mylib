import openpyxl
from pathlib import Path

wb = openpyxl.load_workbook("data.xlsx")    # open  file
Path("Copy").mkdir(exist_ok=True)           # If the folder with the same name does not exist, create a folder
wb.save("Copy/data.xlsx")                   # save copy data
