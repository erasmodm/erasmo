# Rhombus Area Calculator

This project is a Python application that calculates the area of a rhombus. It utilizes object-oriented programming, inheritance, abstract classes, and handles user inputs through a command-line interface.

## Prerequisites

Make sure you have Python installed on your system. 

Also, ensure you have Poetry installed. You can install it via pip.

## Usage

To run the application, execute the following command in the project directory: poetry run python main.py


Follow the on-screen instructions to input the rhombus diagonals and calculate its area.

## Project Structure

The project is organized into the following files:

- `main.py`: The entry point of the application. It handles user input and initiates the rhombus area calculation.
- `geometric_shape.py`: Contains the definition of the abstract class `GeometricShape`, which defines an abstract method `area()` for calculating the area of a geometric shape.
- `rhombus.py`: Contains the `Rhombus` class, which implements the rhombus area calculation using diagonals provided by the user.
- `utils.py`: Contains a utility function `get_input_float` to get float input from the user.

## Testing

The project also includes unit tests to verify the correctness of the rhombus area calculation. You can run the tests by executing the following command: poetry run python -m unittest



