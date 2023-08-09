import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def DB_init():
    try:
        cred = credentials.Certificate("fourstroke-ca632-firebase-adminsdk-6itor-c5b7767834.json")
        firebase_admin.initialize_app(cred,{'databaseURL': 'https://fourstroke-ca632-default-rtdb.asia-southeast1.firebasedatabase.app/'})
    except Exception as e:
        print("DB Initialization Failed error: ",str(e))

def DB_Create(root,parent,parent1,parent2,parent1_data,parent2_data):
    try:
        ref = db.reference(str(root))
        main = ref.child(str(parent))
        p1 = main.child(parent1)
        p1.set(parent1_data)
        p2 = main.child(str(parent2))
        p2.set(parent2_data)
    except Exception as e:
        print("DB creation failed error: ",str(e))
        

        
def DB_Read(path):
    try:
        ref = db.reference(str(path))
        return ref.get()
    except Exception as e:
        print("DB Read failed error: ",str(e))
        
    
def DB_same_road(path,filter):
    try:
        ref = db.reference(str(path))
        dup = {}
        data =ref.get()
        for road in data:
            if road in dup:
                dup.append(data['road'])
            else:
                dup['road'] = data['road']
        print(dup)
    except Exception as e:
        print("DB Read failed error: ",str(e))