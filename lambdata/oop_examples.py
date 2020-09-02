"""Examples of Object Oriented Programming"""


import pandas as pd


class Bicycle:
    """General represention of a bicycle"""
    def __init__(self, brand, size, tire_size, frame_type):
        """Constructor for complex numbers.
        Complex numbers are part real, part imaginary.
        """
        self.brand = str(brand)
        self.size = str(size)
        self.tire_size = int(tire_size)
        self.frame_type = str(frame_type)
    

    def petaling_fast(self):
        return 'zooming'

    
    def condition(self, condition):
        return 'my bikes condition is ' + condition


class MountainBike(Bicycle):
    """General represention of a mountain bike"""
    def __init__(self, brand, size, tire_size, frame_type, suspension_count, suspension_brand):
        super().__init__(brand, size, tire_size, frame_type)
        self.suspension_count = int(suspension_count)
        self.suspension_brand = str(suspension_brand)


        def going_offroad(self):
            return 'Mountain bikes are best for dirt roads'
        

        def petaling_fast(self):
            return 'Sending it!'


        def smooth_ride(self):
            if self.suspension_count <= 1:
                return 'this is bumpy ride'
            else:
                return 'this ride is smooth'


if __name__ == '__main__':
    print('Import successful')