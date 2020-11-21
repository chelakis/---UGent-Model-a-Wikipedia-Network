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

<img src="/img/creation.png" alt="creation" width=60% />

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

<img src="/img/isolated.png" alt="isolated" width=60% />

An example is the AMOLED article. As we can see there are no links to another webpage

<img src="/img/amoled.png" alt="amoled" width=60% />

Another example: Rakel

<img src="/img/rakel.png" alt="rakel" width=60% />

### Degree centrality

These are the articles with the most links from other articles. 

**Degree centrality of Romansh Wikipedia**

We can see that the article with the most ingoing links is the Svizra (Switzerland)

<img src="/img/degreecentr-romansh.png" alt="degreecentr-romansh.png" width=60% />

**Degree centrality of West Flemish Wikipedia**

We can see that the article with the most ingoing links is the Bevolkenge (Population)

<img src="/img/degreecentr-flemish.png" alt="degreecentr-flemish.png" width=60% />

This is obvious because the West Flemish Wikipedia has many articles about cities and places all of which have a link to the 'Bevolkenge' article:

<img src="/img/Bevolkenge.png" alt="Bevolkenge" width=60% />

Here we can see the incoming links to 'Bevolkenge' articles

<img src="/img/Bevolkengeincoming.png" alt="Bevolkengeincoming" width=60% />

**Degree centrality of Dutch Low Saxon Wikipedia**

We can see that the article with the most ingoing links is the Nederland (Netherland)

<img src="/img/degreecentr-dutch.png" alt="degreecentr-dutch" width=60% />

**Some articles with most nodes**

| **WEST-FLEMISH** |  |           |**ROMANSCH** |         **DUTCH** **LOW SAXON**         |          |
| ---------------- | ------------ | --------------------------------- | ---------- | --------------- | -------- |
| West-Vloandern   | 0,1514   | Chantuns da la Svizra | 0,1737 | Netherlands | 0,21 |
|  Belgie          |  0,1427      |    Svizra         |   0,383|   Duutsland     | 0,098 |
| Nederlands          | 0,08957  |    Italia          |   0,111|   Engels        | 0,058 |
|   Frans       |   0,0878     |     Germania         |   0,1052  |  Duuts |  0,0574  |
|  Duutsland          |   0,0732     |  Frantsche     |    0,0959  | Europa|  0,052   |
|   Familie (Biologie) |    0,0732 |                   |  Grunnegs   |   0,1367 |
|   Animalia            |    0,0621                    |            |   Stellingwarfs | 0,1269 |



### Clustering Coefficient

### Other Metrics

|                              | Romansh | West Flemish | Low Saxon |
| ---------------------------- | ------- | ------------ | --------- |
| Density                      | 0,0044  | 0,0022       | 0,0024    |
| Average Clustering           | 0,447   | 0,2209       | 0,2431    |
| Average Shortest path length | 3,471   | 3,048        | 2,963     |

The Romansh Wikipedia has the highest average shortest path length coefficient. We can assume that this has to do with the fact that the Romansh Wikipedia has many Geography articles. This makes the path from a Geography to a non-Geography article a lot longer.

In the following image there are some examples of the shortest paths between random nodes:

<img src="/img/shortestpaths.png" alt="shortestpaths" width=60% />

### Differences and Similarities

* Romansh wiki has many geography articles and is focused around Switzerland

* Flemish wiki has a wide variety of articles (geography, animals, etc) and many articles about Belgium and Flanders

* Dutch Low-Saxon has also articles about geography and many articles connected to Dutch language and dialects

* In all Wikipedia articles with max degree are geographically closely related to the country that speaks the language

### Diagrams

**Degree rank plot**

<img src="/img/rankplot.png" alt="rankplot" width=60% />

**Degree Histogram : Number of nodes with a specific degree**

<img src="/img/degreehist.png"  alt="degreehist" width=60% />

**Degree Histogram : **(Why dutch low saxon has so many nodes with degree = 30?)

<img src="/img/degreehistogram-dutchls.png"  alt="degreehistogram-dutchls" width=60% />

There are so many articles with a node degree = 30 because the Dutch Low-Saxon Wikipedia has many articles for all years/numbers from 100 B.C. till 400 A.D. and these articles are very connected to each other (many links to and from the article to other same articles)

**Entire Romansh Wikipedia graph**

<img src="/img/romansh.png"  alt="romansh" width=60% />

**Neighboors of the node (Nederlaand) for Dutch Low Saxon**

<img src="/img/nederlaand.png"  alt="nederlaand" width=60% />


**Neighboors of the node (Svizra) for Romansh**

<img src="/img/svizra.png"  alt="svizra" width=60% />

## Conclusion

* There are many similarities at the content the three Wikipedia but Dutch and flemish Wikipedia have a wider variety of articles

* The two larger Wikipedia (dutch & flemish) have smaller clustering coefficient and smaller average shortest path length

* The degree rank plot and the degree histogram is similar on all three wikipedia
