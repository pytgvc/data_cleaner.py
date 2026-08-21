
import pandas as pd
import numpy as np
#load file
def load_file():
    filename = input("Enter filename to load:").strip() # extra space remove

    try:
        if filename.endswith(".csv"):
            df = pd.read_csv(filename)
        elif filename.endswith(".xlsx"):
            df = pd.read_excel(filename)
        elif filename.endswith(".txt"):
            df= pd.read_csv(filename) 
        else:
            print("❌ Wrong format!")
            return None
        print("✅ File loaded!")
        return df
    
    except FileNotFoundError:
        print("❌ File not found!")
        return None

    except Exception as e:
        print(f"👎 Error: {e}")
        return None
 # show files info
def show_file_info(df) :
    print ("=" * 60)
    print ("📊 DATA LOADED")
    print ("=" * 60)
    rows = df.shape[0]   # shape[0] Rows shape[1] COLUMNS
    cols = df.shape[1]   #store the total number of rows , columns in the dataframe into variable rows
    missing = df.isnull().sum().sum() # for a single column "two values are not missing and one value is missng"
    duplicates = df.duplicated().sum()
    print("Total Rows:",rows)
    print("Total Columns:",cols)
    print("Missing Values:",missing)
    print("Duplicate Rows:",duplicates)
   
    print("\n📑 Column and Types:")
    for col in df.columns:
       print("-",col,"(",df[col].dtype,")") # used to print every column name and its data type
    print("\n⏮️ Preview (first 10 rows):")  
    print (df.head(10))
# show menu
def show_menu():
     print ("=" * 60)
     print ("🧹CLEANING OPIONS")
     print ("=" * 60)
     print("1.  Remove rows with missing values")
     print("2.  fill missing with mean (numeric columns)")
     print("3.  Fill missing with 'Unknown(text coloumns)")
     print("4.  Remove  duplicate rows ")
     print("5.  Remove special Characters (text)")
     print("6.  Convert data types")
     print("7.  Show cleaned data")
     print("8.  Show report(Before vs After)")
     print("9.  Save and Exist")
     print("10. Cancel")
     print ("=" * 60)
     choice = input("Enter your choice(1-10):")
     return choice
# remove missing rows
def remove_missing_rows(df):
    rows_before = df.shape[0]
    missing = df.isnull().sum().sum()
    if missing == 0:
        print("No missing value to remove!")
    df = df.dropna()
    rows_after= df.shape[0]
    removed=rows_before - rows_after
    print(f"✅ Removed { removed} rows with missing values")
    return df
# fill missing with mean 
def fill_missing_mean(df):
    numeric_columns=df.select_dtypes(include=['number']).columns #select only that columns jinka data type number int float hai
    if len(numeric_columns) == 0:
        print(" No numeric columns found")
        return df
    for col in numeric_columns:
        missing = df[col].isnull().sum()
    if missing > 0:
        mean_value = df[col] .mean()
        df[col].fillna(mean_value,inplace=True)
        print("👊{col} filled with mean,{mean_value}")
    return df
#fill missing text
def fill_missing_text(df):
    text_columns= df.select_dtypes(include=['object']).columns
    if len (text_columns )== 0 :
        print("No  text columns found")
        return df 
    for col in text_columns:
        missing = df[col].isnull().sum()
        if missing > 0 :
          df[col].df.fillna("unknown", inplace=True)
          print( f"✅{col} filled with 'unknown' ")
    return df
 
# remove duplicates
def remove_duplicates(df):
    duplicates_before  = df.duplicated().sum()
    if duplicates_before == 0:
        print("No duplicates rows found")
        return df 
    df = df.drop_duplicates (keep="first")
    duplicates_after  = df.duplicated().sum()
    removed=duplicates_before - duplicates_after
    print(f"👉 Removed{removed} duplicate rows")
    return df
# clean special chars
def clean_special_chars(df):
    print("\n🧹 Clean Special Characters")
    choice = input("Do you want to clean ALL text columns (yes/no)? ").strip().lower()
    if choice == "yes":
        # Select all object (text) columns
        selected_cols = df.select_dtypes(include="object").columns.tolist()#turning data into python list
    else:
        col_name = input("Enter column name to clean: ").strip()
        if col_name not in df.columns:
            print(f"❌ Column '{col_name}' not found in DataFrame!")
            return df
        selected_cols = [col_name]
    # kabhi matt dikh jana
    for col in selected_cols:
        df[col] = df[col].astype(str)  # convert to string to avoid NaN issues
        df[col] = df[col].str.strip()  # remove leading/trailing whitespace
        df[col] = df[col].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)  # keep only letters, numbers, spaces
    
    print(f"✅ Cleaned special characters from columns: {', '.join(selected_cols)}") #','.join(selected_cols) python trick to turn a list of column into nice
    return df
# convert datatypes
def convert_data_types(df):
    print("converting data types")
    col_name = input("Enter column name: ").strip()
    target_type = input("Enter target type (int/float/string/datetime): ").strip().lower()

    if col_name not in df.columns:
        print(f"❌ Column '{col_name}' not found in DataFrame!")
        return df
    
    try:
        if target_type =="datetime":
           df[col_name] = pd.to_datetime(df[col_name]) # convert using  pd.to_datetime()
        elif target_type == "int":
            df[col_name] = df[col_name].astype(int)
        elif target_type == "float":
            df[col_name] = df[col_name].astype(float)
        elif target_type == "string":
            df[col_name] = df[col_name].astype(str)
        else:
            print(f" unknown target type :{target_type}") # f-string
            return df 
        print(f"column ' {col_name}' converted to {target_type}")
    except Exception as e:
        print(f"could not convert column ' {col_name}'- Invalid or mismatch: {e}" )
        return df 
# show_cleaned_data
def show_cleaned_data(df):
 print(" CLEANED DATA PREVIEW")
 print(df.head())
 print(f"shape:{df.shape[0]} rows, {df.shape[1]},columns") # for rows=0 and columns = 1

 # show report original vs cleaned df
def show_report(original_df , cleaned_df):
    print(" SHOW REPORTS")
    rows_before = original_df.shape[0]
    rows_after =  cleaned_df.shape[0]
    print(f"rows before:{rows_before}, rows after:{rows_after}")
    missing_before = original_df.isnull().sum().sum()
    missing_after = cleaned_df.isnull().sum().sum()
    print(f"missing before:{missing_before}, missing after:{missing_after}")
   
    print(f" rows removed(duplicate):{rows_before - rows_after}")
    print("column dtypes changes")
    for col in original_df.columns:
        if col in cleaned_df.columns:
            old_type = original_df[col].dtype 
            new_type = cleaned_df[col].dtype  
        if old_type!=new_type:
            print(f"{col}:{old_type}->{new_type}") # this means agar old_type change mhi hua toh woh print nhi hoga
 #save_files
def save_files(df):
    filename = input("asking for filename or CLEANED_OUTPUT.CSV")    
    if filename == "" :
        filename = "cleaned_output" 
    if not filename.endswith(".csv"):
        filename = filename + ".csv"
    try:
        df.to_csv(filename,index=False)
        print(f"✅file saved successfully✅,{filename}")
    except Exception as e:
       print(f"❌ could not save the file {filename}, invalid file : {e}")
#main loop
df = load_file()
if df is None:
    print("could not load file.exicting program")
    exit()
original_df = df.copy()   

while True:
    show_menu()
    choice = input("Enter your own choice:").strip()

    if choice == "1": show_file_info(df)
    elif choice == "2": df = remove_missing_rows(df)
    elif choice == "3": df = fill_missing_mean(df)
    elif choice == "4": df = fill_missing_text(df)
    elif choice == "5": df = remove_duplicates(df)
    elif choice == "6": df = clean_special_chars(df)
    elif choice == "7": df = convert_data_types(df)
    elif choice == "8": show_cleaned_data(df)
    elif choice == "9": show_report(original_df, df)
    elif choice == "10": save_files(df)
    elif choice == "11":
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again")