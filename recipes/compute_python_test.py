# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
all_loan_requests_final_prepared = dataiku.Dataset("all_loan_requests_final_prepared")
all_loan_requests_final_prepared_df = all_loan_requests_final_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

python_test_df = all_loan_requests_final_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
python_test = dataiku.Dataset("python_test")
python_test.write_with_schema(python_test_df)
