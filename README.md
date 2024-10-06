# Finance Data Cleanup and Reporting Scripts

This repository contains Python scripts for automating the cleanup and reporting of financial data at FOSS United. These scripts are particularly useful for generating monthly state-wise distribution reports of transactions.

## Overview

The main script, `cleanup_script.py`, performs several key functions:

1. Compares transaction logs from Razorpay dashboard with entries logged in our platform.
2. Filters and processes the data to generate a distribution of all logged Razorpay entries.

## Dependencies

The scripts primarily rely on the `pandas` library for data manipulation. Ensure you have it installed:

`pip install pandas`
