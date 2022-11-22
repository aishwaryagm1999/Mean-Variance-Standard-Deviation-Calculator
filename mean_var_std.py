import numpy as np

def calculate(list):
    if len(list) !=9:
      raise ValueError("List must contain nine numbers.")
      return
    ls = np.array(list).reshape(3,3)

    return {
            'mean': [np.mean(ls,axis=0).tolist(),np.mean(ls,axis =1).tolist(),np.mean(ls).tolist()],
            'variance': [np.var(ls,axis=0).tolist(),np.var(ls,axis =1).tolist(),np.var(ls).tolist()],
            'standard deviation': [np.std(ls,axis=0).tolist(),np.std(ls,axis =1).tolist(),np.std(ls).tolist()],
            'max': [np.max(ls,axis=0).tolist(),np.max(ls,axis =1).tolist(),np.max(ls).tolist()],
            'min': [np.min(ls,axis=0).tolist(),np.min(ls,axis =1).tolist(),np.min(ls).tolist()],
            'sum': [np.sum(ls,axis=0).tolist(),np.sum(ls,axis =1).tolist(),np.sum(ls).tolist()]
            }
   
calculate([0,1,2,3,4,5,6,7,8])