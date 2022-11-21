# 100 Node Graph
Time units are in seconds.


  ## 1 Tag Queried
  | Algorithm   | 3 Results | 5 Results | 8 Results |
  | ----------- | --------- | --------- | --------- |
  | Brute Force | 0.0001124	| 0.0001754	| 0.0002791 |
  | Greedy      | 0.0004618	| 0.0007567	| 0.0013595 |
  | Dynamic     | 0.0001224	| 0.0001908	| 0.0003122 |

<p float="left">
  <img src="/images/100-nodes/100-Nodes-1-Tag-Queried.png" width="500" />
</p>




---


  ## 3 Tags Queried
  | Algorithm   | 3 Results | 5 Results | 8 Results |
  | ----------- | --------- | --------- | --------- |
  | Brute Force | 0.0001469	| 0.0001787	| 0.0002721 |
  | Greedy      | 0.0004749	| 0.0016283	| 0.0082615 |
  | Dynamic     | 0.0001213	| 0.0001995	| 0.0003287 |

<p float="left">
  <img src="/images/100-nodes/100-Nodes-3-Tags-Queried.png" width="500" />
</p>




---


  ## 5 Tags Queried
  | Algorithm   | 3 Results | 5 Results | 8 Results |
  | ----------- | --------- | --------- | --------- |
  | Brute Force | 2.68E-05	| 2.24E-05	| 2.47E-05  |
  | Greedy      | 0.0001639	| 0.0001639	| 0.0084734 |
  | Dynamic     | 3.89E-05	| 3.68E-05	| 3.86E-05  |

<p float="left">
  <img src="/images/100-nodes/100-Nodes-5-Tags-Queried.png" width="500" />
</p>

### Regarding the runtimes for Brute Force, Greedy, and Dynamic in this table: 
* When querying 5 tags on the 100 node graph with a setting of 3, 5, and 8 results, only 1 result showed up.
* This means there existed only a single manga that contained the tags in the inputted query, ``Ghosts,Magic,Fantasy,Mystery,Demons``
* Thus, the runtime provided is the time it took to find the one and only search result.

---


  ## No Match Queried (traverse the entire graph)
  | Algorithm   | 3 Results | 5 Results | 8 Results |
  | ----------- | --------- | --------- | --------- |
  | Brute Force | 0.0001302	| 0.0002485	| 0.0001358 |
  | Greedy      | 0.0084853	| 0.008502	| 0.0089906 |
  | Dynamic     | 0.003946	| 0.0034638	| 0.0036073 |

<p float="left">
  <img src="/images/100-nodes/100-Nodes-No-Match-Query.png" width="500" />
</p>




---


## The graphs with the same Y-axis scale

<p float="left">
  <img src="/images/100-nodes/same-y-axis/100-1-y.png" width="500" />
  <img src="/images/100-nodes/same-y-axis/100-3-y.png" width="500" /> 
</p>
<p float="left">
  <img src="/images/100-nodes/same-y-axis/100-5-y.png" width="500" />
  <img src="/images/100-nodes/same-y-axis/100-none-y.png" width="500" /> 
</p>


