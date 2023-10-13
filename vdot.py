import math
import argparse

def calculate_flow_rate(viscosity, tube_length, radius, pressure_differential):
    # Calculate the flow rate in m³/s
    flow_rate = 100**3 * (math.pi * (radius**4) * pressure_differential) / (8 * viscosity * tube_length)
    return flow_rate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate flow rate of a tube")
    parser.add_argument("viscosity", type=float, help="Viscosity in Pa·s")
    parser.add_argument("tube_length", type=float, help="Tube length in meters")
    parser.add_argument("radius", type=float, help="Tube radius in meters")
    parser.add_argument("pressure_differential", type=float, help="Pressure differential in Pa")

    args = parser.parse_args()

    result = calculate_flow_rate(args.viscosity, args.tube_length, args.radius, args.pressure_differential)
    print(f"The flow rate is {result} cubic centimeters per second (cm³/s)")
