"""Temperature conversion utilities.

This module provides functions to convert temperatures between
Celsius, Fahrenheit, and Kelvin scales.
"""

import os
import sys


def convert_temp(value, from_unit, to_unit):
    """Convert temperature between units.

    Args:
        value: Temperature value to convert
        from_unit: Original unit ('C', 'F', 'K')
        to_unit: Target unit ('C', 'F', 'K')

    Returns:
        Converted temperature value
    """
    # Конвертация температуры
    if from_unit == to_unit:
        return value

    # Конвертация в цельсии
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        raise ValueError(f"Unknown unit: {from_unit}")

    # Конвертация из цельсия
    if to_unit == "C":
        result = celsius
    elif to_unit == "F":
        result = celsius * 9 / 5 + 32
    elif to_unit == "K":
        result = celsius + 273.15
    else:
        raise ValueError(f"Unknown unit: {to_unit}")

    return result


def main():
    """Main function to test temperature conversion."""
    print(convert_temp(100, "C", "F"))  # 212.0
    print(convert_temp(32, "F", "C"))  # 0.0
    print(convert_temp(0, "K", "C"))  # -273.15


if __name__ == "__main__":
    main()
