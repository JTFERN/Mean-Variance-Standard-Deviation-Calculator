import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    a= np.array(list).reshape((3,3))
    calc={}
    calc["mean"]=[np.mean(a, axis=0).tolist(),np.mean(a, axis=1).tolist(), np.mean(a)]
    calc["variance"]=[np.var(a, axis=0).tolist(),np.var(a, axis=1).tolist(), np.var(a)]
    calc["standard deviation"]=[np.std(a, axis=0).tolist(),np.std(a, axis=1).tolist(), np.std(a)]
    calc["max"]=[np.amax(a, axis=0).tolist(),np.amax(a, axis=1).tolist(), np.amax(a)]
    calc["min"]=[np.amin(a, axis=0).tolist(),np.amin(a, axis=1).tolist(), np.amin(a)]
    calc["sum"]=[np.sum(a, axis=0).tolist(),np.sum(a, axis=1).tolist(), np.sum(a)]




    return calc