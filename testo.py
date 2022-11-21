from asyncio import threads
import networkx as nx
import os, shutil, timeit, random, sys

def main():
    # The recursion limit for python is set to 1000 to prevent stack overflow. I set this to meet the size of my graph,
    # as DFS (for 1000 and 10,000 node graphs) and Greedy (when using 10,000 node graphs) exceeds this limit.
    sys.setrecursionlimit(10000)

    print("[1] 100 nodes\n[2] 1000 nodes\n[3] 10,000 nodes")
    print("[B] Brute Force\n[G] Greedy\n[D] Dynamic")
    print("Example: 1,B or 3,D")
    print("Change the 'queried tags' and the 'max displayed results' manually in the code")
    user_input = input("Enter: ")
    # user_input = "3,D"
    user_input = [int(item) if item.isdigit() else item for item in user_input.split(',')]

    # Manually change the query here. See all_available_tags.txt for a list of all tags to choose from.
    # query = 'Action'
    query = 'Comedy,Romance,Drama'
    # query = 'Ghosts,Magic,Fantasy,Mystery,Demons'
    # query = 'yuh'
    query = [int(item) if item.isdigit() else item for item in query.split(',')]

    # Manually change the max results displayed here. It will be either 3, 5, or 8.
    max_results = 3
    # max_results = 5
    # max_results = 8

    if user_input[0] == 1:
        from_pickle = nx.read_gpickle("100_nodes.gpickle")
    elif user_input[0] == 2:
        from_pickle = nx.read_gpickle("1000_nodes.gpickle")
    elif user_input[0] == 3:
        from_pickle = nx.read_gpickle("10000_nodes.gpickle")
    else:
        print("invalid input")
        quit()

    if user_input[1] == 'B':
        algo_select = 'B'
    elif user_input[1] == 'G':
        algo_select = 'G'
    elif user_input[1] == 'D':
        algo_select = 'D'
    else:
        print("invalid input")
        quit()

    # TODO: make parameter for all algorithms that specify number of results shown before quitting
    test_cases(algo_select, from_pickle, query, max_results)

def test_cases(algo_select, from_pickle, query, max_results):
    if algo_select == 'B':
        brute_force(from_pickle, query, max_results)
    elif algo_select == 'G':
        total_matches = 0
        starting_node = 0
        start = timeit.default_timer()
        Greedy(from_pickle, query, starting_node, total_matches, start, max_results)
        end = timeit.default_timer()
        print("Total elapsed time: ", end-start, " seconds")
    elif algo_select == 'D':
        starting_node = 0
        Dynamic_Greedy_Revised(from_pickle, query, starting_node, max_results)

# # # # # # # # # # # #  ALGORITHMS  # # # # # # # # # # # #

def Dynamic_Greedy_Revised(graph, query, curr_node, max_results):
    total_matches = 0
    start = timeit.default_timer()

    Dynamic_Greedy_Revised_Util(graph, query, curr_node, total_matches, start, max_results)
    end = timeit.default_timer()
    print("Total elapsed time: ", end - start, " seconds")

# Adapted from: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
def Dynamic_Greedy_Revised_Util(graph, query, curr_node, total_matches, start, max_results):
    key = "manga_%s" % curr_node
    # print(curr_node)
    node_now_visited(graph, curr_node, key)

    # Check for query match of the current node
    if find_common_tags(query, graph.nodes[curr_node][key][1]) is True:
        end = timeit.default_timer()
        print("Found Match:", graph.nodes[curr_node][key][0], ", Node:", curr_node, "at",
              end - start, "seconds")
        total_matches += 1

    # Check if total matches is equal to max_results. If so, break. We don't need to search for anymore.
    if total_matches == max_results:
       quit()

    # Recurse for all nodes neighboring to this current node
    for neighbor in graph.neighbors(curr_node):
        key = "manga_%s" % neighbor
        # If the node has not been visited yet, recurse.
        if graph.nodes[neighbor][key][-1] is False:
            Dynamic_Greedy_Revised_Util(graph, query, neighbor, total_matches, start, max_results)


def Greedy(graph, query, curr_node, total_matches, start, max_results):
    # print("Current node: ", curr_node)
    key1 = "manga_%s" % curr_node
    # Check if there is a match for the current node
    if find_common_tags(query, graph.nodes[curr_node][key1][1]) is True:
        end = timeit.default_timer()
        print("Found Match:", graph.nodes[curr_node][key1][0], ", Node:", curr_node, "at", end - start, "seconds")
        total_matches += 1

    # Check if total matches is equal to max_results. If so, break. We don't need to search for anymore.
    if total_matches == max_results:
       quit()

    node_now_visited(graph, curr_node, key1)

    list_of_connected_nodes = []
    # Get a list of all neighboring nodes from the current node
    for n in graph.neighbors(curr_node):
        # Only add the node to list_of_connected_nodes if it has NOT been visited
        key2 = "manga_%s" % n
        if graph.nodes[n][key2][-1] is False:
            list_of_connected_nodes.append(n)

    # Only follow through with the recursive call if the list of connected nodes is NOT empty
    if list_of_connected_nodes:
        temp_quant_list = []
        # Get the quantity of tags for every neighboring node of the current node
        for connected_node in list_of_connected_nodes:
            key = "manga_%s" % connected_node
            temp_quant = len(graph.nodes[connected_node][key][1])
            temp_quant_list.append(temp_quant)

        temp_dict = {}
        # In order to associate the neighboring node with its quantity of tags, create a dictionary where the key
        # is the neighboring node and the value is the quantity of tags of that neighboring node.
        for idx, i in enumerate(list_of_connected_nodes):
            temp_dict[i] = temp_quant_list[idx]

        # Sort the dictionary from the greatest quantity of tags to the least quantity of tags
        # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        temp_dict = dict(sorted(temp_dict.items(), reverse=True, key=lambda item: item[1]))

        # Recursively call this function, using the neighboring node as an argument for the current node. This will
        # recursively call in the order of greatest to the least quantity of tags per node.
        # print("recursing")
        # print(temp_dict)
        for neighboring_node in temp_dict:
            key = "manga_%s" % neighboring_node
            # Only commence the recursion for the node that has NOT been visited. While I already have a similar check
            # above, without this check, it will continue to needlessly recurse and output duplicate matches.
            if graph.nodes[neighboring_node][key][-1] is False:
                Greedy(graph, query, neighboring_node, total_matches, start, max_results)

# Save all nodes of the graph into a list. Iterate through this list and check for any matches. Simple as.
def brute_force(graph, query, max_results):
    start = timeit.default_timer()
    total_matches = 0
    temp_list = list(graph.nodes)

    # Iterate through every node in the graph. For every node in the graph, compare the query to the list of tags for
    # every node in the graph. If there's a match, output the name of the match.
    for idx, i in enumerate(temp_list):
        key = "manga_%s" % idx

        # Check if total matches is equal to the maximum results. If so, break. We don't need to search for anymore.
        if total_matches == max_results:
            quit()

        if find_common_tags(query, graph.nodes[idx][key][1]) is True:
            end = timeit.default_timer()
            print("Match found:", graph.nodes[idx][key][0], ", Node:", idx, "at", end - start, "seconds")
            total_matches += 1
    end = timeit.default_timer()
    print("Total elapsed time: ", end - start, " seconds")

# # # # # # # # # # # #  GRAPHING  # # # # # # # # # # # #

# https://www.geeksforgeeks.org/python-print-common-elements-two-lists/
def find_common_tags(query, curr_vertex_tags):
    query_set = set(query)
    curr_vertex_tags_set = set(curr_vertex_tags)

    if query_set & curr_vertex_tags_set:
        temp = query_set & curr_vertex_tags_set
        if len(temp) == len(query_set):
            return True
    else:
        return False

# Changes the boolean in the tuple of the current node to True to indicate the node has been visited.
def node_now_visited(graph, curr_node, key):
    temp = list(graph.nodes[curr_node][key])
    temp[-1] = True
    temp = tuple(temp)
    new_attr = {curr_node: {key: temp}}
    nx.set_node_attributes(graph, new_attr)


if __name__ == "__main__":
    main()
