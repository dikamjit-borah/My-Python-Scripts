import numpy as np
import copy

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a_sum_col = []
for i in range(len(a)):
    a_sum_col.append(np.mean(a[:,i], axis=0))
    #np.append(a_sum_col, (sum(a[:,i]) - np.mean(a[:,i], axis=0)), axis = 0)
a_sum_col = np.array(a_sum_col)
print("ORIGINAL MATRIX")
print(a)
print("MEAN OF EACH COLUMN")
print(a_sum_col)
a_new = copy.deepcopy(a)
for i in range(0, len(a)):
    for j in range(0, len(a)):
        a_new[i][j] = a[i][j] - a_sum_col[j]

print("MATRIX AFTER SUBSTRACTING MEAN FROM EACH COLUMN")
print(a_new)
        
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
b_row_sum = []
print("ORIGINAL MATRIX b")
print(b)
#print(np.mean(b[0:,0 ], axis=1))
b_row_sum = ((np.mean(b, axis=1)))/(np.std(b, axis = 1))
b_row_sum = np.array(b_row_sum)
b_new = copy.deepcopy(b)
for i in range(0, len(b)):
    for j in range(0, len(b)):
        b_new[i][j] = b[i][j] - b_row_sum[i]
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
print("b after updation")
print(b_new)
y = b_new.flatten()
print("b after flatten")
print(y)


poly2deg = np.polyfit(x,y,2)
poly3deg = np.polyfit(x,y,3)

print("2 DEGREE POLYFIT")
print(poly2deg)
print("3 DEGREE POLYFIT")
print(poly3deg)