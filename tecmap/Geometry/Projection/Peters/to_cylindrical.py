from ....Geometry import Cylindrical, Spherical
from math import sin

def to_cylindrical(origin):

  if isinstance(origin, Spherical.Point):

    if origin.radius <= 0:
      return Cylindrical.Point(
        0, 0, 0, 'rad'
      )

    else:
      return Cylindrical.Point(
        origin.yaw,
        sin(origin.pitch) * origin.radius,
        origin.radius,
        'rad'
      )

  else:
    return None