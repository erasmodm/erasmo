# main.py

from utils import get_input_float
from rhombus import Rhombus

if __name__ == "__main__":
    try:
        major_diagonal = get_input_float("Enter the major diagonal in cm: ")
        minor_diagonal = get_input_float("Enter the minor diagonal in cm: ")

        rhombus = Rhombus(major_diagonal, minor_diagonal)
        print("Area of the rhombus in cm^2:", rhombus.area())

    except KeyboardInterrupt:
        print("\nOperation interrupted.")
    except Exception as e:
        print("An error occurred:", e)
