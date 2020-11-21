#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup as bs
# !pip3 install networkx
# !pip3 install matplotlib
import requests


next_page = "https://rm.wikipedia.org/w/index.php?title=Spezial:AllPages" #starting wikipedia page
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
        if "proxima pagina" in link.text.strip(): #if the link leads to the next page of all articles
            next_page = "https://rm.wikipedia.org" + url #change the starting wikipedia page to the next one
#             print (next_page)
            flag = True  #change flag to true
            continue 

        if url=='https://rm.wikipedia.org/wiki/Spezial:AllPages': #if last page break
            break

        if "/wiki" in url: #if the link leads to another wiki page
            go_to = "https://rm.wikipedia.org" + url #save that link
#             print(url[6:])
            a_links.append(url[6:]) #link format /wiki/article, save the "article" name at the a_links list
                
matrix=[] #creates a zero content 2d matrix with the length and width of a_links list
for i in range(len(a_links)): 
    row=[] 
    for j in range(len(a_links)): 
        row.append(0) 
    matrix.append(row) 


# In[2]:


len(a_links)


# In[3]:


flag = True #flag = true
dict = {}
i = 0
j = 0
k = len(a_links)
d = []
next_page = "https://rm.wikipedia.org/w/index.php?title=Spezial:AllPages" #resets the starting page 

while flag:
#     print(next_page)
#     print(len(dict))
    res = requests.get(next_page) 
#     print(res.text)
    soup = bs(res.text, "html.parser")
    flag = False
    for link in soup.find_all("a"):

        url = link.get("href", "")
#         print(url)
        if "proxima pagina" in link.text.strip():
            next_page = "https://rm.wikipedia.org" + url
            print(url)
            flag = True
            continue 

        if url=='https://rm.wikipedia.org/wiki/Spezial:AllPages':
            break

        if "/wiki" in url:
#             dict[link.text.strip()] = url
            go_to = "https://rm.wikipedia.org" + url
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
                            if not "Datoteca" in urls2: #ignores all links that lead to a media file
                                if not ":" in urls2: #ignores all command links
                                    for j in range(0,k): #scans all the existing articles at a_links list
#                                         print (i)
#                                         print (j)
                                        if urls2[6:] == a_links[j]: #if the link name matches an existing name at that list
                                            matrix[i][j] = 1 #make that cell =1
            i = i + 1 #move to the next article
            


# In[4]:


len(matrix)


# In[4]:


import networkx as nx
G = nx.DiGraph() #graph constructor
for u in range(len(a_links)): #scan the matrix table
    G.add_node(a_links[u]) #add all strings from a_links table as nodes
    for v in range(len(a_links)):
        if matrix[u][v] == 1: #if the is a non zero cell
            G.add_edge(a_links[u],a_links[v]) #make an edge between the urls2 article and the correspondant a_lists article
                


# In[14]:


import networkx as nx
M = nx.Graph() #graph constructor
for u in range(len(a_links)): #scan the matrix table
    for v in range(len(a_links)):
        if matrix[u][v] == 1: #if the is a non zero cell
            M.add_node(a_links[u])
            M.add_edge(a_links[u],a_links[v]) #make an edge between the urls2 article and the correspondant a_lists article
                


# In[6]:


nx.number_of_isolates(G)


# In[8]:


nx.density(G)


# In[10]:


G.number_of_edges()


# In[26]:


nx.average_clustering(G)


# In[16]:


deg = list(G.degree)
deg.sort(key = operator.itemgetter(1))
print(deg)


# In[16]:


print(list(nx.shortest_path(G, a_links[35], a_links[128])))
print(list(nx.shortest_path(G, a_links[56], a_links[128])))
print(list(nx.shortest_path(G, a_links[55], a_links[420])))
print(list(nx.shortest_path(G, a_links[665], a_links[500])))
print(list(nx.shortest_path(G, a_links[543], a_links[52])))
print(list(nx.shortest_path(G, a_links[132], a_links[12])))
print(list(nx.shortest_path(G, a_links[510], a_links[1025])))
print(list(nx.shortest_path(G, a_links[350], a_links[1025])))
print(list(nx.shortest_path(G, a_links[87], a_links[3128])))
print(list(nx.shortest_path(G, a_links[560], a_links[300])))
print(list(nx.shortest_path(G, a_links[1000], a_links[3000])))


# In[32]:


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
ax.set_xlim(0,80)

plt.savefig('romansch1.png', dpi=300)


# In[13]:


p = nx.clustering(G)


# In[14]:


p = nx.clustering(G)
import operator
sorted_cluster_ndl = sorted(p.items(), key = operator.itemgetter(1))
print(sorted_cluster_ndl)


# In[15]:


c = nx.degree_centrality(G)
import operator
sorted_centrality_rm = sorted(c.items(), key = operator.itemgetter(1))
print(sorted_centrality_rm)


# In[1]:


nx.average_clustering(G)


# In[14]:


n_e = nx.all_neighbors(G,'Europa')


# In[35]:


sumy = 0
no_paths = 0
for i in range(0,400):
    flag = 0
    for j in range(0,400):
        if nx.has_path(G, a_links[i],a_links[j]):
            
            flag = flag + len(nx.shortest_path(G,a_links[i],a_links[j]))
        else:
            no_paths = no_paths + 1
    sumy = sumy + flag
        


# In[36]:


print(sumy)
x = sumy/(400*400)
print(x)
print(no_paths)


# In[23]:


import networkx as nx
import matplotlib.pyplot as plt

degree_sequence = sorted([d for n, d in nx.clustering(G)], reverse=True)
# print "Degree sequence", degree_sequence
dmax = max(degree_sequence)

plt.loglog(degree_sequence, 'b-', marker='o')
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")


plt.show()

plt.savefig("degree_cluster.png")


# In[7]:



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
    plt.savefig('romansch3.png', dpi=400)


# In[17]:


from operator import itemgetter

import matplotlib.pyplot as plt
import networkx as nx

if __name__ == '__main__':
    # Create a BA model graph
    n = 1000
    m = 2
    # find node with largest degree

    nx.draw(G, node_color='b', node_size=5, width=0.2)
    # Draw ego as large and red

    plt.show()
    plt.savefig('romansch5.png', dpi=400)


# In[19]:


O = nx.fast_gnp_random_graph(4000, 0.04, directed="True")
nx.average_clustering(O)

