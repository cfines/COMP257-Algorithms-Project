# Dynamic
Time units are in seconds.


  ## 1 Tag Queried
  | Graph Size   | 3 Results | 5 Results | 8 Results |
  | -----------  | --------- | --------- | --------- |
  | 100 Nodes    | 0.0001224 | 0.0001908 | 0.0003122 |
  | 1000 Nodes   | 0.0001273 | 0.000198	 | 0.0004786 |
  | 10000 Nodes  | 0.0001453 | 0.0002275 | 0.0003506 |


<p float="left">
  <img src="/images/algo-comparison/dynamic/1-query.png" width="500" />
</p>




---


  ## 3 Tags Queried
  | Graph Size   | 3 Results | 5 Results | 8 Results |
  | -----------  | --------- | --------- | --------- |
  | 100 Nodes    | 0.0001213 | 0.0001995 | 0.0003287 |
  | 1000 Nodes   | 0.0001237 | 0.0001976 | 0.0003364 |
  | 10000 Nodes  | 0.0002073 | 0.0002884 | 0.0003543 |

<p float="left">
  <img src="/images/algo-comparison/dynamic/3-query.png" width="500" />
</p>




---


  ## 5 Tags Queried
  | Graph Size   | 3 Results | 5 Results | 8 Results |
  | -----------  | --------- | --------- | --------- |
  | 100 Nodes    | 3.89E-05	 | 3.68E-05	 | 3.86E-05  |
  | 1000 Nodes   | 3.99E-05	 | 3.96E-05	 | 3.88E-05  |
  | 10000 Nodes  | Stack Overflow | Stack Overflow | Stack Overflow | 

<p float="left">
  <img src="/images/algo-comparison/dynamic/5-query.png" width="500" />
</p>



---


  ## No Match Queried (traverse the entire graph)
  | Graph Size   | 3 Results | 5 Results | 8 Results |
  | -----------  | --------- | --------- | --------- |
  | 100 Nodes    | 0.003946	 | 0.0034638 | 0.0036073 |
  | 1000 Nodes   | 0.0078314 | 0.0078055 | 0.0078506 |
  | 10000 Nodes  | Stack Overflow | Stack Overflow | Stack Overflow |  

<p float="left">
  <img src="/images/algo-comparison/dynamic/none-query.png" width="500" />
</p>




---


## The graphs with the same Y-axis scale

<p float="left">
  <img src="/images/algo-comparison/dynamic/same-y-axis/1-query-y.png" width="500" />
  <img src="/images/algo-comparison/dynamic/same-y-axis/3-query-y.png" width="500" /> 
</p>
<p float="left">
  <img src="/images/algo-comparison/dynamic/same-y-axis/5-query-y.png" width="500" />
  <img src="/images/algo-comparison/dynamic/same-y-axis/none-query-y.png" width="500" /> 
</p>


