import re

# 示例Pylint输出
pylint_output = """
************* Module my_module
my_module.py:10:0: C0111: Missing module docstring (missing-docstring)
my_module.py:12:4: W0612: Unused variable 'unused_variable' (unused-variable)
my_module.py:15:0: R0201: Method could be a function (no-self-use)
my_module.py:20:0: C0303: Trailing whitespace (trailing-whitespace)
...

------------------------------------------------------------------
Your code has been rated at 6.67/10 (previous run: 5.00/10, +1.67)
"""

# 从Pylint输出中提取评分
def extract_pylint_score(pylint_output):
    score_pattern = re.compile(r"Your code has been rated at ([0-9.]+)")
    match = score_pattern.search(pylint_output)
    if match:
        score = float(match.group(1))
        return score
    return None
