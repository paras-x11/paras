import os
os.chdir(".")

# print(os.getcwd())

MACHINE_NAME = 'AIA_480'

result = []
patient_dict = {}

with open('sample.txt', 'r') as f:
    data = f.read()

lines = data.strip().split("SampleID=,")

for line in lines:
    if line == "":
        continue

    parts = line.split(",")

    patient_id = parts[0].strip()
    test = parts[2].strip().replace('#', "")
    test_value = parts[4].strip()

    if patient_id not in patient_dict:
        patient_dict[patient_id] = {}

    patient_dict[patient_id][test] = test_value


for key, val in patient_dict.items():
    # print(key, val)
    tup = (MACHINE_NAME, key, f'{val}')
    result.append(tup)

for r in result:
    print(r)










op =[
    ('AIA_360', 'SAKSHI', "{'TSH': '1.353'}"), 
    ('AIA_360', 'TINU', "{'FT3': '1.02'}")
]