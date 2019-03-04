from . import Point
from math import cos, sin, asin, sqrt

def haversine_distance(point_a, point_b):

  if isinstance(point_a, Point) and isinstance(point_b, Point):
    
    if point_a.radius == point_b.radius:
      
      return 2 * asin(sqrt(
        sin((point_b.pitch - point_a.pitch) / 2) ** 2 +
        cos(point_a.pitch) * cos(point_b.pitch) * sin((point_b.yaw - point_a.yaw) / 2) ** 2
      ))
    
    else:
      return None

  else:
    return None