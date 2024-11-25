import datetime
import os
month = datetime.datetime.now().month

if __name__ == "__main__":
    if month == 11:
        os.system("source venv/bin/activate")
        day = datetime.datetime.now().day
        folder_name = f"Day {day}"
        file_names = [f"Day{day}_part_1.py", f"Day{day}_part_2.py", f"test.txt", f"input.txt"]
        input_url = f"https://adventofcode.com/2024/day/{day}/input"
        problem_url = f"https://adventofcode.com/2024/day/{day}"

        os.mkdir(folder_name)
        for file_name in file_names:
            open(f"{folder_name}/{file_name}", "w").close()
        with open("template.py", "r") as template_file:
            template_content = template_file.read()

        with open(f"{folder_name}/Day{day}_part_1.py", "w") as part_1_file:
            part_1_file.write(template_content)

        with open(f"{folder_name}/Day{day}_part_2.py", "w") as part_2_file:
            part_2_file.write(template_content)