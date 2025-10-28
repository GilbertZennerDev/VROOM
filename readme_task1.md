Project 1 – Clustering cross-border workers
Objective:
Create homogeneous travel groups.
Goal:
Build a geo-localized clustering system for employees, with interactive map
visualization.
Description:
We will first collect key information from cross-border workers, including:
•Home location
•Workplace location
•Usual required arrival time at work
•Typical departure time from work to home

Using this data, the system will identify clusters of workers who can be grouped together
for shared rides. These groups should be as homogeneous as possible to minimize
detours, delays, and scheduling conflicts.
The system should also be flexible and dynamic:
If a person declares they will be late (e.g., sleeping in, shift change), the algorithm
should reassign them to a different group or route in real time, without disrupting the rest
of the cluster.
Key Parameters:
Departure time, origin & destination points.
Ideas:
Unsupervised machine learning.
Tools & Resources:
DBScan (Density-Based Spatial Clustering of Applications with Noise)

=================

Need to go step by step

1. Create fitting travel groups
I get users, who live in random places, work at random times. I need to put similar workers together.
Easiest way: Find identical workers, put them into the same car.