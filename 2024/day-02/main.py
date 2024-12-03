from util import get_input
reports = get_input("input.txt")
#reports = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

def part1(reports):
    print("Part 1 Solution: ", sum([1 for report in reports if all([report[i] - report[i-1] in [1, 2, 3] for i in range(1, len(report))]) or all([report[i] - report[i-1] in [-1, -2, -3] for i in range(1, len(report))])]))

def part2(reports):
    def is_safe(report):
        if all([report[i] - report[i-1] in [1, 2, 3] for i in range(1, len(report))]) or all([report[i] - report[i-1] in [-1, -2, -3] for i in range(1, len(report))]):
            return True
        return False
    
    safe_reports = 0
    for report in reports:
        if is_safe(report):
            safe_reports += 1
        else:
            for i in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(i)
                if is_safe(report_copy):
                    safe_reports += 1
                    break
    print("Part 2 Solution: ", safe_reports)

part1(reports)
part2(reports)