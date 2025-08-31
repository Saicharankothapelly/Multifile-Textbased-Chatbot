import os
import pdfplumber
import pandas as pd
import ezdxf
from docx import Document
import subprocess

def load_pdf(file_path: str):
    file_name = os.path.basename(file_path)
    pages_content = []
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text() or ""
            if page_text.strip():
                pages_content.append({
                    "file_name": file_name,
                    "page": i,
                    "text": page_text.strip()
                })
    return pages_content


def load_docx(file_path: str):
    doc = Document(file_path)
    content = []
    for i, para in enumerate(doc.paragraphs, start=1):
        if para.text.strip():  # avoid empty lines
            content.append({
                "paragraph": i,
                "text": para.text.strip()
            })
    return content

def load_excel(file_path: str) -> str:
    excel_texts = []
    xls = pd.ExcelFile(file_path)
    for sheet in xls.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet)
        excel_texts.append(f"--- Sheet: {sheet} ---\n{df.to_string(index=False)}")
    return "\n".join(excel_texts)


def load_csv(file_path: str) -> str:
    df = pd.read_csv(file_path)
    return df.to_string(index=False)





def load_dxf(file_path: str):
    #handles dxf file extract text entities for chatbot
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()
    info = []

    for entity in msp:
        if entity.dxftype() == "TEXT":
            try:
                content = entity.dxf.text.strip()
                position = tuple(entity.dxf.insert)
                info.append({
                    "type": "TEXT",
                    "text": content,
                    "position": position
                })
            except AttributeError:
                continue

        elif entity.dxftype() == "MTEXT":
            try:
                content = entity.text.strip()
                position = tuple(entity.dxf.insert)
                info.append({
                    "type": "MTEXT",
                    "text": content,
                    "position": position
                })
            except AttributeError:
                continue

    return info




def convert_dwg_to_dxf(dwg_path: str) -> str:
    """
    Convert a single DWG to DXF using ODAFileConverter.
    Returns path to the converted DXF file.
    """
    oda_path = r"C:\Program Files\ODA\ODAFileConverter 26.4.0\ODAFileConverter.exe"
    dwg_dir = os.path.dirname(dwg_path)
    out_dir = dwg_dir  # same folder
    dxf_path = os.path.join(out_dir, os.path.basename(dwg_path).replace(".dwg", ".dxf"))

    # Run ODAFileConverter (works on folder, not file)
    cmd = [
        oda_path,
        dwg_dir,         # input folder
        out_dir,         # output folder
        "ACAD2013",      # DXF version
        "DXF",           # output format
        "0",             # recurse = 0
        "1",             # audit = 1
        "*.DWG"          # process all DWGs in folder
    ]

    subprocess.run(cmd, check=True)

    return dxf_path

def load_dwg(file_path: str) -> str:
    """
    Convert DWG -> DXF (in same folder) and then load text.
    """
    dxf_path = convert_dwg_to_dxf(file_path)
    return load_dxf(dxf_path)



def load_file(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return load_pdf(file_path)
    elif ext == ".docx":
        return load_docx(file_path)
    elif ext in [".xlsx", ".xls"]:
        return load_excel(file_path)
    elif ext == ".csv":
        return load_csv(file_path)
    elif ext == ".dxf":
        return load_dxf(file_path)
    elif ext == ".dwg":
        return load_dwg(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

# resume = load_pdf(r"C:\Users\Sai charan\Downloads\Saicharan_Resume_.pdf")
# print(resume)
