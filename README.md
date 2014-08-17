Hierarchical-Clustering-in-Python
=================================

Using Blog Data and the hierarchical clustering algorithm to group similar blogs together. 

- *feedlist.txt*: List of Blog URLs

- *generatefeedvector.py*: Takes in a list of Blog URLs to create a Blog Data Matrix file (blogdata.txt)

- *blogdata.txt*: The matrix to be used in the hierarchical clustering algorithm. Columns are the words within the set of blogs and rows are the blog names. The data in the matrix represents the number of times a word appears in a blog.

-*clusters.py:* File that reads on the blogdata matrix and performs the hierarchical clustering algorithm on the data. 
