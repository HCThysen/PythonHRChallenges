# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# Input Format
# The first line contains the integer n, the number of students' records. 
# The next n lines contain the names and marks obtained by a student, each value separated by a space.
# The final line contains query_name, the name of a student to query.

# Output Format
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #Creating mark list
    list1 = student_marks[query_name]
    avg=0
    num=0
    #Creating average
    for i in list1:
        num+=1
        avg+=i
    avg = avg/num   
    print(f'{avg:.2f}')

# Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. 
# Please use list comprehensions rather than multiple loops, as a learning exercise.

#Print an array of the elements that do not sum to n.
# Input Format
# Four integers x, y, z and n, each on a separate line. 
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print( [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n] )
    