import DB_Manage as db #this python file will handle db operations
import Coordinate_Manager as cdr #to handle coordinates and distance

coordinate1 = {
               'latitude':'8.89850993096244',
               'longitude':' 76.85994083186154'
}

coordinate2 = {
                'latitude':'9.005643755273748',
                'longitude':'76.78299431239033'
}

print(cdr.Cordinate_To_Distance(float(coordinate1['latitude']),float(coordinate1['longitude']),float(coordinate2['latitude']),float(coordinate2['longitude'])))