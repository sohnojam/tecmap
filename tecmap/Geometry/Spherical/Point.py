from math import fmod, fabs, pi
class Point:

  def __init__(self, yaw, pitch, radius, unit='deg'):

    try:
      if unit == 'deg':
        r_yaw = float(yaw) * pi / 180
      elif unit == 'rad':
        r_yaw = float(yaw)
      else:
        r_yaw = 0.0
      self.__yaw = fmod(r_yaw, pi)
    except:
      self.__yaw = 0
    
    try:
      if unit == 'deg':
        r_pitch = float(pitch) * pi / 180
      elif unit == 'rad':
        r_pitch = float(pitch)
      else:
        r_pitch = 0.0
      self.__pitch = fmod(r_pitch, pi / 2)
    except:
      self.__pitch = 0
    
    try:
      self.__radius = fabs(float(radius))
    except:
      self.__radius = 0

  @property
  def yaw(self):
    return self.__yaw
  @property
  def pitch(self):
    return self.__pitch
  @property
  def radius(self):
    return self.__radius