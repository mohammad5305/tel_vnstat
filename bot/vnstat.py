import json
import subprocess
import calendar

def month_usage(interface_name: str) -> tuple[str, ...]:
    """Get this month data from vnstat json"""
    stdout = subprocess.getoutput(f"vnstat -s -i {interface_name} --json m")
    if "error:" in stdout.lower():
        raise RuntimeError(stdout)

    data = json.loads(stdout)


    interface = data['interfaces'][0]
    month = interface['traffic']['month'][-1]
    month_name = str(calendar.month_name[month['date']['month']])

    return (interface['name'],
            month['rx'],
            month['tx'],
            month['rx'] + month['tx'],
            month_name)


def human_bytes(B: float) -> str:
    """Return the given bytes as a human friendly KB, MB, GB, or TB string"""
    KB = float(1024)
    MB = float(KB ** 2)  # 1,048,576
    GB = float(KB ** 3)  # 1,073,741,824
    TB = float(KB ** 4)  # 1,099,511,627,776

    if KB <= B < MB:
        B = B / KB
        prefix = "KB"
    elif MB <= B < GB:
        B = B / MB
        prefix = "MB"
    elif GB <= B < TB:
        B = B / GB
        prefix = "GB"
    elif TB <= B:
        B = B / TB
        prefix = "GB"
    else:
        prefix = "Bytes"

    return f"{B:.2f} {prefix}"

