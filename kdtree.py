#
import pickle
from os import listdir
from PIL import Image
import numpy as np
import skimage.measure
import sys
import time


def dictionmaking(read_file):
    labeldic = {}
    imgdic = {}
    i = 0
    for key in read_file.keys():
        labeldic[i] = key
        vector = []
        for m in range(4):
            for n in range(4):
                vector.append(read_file[key][m][n])
        imgdic[i] = vector
        i += 1
    return labeldic, imgdic


class Node:
    def __init__(self, nid, coords, left, right):
        self.id = nid
        self.coords = coords
        self.left = left
        self.right = right


def build_tree(objects, tree_depth = 0):
    
    if objects == {}:
        return 
    
    dimension = tree_depth % 16
    #because after dimension reduction the images have become a 4*4 matrix.
    
    points = sorted(objects, key=lambda k: objects[k][dimension])
    
    line = int(len(points)/2)
    
    node_id = points[line]
    node = Node(node_id, objects[node_id], None, None)
    
    line_nodes = {}
    if dimension in line_nodes.keys():
        line_nodes[dimension].append(node_id)
    else:
        line_nodes[dimension] = [node_id]
    
    left = {}
    right = {}
    
    for key in points[0:line]:
        left[key] = objects[key]
        
    for key in points[line+1:]:
        right[key] = objects[key]
        
    node.left = build_tree(left, tree_depth + 1)
    node.right = build_tree(right, tree_depth + 1)
    return node



def distance(node, target):
    if node == None or target == None:
        return None
    else:
        dis = []
        for i in range(len(node.coords)): 
            dis.append(abs(node.coords[i] - target[i]))
    return sum(dis)

def similarity(original, target):
    if original == None or target == None:
        return None
    else:
        dis = []
        for i in range(len(original)): 
            dis.append(abs(original[i] - target[i]))
    return sum(dis)


def check_nearest(nearest, node, target, path):
    nearset_d = 100000000
    i = 0
    while(len(nearest) < 5):
        d = distance(node, target)
        if (d < nearset_d):
            nearest.append([d, node.id])
            nearset_d = d
            nearest = sorted(nearest, key = lambda nearest:nearest[1])#(objects, key=lambda k: objects[k][axis])
        target = img[path[i-1]]
        if len(nearest) >= 5:    
            nearest.pop()   
    return nearest



def find_nearest(node, target, path, depth=0):
    path.append(node.id)
    nearest = [] 
    axis = depth % 16
    if(((node.right == None) and (node.left != None)) or (node.left and target[axis] <= node.coords[axis])):
        nearer = node.left
        further = node.right
        if(node.right != None):
            path.append(node.right.id)
        find_nearest(nearer, target, path, depth+1)
    elif(((node.left == None) and (node.right != None)) or (node.right and target[axis] > node.coords[axis])):
        nearer = node.right
        further = node.left
        if(node.left != None):
            path.append(node.left.id)
        find_nearest(nearer, target, path, depth+1)    
    elif((node.left == None) and (node.right == None)):
        d = distance(node, target)
        nearest.append([d, node.id])
#         number = nearest[0][1]
#         nearest = check_nearest(nearest, node, target, path, imgdic)
    return path


def load_pixel(file_name):
    img = Image.open(file_name)
    pix = img.load()
    value = []
    dimension = 0
    for i in range(0,32):
        temp = []
        for j in range(0,32):
            temp.append(pix[i,j][0])
        value.append(temp)
    return(value)

def main():
    new_file = pickle.load(open( "save.p", "rb" ) )
    labeldic, imgdic = dictionmaking(new_file)
    
    root = build_tree(imgdic)#build a kd-tree
    
    testpath = sys.argv[1]#"test/"
    test = []
    for file in listdir(testpath):
        if file.endswith(".jpg"):
            test.append(file)
#     print(test[10:20])
    result = []
    for t in range(len(test)):
        img = Image.open(testpath+test[t]).convert('LA')
        greyname = test[t].replace(".jpg", ".png")
        img.save('temp/'+greyname)
        mat = load_pixel('temp/' + greyname)
        npmatix = np.array(mat)
        testmat = skimage.measure.block_reduce(npmatix, (8,8), func=np.mean)

        testvector = []
        for m in range(4):
                for n in range(4):
                    testvector.append(testmat[m][n])
        path = []
        A = find_nearest(root, testvector, path)
        simi = {}
        for i in range(len(A)):
            candidate = labeldic[A[-i]]
            simi[candidate] = similarity(imgdic[A[-i]], testvector)

        simi = sorted(simi.items(), key=lambda simi: simi[1])
        
        result.append(simi[0][0].replace(".png", ".jpg").replace("greyscale/",""))

    # count = 0
    # for p in range(len(result)):
    #     if(test[p] == result[p]):
    #         count += 1
    #     else:
    #         print(test[p])
    # print(count, len(result))
        print(test[0]) #when demon, get this code back, ZHiyu Wang
        print("the most similar list are:")
        for i in range(1):
            print("L1 similarity:",1-simi[i][1]/sum(testvector), simi[i][0].replace(".png", ".jpg").replace("greyscale/",""))
        
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Running time: --- %s seconds ---" % (time.time() - start_time))