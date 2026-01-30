import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3],     
    'B': [4, 5, 6],     
    'C': [7, 8, 9]})
print(df)

matriix = np.array([[1, 2, 3],
                   [4, 5, 6],[2,9,6]])

matrix2 = np.array([[7, 8, 9],[9,6,3],[9,5,3]])

new_matrix = matriix + matrix2
print(new_matrix)
np.savetxt('matrix_output.csv', new_matrix, delimiter=',')
np.savetxt('matrix_output.csv', new_matrix, delimiter=',')