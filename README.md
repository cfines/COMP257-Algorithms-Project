# COMP257-Algorithms-Project

## Scenario of my Project Proposal
Let’s create a hypothetical scenario in which you are writing the backend of an auto-suggest function of a search bar in your own personal manga library. When the user types in a tag or a combination of tags, the search bar would automatically suggest a limited number of titles related to the tags typed in. The titles are read from a connected graph where each node is a manga. An edge exists between two manga if there is at least one tag both nodes have in common. 

Every node will contain an attribute. This attribute is a dictionary. The key of the dictionary for any particular node is manga_n where n is the index of the node in the graph. The value of the graph is a tuple. This tuple contains a title (string), the tags (list of strings), a link (string), and an indicator that determines if the node has been visited or not (a boolean that is false by default) in that order.

## The following is an explanation of the 3 algorithms I have used:
* **Brute force** iterates through all nodes in the graph and outputs matches containing the queried tag. This will only output 5 matches. 
* **Greedy** goes as follows: Check the starting node (for example node 0, but it can be any) for a match. Get all neighboring nodes from the starting node. Order all neighboring nodes from greatest to least quantity of tags into a list. Iterate through this list and recurse the function, with the neighboring node as the current node. Check this new current node for a query match. If a node has already been visited, skip it. The algorithm is done when 5 matches are found.
* The **Dynamic Programming** method is adapted from DFS. From a given starting node, check if there is any query match. Then, get the first neighbor of the starting node and recurse the function, where the neighboring node is now the current node. Check if there is a query match for the new current node. Then, check the new current node’s first neighbor and recurse the function, where that neighboring node is now the current node. (And so on and so forth.) If a node has already been visited, skip it. The algorithm is done when 5 matches are found.
