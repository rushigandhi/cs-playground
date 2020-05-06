# Breadth-first Search implementation using a Queue
def bfs(adj_mtx, start_node_index):
    output = ''
    visited = [False] * len(adj_mtx)

    # add the start node to the stack
    queue = [start_node_index]
    visited[start_node_index] = True

    # dequeue
    node = queue.pop(0)
    output += str(node) + ' '

    while True:

        # iterate over the total number of nodes
        for n in range(len(visited)):

            # check if edge exists and if destination node is not visited
            if adj_mtx[node][n] == 1 and not visited[n]:

                # visit node and enqueue it
                visited[n] = True
                queue.append(n)

        # when stack is empty, break
        if not queue:
            break

        else:
            # dequeue
            node = queue.pop(0)
            output += str(node) + ' '

    return output
