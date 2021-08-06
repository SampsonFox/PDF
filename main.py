loop = 0

if loop == 0:
    settings = list(map(int, input().split()))
    stud_num = settings[0]
    act_num = settings[1]
    loop += 1

while (loop <= act_num+1):
    if loop == 1:
        grade_list = list(map(int, input().split()))
        loop += 1

    if loop <= act_num + 1 and loop > 1:
        requests = list(input().split())
        commond = requests[0]
        del requests[0]
        req_list = list(map(int, requests))
        loop += 1

        if commond == 'U':
            grade_list[req_list[0] - 1] = req_list[1]

        if commond == 'Q':
            rsponse_list = list(grade_list)
            if req_list[0] > req_list[1]:
                req_list.reverse()
            rsponse_list = rsponse_list[req_list[0] - 1:req_list[1]]
            if len(rsponse_list) != 0:
                print(max(rsponse_list))

    if loop >= act_num + 2:
        loop = 0