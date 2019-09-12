'''
'''

import kNN

datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
print(datingDataMat)
print(datingLabels[0:20])
    
import matplotlib
import matplotlib.pyplot as plt
import array

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:, 2])

plt.show()

