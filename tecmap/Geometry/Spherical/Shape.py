from .Point import Point

class Shape:

  def __init__(self, points=list()):
    
    if isinstance(points, list):
      if all(list(map(lambda item: isinstance(item, Point), points))):
        self.__points = points
      else:
        self.__points = list()
    else:
      self.__points = list()
  
  @property
  def points(self):
    return self.__points

  def appendPoint(self, new_point):
    if not isinstance(new_point, Point):
      raise TypeError
    self.__points.append(new_point)

  def insertPoint(self, new_point_index, new_point):
    if not isinstance(new_point, Point):
      raise TypeError
    if not isinstance(new_point_index, int):
      raise TypeError
    self.__points.insert(new_point_index, new_point)

  def removePoint(self, point_index):
    if not isinstance(point_index, int):
      raise TypeError
    self.__points.pop(point_index)

  def isShape(self):
    return len(self.__points) >= 3

  def contains(self, point):
    if not self.isShape():
      return False
    lines = list(map(lambda index: (self.__points[index], self.__points[index % len(self.__points)]), range(len(self.__points))))
