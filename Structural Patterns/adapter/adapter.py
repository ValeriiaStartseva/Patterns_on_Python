class MeterDataProcessor:
    """
    class which accepted data in metres
    """
    @staticmethod
    def process_data(data_in_meters):
        print("Data in metres", data_in_meters)


class MeterToCentimeterAdapter:
    """
    Class-adapter for convert meters to centimeters
    """

    def __init__(self, meter_data_processor):
        self.meter_data_processor = meter_data_processor

    def process_data(self, data_in_meters):
        data_in_centimeters = data_in_meters * 100
        self.meter_data_processor.process_data(data_in_centimeters)


# test
data_processor = MeterDataProcessor()
adapter = MeterToCentimeterAdapter(data_processor)

adapter.process_data(2)
