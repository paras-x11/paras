import os

os.chdir("C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task1\\")
print(os.curdir)

MACHINE_NAME = 'AIA_360'
result = []

with open ('sample.txt', 'r') as f:
    data = f.read()
# print(data)
# print(type(data))

lines = data.strip().split("SampleID=")
# print(lines)

# for l in lines:
#     print(l)

unique_pairs = []

for line in lines:
    
    if line == "":
        # print("flag")
        continue
    
    parts = line.strip().split(",")
    
    # print("\nParts: ", parts)
    
    try:
        Sample_ID = parts[1].strip()
        # print(Sample_ID)
        Analyte = parts[3].strip().replace('#', '')
        # print(Analyte)
        Conc = parts[5].strip()
        # print(Conc)
        
        pair = (Sample_ID, Analyte)
        # print(unique_pairs)
        
        if pair not in unique_pairs:
            unique_pairs.append(pair)
            # print(pair)
            
            tup = (MACHINE_NAME, Sample_ID, f"{{'{Analyte}' : '{Conc}'}}")
            result.append(tup)
    except IndexError:
        print("index out of range")


for r in result:
    print(r)
    
    
    
    
expected = ('AIA_360', 'TINU', "{'FT3' : '1.02','FT2' : '1.2'}")