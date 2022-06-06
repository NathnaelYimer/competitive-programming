
def gradingStudents(grades): 
    outPut = []
    for i in range (grades_count):
        if grades[i] <38:
            outPut.append(grades[i])
        elif grades[i]>=38:
            if grades[i]%5==0:
                outPut.append(grades[i])
            elif ((grades[i]//5+1)*5)-(grades[i])<3:
                outPut.append((grades[i]//5+1)*5)
            else:
                outPut.append(grades[i])
        else:
            return []
    return outPut

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
