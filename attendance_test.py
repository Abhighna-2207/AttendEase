import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def count_weekdays(start, end):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    if start > end:
        start, end = end, start

    week_count = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}

    current = start
    while current <= end:
        weekday = current.strftime('%A')
        week_count[weekday] += 1
        current += timedelta(days=1)

    return [week_count['Monday'], week_count['Tuesday'], week_count['Wednesday'], week_count['Thursday'], week_count['Friday'], week_count['Saturday']]

def calculate():
    try:
        start = start_entry.get()
        end = end_entry.get()

        attended = list(map(int, attended_entry.get().split()))
        conducted = list(map(int, conducted_entry.get().split()))

        week_count = count_weekdays(start, end)
        classes_per_day = list(map(int, classes_entry.get().split()))

        total_conducted = sum(conducted)
        additional_classes = sum(classes_per_day[i] * week_count[i] for i in range(6))

        holidays = list(map(int, holidays_entry.get().split()))
        for i in range(6):
            additional_classes -= holidays[i] * classes_per_day[i]

        total_conducted += additional_classes

        flag = int(flag_entry.get())

        current_attendance = ((total_conducted - sum(conducted) + sum(attended)) / total_conducted) * 100

        if flag == 1:
            max_skippable = int(0.25 * total_conducted - (sum(conducted) - sum(attended)))
        elif flag == 2:
            max_skippable = int(0.35 * total_conducted - (sum(conducted) - sum(attended)))
        else:
            messagebox.showerror("Error", "Invalid flag value")
            return

        if max_skippable > 0:
            attendance = (sum(attended) + additional_classes - max_skippable) * 100 / total_conducted
            result = f"Your attendance percentage by the end of the semester: {attendance:.2f}%\nYou can skip {max_skippable} classes\nYou need to attend {0 if additional_classes - max_skippable <= 0 else additional_classes - max_skippable}"
        elif max_skippable < 0:
            result = f"Your attendance percentage by the end of the semester: {current_attendance:.2f}%\nLess than necessary {current_attendance:.2f}%\nYou need to attend {additional_classes}"
        else:
            result = f"Your attendance percentage by the end of the semester: {current_attendance:.2f}%\nNO more holidays\nYou need to attend {additional_classes}"

        result_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Attendance Calculator")

# Displaying the formula and note
formula_label = tk.Label(root, text="Formula for Calculating: Attendance = (Total Number of Classes Attended / Total Number of Classes Conducted) * 100")
formula_label.grid(row=0, column=0, columnspan=2)

note_label = tk.Label(root, text="Note: This program calculates the number of classes you can skip and the attendance percentage from tomorrow. Make sure the data you enter is considered from the end of today.")
note_label.grid(row=1, column=0, columnspan=2)

tk.Label(root, text="Enter tomorrow's date (YYYY-MM-DD):").grid(row=2, column=0)
start_entry = tk.Entry(root)
start_entry.grid(row=2, column=1)

tk.Label(root, text="Enter the semester end date (YYYY-MM-DD):").grid(row=3, column=0)
end_entry = tk.Entry(root)
end_entry.grid(row=3, column=1)

tk.Label(root, text="Enter the number of classes attended for each subject (e.g., 15 15 18 23 20 25 22 6):").grid(row=4, column=0)
attended_entry = tk.Entry(root)
attended_entry.grid(row=4, column=1)

tk.Label(root, text="Enter the number of classes conducted for each subject (e.g., 22 21 22 26 22 28 24 7):").grid(row=5, column=0)
conducted_entry = tk.Entry(root)
conducted_entry.grid(row=5, column=1)

tk.Label(root, text="Enter the number of classes per each day of the week (e.g., 3 3 3 2 1 3):").grid(row=6, column=0)
classes_entry = tk.Entry(root)
classes_entry.grid(row=6, column=1)

tk.Label(root, text="Enter the number of holidays per each week (e.g., 0 0 1 1 0 0):").grid(row=7, column=0)
holidays_entry = tk.Entry(root)
holidays_entry.grid(row=7, column=1)

tk.Label(root, text="Enter 1 for satisfactory, 2 for condonation:").grid(row=8, column=0)
flag_entry = tk.Entry(root)
flag_entry.grid(row=8, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=9, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=10, column=0, columnspan=2)

root.mainloop()
