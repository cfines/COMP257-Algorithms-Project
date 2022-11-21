# COMP257-Algorithms-Project

## Scenario of my Project Proposal
Let’s create a hypothetical scenario in which you are writing the backend of an auto-suggest function of a search bar in your own personal manga library. When the user types in a tag or a combination of tags, the search bar would automatically suggest a limited number of titles related to the tags typed in. The titles are read from a connected graph where each node is a manga. An edge exists between two manga if there is at least one tag both nodes have in common. 

Every node will contain an attribute. This attribute is a dictionary. The key of the dictionary for any particular node is manga_n where n is the index of the node in the graph. The value of the graph is a tuple. This tuple contains a title (string), the tags (list of strings), a link (string), and an indicator that determines if the node has been visited or not (a boolean that is false by default) in that order.

## The following is an explanation of the 3 algorithms I have used:
* **Brute force** iterates through all nodes in the graph and outputs matches containing the queried tag. This will only output 5 matches. 
* **Greedy** goes as follows: Check the starting node (for example node 0, but it can be any) for a match. Get all neighboring nodes from the starting node. Order all neighboring nodes from greatest to least quantity of tags into a list. Iterate through this list and recurse the function, with the neighboring node as the current node. Check this new current node for a query match. If a node has already been visited, skip it. The algorithm is done when 5 matches are found.
* The **Dynamic Programming** method is adapted from DFS. From a given starting node, check if there is any query match. Then, get the first neighbor of the starting node and recurse the function, where the neighboring node is now the current node. Check if there is a query match for the new current node. Then, check the new current node’s first neighbor and recurse the function, where that neighboring node is now the current node. (And so on and so forth.) If a node has already been visited, skip it. The algorithm is done when 5 matches are found.


### Brute Force Pseudo Code
<p float="left">
  <img src="/images/pseudo-code/brute-force.png" width="500" />
</p>

* Brute Force will run for O(n) due to the for loop, where n is the number of nodes of the graph.


### Greedy Pseudo Code
<p float="left">
  <img src="/images/pseudo-code/greedy1.png" width="500" />
</p>
<p float="left">
  <img src="/images/pseudo-code/greedy2.png" width="500" />
</p>

* The first for loop gathers all neighbors of the current node and appends them into ``neighbors``. This will be of length n. This n is attributed to the amount of neighbors existing in the current node (that haven't been visited). 
* The second for loop iterates through ``neighbors``, appending values to the list ``quantity_list``. This will be of length n. This n is attributed to the amount of neighbors existing in the current node (that haven't been visited). 
* The third for loop iterates through ``neighbors`` again, appending values to the dictionary ``temp_dict``. Once again, this n is attributed to the amount of neighbors in the current node (that haven’t been visited). 
* The fourth for loop iterates through ``temp_dict``, which will also be of length n. Within this loop, the function is called recursively
* Excluding the recursive aspect, none of these for loops in the function are nested within each other. However, considering the recursion that happens n times (in the fourth loop), the runtime complexity will be O(n^4) for the greedy algorithm.


### Dynamic Pseudo Code
<p float="left">
  <img src="/images/pseudo-code/dynamic.png" width="500" />
</p>

* This is adapted from [DFS](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)
* The time complexity of this algorithm is O(|V| + |E|) where V is the number of nodes and E is the number of edges.
* The algorithm will iterate through all nodes that neighbor the current node. It will recurse the function, where the current neighbor of the iteration is passed ONLY if that neighbor has not been visited. 
* From this new current node, it will again loop through all of its neighbors and recurse the function, where the current neighbor of the iteration is passed ONLY if that neighbor has not been visited. 
* And so on and so forth. Therefore the algorithm will iterate for the amount of |nodes there are in the graph| + |the amount of neighbors there exists in the graph|. O (|V| + |E|).

## Caveats 
There are universal trends regarding combinations of tags in manga (or any form of media for that matter). For example, “adventure” is almost always paired with “action.” “Romance” is almost always paired with “School” or “Drama.” While it would grant me more practical results if I were to manually add real manga titles and their actual tags, it is not practical in the interest of time. Especially when I intend to add 10000 nodes. (The runtime of the graph with 100 nodes is merely a fraction of a second, and I want longer runtimes for more comparable values to analyze.) Additionally, writing a webhook to scrape the tags off the website I get these tags from is outside the scope of this project. Therefore I have randomized a combination of tags for fake manga titles (title_50, 51, 52 … title_n) with a random triangular distribution of the quantity of tags per title, where the min = 5, max = 25, mode = 12. These tags are selected from a pool of around 70 tags. The list of tags randomly selected is found ![here](/misc/all_available_tags.txt)

## Clarification of the Displayed Results
The query results are basically first come first serve. The order that the query results appear in is based on the algorithm used. There may be different match results based on the algorithm used. For example:
* Brute force sequentially iterates through all nodes of the graph. Thus, matches found and displayed are based on the numerical order of the nodes in the graph. 
* Greedy finds matches in the order of quantity of tags. Thus the first result (excluding if the starting node is a match) has the most tags and the last result has the least tags.
* Dynamic finds matches based on the first neighbor of the current node, then the first neighbor of that node, then the first neighbor of that node and so on and so forth. 

## Data Collected
I have measured the runtimes of each algorithm producing results from a query containing 1, 3, and 5 tags and a no-match query (0 matches will come out of this query) from manga graphs that consist of 100, 1000, and 10000 nodes. Additionally,  the maximum results found before exiting the algorithms will be 3, 5, 8 search results.

## Results

### Runtime of Varying Graph Sizes with Varying Number of Queries
* [100 Nodes](/100-RESULTS.md)
* [1000 Nodes](/1000-RESULTS.md)
* [10000 Nodes](/10000-RESULTS.md)

### Runtime of the 3 Algorithms Compared Between their Graph Sizes:
* [Brute Force]()
* [Greedy]()
* [Dynamic]()
