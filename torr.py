import math
import argparse

def calculate_velocity(height):
    # Acceleration due to gravity (m/s^2)
    g = 9.81

    # Calculate velocity using Torricelli's equation
    velocity = math.sqrt(2 * g * height)

    return velocity

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate velocity using Torricelli's equation")
    parser.add_argument("height", type=float, help="Height in meters")

    args = parser.parse_args()
    height = args.height

    result = calculate_velocity(height)
    print(f"The velocity at a height of {height} meters is {result} m/s")
