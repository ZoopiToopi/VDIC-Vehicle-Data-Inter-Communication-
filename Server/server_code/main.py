import DB_Manage as db #this python file will handle db operations

db.DB_init() #initializing db with credentials

data = {   #sample data for db
        'speed':'100',
        'direction':'N',
        'latitude': '8.486200773756977',
        'longitude': '76.92835384022985'
       }
db.DB_Create('test_data',1995,data) #creating db with provided name,id and data

data = db.DB_Read('test_data')
print(data['1995']['latitude'])
