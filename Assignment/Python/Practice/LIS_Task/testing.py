# pip install mysql-connector-python

import json
import logging
import os
import re
import time
import uuid
import hashlib
import mysql.connector
from mysql.connector import Error

# Configuration
my_host = '127.0.0.1'
my_user = 'root'
my_pass = 'Root@1234'
my_db = 'lis'
folder_path = '/home/dhruveel/Desktop/Dhruveel/machine_integration_main_project/machine_integration_main_project/attachments'

# stored_license_key = "34ad7747ef4f423ca6234c0a6de73eedff591ea67235ae8e84486a90ae731b56"
#
#
# def get_mac_address():
#     mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
#     return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
#
#
# def generate_license_key(mac_address):
#     key = hashlib.sha256(mac_address.encode()).hexdigest()
#     return key
#
#
# def check_license(license_key, mac_address):
#     generated_key = generate_license_key(mac_address)
#     return generated_key == license_key
#
#
# # License check
# current_mac = get_mac_address()
# if not check_license(stored_license_key, current_mac):
#     print("Invalid license. This executable can only run on the registered system.")
#     logging.error("Invalid license. This executable can only run on the registered system.")
#     sys.exit(1)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return None

def get_connection():
    try:
        con = mysql.connector.connect(
            host=my_host,
            user=my_user,
            password=my_pass,
            database=my_db
        )
        if con.is_connected():
            return con
    except Error as e:
        return None

def run_query(con, prepared_sql, data_tpl):
    try:
        cur = con.cursor()
        cur.execute(prepared_sql, data_tpl)
        con.commit()
        msg = "Rows affected: {}".format(cur.rowcount)
        return cur
    except Exception as e:
        return None

def close_cursor(cur):
    try:
        cur.close()
    except Exception as e:
        pass

def close_connection(con):
    try:
        con.close()
    except Exception as e:
        pass

# Method for save data in mysql database
def send_to_mysql(data):
    con = get_connection()
    if not con:
        return False
    prepared_sql = 'INSERT INTO machineData (machineName, patientId, test) VALUES (%s, %s, %s)'
    try:
        json_report_data = json.dumps(data[2]) if data[2] else json.dumps({})
        cur = run_query(con, prepared_sql, (data[0], data[1], json_report_data))
        if cur:
            close_cursor(cur)
    except Exception as e:
        return False
    finally:
        close_connection(con)
    return True

# Method for Beckman Coulter Access 2 Machine
def extract_report_data_access_2(access_data):
    lines = access_data.strip().split('\x02')
    machine_name, patient_name, test_name, test_result = 'ACCESS', 'N/A', 'N/A', 'N/A'
    final_list = []
    for line in lines:
        if line.startswith('1H'):
            machine_name = line.split('|')[4]
        elif line.startswith('3O'):
            patient_name = line.split('|')[2]
        elif line.startswith('4R'):
            test_data = line.split('|')
            test_name = test_data[2].replace('^', '').rstrip('1')
            test_result = test_data[3].replace('>', '').replace('<', '')
    final_list.append((machine_name, patient_name, {test_name: test_result}))
    return final_list
    # return (machine_name, patient_name, {test_name: test_result})

# Method for Beckman Coulter AU 480 Machine
def extract_report_data_au_480(au_data):
    machine_name, patient_name = "AU_480", "N/A"
    final_list = []
    sub_data = au_data.strip().split()
    if len(sub_data) > 3:
        patient_name = sub_data[3]
    
    pattern = r'(\d{3})\s+(\d+\.\d+)'
    matches = re.findall(pattern, au_data)
    result = {key: value for key, value in matches}
    
    final_list.append((machine_name, patient_name, result))
    return final_list
    # return (machine_name, patient_name, result)

# Method for Cobas E 411 Machine
def extract_report_data_e_411(hl7_message):
    machine_id = 'e_411'
    final_list = []
    patient_id_match = re.search(r'3O\|1\|([^|]+)', hl7_message)
    patient_id = patient_id_match.group(1) if patient_id_match else None
    results = re.findall(r'R\|\d+\|\^\^\^(\d+)\^\^[^\|]+\|([^\|]+)', hl7_message)
    formatted_results = {result[0]: result[1] for result in results}
    converted_results = convert_values(formatted_results)
    final_list.append((machine_id, patient_id, converted_results))
    return final_list
    # return (machine_id, patient_id, converted_results)

# Method for remove -1 and 1 for Cobas E 411
def convert_values(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        # Handle values with '-1^' or '1^'
        if '-1^' in value:
            value = value.replace('-1^', '')
        elif '1^' in value:
            value = value.replace('1^', '')
        output_dict[key] = value
    return output_dict

# Method for Cobas C 111 Machine
def extract_report_data_c_111(data):
    # Use fixed 'c111' value
    c111 = 'c111'
    lines = data.split("\n")
    pid = ''
    final_list = []
    
    for line in lines:
        if line.__contains__('3O'):
            pid = re.sub(r'\^\d', '', line.split("|")[3]).replace("^","")
            # pid_field = line.split("|")[3]
            # pid = re.sub(r'\^\d+', '', pid_field).replace("^", "")
            
    # Extract results in the desired format
    result_pattern = re.compile(r"(\d)R\|\d\|\^\^\^(\d+)\|([\d.]+)\|[^|]*")
    results = result_pattern.findall(data)

    results_dict = {code: value for _, code, value in results}
    final_list.append((c111, pid, results_dict))
    return final_list
    # return (c111, pid, results_dict)

# Method for Cobas C 311 Machine
def extract_report_data_c_311(data):
    c311 = 'c311'
    lines = data.split("\n")
    pid_field = None  # Initialize with a default value
    final_list = []
    result_dict = {}
    formatted_lines = []
    buffer = ""

    for line in lines:
        line = line.strip()
        if line.startswith(("R|", "O|", "P|", "L|", "C|")):
            if buffer:  
                formatted_lines.append(buffer)
                buffer = ""
            buffer = line 
        else:
            buffer += line
    if buffer:
        formatted_lines.append(buffer)
        
    for line in formatted_lines:
        if line.__contains__('O'):
            pid_field = line.split("|")[2].split('-')[0].strip()
        elif line.startswith('R'):
            parts = line.split('|')
            if len(parts) >= 4:
                test_id = parts[2].replace('^', ' ').replace('/', ' ').strip()
                if '\x02' in test_id:
                    test_id = test_id.split('\x02')[1]
                test_value = parts[3]
                result_dict[test_id] = test_value

    if pid_field:
        final_list.append((c311, pid_field, result_dict))
    return final_list

# Method for Sysmex Machine
def extract_common_report_data_for_sysmex(text):
    lines = text.split('\n')
    formatted_data = []

    obx_data = ""
    for line in lines:
        # Check if line starts with "R", indicating a new OBX segment
        if line.startswith("R"):
            if obx_data:
                formatted_data.append(obx_data.strip())
            obx_data = line  # Initialize with the current line
        elif obx_data and line.strip():
            # Join the current line to the OBX data, ensuring proper spacing
            obx_data += "|" + line.strip()
        else:
            if obx_data:
                # Append the final OBX data segment
                formatted_data.append(obx_data.strip())
                obx_data = ""
            # Append non-OBX lines directly to the formatted dataw
            formatted_data.append(line)

    # Append any remaining OBX data
    if obx_data:
        formatted_data.append(obx_data.strip())
    
    if formatted_data:
        machine_name = 'sysmex'
        patients = []  # Store multiple patient records
        patient_name = None
        report_data = {}

        for line in formatted_data:
            if line.startswith('O'):
                if patient_name and report_data:
                    patients.append((machine_name, patient_name, report_data))
                    report_data = {}

                patient_name = line.split('|')[3].replace('^M', '').replace('^F', '').replace('^', '').strip()
            elif line.startswith('R'):
                if len(line.split('|')) > 3:
                    field_name = line.split('|')[2].replace('^1', '').replace('^', '')
                    value = line.split('|')[3].strip()
                    report_data[field_name] = value

        # Append the last patient's data after the loop
        if patient_name and report_data:
            patients.append((machine_name, patient_name, report_data))

        return patients

# Method for XN 350 Machine
def extract_report_data_xn_350(text):
    return extract_common_report_data_for_sysmex(text, 'XN-350')

# Method for XN 550 Machine
def extract_report_data_xn_550(text):
    return extract_common_report_data_for_sysmex(text, 'XN_550')

# Method for XN 330 Machine
def extract_report_data_xn_330(text):
    return extract_common_report_data_for_sysmex(text, 'XN-330')

# Method for XP 100 Machine
def extract_report_data_xp_100(text):
    return extract_common_report_data_for_sysmex(text, 'XP-100')

# Method for XP 100 Machine
def extract_report_data_xn_1000(text):
    return extract_common_report_data_for_sysmex(text, 'XP-1000')

# Method for CELL TAK @+ Mek 6500 Machine
def remove_starting_chars(data):
    return [re.sub(r'^\x05|\x03|\x02', '', item) for item in data]

# Method for process all file in given folder
def process_all_files(folder_path):
    try:
        final_results = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            text_data = read_file(file_path)
            if not text_data:
                continue
            extractors = {
                'xn_330_': extract_report_data_xn_330,
                'xp_100_': extract_report_data_xp_100,
                'xn_350_': extract_report_data_xn_350,
                'xn_550_': extract_report_data_xn_550,
                'xn_1000_': extract_report_data_xn_1000,
                'e_411_': extract_report_data_e_411,
                'c_111_': extract_report_data_c_111,
                'c_311_': extract_report_data_c_311,
                'access_2_': extract_report_data_access_2,
                'au_480_': extract_report_data_au_480,
                
            }
            extractor = next((ext for prefix, ext in extractors.items() if filename.startswith(prefix)), None)
            if extractor:
                results = extractor(text_data)
                if isinstance(results, list):
                    for result in results:
                        if send_to_mysql(result):
                            try:
                                # os.remove(file_path)
                                # file_path = None
                                pass
                            except Exception as e:
                                pass
                        final_results.append(result)
                else:
                    try:
                        if file_path:
                            # os.remove(file_path)
                            # file_path = None
                            pass
                    except Exception as e:
                        pass
            else:
                try:
                    if file_path:
                        # os.remove(file_path)
                        # file_path = None
                        pass
                except Exception as e:
                    pass
        return final_results
    except Exception as e:
        print(f"Exception Occur :- {e}")

while True:
    all_results = process_all_files(folder_path)
    for result in all_results:
        print(f"Data Inserted :- {result}")
    time.sleep(2)