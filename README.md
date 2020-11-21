# Network Topology of Wikipedia

## Contents

*img folder:* images

*src folder:* source code

## Abstract 

Today one of the greatest collections of information is Wikipedia, consisting of more than 52 000 000 articles in 309 different languages. Each articles has some keywords within the text, which point to other articles with more information on these specific subjects. As such, the whole of Wikipedia (for a certain language) can be represented by a directed graph, with nodes representing the articles and arcs pointing to other articles.

**The goal of this project will be to explicitly construct the network of articles for a certain language.** 

Once the network is constructed, it can be analyzed by studying different metrics, such as the distribution of vertex degrees, the average path length, the clustering coefficient,… (be creative!). Some interesting question could be:

* What do you expect for the distribution of vertex degrees and what do you actually find?
* Is the network completely connected or are there disconnected components which are not reachable from certain clusters of articles?
* Are there clear clusters of articles for certain subject/categories (e.g. biology, music, astronomy,…)? Are there quantitative differences between these clusters
* How many clicks does one on average need to reach a certain article starting from a random other article? I.e. does the network obey the small-world property (like Watts-Strogatz graphs)? What do you expect intuitively?
* Are there quantitative differences between the networks constructed for different languages (e.g. West-Vlaams and Hakka)?

## Introduction

As mentioned above the goal of this project is to create a network of Wikipedia articles based on the hyperlinks from one article to another. The languages that I decided to work on are the following:

* **Romansh Wikipedia** *4544 articles*
* **West Flemish Wikipedia** *11321 articles*
* **Dutch Low Saxon Wikipedia** *11077 articles*

## Data extraction

In order to scrap all Wikipedia articles, Python in combination with BeautifulSoup was used. The script accesses each Wikipedia article and searches for links to other Wikipedia articles. The drawback of this code is that it is slow and inefficient for large Wikipedias and its speed is based on the internet connection of the user. On the other hand it works pretty well for the size of Wikipedias that we want to work on.

## Approach

The script first scans.all the articles from the “all articles” page and saves the title at a list *(called a_links)*. Then it creates a NxN matrix with all values equal to zero (where N the number of articles). In the end, scans again all the articles and if a link is found, makes the specific cell that corresponds to these articles equal to 1. Of course links to images, navigation links and links to images have to be excluded.

***How nodes are created:***

<img src="D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\creation.png" alt="creation" style="zoom:60%;" />

***Code that creates nodes between articles that have a link to each other:***

```
import networkx as nx
G = nx.DiGraph() #graph constructor
for u in range(len(a_links)): #scan the matrix table
    for v in range(len(a_links)):
        if matrix[u][v] == 1: #if the is a non zero cell
            G.add_edge(a_links[u],a_links[v]) #make an edge between the articles
```



### Network Construction using Networkx library

### Number of nodes and edges

|                           | Romansh | West Flemish | Dutch Low Saxon |
| ------------------------- | ------- | ------------ | --------------- |
| Number of Nodes           | 4544    | 11338        | 11077           |
| Number of Edges           | 90986   | 253886       | 246389          |
| Edges per node on average | 20,02   | 22,39        | 22,24           |

### Isolated nodes

These are the nodes that have no link to another webpage. In the following image are some isolated articles from Romansh Wikipedia.

| Romansh | West Flemish | Dutch Low Saxon |
| ------- | ------------ | --------------- |
| 80      | 60           | 15              |

![isolated](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\isolated.png)

An example is the AMOLED article. As we can see there are no links to another webpage

![amoled](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\amoled.png)

Another example: Rakel

![rakel](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\rakel.png)

### Degree centrality

These are the articles with the most links from other articles. 

**Degree centrality of Romansh Wikipedia**

We can see that the article with the most ingoing links is the Svizra (Switzerland)

![degreecentr-romansh](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\degreecentr-romansh.png)

**Degree centrality of West Flemish Wikipedia**

We can see that the article with the most ingoing links is the Bevolkenge (Population)

![degreecentr-flemish](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\degreecentr-flemish.png)

This is obvious because the West Flemish Wikipedia has many articles about cities and places all of which have a link to the 'Bevolkenge' article:

![Bevolkenge](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\Bevolkenge.png)

Here we can see the incoming links to 'Bevolkenge' articles

![Bevolkengeincoming](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\Bevolkengeincoming.png)

**Degree centrality of Dutch Low Saxon Wikipedia**

We can see that the article with the most ingoing links is the Nederland (Netherland)

![degreecentr-dutch](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\degreecentr-dutch.png)

**Some articles with most nodes**

| **WEST-FLEMISH** | **ROMANSCH** | **DUTCH** **LOW SAXON**           |            |                 |          |
| ---------------- | ------------ | --------------------------------- | ---------- | --------------- | -------- |
| West-Vloandern   | **0,1514**   | **Chantuns** **da la** **Svizra** | **0,1737** | **Netherlands** | **0,21** |
|                  |              |                                   |            |                 |          |
|                  |              |                                   |            |                 |          |
|                  |              |                                   |            |                 |          |
|                  |              |                                   |            |                 |          |
|                  |              |                                   |            |                 |          |
|                  |              |                                   |            |                 |          |



### Clustering Coefficient

### Other Metrics

|                              | Romansh | West Flemish | Low Saxon |
| ---------------------------- | ------- | ------------ | --------- |
| Density                      | 0,0044  | 0,0022       | 0,0024    |
| Average Clustering           | 0,447   | 0,2209       | 0,2431    |
| Average Shortest path length | 3,471   | 3,048        | 2,963     |

The Romansh Wikipedia has the highest average shortest path length coefficient. We can assume that this has to do with the fact that the Romansh Wikipedia has many Geography articles. This makes the path from a Geography to a non-Geography article a lot longer.

In the following image there are some examples of the shortest paths between random nodes:

![shortestpaths](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\shortestpaths.png)

### Differences and Similarities

* Romansh wiki has many geography articles and is focused around Switzerland

* Flemish wiki has a wide variety of articles (geography, animals, etc) and many articles about Belgium and Flanders

* Dutch Low-Saxon has also articles about geography and many articles connected to Dutch language and dialects

* In all Wikipedia articles with max degree are geographically closely related to the country that speaks the language

### Diagrams

**Degree rank plot**

![rankplot](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\rankplot.png)

**Degree Histogram : Number of nodes with a specific degree**

![degreehist](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\degreehist.png)

**Degree Histogram : **(Why dutch low saxon has so many nodes with degree = 30?)

![degreehistogram-dutchls](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\degreehistogram-dutchls.png)

There are so many articles with a node degree = 30 because the Dutch Low-Saxon Wikipedia has many articles for all years/numbers from 100 B.C. till 400 A.D. and these articles are very connected to each other (many links to and from the article to other same articles)

**Entire Romansh Wikipedia graph**

![romansh](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\romansh.png)

**Neighboors of the node (Nederlaand) for Dutch Low Saxon**

![nederlaand](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\nederlaand.png)

**Neighboors of the node (Svizra) for Romansh**

![svizra](D:\Αρχεία\HMMY\UGent\Network Modelling & Design\img\svizra.png)

## Conclusion

* There are many similarities at the content the three Wikipedia but Dutch and flemish Wikipedia have a wider variety of articles

* The two larger Wikipedia (dutch & flemish) have smaller clustering coefficient and smaller average shortest path length

* The degree rank plot and the degree histogram is similar on all three wikipedia