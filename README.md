
---

# H14 Drone Controller

This repository contains a Python-based drone controller, created by reverse engineering the protocol of the **H14 Toy Drone**. The goal of this project is to provide a learning and experimental environment for controlling the drone. It is **for educational purposes only** and should be used only for experimenting with drone control and networking concepts.

---

## Example Usage
```
from drone_controller import DroneController

controller = DroneController()
controller.start()

controller.run_command("engage_motors", 2)

controller.run_command("forward_thrust", 2)

controller.run_command("disengage_motors", 0)
```
The preceding code spins up the drone motor for 2 seconds, applies forward thrust for 2 more and then turns off all motors.

**Clone the repository:**

   ```bash
   git clone https://github.com/AzharBhyat/h14-drone-control.git
   cd drone-controller
   ```

**Commands JSON file:**

   The project includes a `commands.json` file that defines the drone's control commands. The `commands.json` file contains various commands that can be sent to the drone. Each command is a byte string representing a specific action. Here’s an example of how a command is defined:

```json
{
    "resting_packet": "cc 5a 01 83 09 66 80 80 80 80 00 00 99 74",
    
    "engage_motors": "cc 5a 01 83 09 66 80 80 bf 80 00 3f 99 74",

    "forward_thrust": "cc 5a 01 83 09 66 80 80 fa 86 00 7c 99 74"
}
```

The key is the **name** of the command, and the value is the **byte sequence** representing the action. You can extend this with more commands to add more functionality.
https://medium.com/@bhyatazhar14/python-powered-toy-drone-3f83583d29da.

### 📝 Notes:

* The drone's control mechanism is based on a UDP socket communication. The controller sends packets to the drone's IP, and the drone responds accordingly.
* Ensure that the drone is powered on and connected to the same wifi network as the your pc.


---
