import os
os.chdir("C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task1\\")

MACHINE_NAME = 'AIA_360'
result = []
unique_pairs = []
unique_tests = dict()

with open ('sample.txt', 'r') as f:
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
        
        pair = (Sample_ID, Analyte)
        
        test_pair = {Sample_ID: (Analyte, Conc)}
        print("\n\ntp1", test_pair)
        unique_tests.update(test_pair)
        
        
        if pair not in unique_pairs:
            unique_pairs.append(pair)
            
            for test_pair in unique_tests.items():
                unique_tests
                tup = (MACHINE_NAME, Sample_ID, f"{{'{Analyte}' : '{Conc}'}}")
                result.append(tup)
            
            # tup = (MACHINE_NAME, Sample_ID, f"{{'{Analyte}' : '{Conc}'}}")
            # result.append(tup)
            
    except IndexError:
        print("index out of range")


for r in result:
    print(r)
    
    
    
    
expected = ('AIA_360', 'TINU', "{'FT3' : '1.02','FT2' : '1.2'}")