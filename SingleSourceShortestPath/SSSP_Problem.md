
# Single Source Shortest Path

<br>
<br>

### Ordering in a DAG:
Topological Ordering: Ordering of nodes in a directed graph where for each directed edge 
from Node A to Node B, Node A appears before Node B.
<br>
<br>
> Refer: topological-sort.py

<br>

### Single Source Shortest Path for DAG: 
Topological Ordering and Traversal to update the Distance Vector in that order.
<br>
<br>
> Refer: sssp-topo.py

<br>

### Single Source Longest Path for DAG: 
Topological Ordering and Traversal to update the Distance Vector in that order.
Negate weights before insertion and during the end output to convert SSSP to SSLP.
<br>
<br>
> Refer: sslp-topo.py

<br>

### Single Source Shortest Path for Graphs (with Positive Cycles):
Djikstra's Algorithm is the best Algorithm for this task. <br>
It cannot handle Negative Cycles.
<br><br>
> Refer: djiktra.py

<br>

### Single Source Shortest Path for Graphs (with Positive Cycles) Optimized by using a Priority Queue:
Optimized Djikstra's Algorithm using a Heap Based Priority Queue.
<br><br>
> Refer: djiktra-pq.py

<br>

### Single Source Shortest Path for Graphs (with Negative Cycles):
Bellman Ford Algorithm finds the shortest path as well as the location of Negative Cycles, if they exist.
<br>
> Refer: bellman-ford.py

<br>
