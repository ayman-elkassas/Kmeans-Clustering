import numpy as np

data=np.array([[1,2],[1.5,1.8],[5,8],[8,8],[1,.6],[9,11],[1,3],[8,9],[0,3],[5,4],[6,4]])

k=2
tolerance=.001
max_iteration=300

def train(data,k,tolerance,max_iter):
    centroid={}
    for i in range(k):
        centroid[i]=data[i]

    for i in range(max_iter):
        cluster={}

        for featureSet in data:
            distances=[np.linalg.norm(featureSet-centroid[j]) for j in centroid]
            idx=distances.index(min(distances))
            cluster[idx]=featureSet

        prevoiuse_centroid=dict(centroid)

        for j in centroid:
            centroid[j]=np.average(cluster[j],axis=0)

        optimized=True
        for n in centroid:
            current=centroid[n]
            previous=prevoiuse_centroid[n]

            if(np.sum(current-previous(previous)*100)>tolerance):
                optimized=False

def test(pattern,centroid):
    distances=[np.linalg.norm(pattern-centroid[i]) for j in centroid]
    idx=distances.index(min(distances))
    return idx

train(data,k,tolerance,max_iteration)
i=test([5,3],data[:k])