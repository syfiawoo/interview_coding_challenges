def partition_grades(grades, pass_grade):
    next_pass_index = 0
    for i in range(len(grades)):
        if grades[i] >= pass_grade:
            curr = grades[next_pass_index]
            grades[next_pass_index] = grades[i]
            grades[i] = curr
            next_pass_index += 1
    print(grades)
