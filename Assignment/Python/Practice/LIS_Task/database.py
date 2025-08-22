import os
import mysql.connector
import json
import datetime

os.chdir("C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task1\\")

my_host = '127.0.0.1'
my_user = 'root'
my_pass = 'root1'
my_db = 'lis'

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            return data
    except Exception as e:
        return None

def get_connection():
    try:
        con = mysql.connector.connect(
            host = my_host,
            user = my_user,
            password = my_pass,
            database = my_db
        )
        if con.is_connected():
            return con
        return None
    except Exception as e:
        return None


# def send_data_to_mysql(data_list):
#     print("\n-> Data At starting: ", data_list)
#     con = get_connection()
#     if not con:
#         print("Failed to connect to database")
#         return False

#     prepared_sql = 'INSERT INTO MACHINE_DATA (machinename, patientid, test) VALUES (%s, %s, %s)'

#     try:
#         for data in data_list:
#             json_report_data = json.dumps(data[2] or {})
#             print("Inserting:", data[0], data[1], json_report_data)
#             cur = con.cursor()
#             cur.execute(prepared_sql, (data[0], data[1], json_report_data))
#         con.commit()
#         print("Rows affected:", cur.rowcount)
#         cur.close()
#     except Exception as e:
#         print("Error during insert:", e)
#         return False
#     finally:
#         con.close()
#     return True

def send_data_to_mysql(data_list):
    print("\n-> Data At starting: ", data_list)
    con = get_connection()
    if not con:
        print("Failed to connect to database")
        return False

    try:
        cur = con.cursor()

        for data in data_list:
            machinename, patientid, new_test_json = data
            new_tests = json.loads(new_test_json.replace("'", '"'))

            # Step 1: Check if patient already exists
            cur.execute(
                "SELECT test FROM MACHINE_DATA WHERE machinename = %s AND patientid = %s",
                (machinename, patientid)
            )
            row = cur.fetchone()

            if row:
                # Existing entry found, merge test results
                try:
                    existing_tests = json.loads(row[0])
                except json.JSONDecodeError:
                    try:
                        existing_tests = json.loads(row[0].replace("'", '"'))  # fallback
                    except:
                        existing_tests = {}

                existing_tests.update(new_tests)

                # Update row
                merged_tests_json = json.dumps(existing_tests)
                cur.execute(
                    "UPDATE MACHINE_DATA SET test = %s WHERE machinename = %s AND patientid = %s",
                    (merged_tests_json, machinename, patientid)
                )
                print(f"Updated {patientid} with new test data.")
            else:
                # Insert new row
                json_test_data = json.dumps(new_tests)
                cur.execute(
                    "INSERT INTO MACHINE_DATA (machinename, patientid, test) VALUES (%s, %s, %s)",
                    (machinename, patientid, json_test_data)
                )
                print(f"Inserted new patient {patientid}.")

        con.commit()
        cur.close()
    except Exception as e:
        import traceback
        print("❌ Error during insert/update:\n", traceback.format_exc())
        return False

    finally:
        con.close()
    return True



# ASTM Protocol
def au_480(file_path):

    MACHINE_NAME = 'AU_480'
    result = []

    data = read_file(file_path)

    astm_symbols = ['\x02',  '\x03',  '\x04',  '\x05',  '\x06',  '\x15',  '\x17']

    for sym in astm_symbols:
        data = data.replace(sym, '')
    # print("\n->Data: ", type(data), " \n", data)


    data_blocks = data.strip().split('D ')
    # print("\n->Data Blocks: ", type(data_blocks), " \n", data_blocks)

    for block in data_blocks:
        lines = block.strip().split()
        # print("\n->Lines: ", type(lines), "\n", lines)

        if len(lines) < 3:
            # print("\n->Skipping invalid block: ", type(data_blocks), " \n", lines)
            continue

        patient_id = lines[2]
        # print("\n->Patient ID:", patient_id)

        patient_dict = {patient_id : {}}

        for i in range(4, len(lines), 2):
            key = lines[i]
            val = lines[i+1]

            patient_dict[patient_id][key] = val

        # print("\n-> patient_dict: ", patient_dict)

        for id, tests in patient_dict.items():
            tup = (MACHINE_NAME, id, f"{tests}")
            result.append(tup)
    return result

au_480_path = "C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task2\\au_480.txt"
au_480_output = au_480(au_480_path)

# print("\n\n-> FINAL au_480 OUTPUT: ")
# for op in au_480_output:
#     print(op)

# ============================================================================================================================================================================================================== #
# ============================================================================================================================================================================================================== #

# HL7 Protocol contains: OBX , OBR etc
def bc_5150(file_path):
    MACHINE_NAME = 'BC_5150'
    patients = []
    unique_patient_id = set()  

    data = read_file(file_path)

    control_chars = ['\x02', '\x03', '\x04', '\x05', '\x06', '\x15', '\x17', '\x1c', '\x0b']
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
                    # print("=====>Test Info:   ", test_info)
                    if len(test_info) >= 2:
                        test_name = test_info[1]
                        test_value = segments[5]

                        patient_dict[patient_id][test_name] = test_value

        if patient_id and patient_id not in unique_patient_id:
            tup = (MACHINE_NAME, patient_id, str(patient_dict[patient_id]))
            # print("\n->tup: ", tup)
            patients.append(tup)
            unique_patient_id.add(patient_id)

    return patients


bc_5150_path = "C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task2\\bc_5150.txt"
bc_5150_output = bc_5150(bc_5150_path)

# print("\n\n-> FINAL bc_5150 OUTPUT: ")
# for op in bc_5150_output:
#     print(op)


# ============================================================================================================================================================================================================== #
# ============================================================================================================================================================================================================== #

#ASTM protocol contains: HP OR , 1H, 2p etc.
def cell_counter(file_path):
    MACHINE_NAME = 'CELL_COUNTER'
    patients = []
    unique_patient_id = set()  

    data = read_file(file_path)

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

cell_counter_path = "C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task2\\cell_counter.txt"
cell_counter_output = cell_counter(cell_counter_path)

# print("\n\n-> FINAL cell_counter OUTPUT: ")
# for op in cell_counter_output:
#     print(op)

cell_counter_path2 = "C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task2\\cell_counter copy.txt"
cell_counter_output2 = cell_counter(cell_counter_path2)

# print("\n\n-> FINAL cell_counter2 OUTPUT: ")
# for op in cell_counter_output2:
#     print(op)


# ============================================================================================================================================================================================================== #
# ============================================================================================================================================================================================================== #

def fuji_film(file_path):
    MACHINE_NAME = 'FUJI_FILM'
    patient = []
    unique_patien_ids = set()

    data = read_file(file_path)

    astm_symbols = ['\x02',  '\x03',  '\x04',  '\x05',  '\x06',  '\x15',  '\x17']

    for sym in astm_symbols:
        data = data.replace(sym, '')
    # print("\n->Data: ", type(data), " \n", data)

    data_blocks = data.strip().split("R,")


    for block in data_blocks:
        lines = block.strip().split(",")
        # print("\n->lines: ", lines)

        if len(lines) < 3:
            # print("\n->Skipping invalid block: ", type(data_blocks), " \n", lines)
            continue

        patient_id = lines[4].strip()
        # print("\n->patient_id: ", f"|{patient_id}|")

        patient_dict = {patient_id : {}}

        for i in range(11, len(lines), 7):
            # print(f"\n->test_name{i}:", lines[i])
            # print(f"\n->test_value:", lines[i+2])

            test_name = lines[i].strip()
            test_value = lines[i+2].strip().split()[0]

            patient_dict[patient_id][test_name] = test_value


        if patient_id not in unique_patien_ids:
            for id, tests in patient_dict.items():
                tup = (MACHINE_NAME, id, f"{tests}")
                patient.append(tup)
            unique_patien_ids.add(patient_id)
    return patient


fuji_film_path = "C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task2\\fuji_film.txt"
fuji_film_output = fuji_film(fuji_film_path)

# print("\n\n-> FINAL fuji_film OUTPUT: ")
# for op in fuji_film_output:
#     print(op)


# ============================================================================================================================================================================================================== #
# ============================================================================================================================================================================================================== #

def snibe(file_path):
    MACHINE_NAME = 'CELL_COUNTER'
    patients = []
    unique_patient_ids = set()

    data = read_file(file_path)

    control_chars = ['\x02', '\x03', '\x04', '\x05', '\x06', '\x15', '\x17', '\x1c', '\x0b']
    for sym in control_chars:
        data = data.replace(sym, '')

    data_blocks = data.strip().split("MSH")

    for block in data_blocks:
        block = block.strip()
        if not block:
            continue

        lines = block.split("\n")
        # print("\n->lines", lines)
        patient_id = None
        patients_dict = {}

        for i, line in enumerate(lines):
            segment = line.strip().split("|")
            # print("==================> segment", segment)
            if line.startswith("SPM"):
                patient_id = segment[2].strip().split("^")[0]
                # print("==================> patient_id", patient_id)
                if patient_id not in patients_dict:
                    patients_dict[patient_id] = {}

            if line.startswith("OBX"):
                if len(segment) > 4:
                    test_name = segment[3].strip()
                    test_value = segment[5].strip().split("^")[0]
                    # print("==================> test name", test_name)
                    # print("==================> test value", test_value)

                    patients_dict[patient_id][test_name] = test_value

        if patient_id not in unique_patient_ids :
            tup = (MACHINE_NAME, patient_id, str(patients_dict[patient_id]))
            patients.append(tup)
            unique_patient_ids.add(patient_id)

    return patients


snibe_path = "C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task2\\snibe.txt"
snibe_output = snibe(snibe_path)


# Test the new function with snibe_output
# save_machine_patients_to_file('C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\output_folder', snibe_output)

# print("\n\n-> FINAL snibe OUTPUT: ")
# for op in snibe_output:
#     print(op)


# ============================================================================================================================================================================================================== #
# ============================================================================================================================================================================================================== #




folder_path = 'C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\output_folder'


result = send_data_to_mysql(snibe_output)
print(result)
