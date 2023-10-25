# source https://quera.org/college/11644/chapter/56281/lesson/190712/?comments_page=1&comments_filter=ALL

start_hours = input().split()
working = 7
job_done = []
for i in start_hours:
    if working <= int(i) :
        working = int(i) + 3
        job_done.append(f'{start_hours.index(i) + 1} ')
print(" ".join(job_done))