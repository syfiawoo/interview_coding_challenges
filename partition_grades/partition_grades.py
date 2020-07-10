def partition_grades(grades, pass_grade):
    next_pass_index = 0  # keep track of next index to be swapped
    # go through all the grades
    for i in range(len(grades)):
        # check if a passing grade was found
        if grades[i] >= pass_grade:
            # swap the current passing grade with the next index to be swapped
            curr = grades[next_pass_index]
            grades[next_pass_index] = grades[i]
            grades[i] = curr
            next_pass_index += 1  # advance to next position
    print(f'Partitioned grades: {grades}')
