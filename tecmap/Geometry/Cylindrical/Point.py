from math import fmod, fabs, pi

class Point:

  def __init__(self, yaw, height, radius=1, unit='deg'):

    try:
      if unit == 'deg':
        r_yaw = float(yaw) * pi / 180
      elif unit == 'rad':
        r_yaw = float(yaw)
      else:
        r_yaw = 0.0

      while r_yaw < 0:
        r_yaw += 2*pi

      self.__yaw = fmod(r_yaw, 2*pi)

    except:
      self.__yaw = 0.0
    
    try:
      self.__height = float(height)
    except:
      self.__height = 0.0

    try:
      self.__radius = fabs(float(radius))
    except:
      self.__radius = 0.0
  
  @property
  def yaw(self):
    return self.__yaw
  @property
  def height(self):
    return self.__height
  @property
  def radius(self):
    return self.__radius