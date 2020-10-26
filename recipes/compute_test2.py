# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
all_loan_requests_final_prepared = dataiku.Dataset("all_loan_requests_final_prepared")
df = all_loan_requests_final_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['index'] = df.index

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

#test2_df = all_loan_requests_final_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
test2 = dataiku.Dataset("test2")
test2.write_with_schema(df)