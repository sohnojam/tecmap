from ....Geometry import Cylindrical, Spherical
from math import tan, fabs, pi

def to_cylindrical(origin, pitch_limit=(pi/2)*0.9):

  if isinstance(origin, Spherical.Point):

    if origin.radius <= 0:
      return Cylindrical.Point(
        0, 0, 0, 'rad'
      )

    elif fabs(origin.pitch) > pitch_limit:
      return None

    else:
      return Cylindrical.Point(
        origin.yaw,
        tan(origin.pitch) * origin.radius,
        origin.radius,
        'rad'
      )
  
  else:
    return None