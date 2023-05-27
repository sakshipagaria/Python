# # t = int(input())  # number of test cases

# # for _ in range(t):
# #     n = int(input())  # number of jobs
# #     jobs = []

# #     for i in range(1, n+1):
# #         ti, si = map(int, input().split())
# #         penalty = si / ti  # calculate penalty per day
# #         jobs.append((i, ti, si, penalty))

# #     # sort jobs by penalty in ascending order
# #     jobs.sort(key=lambda x: x[3])

# #     # print the job positions in the order they were sorted
# #     print(*[job[0] for job in jobs])
# #     print()  # print a blank line between test cases


# # function to calculate fine for a job
# def calculate_fine(job):
#     return job[1] * job[0]

# # read number of test cases
# num_cases = int(input())

# # iterate through each test case
# for i in range(num_cases):
#     input() # ignore blank line
    
#     # read the jobs for this case
#     num_jobs = int(input())
#     jobs = []
#     for j in range(num_jobs):
#         job = tuple(map(int, input().split()))
#         jobs.append(job)
    
#     # sort the jobs in descending order of fine
#     jobs = sorted(jobs, key=calculate_fine, reverse=True)
    
#     # print the sequence of jobs with minimal fine
#     job_positions = [str(jobs.index(job)+1) for job in jobs]
#     print(' '.join(job_positions))
    
#     # print a blank line after each case, except for the last one
#     if i != num_cases-1:
#         print()


# Read the number of test cases
num_cases = int(input())

# Process each test case
for _ in range(num_cases):
    # Read the number of jobs
    num_jobs = int(input())

    # Create a list to store the jobs
    jobs = []

    # Read the completion time and penalty for each job
    for i in range(num_jobs):
        time, penalty = map(int, input().split())
        jobs.append((i + 1, time, penalty))

    # Sort the jobs based on the ratio of penalty per day
    jobs.sort(key=lambda x: x[2] / x[1])

    # Print the positions of the jobs in the sorted order
    print("".join(str(job[0]) for job in jobs))

    # Print a blank line after each test case
    print()
