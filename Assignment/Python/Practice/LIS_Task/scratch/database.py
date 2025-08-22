import os
import mysql.connector
import json
import time

os.chdir(".\\scratch\\")

print(os.getcwd())

my_host = "localhost"
my_port = 3306
my_user = "root"
my_password = "root1"
my_database = "lis"

folder_path = "D:\\paras\\Assignment\\Python\\Practice\\LIS_Task\\scratch\\report_file\\"

def get_connection():
    try:
        con = mysql.connector.connect(
            host = my_host,
            port = my_port,
            user = my_user,
            password = my_password,
            database = my_database
        )
        if con.is_connected():
            return con
        else:
            return False
    except Exception as e:
        return False
    
def close_cursor(cur):
    try:
        if cur:
            cur.close()
            return True
    except Exception as e:
        return False
    
def close_connection(con):
    try:
        if con:
            con.close()
            return True
    except Exception as e:
        return False

def run_query(con, prepared_sql, data_tpl):
    try:
        with con.cursor() as cur:
            cur.execute(prepared_sql, data_tpl)
            con.commit()
            return cur
    except Exception as e:
        return False
    
def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        return e
    
def extract_data_from_au_480(data):
    MACHINE_NAME = 'AU_480'
    result = []

    astm_symbols = ['\x02', '\x03', '\x04', '\x05', '\x06', '\x15', '\x17']
    for sym in astm_symbols:
        data = data.replace(sym, '')

    data_blocks = data.strip().split('D ')

    for block in data_blocks:
        lines = block.strip().split()

        if len(lines) < 3:
            continue

        patient_id = lines[2]
        patient_dict = {patient_id: {}}

        for i in range(4, len(lines), 2):
            key = lines[i]
            val = lines[i+1]
            patient_dict[patient_id][key] = val

        for id, tests in patient_dict.items():
            tup = (MACHINE_NAME, id, f"{tests}")
            result.append(tup)
    return result


def extract_data_from_bc_5150(data):
    MACHINE_NAME = 'BC_5150'
    patients = []
    unique_patient_id = set()

    control_chars = ['\x02', '\x03', '\x04', '\x05',
                     '\x06', '\x15', '\x17', '\x1c', '\x0b']
    for sym in control_chars:
        data = data.replace(sym, '')

    data_blocks = data.strip().split('MSH')

    for block in data_blocks:
        block = block.strip()
        if not block:
            continue

        lines = block.split('\n')
        patient_id = None
        patient_dict = {}

        for line in lines:
            segments = line.strip().split('|')

            if line.startswith("OBR"):
                patient_id = segments[3]
                if patient_id not in patient_dict:
                    patient_dict[patient_id] = {}

            if line.startswith("OBX") and patient_id:
                if len(segments) >= 6:
                    test_info = segments[3].split('^')
                    if len(test_info) >= 2:
                        test_name = test_info[1]
                        test_value = segments[5]
                        patient_dict[patient_id][test_name] = test_value

        if patient_id and patient_id not in unique_patient_id:
            tup = (MACHINE_NAME, patient_id, str(patient_dict[patient_id]))
            patients.append(tup)
            unique_patient_id.add(patient_id)

    return patients


def extract_data_from_cell_counter(data):
    MACHINE_NAME = 'CELL_COUNTER'
    patients = []
    unique_patient_id = set()  


    control_chars = ['\x02', '\x03', '\x04', '\x05', '\x06', '\x15', '\x17', '\x1c', '\x0b']
    for sym in control_chars:
        data = data.replace(sym, '')

    lines = data.strip().split('\n')
    patient_id = None
    patient_dict = {}

    for line in lines:
        line = line.strip()
        if not line:
            continue

        segments = line.split('|')

        # print("\n->segmentes:", segments)

        if line.startswith('P'):
            patient_id = segments[4] if len(segments) > 4 else None
            # print("\n->patient_id: ", patient_id)
            if patient_id and patient_id not in patient_dict:
                patient_dict[patient_id] = {}

        if line.startswith('R') and patient_id:
            test_name = segments[2].strip('^') 
            test_value = segments[3]

            # print("\n-> test_name" , test_name)
            # print("-> test_values" , test_value)

            if test_value.startswith('Qk'):
                continue

            patient_dict[patient_id][test_name] = test_value
            # print("\n->patient_dict: ", patient_dict)

    for pid, tests in patient_dict.items():
        if pid and pid not in unique_patient_id:
            tup = (MACHINE_NAME, pid, str(tests))
            # print("\n->tup: ", tup)
            patients.append(tup)
            unique_patient_id.add(pid)

    return patients



def process_all_files(folder_path):
    final_result = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        data = read_file(file_path)
        if not data:
            continue

        extractors={
            'au_480' : extract_data_from_au_480,
            'bk_5150' : extract_data_from_bc_5150,
            'cell_counter' : extract_data_from_cell_counter,
        }

        for prefix, ext in extractors.items():
            if file_path.startswith(prefix):
                extractors = ext

                
    return final_result

while True:
    all_results = process_all_files(folder_path)
    # for result in all_results:
    #     print("|N-> Data Inserted: ", result)
    time.sleep(2)