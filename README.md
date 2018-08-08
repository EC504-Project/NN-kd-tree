# EC504 Project -- Nearest Neighbor Search
# NN-kd-tree
using kd-tree to do the Approximate Nearest Neighbor search
## Timeline:
- March 24 - March 31: implement kd-tree and LSH
- March 31 - April 7: Test both algorithm and compare performance
- **April 9: Midterm Report Due**
- **May 2: Final Presentation**
- **May 4: Final Report Due**
## kd-tree
- Group Members: Zhiyu Wang, Zheng Gu
- Development Language: Python
### Kd-tree
-To make kd-tree structure feasible, we decided to do dimension reduction to the original data. Due to we chose CIFAR-10 as our data set, all the input file would be a 32*32 RGB images, and we decided to use grayscale value as the features, so the first thing is to convert the color image to grayscale images. By loading the grayscale images pixel by pixel, for each image, we got a 32*32 matrix.
-To accurate the speed of kd-tree, we chose average pooling and max pooling to preprocessing the image matrix. By comparing the result and analyzing the situation, we decided to go with average pooling, because we want to separate the images as much as possible. All the difference in the grayscale value should be taken into consideration. After the average pooling with a 8*8 kernel, each image turned into a 4*4 matrix. 
-By scanning through the 4*4 matrix, each image could be represented as a 16 dimensional vector. Then we built the kd-tree and did nn search on these new data set. It provided good performance.

#### Steps
Image preprocessing
Import pickle to accomplish the serialization of the binary file.
Import image library from PIL, to load the grayscale image and store as a matrix.
Import the skimage.measure to finish the mean pooling of matrix and convert images to 16d vectors.
Similarity calculation
Import numpy to do the calculation of the similarity between two vectors.
General use
Import sys to read the test path from command line.
Import time to get the running time of the main function.

### Functions of current version
- Read the path of images in document
- Convert image from RGB to grey scale
- Cosine Similarity Hash
- Write out Object using Serialization
### Limitations of Current Implementation
- Cosine hash can only work with images all have the same dimensions 
### Functions to Implement
- ~~Convert image from RGB to grey scale~~
- Convert images to Vectors
- ~~Implement LSH with cosine similarity~~
- ~~Store image using [Object Serialization](https://www.tutorialspoint.com/java/java_serialization.htm)~~
- Double check similarity using [L1 distance](https://stats.stackexchange.com/questions/53068/euclidean-distance-score-and-similarity)
### Servral problem:
1. The data set have 80 millions 32 * 32 pictures and it is too large to handle for us. Perhaps we can use a subset?
2. The preprocessing of the dataset is necessary. Can we sample several pixels of the picture?
3. The size of the hash table and how many hash tables should we create? The more hash tables we create, the better accuracy will be achieved. However, the computation will be much more complex.
## External Library
- [Apache Commons Math3](http://commons.apache.org/proper/commons-math/)
- [Apache Commons Collections3](https://commons.apache.org/proper/commons-collections/)
## Resources
- [Intro to LSH Video on Youtube](https://www.youtube.com/watch?v=bQAYY8INBxg&t=403s)
- [Locality-Sensitive Hashing for Scalable Image Search](http://www.cs.utexas.edu/users/grauman/papers/iccv2009_klsh.pdf)
- [Nearest Neighbor Search MIT Lecture](https://www.youtube.com/watch?v=vAboxtLEeH0)
- [Different Similarities](http://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/)
