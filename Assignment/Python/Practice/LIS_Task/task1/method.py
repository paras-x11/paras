import os
os.chdir("C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task1\\")

MACHINE_NAME = 'AIA_360'

def process_file(file_path):
    
    result = []
    unique_tests = dict()

    with open (file_path, 'r') as f:
        data = f.read()

    lines = data.strip().split("SampleID=")


    for line in lines:
        
        if line == "":
            continue
        
        parts = line.strip().split(",")
        
        try:
            Sample_ID = parts[1].strip()
            Analyte = parts[3].strip().replace('#', '')
            Conc = parts[5].strip()
            
            if Sample_ID not in unique_tests:
                unique_tests[Sample_ID] = {} 
                
            unique_tests[Sample_ID][Analyte] = Conc
                
        except IndexError:
            print("index out of range")


    for id, test in unique_tests.items():
        tup = (MACHINE_NAME, id, f"{test}")
        result.append(tup)
        
    return result

path="C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task1\\sample.txt"

output = process_file(path)

for op in output:
    print(op)




        