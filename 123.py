print('123')
print('321')
def generate_pascal_triangle(n):
    # Initialize the triangle with the first row
    triangle = [[1]*(i+1) for i in range(n)]
    
    # Generate the rest of the triangle
    for i in range(1, n):
        for j in range(1, i):
            # The current element is the sum of the two elements above it
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    
    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(' '.join(str(num) for num in row))

# Example usage
n = 5
triangle = generate_pascal_triangle(n)
print_pascal_triangle(triangle)