class Converter:
    meter = {
        "inches": 39.37,
        "feet": 3.28,
        "yards": 1.093,
        "miles": 0.00062,
        "kilometers": 0.001,
        "meters": 1,
        "centimeters": 100,
        "millimeters": 1000
    }

    def __init__(self, length, unit):
        self.unit = unit.lower()  # Convert unit to lowercase for consistency
        self.length = length

    def convert_to_meter(self):
        # Convert the given length to meters
        return self.length / Converter.meter[self.unit]

    def meters(self):
        # Return the length in meters
        return self.convert_to_meter() * Converter.meter["meters"]

    def feet(self):
        # Return the length in feet
        return self.convert_to_meter() * Converter.meter["feet"]

    def inches(self):
        # Return the length in inches
        return self.convert_to_meter() * Converter.meter["inches"]

    def miles(self):
        # Return the length in miles
        return self.convert_to_meter() * Converter.meter["miles"]

    def centimeters(self):
        # Return the length in centimeters
        return self.convert_to_meter() * Converter.meter["centimeters"]

    def millimeters(self):
        # Return the length in millimeters
        return self.convert_to_meter() * Converter.meter["millimeters"]

    def kilometers(self):
        # Return the length in kilometers
        return self.convert_to_meter() * Converter.meter["kilometers"]

# Example usage:
a = Converter(12, "inches")
print(round(a.meters(), 2))         # Convert to meters
print(round(a.feet(), 2))           # Convert to feet
print(round(a.inches(), 2))         # Convert to inches (same value)
print(round(a.miles(), 4))          # Convert to miles
print(round(a.centimeters(), 2))    # Convert to centimeters
print(round(a.millimeters(), 2))    # Convert to millimeters
print(round(a.kilometers(), 4))     # Convert to kilometers
