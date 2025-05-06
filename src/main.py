from drone_controller import DroneController

controller = DroneController()
controller.start()

controller.run_command("engage_motors", 2)

controller.run_command("forward_thrust", 2)

controller.run_command("disengage_motors", 0)
