# Iterative Depth-first Search implementation using a Stack
def dfs(adj_mtx, start_node_index):
    output = ''
    visited = [False] * len(adj_mtx)

    # add the start node to the stack
    stack = [start_node_index]
    visited[start_node_index] = True

    # pop top of stack
    node = stack.pop()
    output += str(node) + ' '

    while True:

        # iterate over the total number of nodes
        for n in range(len(visited)):

            # check if edge exists and if destination node is not visited
            if adj_mtx[node][n] == 1 and not visited[n]:

                # visit node and add it to the stack
                visited[n] = True
                stack.append(n)

        # when stack is empty, break
        if not stack:
            break

        else:
            # pop an element off the stack
            node = stack.pop()
            output += str(node) + ' '

    return output
