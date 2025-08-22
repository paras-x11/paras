import json
import logging
import os
import re
import time
import uuid
import hashlib
import shutil
import mysql.connector
from mysql.connector import Error

os.chdir("C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task1\\")

my_host = '127.0.0.1'
my_user = 'root'
my_pass = 'root1'
my_db = 'lis'
folder_path = 'C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\scratch\\report_file'
backup_folder = 'C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\scratch\\backup_file'


def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
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
        return con if con.is_connected() else None
    except Exception:
        return None



def send_to_mysql(data_list):
    print("\n-> Data At starting: ", data_list)
    con = get_connection()
    if not con:
        print("Failed to connect to database")
        return False

    try:
        cur = con.cursor()

        for data in data_list:
            machinename, patientid, test_json = data

            try:
                incoming_tests = json.loads(test_json.replace("'", '"'))
            except Exception as e:
                print(f"❌ Invalid JSON for patient {patientid}: {e}")
                continue

            # Step 1: Get existing test data for the same machine + patient
            cur.execute("""
                SELECT test FROM MACHINE_DATA 
                WHERE machinename = %s AND patientid = %s
                LIMIT 1
            """, (machinename, patientid))

            row = cur.fetchone()

            is_duplicate = False
            if row:
                try:
                    existing_tests = json.loads(row[0])
                    # Compare dictionaries
                    if existing_tests == incoming_tests:
                        is_duplicate = True
                        print(f"⏩ Skipped exact duplicate for {patientid}.")
                except Exception as e:
                    print(f"⚠️ Error parsing existing JSON: {e}")

            if not is_duplicate:
                normalized_json = json.dumps(incoming_tests, separators=(',', ':'))  # compact & consistent
                cur.execute("""
                    INSERT INTO MACHINE_DATA (machinename, patientid, test) 
                    VALUES (%s, %s, %s)
                """, (machinename, patientid, normalized_json))
                print(f"✅ Inserted new patient {patientid}.")

        con.commit()
        cur.close()
    except Exception as e:
        import traceback
        print("❌ Error during insert:\n", traceback.format_exc())
        return False
    finally:
        con.close()
    return True




def au_480(data):
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


def bc_5150(data):
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


def process_all_files(folder_path):
    try:
        final_results = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            text_data = read_file(file_path)
            if not text_data:
                continue

            extractors = {
                'au_480': au_480,
                'bc_5150': bc_5150,
            }

            extractor = next(
                (ext for prefix, ext in extractors.items() if filename.startswith(prefix)), None)

            if extractor:
                results = extractor(text_data)
                if isinstance(results, list):
                    for result in results:
                        if send_to_mysql([result]):
                            try:
                                backup_path = os.path.join(
                                    backup_folder, filename)
                                shutil.copy(file_path, backup_path)
                                os.remove(file_path)
                                file_path = None
                            except Exception as e:
                                print(f"❌ Error during backup/delete: {e}")
                        final_results.append(result)
                else:
                    try:
                        backup_path = os.path.join(backup_folder, filename)
                        shutil.copy(file_path, backup_path)
                        os.remove(file_path)
                        file_path = None
                    except Exception as e:
                        print(f"❌ Error during backup/delete: {e}")
            else:
                try:
                    backup_path = os.path.join(backup_folder, filename)
                    shutil.copy(file_path, backup_path)
                    os.remove(file_path)
                    file_path = None
                except Exception as e:
                    print(f"❌ Error during backup/delete: {e}")
        return final_results
    except Exception as e:
        print(f"Exception Occurred :- {e}")


while True:
    all_results = process_all_files(folder_path)
    for result in all_results:
        print(f"Data Inserted :- {result}")
    time.sleep(2)
