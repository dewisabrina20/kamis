import streamlit as st 

def MyBG_colour(wch_colour): 
    my_colour = f"<style> .stApp {{background-color: {wch_colour};}} </style>"
    st.markdown(my_colour, unsafe_allow_html=True)
    
MyBG_colour("#DBE9FA")

#Tampilan Halaman Web
add_selectbox = st.sidebar.selectbox("Menu :mag:", ("Beranda", "Normalitas dan Molaritas",  "Perhitungan Normalitas", "Perhitungan Molaritas"))

#Halaman Beranda
if add_selectbox == "Beranda" :
    st.header(":black[Norm&Mol Calcula]", divider="rainbow")
    st.subheader(":black[Web Aplikasi Perhitungan Normalitas dan Molaritas]")
    
    st.image("https://hal511.files.wordpress.com/2024/05/whatsapp-image-2024-05-18-at-09.30.44.jpeg?w=1024")
    st.subheader(":black[Tentang Aplikasi🖥️]")
    st.markdown('''Norm&Mol Calcula merupakan web aplikasi yang dibuat untuk mempermudah perhitungan normalitas dan molaritas suatu 
                larutan dengan cepat dan akurat. ''')
    st.subheader(":black[Creator🖌️]")
    st.image("https://hal511.files.wordpress.com/2024/05/whatsapp-image-2024-05-18-at-10.05.30.jpeg?w=1024")
    
#Normalitas
if add_selectbox == "Normalitas dan Molaritas" :
    st.header(":rainbow[Tentang Normalitas dan Molaritas]")
    tab1, tab2 = st.tabs(["Normalitas", "Molaritas"])
    
    with tab1 :
        st.subheader(":violet[Pengertian]")
        st.markdown('''Normalitas (N) adalah satuan konsentrasi yang digunakan dalam kimia untuk mengukur jumlah
                ekuivalen zat terlarut per liter larutan. Satu ekuivalen zat terlarut adalah jumlah yang bereaksi 
                atau menggantikan satu mol ion hidrogen (H+) dalam reaksi asam-basa atau satu mol elektron dalam 
                reaksi redoks.''')
        
        st.subheader(":violet[Rumus Perhitungan]")
        st.image('https://hal255.files.wordpress.com/2024/05/blue-simple-keep-calm-desktop-wallpaper-1.png?w=1024')
        st.markdown('''Keterangan :\n
        N = Normalitas larutan \n 
    mg sampel = massa titrat yang ditimbang \n
    mL titran = volume yang didapat saat titrasi \n 
    BE = bobot ekuivalen sampel \n 
    fp = faktor pengali \n''')
    
        st.subheader(":violet[Tujuan]")
        st.markdown("""
            - Normalitas membantu dalam menghitung konsentrasi larutan titran atau titrat dengan tepat. 
            - Normalitas digunakan untuk standardisasi larutan titran, memastikan bahwa konsentrasi larutan
                titran tepat dan dapat direproduksi dalam eksperimen lainnya.
            """)
    
        st.subheader(":violet[Kelebihan]")
        st.markdown("""
            - Normalitas memberikan cara yang lebih tepat untuk mengukur konsentrasi dalam titrasi, terutama
                ketika reaksi melibatkan lebih dari satu ekuivalen per molekul.
            - Normalitas dapat diterapkan pada berbagai jenis reaksi kimia, termasuk asam-basa, redoks, 
                dan pengendapan.
            """)
    
    with tab2 :
        st.subheader(":blue[Pengertian]")
        st.markdown('''Molaritas (M) adalah satuan konsentrasi yang mengukur jumlah mol zat terlarut per liter 
                    larutan. Satu mol adalah jumlah zat yang mengandung (6,02 x 10^-23) partikel, seperti atom,
                    molekul, atau ion yang dikenal dengan bilangan Avogadro. Molaritas sering digunakan untuk 
                    menyatakan konsentrasi suatu larutan dan memudahkan perhitungan dalam reaksi kimia.''')
    
        st.subheader(':blue[Rumus Perhitungan]')
        st.image('https://hal255.files.wordpress.com/2024/05/whatsapp-image-2024-05-12-at-20.33.20.jpeg?w=1024')
        st.markdown('''Keterangan :\n
        M = Molaritas larutan \n 
    mg sampel = massa titrat yang ditimbang \n
    mL titran = volume yang didapat saat titrasi \n 
    BM = bobot molekul sampel \n 
    fp = faktor pengali \n''')
    
        st.subheader(":blue[Tujuan]")
        st.markdown(""" 
            - Molaritas digunakan untuk mengukur konsentrasi larutan titran atau titrat.
            - Dengan molaritas, memudahkan menghitung jumlah mol zat yang bereaksi bereaksi berdasarkan volume larutan
                yang digunakan.
            - Molaritas digunakan untuk menstandardisasi larutan titran, memastikan bahwa konsentrasi larutan titran
                tepat dan dapat di reproduksi dalam eksperimen lainnya.        
            """)
    
        st.subheader(":blue[Kelebihan]")
        st.markdown(""" 
            - Molaritas adalah cara yang sederhana untuk menyatakan konsentrasi larutan, memudahkan perbandingan dan 
                perhitungan antara berbagai larutan.
            - Molaritas langsung berkaitan dengan jumlah mol reaktan dan produk dalam reaksi kimia, memudahkan perhitungan
                stoikiometri.        
            """)

#Halaman Perhitungan Normalitas
if add_selectbox == "Perhitungan Normalitas":
    
    st.title(':rainbow[Perhitungan Normalitas]')
    mg = st.number_input("Masukkan nilai massa titrat (mg)", min_value= 0.01 )
    mL = st.number_input("Masukkan nilai volume titran (mL)", min_value= 0.01)
    fp = st.number_input("Masukkan nilai faktor pengali", min_value= 1.00 ) 
    BE = st.number_input("Masukkan nilai bobot ekuivalen (mg/mgrek)", min_value= 0.01)
    
    #Perhitungan Normalitas
    if st.button("Normalitas"):
        Normalitas_Larutan = (mg/(BE*mL*fp))
        st.success (f"Normalitas Larutan Adalah  {Normalitas_Larutan:.4f} N")
        
#Halaman Perhitungan Molaritas
if add_selectbox == "Perhitungan Molaritas":
    
    st.title(':rainbow[Perhitungan Molaritas]')
    mg = st.number_input("Masukkan nilai massa titrat (mg)", min_value= 0.01 )
    mL = st.number_input("Masukkan nilai volume titran (mL)", min_value= 0.01)
    fp = st.number_input("Masukkan nilai faktor pengali", min_value= 1.00)
    BM = st.number_input("Masukkan nilai bobot molekul (mg/mmol)", min_value= 0.01)
    
    #Perhitungan Molaritas
    if st.button("Molaritas"):
        Molaritas_Larutan = (mg/(BM*mL*fp))
        st.success (f"Molaritas Larutan Adalah {Molaritas_Larutan:.4f} M")
