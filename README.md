# Course_Attendance_Calci

This is a Tkinter-based GUI application to calculate the attendance percentage for students. The application helps to determine the number of classes a student can skip and the required attendance percentage based on the entered data.

### Features
- Calculate attendance percentage based on the total number of classes attended and conducted.
- Determine the number of skippable classes.
- Consider holidays and daily class schedules.
- Provide results based on different attendance criteria (satisfactory or condonation).
### Requirements
- Python 3.x
- Tkinter library
### How to Run
1. Make sure you have Python installed on your system. You can download it from python.org.

2. Install Tkinter if it's not already installed. You can do this using the following command:
```
pip install tk
```
3. Save the provided code in a file named attendance_calculator.py.

4. Run the script:
```
python attendance_calculator.py
```
### Usage
- Enter tomorrow's date: The date from which the calculation should start, in the format **YYYY-MM-DD**.

- Enter the semester end date: The date until which the calculation should be performed, in the format **YYYY-MM-DD**.

- Enter the number of classes attended for each subject: Enter the data as space-separated values (e.g.,** 15 15 18 23 20 25 22 6**).

- Enter the number of classes conducted for each subject: Enter the data as space-separated values (e.g., **22 21 22 26 22 28 24 7**).

- Enter the number of classes per each day of the week: Enter the data as space-separated values (e.g., **3 3 3 2 1 3**).

- Enter the number of holidays per each week: Enter the data as space-separated values (e.g.,** 0 0 1 1 0 0**).

- Enter the flag for attendance criteria:
    **1** for satisfactory attendance.
    **2** for condonation.
- Click on the Calculate button to get the results.

### Output
The result section will display:

- The projected attendance percentage by the end of the semester.
- The number of classes that can be skipped.
- The number of classes that need to be attended to maintain the required attendance percentage.

![image](https://github.com/Abhighna-2207/Course_Attendance_Calci/assets/151511020/2b1fd4e5-2ec7-4de4-8937-18f4694be7f3)

![image](https://github.com/Abhighna-2207/Course_Attendance_Calci/assets/151511020/d1d17f7d-5895-4e83-84e8-dd8f0a04e18f)


### Example
Here's an example of the input values:

- Tomorrow's date: **2024-07-06**
- Semester end date: **2024-12-20**
- Classes attended: **15 15 18 23 20 25 22 6**
- Classes conducted: **22 21 22 26 22 28 24 7**
- Classes per day of the week:** 3 3 3 2 1 3**
- Holidays per week: **0 0 1 1 0 0**
- Flag: **1**

