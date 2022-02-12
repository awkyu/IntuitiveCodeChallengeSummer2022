class SensorData:
    """
    SensorData is a class that encompasses data verification functions of a given file with a given tolerance of error
    """
    ENCODER_COUNT = 2048.0  # Encoder Counts per Revolution (of Motor Shaft)
    GEAR_REDUCTION = 30.0  # Gear Reduction between Motor Shaft and Output Gear Shaft (30:1)
    POTENTIOMETER_MAX = 255.0  # Maximum Potentiometer Value (8-bit value)
    CALIBRATION_TIME = 500  # Time from start that is assumed working (milliseconds)

    def __init__(self, filename, min_tolerance, tolerance_buffer):
        """
        Constructor for SensorData

        :param filename: the filename of the data file containing both Encoder and Potentiometer Data, with each
                        line formatted as shown below:
                        <time> <encoder> <potentiometer>
        :param min_tolerance: the tolerance of error in degrees between the encoder and potentiometer
        """
        self.filename = filename
        self.min_tolerance = min_tolerance
        file = open(self.filename, "r")
        lines = file.readlines()
        self.data = []
        for line in lines:
            self.data.append([float(x) for x in line.split()])

        starting_angle = self.data[0][2] / self.POTENTIOMETER_MAX * 360.0  # starting angle
        # min angle during calibration time
        min_calibration = min([x[2] / self.POTENTIOMETER_MAX * 360.0 for x in self.data[0:self.CALIBRATION_TIME]])
        # max angle during calibration time
        max_calibration = max([x[2] / self.POTENTIOMETER_MAX * 360.0 for x in self.data[0:self.CALIBRATION_TIME]])

        # calibrate tolerance based on noise from first 0.5 seconds
        self.min_tolerance = max(self.min_tolerance, max_calibration - min_calibration + tolerance_buffer)

        for point in self.data:
            point[2] = point[2] / self.POTENTIOMETER_MAX * 360.0
            point[1] = point[1]/self.ENCODER_COUNT/self.GEAR_REDUCTION*360 + starting_angle

    def verify_data(self):
        """
        Method to verify the data between encoder and potentiometer

        :return: the time of the error (seconds) or None if no error is found
        """
        for point in self.data:
            if abs(point[1] - point[2]) > self.min_tolerance:  # just checks the difference between the two sensors
                return point[0]                                # if the difference is greater than the tolerance, error
        return None
