import subprocess

def get_input(day, year, *file):
    # session cookie should be retrived from inspect element -> application -> cookies -> session
    SESSION = '53616c7465645f5f944dff9a9977a891904475dc2dcb0f28abe5c60bd12df2fb5429930cd77abef1ddcc855fdc7554ddc0a877be843f6a1101d3f87bf5fa5e0c'
    useragent = 'https://github.com/dhavalpandey/AdventofCode2024/blob/master/get_input.py by dhavalpandey2007@outlook.com'
    cmd = f'curl https://adventofcode.com/{year}/day/{day}/input --cookie "session={SESSION}" -A \'{useragent}\''
    output = subprocess.check_output(cmd, shell=True)
    output = output.decode('utf-8')
    if file:
        with open(file[0], 'w') as f:
            f.write(output)
    else:
        print(output, end='')