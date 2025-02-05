import math

def distance(point1,point2):
    return math.sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2+(point2[2]-point1[2])**2)


points=[]
for i in range(4):
    print(f"\nEnter point no {i+1}")
    x ,y,z=map(int ,input().split())
    points.append((x,y,z))


nearest=[]

for i in range(4):
    nearest_point= None
    min_distance = distance(points[0],points[1])
    for j in range(4):
        if i!=j:
            if(min_distance>distance(points[i],points[j])):
                min_distance=distance(points[i],points[j])
                nearest_point= points[j]
    nearest.append(nearest_point)     
       
print("\nNearest points are:")
print(nearest)
     
   
