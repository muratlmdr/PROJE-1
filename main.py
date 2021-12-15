import base64
import datetime
from flask import Flask, render_template, request, redirect, session
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'TPM'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["TPMdb"]
uyeler_tablosu = mydb["uyeler"]
#urunler_tablosu = mydb["urunler"]
#sepet_urunleri_tablosu = mydb["sepet_urunleri"]

@app.route('/')
def baslangic():
    kullanici = None
    if 'kullanici' in session:
        kullanici = session["kullanici"]

    #haftanin_firsatlari = urunler_tablosu.find({"etiket": "haftanin_firsatlari"})

    return render_template("anasayfa.html")  #urunler=haftanin_firsatlari, #kullanici=kullanici)





if __name__ == "__main__":
    app.run(debug=True)