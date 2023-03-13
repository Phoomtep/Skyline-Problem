#Phoomtep Pitakamnuay 1630704896 327C
#CityFrame = createFrame(maxLength*(2/3) x maxLength); maxlength>0
#Building = build(left x ht x right); (left x ht x right)>0 , left<right
#Skyline  = createSkyline(ΣBuilding)


def left():
  xCoordinated = input("left>>")
  try:
    xCoordinated = int(xCoordinated)
    if xCoordinated < 0:
      print("Length cannot be less than zero")
      return left()
  except ValueError:
    print("Length cannot be string")
    return left()
  return xCoordinated


def right():
  xCoordinated = input("right>>")
  try:
    xCoordinated = int(xCoordinated)
    if xCoordinated <= 0:
      print("Length cannot be less than zero")
      return right()
  except ValueError:
    print("Length cannot be string")
    return right()
  return xCoordinated


def ht():
  hight = input("hight>>")
  try:
    hight = int(hight)
    if hight <= 0:
      print("Length cannot be less than zero")
      return ht()
  except ValueError:
    print("Length cannot be string")
    return ht()
  return hight


def build(building):
  building.append(left())
  building.append(ht())
  building.append(right())
  if building[0] > building[2]:
    print("The left edge must not be greater than the right edge.")
    return build(building=[])
  if building[0] == building[2]:
    print("The left edge must not be equal to the right edge.")
    return build(building=[])
  return building


def buildCity(buildings):
  add = input("Do you want to add building (y/n): ")
  if add == "n":
    return buildings

  elif add == "y":
    buildings.append(build(building=[]))
    return buildCity(buildings)

  else:
    print("Invalid command")
    return buildCity(buildings)


def createCityFrame(city):
  length = city[0][2]
  for i in city:
    if i[2] > length:
      length = i[2]
  width = length * (2 / 3)
  return "%.2fx%.2f" % (width, length), length


def createSkyline(city, length):
  skyline = []
  maxht = 0

  for i in range(length + 1):
    temp = [0]
    for j in city:
      if j[0] > i:
        break
      if i in range(j[0], j[2]):
        temp.append(j[1])
    if max(temp) != maxht:
      maxht = max(temp)
      skyline.append([i, maxht])

  return skyline


city = buildCity(buildings=[])
city.sort()

print("=" * 60)

if len(city) != 0:
  cityFrame, length = createCityFrame(city)
  print("Frame(widthxlength): " + cityFrame)
  skyline = createSkyline(city, length)
  print("Input:")
  print(city)
  print("Output:")
  print(skyline)
