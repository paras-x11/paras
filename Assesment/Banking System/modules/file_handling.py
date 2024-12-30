class File_Handler():
    
    def log_transaction(self, log):
        with open("Transaction Log.txt", 'a') as f:
            f.write(f"{log} \n")
        print("Transaction logged successfully.")

    def read_log(self):
        with open("Transaction Log.txt", 'r') as f:
            log = f.read()
        print(log)           
 