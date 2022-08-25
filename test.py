from PIL import Image
import pytesseract
from zipfile import ZipFile
import io
from io import StringIO
import csv
import json

#   level   INTEGER,
# 	page_num    INTEGER,
# 	block_num   INTEGER,
# 	par_num     INTEGER,
# 	line_num    INTEGER,
# 	word_num    INTEGER,
# 	left    INTEGER,
# 	top INTEGER,
# 	width   INTEGER,
# 	height  INTEGER,
# 	conf    REAL,
# 	text    TEXT


with ZipFile('../vad/zips/vemardet-1918-tif.zip') as myzip:
    pages = filter(lambda file: file.endswith('.tif'), myzip.namelist())
    for fil in pages:
        with myzip.open(fil, mode='r') as mypage:
            print(fil)
            image = Image.open(io.BytesIO(mypage.read()))
            data = pytesseract.image_to_data(image, lang='swe')
            for line in data.split("\n"):
                cols = line.split("\t")
                print(cols)


            # tsv = pytesseract.image_to_data(image, lang='swe')
            # f = StringIO(tsv)
            # for row in csv.reader(f, delimiter="\t"):
            #     print(row)
