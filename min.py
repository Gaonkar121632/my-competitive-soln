import numpy as np
value = 4
A = np.array([1,7,35,6])
idx = (np.abs(A-value)).argmin()
print(A[idx])