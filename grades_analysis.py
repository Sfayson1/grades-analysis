import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Start program with student ID
print("SHEFAY9008")
# ---------------------------------------------------------

def main():

    # Step 3: Create a classroom roster of 10 students in an array
    students = ["Alex", "Brianna", "Chris", "Danielle", "Evan","Faith", "George", "Hannah", "Isaac", "Jasmine"]

    # Step 4: Create an index for student and subject using MultiIndex
    subjects = ["Math", "Science"]
    index = pd.MultiIndex.from_product([students, subjects], names=["Student", "Subject"])

    # Step 5: Create a DataFrame of grades for each student for two subjects
    grades = [92, 87, 85, 90, 88, 95, 78, 84, 91, 89,   # Math grades
              88, 90, 82, 85, 87, 93, 80, 86, 89, 90]   # Science grades

    df = pd.DataFrame({"Grade": grades}, index=index)

    # # Display the DataFrame
    # print("\nClassroom Grades DataFrame:")
    # print(df)

    # Step 6: Group by the mean of the subject
    subject_means = df.groupby("Subject").mean()

    print("\nSubject      Grade")
    for subject, row in subject_means.iterrows():
        print(f"{subject:<12}{row['Grade']:.2f}")


    # Step 7: Display the vertical bar graph
    subject_means.plot(kind="bar", legend=False)
    plt.title("Average Grade by Subject")
    plt.ylabel("Average Grade")
    plt.xlabel("Subject")
    plt.ylim(0, 100)
    plt.show()

main()
