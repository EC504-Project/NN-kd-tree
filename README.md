# EC504 Project -- Nearest Neighbor Search
# NN-kd-tree
using kd-tree to do the Approximate Nearest Neighbor search
## Timeline:
- March 24 - March 31: implement kd-tree and LSH
- March 31 - April 7: Test both algorithm and compare performance
- **April 9: Midterm Report Due**
- **May 2: Final Presentation**
- **May 4: Final Report Due**
## Locality Sensistive Hashing
- Group Members: Yutong Gao, Zhiyuan Ruan, Hongtao Zhao
- Development Language: Java
### LSH Background
- Locality sensitive hashing(LSH): hashing items into bins many times and looking only at those items that fall into the same bin at least once (without looking at every pair).
- Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. If the angle is 0 degree the cosine value will be one and if the angle is 90 degree the cosine value will be 0. In paper 'Kernelized Locality-Sensitive Hashing for Scalable Image Search', it is proved that we can find a vector r and transfer of r multiply the vector of picture can be used to generate hash codes for pictures. Using different vector r to create hash tables and we can put similar picture to the same bucket theoretically. 
- Because we ignore the length of the vector. We need to do double check when we input a picture to find similiarity. Hamming distance will be helpful. We transfer the picture to gray version and caculate the mean of all the pixels. Compare the value of pixels with mean, if it's large assign 1, otherwise assign 0. Now we get the fingureprint of every picture in the bucket. And we find the bucket input belong to, compare the input fingerprint wich is a list of 0 and 1 to the picture in the bucket then we can find the similarity.
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
