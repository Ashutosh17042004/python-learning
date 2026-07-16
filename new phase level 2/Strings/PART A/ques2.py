"""
Q2 ⭐⭐⭐ (File Extension Analyzer)

Given

filename = "project_report_final_v2.pdf"

Without using split(),

Print

Filename : project_report_final_v2

Extension : pdf

Use slicing."""

original_filename = "project_report_final_v2.pdf"

filename = original_filename[: original_filename.index(".")]
extension = original_filename[original_filename.index(".") + 1 :]


print(f"""
Filename : {filename}
Extension : {extension}""")
