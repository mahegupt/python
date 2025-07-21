'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. 

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array
Solution - 1:
1. Build an adjacency list (graph representation).
2. Track number of prerequisites of each course (in_degree[i] = number of prerequisites for course i).
3. Use a queue to store courses with in_degree = 0 (i.e., no prerequisites).
4. Process the queue:
    Remove a course, add it to the result.
    Reduce in_degree of dependent courses.
    If any course’s in_degree reaches 0, push it into the queue.
5. If all courses are processed, return the order. Otherwise, return [] (cycle detected).
'''

from collections import deque

def findOrder(numCourses, prerequisites):
    adj_graph = [[] for i in range(numCourses)]
    num_prerequisites = [0] * numCourses

    #Build adjacency list and count number of prerequisite.
    for course, prereq in prerequisites:
        adj_graph[prereq].append(course)
        num_prerequisites[course] += 1

    ##Populate the queue for courses which has 0 prerequisites
    queue = deque([i for i in range(numCourses) if num_prerequisites[i] == 0])

    #Generate the result.
    result = []
    while queue:
        c = queue.popleft()
        result.append(c)

        for neighbor in adj_graph[c]:
            num_prerequisites[neighbor] -= 1
            if (num_prerequisites[neighbor] == 0):
                queue.append(neighbor)

    return result if len(result) == numCourses else []



numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

print(findOrder(numCourses, prerequisites))
