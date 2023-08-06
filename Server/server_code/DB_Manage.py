import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def DB_init():
    try:
        cred = credentials.Certificate("fourstroke-ca632-firebase-adminsdk-6itor-c5b7767834.json")
        firebase_admin.initialize_app(cred,{'databaseURL': 'https://fourstroke-ca632-default-rtdb.asia-southeast1.firebasedatabase.app/'})
    except Exception as e:
        print("DB Initialization Failed error: ",str(e))

def DB_Create(db_name,id,data):
    try:
        ref = db.reference(str(db_name))
        ref.child(str(id)).set(data)
    except Exception as e:
        print("DB creation failed error: ",str(e))