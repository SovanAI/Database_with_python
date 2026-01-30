df = pd.DataFrame({
    'A': [1, 2, 3],     
    'B': [4, 5, 6],     
    'C': [7, 8, 9]})
print(df)
df.to_csv('output.csv', index=False)