def generate(numRows):
    if numRows == 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, numRows):
        prev_row = triangle[-1]
        current_row = [1]
        
        for j in range(1, i):
            current_row.append(prev_row[j-1] + prev_row[j])
        
        current_row.append(1)
        triangle.append(current_row)
    
    return triangle
print(generate(2))