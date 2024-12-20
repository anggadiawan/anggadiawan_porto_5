import streamlit as st
from data.cv_data import data  # Import data dari file di folder data

# Fungsi utama untuk aplikasi
def main():
    # Menampilkan nama di tengah
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title(data["nama"])
    
    # Kontak
    st.write(f"📞 {data['kontak']['telepon']} | 📧 {data['kontak']['email']}")

    # Biodata
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