from flask import request, make_response, flash
from ocrproject import app
from src.utils.utils import read_image
import gspread
from oauth2client.service_account import ServiceAccountCredentials
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
# API KEY: AIzaSyA1m0wMnB2AOKWHShHid9NZjSyPc7l_tH8

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets",\
    "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("/home/venkateshiyer/Downloads/credentials.json", scope)
client = gspread.authorize(credentials)
gsheet = client.open("OCR-data").sheet1

@app.route("/")
def welcome_page():
    return 'Welcome to the ocr project'

@app.route("/image", methods=["GET", "POST"])
def image_to_text():
    if request.method == "POST":
        get_image = request.files['file']
        if get_image.filename == '':
            flash('File does not exist')
        get_text = read_image(get_image)
        row = [get_image.filename, get_text]
        gsheet.insert_row(row, 2)
        # print(get_text)
        # get_image.save("Savedimage.png")
        # print("This is get image:", get_image)
        # for files in get_image:
        #     get_image_name = files.filename
        #     get_text = read_image(get_image_name)
        #     print(get_text)
        
    return make_response("Text from file", get_text)

