import subprocess

argv = [
    ["6af2f708-b3cc-4b94-a192-5205a92c4390", "654465484165465847", "+8801256987425"],
    ["f3872c19-ef22-4be2-9afe-855ce068a304", "123456789", "+8801717018376"],
    ["68c9ba70-bf65-4aaa-86f7-b827bc0607f8", "65465465846584687",	"5446685465846584"],
    ["91d5f3cc-6002-4591-aa3a-2f16fae03144", "4654654",	"5464654"]
]

i = 0
while i < len(argv):
    process = subprocess.Popen(
        ["python", "device.py", argv[i][0], argv[i][1], argv[i][2]]
    )
    try:
        print("Simulating Device ", i, "in PID ", process.pid)
        process.wait(timeout=3)
    except subprocess.TimeoutExpired:
        print("Timed out - killing PID", process.pid)
        process.kill()
    i = i + 1
    