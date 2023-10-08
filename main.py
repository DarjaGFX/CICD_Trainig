from fastapi import FastAPI
from typing import List
import csv
import io

from fastapi.responses import Response

app = FastAPI()


@app.get('/')
def index():
    return {'status': 200, 'data': "works well!\n Yeeeeeeeeeeeeeey"}


@app.get("/file")
def get_file():
    report = [[1, 'salam'], [2, 'hi'], [3, 'hallo']]  # Your data

    buffer = io.StringIO()  # StringIO stream for the CSV data
    writer = csv.writer(buffer)
    writer.writerows(report)  # Write the data into the buffer

    csv_data = buffer.getvalue()  # Get the CSV data as a string
    buffer.close()  # Close the buffer

    headers = {'Content-Disposition': 'attachment; filename="report.csv"'}
    return Response(csv_data, headers=headers, media_type='text/csv')
