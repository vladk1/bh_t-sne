import numpy as Math
import pylab as Plot

X = Math.loadtxt("bhtsne_output.txt")
print(X)
labels = Math.loadtxt("word.txt");
Plot.scatter(X[:,0], X[:,1], 30, labels);
Plot.show();