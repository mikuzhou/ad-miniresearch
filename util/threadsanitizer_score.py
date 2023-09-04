import re

# 从TSan输出中提取数据竞争报告
def extract_race_reports(tsan_output):
    race_reports = []
    race_report_start = re.compile(r"WARNING: ThreadSanitizer: data race (.+)")
    in_race_report = False

    for line in tsan_output.splitlines():
        if re.match(race_report_start, line):
            in_race_report = True
            race_report = line
        elif in_race_report:
            race_report += "\n" + line
            if line.strip() == "":
                race_reports.append(race_report)
                in_race_report = False

    return race_reports

# 分析并评分TSan输出中的数据竞争
def score_python_code(tsan_output):
    race_reports = extract_race_reports(tsan_output)
    if not race_reports:
        return "No data races detected. Code is thread-safe."

    # 根据竞争数量和严重性进行评分
    num_races = len(race_reports)
    severity_scores = {"WARNING: ThreadSanitizer: data race (": 3, "Race detected:": 2}
    total_score = 0

    for report in race_reports:
        for severity, score in severity_scores.items():
            if severity in report:
                total_score += score

    return f"Detected {num_races} data race(s). Code scored {total_score} out of 10."

# 示例TSan输出
tsan_output = """
WARNING: ThreadSanitizer: data race (pid=12345)
  Write of size 4 at 0x00010010 by thread T1:
    #0 Thread 1 (tid=101)
      ...
  Previous write of size 4 at 0x00010010 by thread T2:
    #0 Thread 2 (tid=102)
      ...

Race detected: Read of size 8 at 0x00020020 by thread T3:
  ...
  Previous write of size 8 at 0x00020020 by thread T4:
    ...
"""

# 调用评分函数并输出结果
result = score_python_code(tsan_output)
print(result)
