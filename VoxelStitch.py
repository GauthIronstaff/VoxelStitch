from PIL import Image
regions = []
for i in xrange(-200,200):
    y = i
    for i in xrange(-200,200):
        try:
            filename = "images/" + str(i) + "," + str(y) + ".png"
            im = Image.open(filename)
            #print im.format, im.size, im.mode
            #print(filename)
            regions.append((i,y))
        except IOError:
            pass
print(regions)
minRegion = map(min, zip(*regions))
maxRegion = map(max, zip(*regions))
print(minRegion)
print(maxRegion)
minCoords = (minRegion[0]*256,minRegion[1]*256)
maxCoords = (maxRegion[0]*256,maxRegion[1]*256)
print(minCoords)
print(maxCoords)
xOffset = minRegion[0]
yOffset = minRegion[1]
print(xOffset)
print(yOffset)
totalRegionResolution = (maxRegion[0]-minRegion[0]+1,maxRegion[1]-minRegion[1]+1)
print(totalRegionResolution)
pixelResolution = (totalRegionResolution[0]*256,totalRegionResolution[1]*256)
print(pixelResolution)
canvas = Image.new("RGB", pixelResolution, "black")
canvas.format = "PNG"
for i in range(len(regions)):
    currentRegion = regions[i]
    filename = "images/" + str(currentRegion[0]) + "," + str(currentRegion[1]) + ".png"
    print(filename)
    openRegion = Image.open(filename)
    #print(str(currentRegion[0]-xOffset))
    #print(str(currentRegion[1]-yOffset))
    canvas.paste(openRegion, ((currentRegion[0]-xOffset)*256,(currentRegion[1]-yOffset)*256))
canvas.show()
canvas.save('compiledMap.png')
