import DB_Manage as db #this python file will handle db operations
import random

road = ['road1','road2','road3','road4','road5','road6','road7','road8','road9','road10']
dir = ['N','S','W','E']



def Init():
        db.DB_init() #initializing db with credentials
        
        
        
def random_db(count):
        while(count):
                dbname = 'demo_data'
                road_name = random.choice(road)
                speed = str(random.randint(0,140))
                direction = random.choice(dir)
                latitude = str(random.uniform(8.000000,9.800000))
                longitude = str(random.uniform(77.000000,77.500000))
                veh_id = count
                data = {
                        'road' : road_name,
                        'direction': direction,
                        'speed' : speed,
                        'latitude' : latitude,
                        'longitude' : longitude
                }
                db.DB_Create(dbname,veh_id,data)
                count = count - 1               

Init()


random_db(100)






