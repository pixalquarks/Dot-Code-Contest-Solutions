# Villages in a cluster

## Problem Statement

Stark Industries got a new project of connecting villages. So, Indian Govt. provides them some maps regarding village's locations. Some villages are connected with other villages by roads. Villages those are inter-connected are forming a cluster. Every village under one cluster is connected with one another. No two villages under different clusters are connected.

Now as the head of their analytical team your job is to find the average number of villages per clusters(return float value upto 2 decimal). if there is no cluster return -1.

## Input Format

First line of input: K = Number of Edges

For next K lines, each line contains two space separated integer x, y denoting that x is connected to y and y is also connected to x.

## Constraints

0 <= edges.lenght <= 10^5

## Output Format

Output a float upto 2 decimal places, value of average number of villages per cluster.

## Solution

This question is a modification of connected components in a graph. And to find the total number of connected components, BFS can be used. First we convert the edge list into adjacency list. Then perform bfs starting from the first node, and count the total number of times bfs was performed. That is out number of connected components, i.e. clusters.
