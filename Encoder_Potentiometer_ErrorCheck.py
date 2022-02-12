"""
Coding Challenge for Intuitive Surgical

Feel free to redefine some of the tolerance globals below. I left these as globals for this use case,
but in an actual application, I would just define these as defaults within class/method

"Usage:   python Encoder_Potentiometer_ErrorCheck.py <filename>"
"Example: python Encoder_Potentiometer_ErrorCheck.py 'Code Challenge Data\\normal.txt'"
"""

import sys
import file_utilities as futil
from data_check import SensorData

MIN_TOLERANCE = 2.0  # Minimum Tolerance (degrees) between encoder and potentiometer
TOLERANCE_BUFFER = 0.5  # Tolerance Buffer (degrees) in addition to Tolerance calculated during calibration time


def main():
    try:
        checked_filename = futil.check_file(sys.argv)
        data_instance = SensorData(checked_filename, MIN_TOLERANCE, TOLERANCE_BUFFER)
        error_time = data_instance.verify_data()
        if error_time is None:
            print("No Error Found")
        else:
            print("Error Found at " + str(error_time) + " seconds")
    except FileNotFoundError as fnfe:
        print("Error:   " + str(fnfe))
        futil.usage()
    except Exception as e:
        print("Error:   " + str(e))
        futil.usage()


if __name__ == "__main__":
    main()
