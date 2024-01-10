# Connected Components

Graph doesn't necessarily need to be connected (i.e if you start from one node you can reach all nodes) . 

![](Images/Pasted%20image%2020240109220912.png)

Above graph has 10 nodes and 8 edges and 4 different connected components. ==Therefore always run loop to Check all nodes==

```python
for i in range(10):
	if not visited[i]:
		traversal(i)
```
	

