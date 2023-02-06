# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
all_loan_requests_final_prepared_filtered = dataiku.Dataset("all_loan_requests_final_prepared_filtered")
df = all_loan_requests_final_prepared_filtered.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['new'] = 1

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

#python_out_df = all_loan_requests_final_prepared_filtered_df # For this sample code, simply copy input to output


# Write recipe outputs
python_out = dataiku.Dataset("python_out")
python_out.write_with_schema(df)