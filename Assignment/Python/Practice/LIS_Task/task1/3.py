import os
os.chdir("C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task1\\")

MACHINE_NAME = 'AIA_360'

result = []
unique_tests = dict()

# with open ('sample.txt', 'r') as f:
#     data = f.read()

data = """
    SampleID=, SAKSHI          , Analyte=, #TSH , Conc=, 1.353, Unit=, uIU/ml    , Position=, 1, TestNumber=, 1, Rate=, 2.673996, Flag=,   ,Date=, 10/07/25 17:24

  SampleID=, TINU1            , Analyte=, #FT3 , Conc=, 1.0, Unit=, pg/ml     , Position=, 2, TestNumber=, 1, Rate=, 40.031321, Flag=, CV,Date=, 10/07/25 17:25
 
SampleID=, TINU1            , Analyte=, #TSH , Conc=, 1.02, Unit=, pg/ml     , Position=, 2, TestNumber=, 1, Rate=, 40.031321, Flag=, CV,Date=, 10/07/25 17:25
 

"""

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
        
        # test_pair = {Sample_ID: (Analyte, Conc)}
        # print("\n\ntp", test_pair)
        
        if Sample_ID not in unique_tests:
            unique_tests[Sample_ID] = {} 
            print("\nin condition checking=" , unique_tests) 
            
        unique_tests[Sample_ID][Analyte] = Conc
        print("Analyte, conc: ",Analyte, Conc)
        print("\nafter checking assining val=", unique_tests)
        print("unique_tests[Sample_ID]=", unique_tests[Sample_ID])
        print("unique_tests[Sample_ID][Analyte]=", unique_tests[Sample_ID][Analyte])
            
    except IndexError:
        print("index out of range")


for id, test in unique_tests.items():
    tup = (MACHINE_NAME, id, f"{test}")
    result.append(tup)
    
    
print("\n\n\n\nResult: ")

for r in result:
    print(r)







# for sample_id, tests in unique_tests.items():
#     print(f"{sample_id}: {tests}")
    

   
expected = ('AIA_360', 'TINU', "{'FT3' : '1.02','FT2' : '1.2'}")