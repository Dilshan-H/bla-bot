# Data Formatting & Encrypting

This file contains the information about the data formatting and encrypting process.

## Contents
- [Standard Data Format](#standard-data-format)
    - [Results - `results.csv`](#results---resultscsv)
    - [Staff Info - `staff_info.txt`](#full-batch-data---full_batch_datacsv)
    - [Batch Data - `full_batch_data.csv`](#full-batch-data---full_batch_datacsv)
    - [General Resources - `resources.txt`](#general-resources---resourcestxt)

- [File Encryption](#file-encryption)

---

## Standard Data Format
The functionality of the bot is based on the data stored in the `DATA` folder. The data is stored in the form of CSV and text files. And later, we have to encrypt them for security concerns (if your intention is to adding the bot to a private group, this is REQUIRED!).
You can find the templates of the CSV and text files in the `DATA/Templates` folder. You can use those templates to add your data.

### Results - `results.csv`
Contains the results of the students. The data is stored in the following format.
**S1, S2, S3, S4, S5, S6, S7, S8** are the semester results. **Y1, Y2, Y3, Y4** are the year results. **CGPA** and **OGPA** are the cumulative and overall GPAs respectively.  
**Errors** are about the missing/invalid information. This parameter can be either one of the following values. (You can also add your own error types using `gpa_values.py` if you want to.) 

- `ERROR` - The NIC/ID number is not registered in database.
- `HOLD` - The results are on hold. Only the partially calculated GPA values present.
- `NEW` - Calculated GPA values are based on student's current results within a batch; OGPA, CGPA and Academic Status will not represent accurate information. (Useful for a repeated/batch-missed student.)

| user_id | NIC_no     | s1    | s2   | s3   | s4 | s5 | s6 | s7 | s8 | Errors | Y1      | Y2 | Y3 | Y4 | cgpa   | ogpa |
| ------- | ---------- | ----- | ---- | ---- | -- | -- | -- | -- | -- | ------ | ------- | -- | -- | -- | ------ | ---- |
| 123451  | 1234567890 | 3.623 | 2.66 | 3.11 |    |    |    |    |    |        | 3.41231 |    |    |    | 3.1234 |      |

### Staff Info - `staff_info.txt`
STAFF info is stored in here.
Contact information that relates to a single person written as blocks. And, each bock is seperated with a newline (new empty line).
See examples given below.

```text
# ----- Begining of the file -----

Dr. A.B. John Doe
DEAN, FACULTY OF ABC
Office: 0123456789
Email: abc@uni.com

Mr. Alex White
HEAD, DEPARTMENT OF ABC
Office: 0123456789
Email: abc@uni.com, abc@alex.com

Ms. Jane Doe
Assistant Registrar - Faculty of ABC
Direct Line: 0123456789
Office: 0123456789
Extension: 1234
Email: abc@uni.com
Fax: 0123456789

# ----- End of the file -----

```

### Batch Data - `full_batch_data.csv`

| Uni_reg_no | Name_with_initials | BDay       | Uni_email       | Email            | Postal_address       | District | Contact_no | Errors            | Short_name |
| ---------- | ------------------ | ---------- | --------------- | ---------------- | -------------------- | -------- | ---------- | ----------------- | ---------- |
| 123456     | A.B.C. Jane Doe    | 1985-01-01 | janedoe@uni.com | janedoe@jane.com | 123/A, ABC Road, ABC | ABCD     | 123456789  |                   | Jane       |
| 1234562    | A.B.C. John Doe    | 1985-01-01 | johndoe@uni.com | johndoe@jane.com | 123/A, ABC Road, ABC | ABCD     | 123456789  | Invalid ID number | John       |

### General Resources - `resources.txt`

| keywords                               | title                                                 | data                                                                                       |
| -------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| keyword1, keyword2 | This text contains the title of the resource content. | Here goes the description or the URL - [https://examplesite.com](https://examplesite.com/) |



## File Encryption
The bot will use the encrypted files to fetch the data.
After you have added the data to the CSV and text files according to above formats, you have to encrypt them using the `encrypt_data.py` file.

**NOTE**: You have to run the `encrypt_data.py` file from the `DATA` folder for that. If you are not in the `DATA` folder, you can use the following command to change the directory.

```bash
cd DATA
```

Then, run the `encrypt_data.py` file using the following command.

On Poetry shell:
```bash
poetry run python3 encrypt_data.py
```

On Linux shell:
```bash
python3 encrypt_data.py
```
On Windows CMD prompt:
```bash
py encrypt_data.py
```

**IMPORTANT**:
- The **key** will be saved in the current folder with name format `KEY_date_time.txt`. Open the key file and copy the key. Use that key while configuring the environment variables.
- **DO NOT run this file again, if you are updating the existing data.** It will generate a new key and you have to update the environment variables again. Instead, you can use the same key to encrypt the updated data files. Open the key file and copy the key. Uncomment the `key` variable in the `encrypt_data.py` file and paste the key there. Then, run the `encrypt_data.py` file again.
- **DO NOT** share the **key file** or **csv/txt** files with anyone or commit it to a public repository (these files are already added to `.gitignore` file. So, you don't have to worry about it).
- [Optional] Delete the original data files after encryption. (**Make backups somewhere else first!** and then delete the files that having the `.csv` and `.txt` extensions.)