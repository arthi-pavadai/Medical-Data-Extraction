# 🩺 Medical Data Extraction (Python)

A Python-based system that automatically extracts **prescription information** and **patient details** from PDF documents.  
Using OCR and image processing techniques, the system converts uploaded medical PDFs into machine-readable text and maps the extracted information into a structured form.

---

## ✅ Key Features

- 📄 Supports PDF prescriptions and patient documents
- 🖼 Converts PDFs to image format for OCR processing
- 🔍 Extracts patient name, address, phone number, prescription refills, medication and vaccination details
- 🧠 Uses Tesseract OCR for text recognition
- 🤖 Image pre-processing with OpenCV for better accuracy
- 📤 Supports file upload through API endpoint
- 📦 Outputs results in structured JSON / form format

---

## 🛠️ Tech Stack & Packages

| Package          | Purpose                                                                 |
|------------------|-------------------------------------------------------------------------|
| **pdf2image**     | Converts PDF pages to images                                            |
| **pytesseract**   | OCR engine used for text extraction                                     |
| **opencv-python** | Image preprocessing (e.g. resizing, thresholding, noise removal)        |
| **fastapi**       | API for document upload and extraction endpoints                        |
| **uvicorn**       | ASGI server to run FastAPI app                                          |
| **python-multipart / UploadFile** | Handles file upload through API                        |

---

## 📂 Project Structure

```plaintext
medical-data-extraction/
├── app/
│   ├── main.py                # FastAPI entry point (upload & extract endpoints)
│   ├── extraction/
│   │   ├── utils.py           # PDF to image conversion (pdf2image)
│   │   ├── extractor.py       # OCR processing with pytesseract, OpenCV image pre-processing
│   │   └── parser.py          # Logic to map raw text to structured fields
│  ├── tests/                     # Unit tests for extraction & parsing
├── requirements.txt
└── README.md
```

🚀 How to Run
1️⃣ Install Dependencies
```
python -m venv venv
source venv/bin/activate      # (Linux/Mac)
pip install -r requirements.txt
```

2️⃣ Start the FastAPI Server
```
uvicorn app.main:app --reload
```
📥Request (via /extract)
<img width="618" height="197" alt="image" src="https://github.com/user-attachments/assets/b93a5ac9-2d12-4415-bf69-e5011ad70c6f" />


✅ Example Response
Prescription document:-
```
{
    "patient_name": "Marta Sharapova",
    "patient_address": "9 tennis court, new Russia, DC",
    "medicine": "K\n\nPrednisone 20 mg\nLialda 2.4 gram",
    "directions": "Prednisone, Taper 5 mig every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month",
    "refills": "2"
}
```
Patient details document:
```
{
    "patient_name": "Kathy Crawford",
    "patient_phone_no": "(737) 988-0851",
    "Hep_B_status": "No",
    "Medical_problems": "Migraine\n\nCO\naa"
}
```
