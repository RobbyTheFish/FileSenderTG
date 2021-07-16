from flask import Flask, request
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

def send_file(chat_id, type_req, text):
    if type_req == "bot_command" and "/start" in text:
        id_file = text.replace("/start ", "")
        print(chat_id, id_file, type_req)
        #TODO
        #Request to DB with selecting id of file
        #Get file from db
        #send file to user



@app.route("/", methods=["GET", "POST"])
def recieve_update():
    if request.method == "POST":
        print(request.json)
        chat_id = request.json["message"]["chat"]["id"]
        type_req = request.json["message"]["entities"][0]["type"]
        text = request.json["message"]["text"]
        send_file(chat_id, type_req, text)
    return {"ok": True}


if __name__ == "__main__":
    app.run()
