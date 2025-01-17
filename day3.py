def avg(n,x):
    marks = []
    for _ in range(x):
        marks.append(list(map(float, input().split())))
        
    #transpose the marks
    transposed_marks = zip(*marks)
    
    for student_marks in transposed_marks:
        average = sum(student_marks) / x
        print(f"{average:.1f}")
        
n, x = map(int, input().split())
avg(n,x)