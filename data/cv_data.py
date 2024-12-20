import streamlit as st

# Data disimpan dalam variabel terpisah
data = {
    "nama": "Anggadiawan Pradipta Mulya",
    "kontak": {
        "telepon": "+6281808037589",
        "email": "anggadiawanpmwork@gmail.com",
        "lokasi": "Bekasi City, West Java",
    },
    "summary": """
    I am a structural and research engineer with a strong foundation in modular construction, seismic design, 
    and advanced structural analysis. Proficient in designing steel and concrete structures, conducting linear 
    and nonlinear dynamic analysis, and optimizing structural systems.
    """,
    "pendidikan": [
        {
            "institusi": "Institut Teknologi Bandung (ITB)",
            "gelar": "Master of Science in Structural Engineering",
            "periode": "01/2022 – 06/2024",
            "gpa": "3.5/4.0",
            "thesis": "Optimization of the Number of Viscoelastic Dampers (VED) using Gaussian Process Regression (GPR).",
        },
        {
            "institusi": "Institut Teknologi Sepuluh Nopember (ITS)",
            "gelar": "Bachelor of Science in Civil Engineering",
            "periode": "07/2017 – 08/2021",
            "gpa": "3.53/4.0",
            "thesis": "Strengthening with CFRP Sheets for a 16-story Hotel due to Earthquake Codes.",
        },
    ],
    "pengalaman_kerja": [
        {
            "perusahaan": "PT. Adhi Persada Gedung, Mobox Division",
            "periode": "06/2024 – 12/2024",
            "deskripsi": "Structural Engineer and Research Engineer, working on modular structures and floating modular systems.",
        },
        {
            "perusahaan": "PT. Toyo Cahya Konstruksi",
            "periode": "01/2021 – 12/2021",
            "deskripsi": "Structural Engineer, focusing on steel warehouses, road settlements, and high-rise structures.",
        },
    ],
    "pengalaman_organisasi": [
        {
            "organisasi": "Himpunan Mahasiswa Sipil (HMS), ITS",
            "periode": "01/2019 – 01/2020",
            "deskripsi": "Organized training events, discussions on sustainable construction, and guided students for competitions.",
        },
    ],
    "pelatihan": [
        {
            "judul": "Yearly Seminar Himpunan Ahli Konstruksi Indonesia (HAKI)",
            "periode": "08/2023",
            "deskripsi": "Presented a paper on 'Application of Response Spectrum Analysis (RSA) in High-Rise Buildings with VED.'",
        },
    ],
    "skill": [
        "Structural Analysis & Design: Concrete, Steel, Timber Design, Retrofitting, Dynamic Analysis.",
        "Software: ETABS, SAP2000, SAFE, AutoCAD, Python, IDEA StatiCa, Revit, MATLAB.",
        "Languages: English (Conversational & Written Proficiency).",
    ],
}
