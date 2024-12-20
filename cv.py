import streamlit as st

# Fungsi utama untuk aplikasi
def main():
    cv_page()  # Langsung menampilkan halaman CV tanpa menu navigasi

# Halaman Curriculum Vitae
def cv_page():
    st.title("Anggadiawan Pradipta Mulya")
    # Foto dan Nama
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image('img/DSC_2767k_cop.jpg', width=150)  # Ganti dengan path foto Anda
    with col2:
        st.write("""
        **Kontak:**
        - 📞 +6281808037589
        - 📧 anggadiawanpmwork@gmail.com
        - 📍 Bekasi City, West Java
        """)
    
    # Biodata
    st.subheader("Summary")
    st.write("""
    I am a structural and research engineer with a strong foundation in modular construction, seismic design, 
    and advanced structural analysis. Proficient in designing steel and concrete structures, conducting linear 
    and nonlinear dynamic analysis, and optimizing structural systems.
    """)

    # Pendidikan
    st.subheader("Pendidikan")
    st.write("""
    - **Institut Teknologi Bandung (ITB)**, Bandung, Indonesia  
      Master of Science in Structural Engineering (01/2022 – 06/2024), GPA: 3.5/4.0  
      *Thesis:* Optimization of the Number of Viscoelastic Dampers (VED) using Gaussian Process Regression (GPR).
    
    - **Institut Teknologi Sepuluh Nopember (ITS)**, Surabaya, Indonesia  
      Bachelor of Science in Civil Engineering (07/2017 – 08/2021), GPA: 3.53/4.0  
      *Final Project:* Strengthening with CFRP Sheets for a 16-story Hotel due to Earthquake Codes.
    """)

    # Pengalaman Kerja
    st.subheader("Pengalaman Kerja")
    st.write("""
    - **PT. Adhi Persada Gedung, Mobox Division** (06/2024 – 12/2024)  
      Structural Engineer and Research Engineer, working on modular structures and floating modular systems.
    
    - **PT. Toyo Cahya Konstruksi** (01/2021 – 12/2021)  
      Structural Engineer, focusing on steel warehouses, road settlements, and high-rise structures.
    """)

    # Pengalaman Organisasi
    st.subheader("Pengalaman Organisasi")
    st.write("""
    - **Himpunan Mahasiswa Sipil (HMS), ITS** (01/2019 – 01/2020)  
      Organized training events, discussions on sustainable construction, and guided students for competitions.
    """)

    # Pengalaman Pelatihan
    st.subheader("Pengalaman Pelatihan")
    st.write("""
    - Speaker at **Yearly Seminar Himpunan Ahli Konstruksi Indonesia (HAKI)** (08/2023).  
      Presented a paper on "Application of Response Spectrum Analysis (RSA) in High-Rise Buildings with VED."
    """)

    # Skill
    st.subheader("Skill")
    st.write("""
    - **Structural Analysis & Design**: Concrete, Steel, Timber Design, Retrofitting, Dynamic Analysis.
    - **Software**: ETABS, SAP2000, SAFE, AutoCAD, Python, IDEA StatiCa, Revit, MATLAB.
    - **Languages**: English (Conversational & Written Proficiency).
    """)

if __name__ == "__main__":
    main()
