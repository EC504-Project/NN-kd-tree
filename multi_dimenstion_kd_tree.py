# Thanks to reference:https://gist.github.com/rhigdon/199174
# the reference is the implementation of a 2-D kd-tree.
# I expend it to multi-dimensional version.
# Zhiyu Wang.
#import all the necessary modules.
from PIL import Image
from os import listdir
from os.path import isfile, join
import operator

#indicate the path to dataset.

path = "./CarData/TrainImages/"
target_path = "./CarData/TestImages/"
dirs = []
target_d =[]
for file in listdir(path):
    if file.endswith(".pgm"):
        dirs.append(file)

for file in listdir(target_path):
    if file.endswith(".pgm"):
        target_d.append(file)
        

print(len(dirs))
print(dirs)
print(target_d)

def load_pixel(file_name):
    img = Image.open(file_name).convert('LA')
    pix = img.load()
    value = {}
    dimension = 0
    for i in range(0,40):
        for j in range(0,10):
            value[dimension] = pix[i,j][0]
            dimension+=1
    return(value)

object = {}
obj_name = {}
index = 0

for file_name in dirs[0:500]:
    object[index] = load_pixel(path + file_name)
    obj_name[index] = file_name
    index+=1
    
target = {}
target_name = {}
index_t = 0
for file_name in target_d:
    target[index_t] = load_pixel(target_path+file_name)
    target_name[index_t] = file_name
    index_t+=1

print(target_name)
print(target[0])

import fileinput
class Node:
    def __init__(self, id, coords, left, right):#, prev
        self.id = id
        self.coords = coords
        self.left = left
        self.right = right
#         self.prev = prev



line_nodes = {}
def build_tree(objects, tree_depth = 0):
    if objects == {}:
        return

    #Zhiyu Wang:
    #here we expend the dimension to 400*100, because the size of each image is 400*100, which means, there are 40000
    #pixels for one image.
    dimension = tree_depth % (400*100) + 1;
    
    
    #Zhiyu Wang:
    #Sort the points by the dimension this round reaching.
    #Here is the problem why kd tree is not working.
    #the dimension is 40000, however we just got 500 samples in the dataset, which means,
    #we just used the first 500 dimension as element to devide the dataset.
    points = sorted(objects, key=lambda k: objects[k][dimension])#dimension is from 0 to 8.

    #Zhiyu Wang:
    #Find the index of the median point, for 2-d kd-tree we are going to drew a line to devide the points.
    line = int(len(points)/2)

    id_no = points[line]
    node = Node(points[line], objects[id_no], None, None)
    

    if(dimension in line_nodes.keys()):
        line_nodes[dimension].append(id_no)
    else:
        line_nodes[dimension] = [id_no]
    #indicate the left and right sides of the tree, and do the node building recursively. 
    left = {}
    right = {}
    for key in points[0:line]:
        left[key] = objects[key]
    for key in points[line+1:]:
        right[key] = objects[key]

    node.left = build_tree(left, tree_depth + 1)
    node.right = build_tree(right, tree_depth + 1 )
    return node



root = build_tree(object)
for key in line_nodes.keys():
    print(line_nodes[key])


def distance(node, target):
    if node == None or target == None:
        return None
    else:
        dis = []
        for i in range(len(node.coords)): 
            dis.append(abs(node.coords[i] - target[i]))
    return sum(dis)

nodel=root.left
noder=root.right
print(root.id)
print(nodel.id)
print(noder.id)


def check_nearest(nearest, node, target):
    d = distance(node, target)
    nearset_d = 100000000
    if len(nearest) < 4 or d < nearset_d:
        if len(nearest) >= 4:
            nearest.pop()
        nearest.append([d, node.id])
        nearset_d = d
        nearest = sorted(nearest, key = lambda nearest:nearest[1])#(objects, key=lambda k: objects[k][axis])
    return nearest

path = []
def find_nearest(node, target, depth=0):
    path.append(node.id)
    nearest = [] 
    axis = depth % 25
    print(depth)
    if(((node.right == None) and (node.left != None)) or (node.left and target[axis] <= node.coords[axis])):
        nearer = node.left
        further = node.right
        find_nearest(nearer, target, depth+1)
    elif (((node.left == None) and (node.right != None)) or (node.right and target[axis] > node.coords[axis])):
        nearer = node.right
        further = node.left
        find_nearest(nearer, target, depth+1)    
    elif((node.left == None) and (node.right == None)):
        d = distance(node, target)
        nearest.append([d, node.id])
        print(nearest)
        number = nearest[0][1]
        print(obj_name[number])
        nearest = check_nearest(nearest, node, target)
    return path


A = find_nearest(root, target[10])
print(A)