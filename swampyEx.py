from swampy.World import  World

def draw_rect(canvas,rect,color):
    canvas.rectangle(rect, outline="black", width=2, fill=color)

    
world = World()
canvas = world.ca(width=500, height=500, background='white')
bbox = [[-150,-100], [150, 100]]
draw_rect(canvas,bbox,"red")
# canvas.circle([-25,0], 70, outline=None, fill='red')
world.mainloop()
