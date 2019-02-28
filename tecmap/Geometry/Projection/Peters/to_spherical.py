from ....Geometry import Cylindrical, Spherical
from math import asin

def to_spherical(origin):
  
  if isinstance(origin, Cylindrical.Point):
    
    if origin.radius <= 0:
      return Spherical.Point(
        0, 0, 0, 'rad'
      )

    else:
      return Spherical.Point(
        origin.yaw,
        asin(origin.height / origin.radius),
        origin.radius,
        'rad'
      )

  else:
    return None