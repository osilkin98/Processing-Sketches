# screensize 
max_x = 720
max_y = 500

def setup():
    size(max_x, max_y)
    # background(255, 255, 255)
    noLoop()

# color palette, only 5 colors cause y not
palette = [
    "#080E33",
    "#0C154A",
    "#111E6C",
    "#192DA1",
    "#2039CC",
]


# elevation increment e.g. which elevation levels to record
elevation_mult = 5
max_elevation = 100

elevation = [[0 for y in range(max_y)] for x in range(max_x)]
elevation_init = False


def create_noise():
    print("Creating noise")
    global max_elevation
    global elevation, elevation_init
    intensity = random(0.005, 0.03)    
    for x in range(max_x):
        for y in range(max_y):
            elevation[x][y] = noise(x * intensity, y * intensity) * max_elevation
    
    elevation_init = True

def draw():
    background(255, 255, 255)
    
    complete = 0
    max_count = max_x * max_y
    if elevation_init:
        for x in range(max_x):
            for y in range(max_y):
                # print("({:d}, {:d}) => {:.3f}".format(x, y, elevation[x][y])) 
                if(int(elevation[x][y]) % elevation_mult == 0):
                    stroke(0, 0, 0)

                else:
                    pal_index = int(elevation[x][y]) / 20
                    # print("Chose palette index " + str(pal_index) + ": " + str(palette[pal_index]))
                    stroke(palette[pal_index])
                point(x,y)
             
                complete += 1
                if( complete % 20 == 0):
                    print("{:.3f}% complete".format(float(complete)/max_count*100))
                
                 
                # complete = ((float(x) * float(max_y)) + float(y + 1)) / (float(max_x * max_y)) * 100
                
                # print("[{0:4d}, {0:4d}] / [{0:4d}, {0:4d}]: {0:.2f}% complete".format(x, y, max_x, max_y, complete))
                
                
    # Create a white rectangle textbox 
    fill(255, 255, 255)
    rect(0, 0, 100, 50)
    
    # Create black text
    fill(0,0,0)
    textSize(16)
    text("Inc: " + str(elevation_mult), 10, 40)
    
    
    # Create a color key
    fill(255, 255, 255)
    rect(0, 60, 100, 100) # 150px tall key 
    
    
    x_allign = 10
    y_allign = 80    
    for depth, col in enumerate(palette):
        fill(0,0,0) # black text
        textSize(12)
        text("{0:2d} - {1:3d}: ".format(depth*20, (depth+1)*20), x_allign, y_allign + depth * 14)
        
        # create a rect with the color we want 
        fill(col)
        rect(70, y_allign - 10 + depth * 14, 20, 10)
     
def mouseWheel(event):
    global elevation_mult
    print("Current elevation: " + str(elevation_mult))
    elevation_mult += event.getCount()
    # constrain the elevation contours between 0 and 100
    if(0 < event.getCount()):
        elevation_mult = min(elevation_mult, 100)
    else:
        elevation_mult = max(elevation_mult, 1)

    redraw()

def mouseClicked():
    create_noise()
    redraw()
