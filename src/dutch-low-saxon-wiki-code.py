#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
# !pip3 install networkx
# !pip3 install matplotlib
import requests


next_page = "https://nds-nl.wikipedia.org/w/index.php?title=Spesiaal:Alle_ziejen" #starting wikipedia page
a_links = [] #table of Wikipedia articles
b_links = []

flag = True #boolean
dict = {}

while flag: 

    res = requests.get(next_page)  #request page
#     print(res.text)
    soup = bs(res.text, "html.parser") #beautiful page constructor
    flag = False 
    for link in soup.find_all("a"): #finds all the "a" classes in the webpage

        url = link.get("href", "") #gets all the hyperlinks from the "a" class
#         print(url)
        if "Volgende zied" in link.text.strip(): #if the link leads to the next page of all articles
            next_page = "https://nds-nl.wikipedia.org" + url #change the starting wikipedia page to the next one
            print (next_page)
            flag = True  #change flag to true
            continue 

        if url=="https://nds-nl.wikipedia.org/wiki/Spesiaal:Alle_ziejen": #if last page break
            break

        if "/wiki" in url: #if the link leads to another wiki page
            go_to = "https://nds-nl.wikipedia.org" + url #save that link
#             print(url[6:])
            a_links.append(url[6:]) #link format /wiki/article, save the "article" name at the a_links list
                
matrix=[] #creates a zero content 2d matrix with the length and width of a_links list
for i in range(len(a_links)): 
    row=[] 
    for j in range(len(a_links)): 
        row.append(0) 
    matrix.append(row) 


# In[4]:


len(matrix)


# In[5]:


flag = True #flag = true
dict = {}
i = 0
j = 0
k = len(a_links)
d = []
next_page = "https://nds-nl.wikipedia.org/w/index.php?title=Spesiaal:Alle_ziejen" #starting wikipedia page


flag = True #boolean
dict = {}

while flag: 

    res = requests.get(next_page)  #request page
#     print(res.text)
    soup = bs(res.text, "html.parser") #beautiful page constructor
    flag = False 
    for link in soup.find_all("a"): #finds all the "a" classes in the webpage

        url = link.get("href", "") #gets all the hyperlinks from the "a" class
        print(url)
        if "Volgende zied" in link.text.strip(): #if the link leads to the next page of all articles
            next_page = "https://nds-nl.wikipedia.org" + url #change the starting wikipedia page to the next one
            print (next_page)
            flag = True  #change flag to true
            continue 

        if url=='https://nds-nl.wikipedia.org/wiki/Spesiaal:Alle_ziejen': #if last page break
            break


        if "/wiki" in url: #if the link leads to another wiki page
            go_to = "https://nds-nl.wikipedia.org" + url #save that link
#             print(url[6:])
           
    #same as above till this line
            
#             print(go_to)
            res2 = requests.get(go_to) #requests each article's content
            soup2 = bs(res2.text, "html.parser") #bs constructor of each wikipedia article
            texts = soup2.find(class_="mw-parser-output") #finds the class of the main body of the article
#             print(texts)
            b_links.clear() 
            for links in texts.find_all('a'): #finds all the "a" classes in the article
                urls2 = links.get("href", "") #finds all the links from the "a" classes
                if "/wiki" in urls2: #if it leads to another wikipedia article
                    if not "redlink=1" in urls2: #ignores all links that lead to an article that does not exist
                        if not "action=edit" in urls2: #ignores all edit links of the article
                            if not "Bestaand" in urls2: #ignores all links that lead to a media file
                                if not ":" in urls2: #ignores all command links
                                    for j in range(0,k): #scans all the existing articles at a_links list
#                                         print (i)
#                                         print (j)
                                        if urls2[6:] == a_links[j]: #if the link name matches an existing name at that list
                                            matrix[i][j] = 1 #make that cell =1
            i = i + 1 #move to the next article
            


# In[6]:


len(matrix)


# In[7]:


import networkx as nx
G = nx.DiGraph() #graph constructor
for u in range(len(a_links)): #scan the matrix table
    G.add_node(a_links[u]) #add all strings from a_links table as nodes
    for v in range(len(a_links)):
        if matrix[u][v] == 1: #if the is a non zero cell
            G.add_edge(a_links[u],a_links[v]) #make an edge between the urls2 article and the correspondant a_lists article
                


# In[11]:


G.number_of_edges()


# In[8]:


nx.number_of_isolates(G)


# In[9]:


nx.density(G)


# In[11]:


list(nx.shortest_path(G, 'Alps', 'Aara'))


# In[20]:


nx.average_clustering(G)


# In[33]:


i = 100

print("Page:", a_links[i])
for j in range(len(matrix)):

    if matrix[i][j]==1: 
        print(j, a_links[j])


# In[12]:


import networkx as nx
MNIT = nx.Graph() #graph constructor
for u in range(len(a_links)): #scan the matrix table
    for v in range(len(a_links)):
        if matrix[u][v] == 1: #if the is a non zero cell
            MNIT.add_edge(a_links[u],a_links[v]) #make an edge between the urls2 article and the correspondant a_lists article
                
print(nx.average_shortest_path_length(MNIT))


# In[18]:


import collections
import matplotlib.pyplot as plt
import networkx as nx



degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)
ax.set_xlim(0,50)

plt.savefig('dutch1.png', dpi=300)


# In[21]:


p = nx.clustering(G)


# In[14]:


p = nx.clustering(G)
import operator
sorted_cluster_rm = sorted(p.items(), key = operator.itemgetter(1))
print(sorted_cluster_rm)


# In[15]:


c = nx.degree_centrality(G)
import operator
sorted_centrality_rm = sorted(c.items(), key = operator.itemgetter(1))
print(sorted_centrality_rm)


# In[16]:


nx.average_clustering(G)


# In[65]:


list(nx.all_neighbors(G,'Europa'))


# In[17]:


deg = list(G.degree)
deg.sort(key = operator.itemgetter(1))
print(deg)


# In[19]:


import networkx as nx
import matplotlib.pyplot as plt

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
# print "Degree sequence", degree_sequence
dmax = max(degree_sequence)

plt.loglog(degree_sequence, 'b-', marker='o')
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")


plt.show()

plt.savefig("degree_histogram_duthc.png")


# In[20]:



from operator import itemgetter

import matplotlib.pyplot as plt
import networkx as nx

if __name__ == '__main__':
    # Create a BA model graph
    n = 1000
    m = 2
    # find node with largest degree
    node_and_degree = G.degree()
    (largest_hub, degree) = sorted(node_and_degree, key=itemgetter(1))[-1]
    # Create ego graph of main hub
    hub_ego = nx.ego_graph(G, largest_hub)
    # Draw graph
    pos = nx.spring_layout(hub_ego)
    nx.draw(hub_ego, pos, node_color='b', node_size=20, width=0.5, with_labels=False)
    # Draw ego as large and red
    nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], node_size=50, node_color='r')
    plt.show()
    plt.savefig('dutch_mainnode.png', dpi=400)

