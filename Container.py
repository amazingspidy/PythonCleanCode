class Boundaries:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __contains__(self, coord):
    x, y = coord
    return 0 <= x < self.width and 0 <= y < self.height


class Grid:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.limits = Boundaries(width, height)

  def __contains__(self, coord):
    return coord in self.limits


def user_display(user_metadata: dict = None):
  user_metadata = user_metadata or {"name": "John", "age": 30}
  name = user_metadata.pop("name")
  age = user_metadata.pop("age")
  return f"{name} ({age})"


#dis1 = user_display()
#print(dis1)
#dis2 = user_display({"name": "Woon", "age": 44})
#print(dis2)
#dis3 = user_display()
#print(dis3)


def testing(value: int = 1):
  return value


print(testing())
print(testing(14))
print(testing())
