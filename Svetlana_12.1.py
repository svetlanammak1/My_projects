## Example from CW: Svetlana
## Date: 08/12/2021 
## Task: The program  realizes Temperature Converter

import xml.etree.ElementTree as ET

class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
        return 9.0/5.0 * temperature_in_celsius


class ForecastXmlParser:
    def __init__(self,temperature_converter):
        self.temperature_converter = temperature_converter
        #print(self.temperature_converter)

    def parse(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            day = child.find('day').text
            temperature_in_celsius = int(child.find('temperature_in_celsius').text)
            temperature_in_fahrenheit =  round(self.temperature_converter.convert_celsius_to_fahrenheit(temperature_in_celsius),1)
            print('{0}: {1}  Celsius {2} Fahrengeit'.format(
                    day, temperature_in_celsius , temperature_in_fahrenheit))

temperature_converter = TemperatureConverter() 
Forecast_xml_parser = ForecastXmlParser(temperature_converter)
Forecast_xml_parser.parse('forecast.xml')