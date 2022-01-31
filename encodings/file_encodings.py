# -------------------------- #
# ----- FILE ENCODINGS ----- #
# -------------------------- #


# --- guess file encodings with chardet
import chardet

# look at the first 100 thousand bytes to 'guess' the character encoding
with open(fname, 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100_000)) # 10_000 might work already, but not always

# check what the character encoding might be
print(result) #>> {'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}



# --- address "mixed type issues in pandas.read_csv"
# setting "low_memory=False" is lazy and we tell python to be inefficient
# alternatively, use a converter:
def convert_dtype(x):
    if not x:
        return ''
    try:
        return str(x)   
    except:        
        return ''

pd.read_csv('file.csv',converters={'first_column': convert_dtype,'second_column': convert_dtype})
# keep in mind that converting takes more time.