# simulation/timestep.py

class SimulationClock:
    def __init__(self, timestep_hours=1):
        self.timestep_hours = timestep_hours
        self.current_time = 0

    def tick(self):
        self.current_time += self.timestep_hours
        return self.current_time
