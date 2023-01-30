def main():
    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    print(solution(id_list, report, k))

def solution(id_list, report, k):
    answer = []
    num_mail = {}
    for id in id_list:
        num_mail[id] = 0

    num_reported = {}
    for id in id_list:
        num_reported[id] = 0

    report_dict = {}
    for id in id_list:
        report_dict[id] = {}

    for report_log in report:
        temp = report_log.split(" ")
        reporter = temp[0]
        reported = temp[1]

        if report_dict[reported].get(reporter) != True:
            report_dict[reported][reporter] = True
            num_reported[reported] += 1
            if num_reported[reported] == k:
                for i_reporter in report_dict[reported].keys():
                    num_mail[i_reporter] += 1
            if num_reported[reported] > k:
                num_mail[reporter] += 1
        else:
            continue

    for id in id_list:
        answer.append(num_mail[id])

    return answer

main()