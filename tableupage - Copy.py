import tabula

pdf_path = "tablea.parsing\WAIS-WMS_Clinical Partner.pdf"


page_number = 3   # Page number to extract from
table_index = 2   # Which table on that page (e.g., 2nd table)

try:
    tables = tabula.read_pdf(pdf_path, pages=page_number, multiple_tables=True)

    
    if tables and len(tables) >= table_index:
        print(f"Table {table_index} on Page {page_number}:")
        print(tables[table_index - 1])  # -1 because list index starts at 0
    else:
        print(f"Table {table_index} not found on Page {page_number}. Total tables found: {len(tables)}")

except Exception as e:
    print("An error occurred while extracting tables:", e)
