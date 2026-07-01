import zipfile, re
from pathlib import Path
files = [Path('Zomato_Customer_Analysis_Report.docx'), Path('Zomato_Customer_Analysis_Report_Final_Project V1.docx'), Path('Zomato_Decomposition_Plan 1st Revision.pdf')]
for path in files:
    print(f'===== {path} =====')
    if not path.exists():
        print('MISSING')
        continue
    if path.suffix == '.docx':
        try:
            with zipfile.ZipFile(path) as z:
                xml = z.read('word/document.xml').decode('utf-8', errors='ignore')
            text = re.sub(r'<[^>]+>', ' ', xml)
            text = re.sub(r'\s+', ' ', text)
            print(text[:6000])
        except Exception as e:
            print('DOCX EXTRACTION ERROR:', e)
    elif path.suffix == '.pdf':
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(path)
            text = '\n'.join(page.extract_text() or '' for page in reader.pages)
            print(text[:6000])
        except Exception as e:
            print('PDF EXTRACTION ERROR:', e)
    print()
