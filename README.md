
# Main Features
# lambdata
A Python package with some helpful Fata Science utilities

# Classes
Cotains two classes, one Bicycle and another MountainBike. Mountain bike takes inheritance from the bicycle class. Bicycles attributes are brand, size, tire size and frame type. MountainBike has the same but take 2 extra attrubes suspension count and suspension brand.

An example to make a bike or mountain bike object:

Bicycle('giant', 'L', 32, 'roady')
MountainBike('fezzari', 'L', 30, 'mountain', 2, 'Fox')

Bicycle class has two methods peataling_fast and condition. Condition class requires you pass in a string for the condtion of the bike.

Mountain bike has three methods peataling_fast, going_offraod, and smooth_ride.

# Tests
Bicycle has been full tested.

# How to install

use: 
pip install -i https://test.pypi.org/simple/ lambdata-jmckinney==0.0.9

make sure to had python3.6 or higher

to import use:
from lambdata.oop_examples import Bicycle, MountainBike


# License
<a herf="https://opensource.org/licenses/MIT">MIT</a>