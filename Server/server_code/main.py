import DB_Manage as db #this python file will handle db operations
import Coordinate_Manager as cdm
import random

road = ['road1','road2','road3','road4','road5','road6','road7','road8','road9','road10']
dir = ['N','S','W','E']
ran_dirN_S=['N','S']
ran_dirW_E=['W','E']

vehicle = ['1','2','3','4']



def Init():
        db.DB_init() #initializing db with credentials
        
        
        
# def random_db(count):
#         while(count):
#                 dbname = 'demo_data'
#                 child_node1 = 'Emergency'
#                 trigger_state = False
#                 veh_type = random.choice(vehicle)
#                 veh_id_emer = random.randint(1,1000)
#                 road_name = random.choice(road)
#                 speed = str(random.randint(0,140))
#                 direction = random.choice(dir)
#                 if(direction == 'N' or direction == 'S'):
#                         emer_dir = random.choice(ran_dirN_S)
#                 else:
#                         emer_dir = random.choice(ran_dirW_E)

#                 emer_speed = random.randint(80,140)
#                 emer_lat = str(random.uniform(8.000000,9.800000))
#                 emer_long = str(random.uniform(77.000000,77.500000))
#                 latitude = str(random.uniform(8.000000,9.800000))
#                 longitude = str(random.uniform(77.000000,77.500000))
#                 veh_id = count
#                 emer_data = {
#                         'key'  : str(veh_id_emer),
#                         'direction': emer_dir,
#                         'speed' : emer_speed,
#                         'latitude' : emer_lat,
#                         'longitude' : emer_long,
#                         'veh_type': veh_type,
#                         'trigger' : trigger_state
#                 }
#                 normal_data = {
#                         'key'  : str(veh_id),
#                         'road' : road_name,
#                         'direction': direction,
#                         'speed' : speed,
#                         'latitude' : latitude,
#                         'longitude' : longitude
#                 }
#                 db.DB_Create(dbname,veh_id,'Emergency','Vehicle_Data',emer_data,normal_data)
#                 count = count - 1      
Init()
random_db(1000)








