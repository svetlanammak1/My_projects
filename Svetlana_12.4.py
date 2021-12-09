## Example from CW: Svetlana
## Date: 08/12/2021 
## Task: The program writes out info using logging package to battery.temperature.txt file

import logging
import random

FORMAT = '%(levelname)s - %(message)s'

class BatterySimulation:
    def __init__(self, logger):
        self.logger = logger

    def simulate_last_hour(self):
        for minute in range(1,     60 +1):
            temperature = random.randint(20, 40)

            if temperature < 30:
                self.logger.debug('{0} C'.format(temperature))
            elif   temperature >= 30  and temperature <= 35:
                self.logger.warning('{0} C'.format(temperature))
            elif   temperature > 35:
                self.logger.critical('{0} C'.format(temperature))  
            else:
                raise Exception('temperature out of rang') 

logger = logging.getLogger('battery.temperature')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('battery.temperature.txt', 'w')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s - %(message)s')

handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info("start")
battery_simulation = BatterySimulation(logger)
battery_simulation.simulate_last_hour()