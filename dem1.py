import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Folder to save plots
UPLOAD_FOLDER = "static/uploads"  # Make sure the folder exists in your project

def run_fun(curr_pres=75, curr_total=109, start_date="2025-02-03", end_date="2025-04-26", holidays=None, absent=None):
    if holidays is None:
        holidays = ["2025-01-15", "2025-01-26", "2025-02-26", "2025-03-14", "2025-03-30", "2025-03-31", "2025-04-01", "2025-04-05", "2025-04-06", "2025-04-14", "2025-04-18"]
    if absent is None:
        absent = ["2025-01-16", "2025-01-17", "2025-01-18", "2025-01-20","2025-02-10", "2025-02-11", "2025-02-12", "2025-02-13", "2025-03-15", "2025-03-17"]

    def work(start_date, end_date, holidays, absent):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        holidays = [datetime.strptime(day, "%Y-%m-%d") for day in holidays]
        absent = [datetime.strptime(day, "%Y-%m-%d") for day in absent]
        total = 0
        net_total_pres = 0
        curr = start
        l = []
        while curr <= end:
            if curr not in holidays:
                if curr.weekday() == 0 or curr.weekday() == 1:
                    if curr not in absent:
                        net_total_pres += 5
                    total += 5
                elif curr.weekday() == 6:
                    pass
                else:
                    if curr not in absent:
                        net_total_pres += 6
                    total += 6
                l.append((curr, ((curr_pres + net_total_pres) / (curr_total + total)) * 100))
            curr += timedelta(days=1)
        return total, net_total_pres, l

    total_work_days, net_total_pres, l = work(start_date, end_date, holidays, absent)

    at = ((curr_pres + total_work_days) / (curr_total + total_work_days)) * 100
    at_after_absent = ((curr_pres + net_total_pres) / (curr_total + total_work_days)) * 100
    leaves_left = curr_pres + net_total_pres - (0.76 * (curr_total + total_work_days))

    # Attendance data
    dates, percentages = zip(*l)

    # Generate plot and save it
    colors = ["red" if p < 75 else "blue" for p in percentages]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(dates, percentages, color=colors, picker=True, s=50)

    # Reduce clutter on x-axis by showing fewer date labels
    step = max(1, len(dates) // 10)  # Show approximately 10 labels
    plt.xticks(dates[::step], rotation=45, fontsize=8)
    plt.yticks(fontsize=10)
    plt.title("Attendance Percentage Progress Over Time", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Attendance Percentage (%)", fontsize=12)
    plt.grid(alpha=0.3)
    plt.tight_layout()

    # Save the plot image
    img_path = "static/uploads/attendance_plot.png"
    fig.savefig(img_path)
    plt.close(fig)

    # Return result as a dictionary
    return {
        'attendance_percentage': at,
        'attendance_after_absent': at_after_absent,
        'leaves_left': leaves_left,
        'plot_url': img_path  # Return the path to the plot image
    }
