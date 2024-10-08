from robot.robot import Robot_

from models import *

import socketio

from termcolor import colored
import traceback
from datetime import datetime, timedelta

class RobotClient:
    def __init__(self, auth_data):
        self.sio = socketio.Client()
        self.auth_data = auth_data

        self.robot = Robot_(self.sio, auth_data)

        self.robot_info = Robot.filter_one(Robot.id > 0)

        # Socket.io event handlers
        self.sio.event(self.connect)
        self.sio.event(self.connect_error)
        self.sio.event(self.disconnect)
        self.sio.event(self.quit)

        self.sio.on("mission", self.handle_mission)
        self.sio.on("join_robot", self.handle_robot_connection)
    
    def setup(self):
        try:
            pass
        except Exception as e:
            error_details = traceback.format_exc()
            print(colored(f"[TRACEBACK] {error_details}", "red", attrs=["bold"]))

    def connect(self):
        try:
            self.sio.emit("join_robot", self.auth_data)
            print(colored("[INFO] Successfully connected to the server.", "green" ,attrs=["bold"]))
        except Exception as e:
            error_details = traceback.format_exc()
            print(colored(f"[TRACEBACK] {error_details}", "red", attrs=["bold"]))

    def connect_error(self, data):
        try:
            print(colored("[INFO] Failed to connect to the server.", "yellow" ,attrs=["bold"]))
        except Exception as e:
            error_details = traceback.format_exc()
            print(colored(f"[TRACEBACK] {error_details}", "red", attrs=["bold"]))

    def disconnect(self):
        try:
            print(colored("[INFO] Disconnected from the server.", "yellow" ,attrs=["bold"]))
        except Exception as e:
            error_details = traceback.format_exc()
            print(colored(f"[TRACEBACK] {error_details}", "red", attrs=["bold"]))

    def quit(self):
        try:
            self.sio.emit("leave_robot", self.auth_data)
            print(colored("[INFO] Successfully quit from the server.", "green" ,attrs=["bold"]))
        except Exception as e:
            error_details = traceback.format_exc()
            print(colored(f"[ERR] {e}\n[TRACEBACK] {error_details}", "red", attrs=["bold"]))

    def save_mission(self, rank):
        try:
            robot_id = self.robot_info.id

            # Check active mission around    
            is_active_mission = Mission.filter_one(Mission.is_active==True)
            
            flag = True 
            
            if is_active_mission is not None and rank > is_active_mission.rank:
                Mission.update(
                    is_active_mission.id,
                    is_active = False,
                    completed = False
                )

                print(colored(f"[WARN] A more important mission has come.", "yellow" ,attrs=["bold"])) 
            elif is_active_mission is not None:
                flag = False     

            mission = Mission.create(
                          robot_id=robot_id,
                          is_active=flag,
                          rank=rank
                      )

            print(colored(f"[INFO] Mission saved to database id:{mission.id}.", "green" ,attrs=["bold"])) 

            response = mission if flag else is_active_mission

            return response, flag 
        except Exception as e:
            error_details = traceback.format_exc()
            print(colored(f"[ERR] {e}\n[TRACEBACK] {error_details}", "red", attrs=["bold"]))

    def save_road_map(self, mission, message):
        try:
            for road_map in message:
                area_name = road_map.get("area_name")
                index = road_map.get("index") 

                if area_name is None:
                    print(colored(f"[WARN] Message not valid.", "yellow" ,attrs=["bold"])) 
                    return

                RoadMap.create(
                    mission_id = mission.id,
                    area_name = area_name,
                    index = index 
                )

            print(colored(f"[INFO] Road map successfully saved to database.", "green" ,attrs=["bold"])) 
        except Exception as e:
            error_details = traceback.format_exc()
            print(colored(f"[ERR] {e}\n[TRACEBACK] {error_details}", "red", attrs=["bold"]))

    def handle_mission(self, data):
        try:
            message = data.get("message")
        
            if not message:
                print(colored(f"[WARN] Invalid message : {data}.", "yellow" ,attrs=["bold"])) 
                return  
            
            rank = message.get("rank")
            
            if rank is None:
                print(colored(f"[WARN] Rank not found.", "yellow" ,attrs=["bold"])) 
                return  

            mission,flag = self.save_mission(rank)

            if mission is  None:
                print(colored(f"[WARN] Mission not found.", "yellow" ,attrs=["bold"])) 
                return  

            road_map = message.get("road_map") 

            if road_map is  None:
                print(colored(f"[WARN] Road map not found.", "yellow" ,attrs=["bold"])) 
                return  

            self.save_road_map(mission, road_map)

            print(colored(f"[INFO] Mission successuly coming.", "green" ,attrs=["bold"])) 
            
            if flag:
                self.robot.reset()

            self.robot.run(mission)
        except Exception as e:
            error_details = traceback.format_exc()
            print(colored(f"[TRACEBACK] {error_details}", "red", attrs=["bold"]))

    def handle_camera(self, data):
        try:
            if 199 < int(data.get("status")) < 300:
                print(colored(f"[INFO] Camera information succesfuly send to server.\n[WARN] Status code : {data.get('status')}", "green", attrs=["bold"])) 
            else:
                print(colored(f"[WARN] Not connect to do server.\n[WARN] Status code : {data.get('status')}", "yellow", attrs=["bold"])) 
        except Exception as e:
            error_details = traceback.format_exc()
            print(colored(f"[TRACEBACK] {error_details}", "red", attrs=["bold"]))

    def handle_robot_connection(self, data):
        try:
            if 199 < int(data.get("status")) < 300:
                print(colored(f"[INFO] Connected to the server.\n[INFO] Status code : {data.get('status')}", "green", attrs=["bold"]))
            else:
                print(colored(f"[WARN] Not connect to do server.\n[WARN] Status code : {data.get('status')}", "yellow", attrs=["bold"]))
        except Exception as e:
            error_details = traceback.format_exc()
            print(colored(f"[TRACEBACK] {error_details}", "red", attrs=["bold"]))

    def start(self, server_url):
        try:
            self.sio.connect(server_url)
            self.sio.wait()
        except KeyboardInterrupt:
            print(colored("[WARN] Connection forcibly closed.", "yellow" ,attrs=["bold"]))
        except Exception as e:
            error_details = traceback.format_exc()
            print(colored(f"[TRACEBACK] {error_details}", "red", attrs=["bold"]))
