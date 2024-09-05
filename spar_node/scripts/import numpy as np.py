import numpy as np

nan_list = np.full((100, 2), np.nan)
print(nan_list.dtype)
nan_list[1,1] = 1
print("sds", (nan_list[1,1]))