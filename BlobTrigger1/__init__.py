import logging

import azure.functions as func
import pandas as pd
from io import BytesIO, StringIO

def main(myblob: func.InputStream,
        outputblob:func.Out[func.InputStream]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    blob_bytes = myblob.read()
    blob_to_read = BytesIO(blob_bytes)
    df = pd.read_table(blob_to_read, sep='   ')
    print("Length of csv: "+ str(len(df.index)))

    outputs = df.to_csv(index=False)
    outputblob.set(outputs)
    #print (file)
