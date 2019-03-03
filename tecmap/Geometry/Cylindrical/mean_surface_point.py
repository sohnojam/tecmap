from .Point import Point
from math import fabs, fmod, pi

def mean_surface_point(point_a, point_b):

  if isinstance(point_a, Point) and isinstance(point_b, Point):

    if point_a.radius == point_b.radius:
      
      if fabs(point_a.yaw - point_b.yaw) > pi:
        return Point(
          fmod((point_a.yaw + point_b.yaw + 2*pi) / 2, 2*pi),
          (point_a.height + point_b.height) / 2,
          point_a.radius,
          'rad'
        )
      else:
        return Point(
          (point_a.yaw + point_b.yaw) / 2,
          (point_a.height + point_b.height) / 2,
          point_a.radius,
          'rad'
        )

    else:
      return None

  else:
    return None