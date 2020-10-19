import requests

minZoom = 6
maxZoom = 10

for zoom in range(minZoom, maxZoom + 1):
  print("Loading zoom level " + str(zoom))
  for x in (range(0, pow(2, zoom))):
    print("Loading X " + str(x))
    for y in (range(0, pow(2, zoom))):
      tile = str(zoom) + "/" + str(x) + "/" + str(y)
      url = "http://s.maprinto.com:8080/tile/" + tile + ".png"
      requests.get(url)