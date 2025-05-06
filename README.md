
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

   The project includes a `commands.json` file that defines the drone's control commands. Make sure this file is in the root of the repository for the controller to function properly. You can experiment yourself and add more commands as you wish for increased functionality.

1. **Run the controller**:

   ```bash
   python main.py
   ```

   This will initialize the drone controller and start the loop for sending commands.

2. **Control the drone**:

   To run a specific command, call the `run_command` function. For example, to fly the drone forward use "forward_thrust", you can execute the corresponding command (ensure it's available in `commands.json`).

---

## Commands

The `commands.json` file contains various commands that can be sent to the drone. Each command is a byte string representing a specific action. Here’s an example of how a command is defined:

```json
{
  "fly_forward": "cc 5a 01 83 09 66 80 80",
  "fly_backward": "cc 5a 01 83 09 66 80 81",
  "resting_packet": "cc 5a 01 82 36 b7"
}
```

The key is the **name** of the command, and the value is the **byte sequence** representing the action.

---


This project is released for educational purposes only. You are free to experiment with the code, but please ensure that you follow all safety guidelines while using the drone.

---

### 📝 Notes:

* The drone's control mechanism is based on a UDP socket communication. The controller sends packets to the drone's IP, and the drone responds accordingly.
* Ensure that the drone is powered on and connected to the same wifi network as the your pc.

---