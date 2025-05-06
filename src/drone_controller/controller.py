import socket
import time
import threading
from .utils import load_commands_dict

class DroneController:
    def __init__(self, commands_path="commands.json", controller_port=7070, command_port=7060,
                 drone_ip="192.168.28.1", drone_port=7080, controller_ip="192.168.28.2",):
        # Load command mappings from a JSON file and set the default packet to 'resting'
        # This simulates the drones app
        self.controller_commands = load_commands_dict(commands_path)
        self.current_packet = self.controller_commands["resting_packet"]

        # Network configuration for controller and drone
        self.controller_port = controller_port
        self.command_port = command_port
        self.controller_ip = controller_ip
        self.drone_ip = drone_ip
        self.drone_port = drone_port

        self.running = False
        self.lock = threading.Lock() # For Thread access safety
        self.intial_run = True

        # Initalise a socket connection for non controller behaviours
        # before communicating with the drone, required for the drone to accept commands even
        # though commands are on another socket
        self.controller_init()

    def get_current_packet(self):
        # Thread-safe getter for the currently active command packet
        with self.lock:
            return self.current_packet
        
    # Thread-safe setter for the current packet; allows for command duration (delay)
    # Waits the specified duration before allowing the next command rudementry Queing
    def update_current_packet(self, new_packet: bytes, command_duration=0):
        with self.lock:
            self.current_packet = new_packet
        time.sleep(command_duration) 

    def controller_init(self):
        # Initialize the controller by sending a handshake/init packet to the drone
        initial_packet = self.controller_commands["initial_packet"]
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.controller_ip, self.controller_port))
            s.sendto(initial_packet, (self.drone_ip, self.drone_port))
            # implement logging
            self.connection_status = f"Initialized ip:{self.controller_ip} port:{self.controller_port}"
        with self.lock:
            self.current_packet = self.controller_commands["resting_packet"]

    def start(self):
        # Start the controller loop in a separate thread background thread
        thread = threading.Thread(target=self.controller_loop, daemon=True)
        thread.start()
        self.running = True

    def controller_loop(self):
        # Main loop that continuously sends the current packet to the drone
        # On first run, send the resting packet repeatedly for 2 seconds at 40ms intervals
        # to establish the connection (just the drones protocol)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            if self.intial_run:
                packet = self.controller_commands["resting_packet"]
                for i in range(50):
                    s.sendto(packet, (self.drone_ip, self.drone_port))
                    time.sleep(0.04)

            while self.running:
                packet = self.get_current_packet()
                if(packet == self.controller_commands['resting_packet']):
                    s.sendto(packet, (self.drone_ip, self.drone_port))
                else:
                    for i in range(2):
                        s.sendto(packet, (self.drone_ip, self.drone_port))
                    self.update_current_packet(self.controller_commands["resting_packet"])                
                time.sleep(0.04)

    def run_command(self, command: str, command_duration=0):
        try:
            self.update_current_packet(self.controller_commands[command], command_duration)
        except:
            print(f"Command {command} not found: Check commands.json")
