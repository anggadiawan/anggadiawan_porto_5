import streamlit as st
from data.cv_data import data  # Import data dari file di folder data


# Fungsi utama untuk aplikasi
def main():
    cv_page()  # Langsung menampilkan halaman CV tanpa menu navigasi

# Halaman Curriculum Vitae
def cv_page():
    st.title(f"{data['nama']}")
    
    # Foto dan Nama
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("img/DSC_2767k_cop.jpg", width=150)  # Path ke foto dalam folder 'img'
    with col2:
        st.write(f"""
        - 📞 {data['kontak']['telepon']}
        - 📧 {data['kontak']['email']}
        - 📍 {data['kontak']['lokasi']}
        """)
    
    # Biodata
    st.divider()
    st.subheader("Summary")
    st.write(data["summary"])

    # Pendidikan
    st.subheader("Pendidikan")
    for edu in data["pendidikan"]:
        st.write(f"""
        - **{edu['institusi']}**, {edu['gelar']}  
          {edu['periode']}, GPA: {edu['gpa']}  
          *Thesis:* {edu['thesis']}
        """)

    # Pengalaman Kerja
    st.subheader("Pengalaman Kerja")
    for kerja in data["pengalaman_kerja"]:
        st.write(f"""
        - **{kerja['perusahaan']}** ({kerja['periode']})  
          {kerja['deskripsi']}
        """)

    # Pengalaman Organisasi
    st.subheader("Pengalaman Organisasi")
    for org in data["pengalaman_organisasi"]:
        st.write(f"""
        - **{org['organisasi']}** ({org['periode']})  
          {org['deskripsi']}
        """)

    # Pengalaman Pelatihan
    st.subheader("Pengalaman Pelatihan")
    for pelatihan in data["pelatihan"]:
        st.write(f"""
        - **{pelatihan['judul']}** ({pelatihan['periode']})  
          {pelatihan['deskripsi']}
        """)

    # Skill
    st.subheader("Skill")
    for skill in data["skill"]:
        st.write(f"- {skill}")

if __name__ == "__main__":
    main()
