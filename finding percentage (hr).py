if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
output=list(student_marks[query_name])
per=sum(output)/len(output)
print("%.2f" % per)

--------output----------
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

=56.00
