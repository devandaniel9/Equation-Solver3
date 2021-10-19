# Title

# List import
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 15}

plt.rc('font', **font)


# Menjalankan program
# streamlit run 'Equation Solver 3 - 3.py'

# Streamlit
st.title('Equation Solver 3')
st.write('#### **Made by Devan Daniel Nainggolan - Kelas 8 Betania**')

st.write('''

- Program ini dapat menyelesaikan persamaan **Linear**, **2 Variabel**, dan **Kuadrat**
- Program ini juga dapat menampilkan langkah penyelesaian dan grafik solusi dari soal
- Silahkan masukkan jenis persamaan dan variabelnya di menu sebelah kiri

''')


st.write('')

st.write('### **Persamaan**')

st.sidebar.write('### **Persamaan**')
persamaan_list = ["Persamaan Linear", "Persamaan 2 Variabel", "Persamaan Kuadrat"]
persamaan = st.sidebar.selectbox("Pilih persamaan:", persamaan_list)

# Konversi float ke int, contoh: 3.0 menjadi 3, 3.2 menjadi 3.2
def fungsi(angka):
    if round(angka, 5) == round(angka, 0):
        angka = int(angka)
    else:
        angka = round(angka, 5)
    
    return angka

# Plus minus
def fungsi2(angka):
    if angka < 0:
        angka = f"- {-angka}"
    else:
        angka = f"+ {angka}"

    return angka

# Kurung
def fungsi3(angka):
    if angka < 0:
        angka = f"({angka})"

    return angka

# Angka 1 dengan variabel
def fungsi4(angka):
    if angka == "+ 1" or angka == 1:
        if angka == 1: angka = ""
        else: angka = "+ "
    elif angka == "- 1" or angka == -1:
        if angka == -1: angka = "-"
        else: angka = "- "

    return angka

# Plus minus 2
def fungsi5(angka):
    if angka < 0:
        angka = "-"
    else:
        angka = "+"

    return angka

if persamaan == persamaan_list[0]:
    st.latex(r"ax + b = c")
    st.latex(r"a \neq 0")
    st.sidebar.write('### **Masukkan angka**')
    a = float(st.sidebar.text_input("a (Default: 2)", value=2))
    b = float(st.sidebar.text_input("b (Default: 1)", value=1))
    c = float(st.sidebar.text_input("c (Default: 5)", value=5))

    st.write('### **Hasil Persamaan**')

    ruas_kiri = fr"{fungsi4(fungsi(a))}x {fungsi2(fungsi(b))}"
    ruas_kanan = fungsi(c)

    hasil_persamaan = fr"{ruas_kiri} = {ruas_kanan}"

    st.latex(hasil_persamaan)

    st.write('### **Hasil Penyelesaian**')

    try:
        hasil = (c - b) / a
        st.latex(f"x = {fungsi(hasil)}")

        muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)
        muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)
    except:
        st.write("Ada yang bermasalah pada input persamaan")

        muncul_1 = False
        muncul_2 = False

    if muncul_1:
        st.write('### **Langkah Penyelesaian**')

        nomor = 1
        st.write(f"### {nomor}. Siapkan inputnya")
        st.latex(fr"{hasil_persamaan}")
        nomor += 1
        st.write(f"### {nomor}. Buatlah pengurangan ruas kiri dan kanan")
        st.latex(fr"{ruas_kiri} - {fungsi(b)} = {ruas_kanan} - {fungsi(b)}")
        nomor += 1
        st.write(f"### {nomor}. Kurangkan kedua ruas")
        st.latex(fr"{fungsi4(fungsi(a))}x = {fungsi(c - b)}")
        if fungsi(a) != 1:
            nomor += 1
            st.write(f"### {nomor}. Buatlah pembagian ruas kiri dan kanan")
            st.latex(fr"\frac{{{fungsi(a)}}}{{{fungsi(a)}}}x = \frac{{{fungsi(c - b)}}}{{{fungsi(a)}}}")
            nomor += 1
            st.write(f"### {nomor}. Bagikan kedua ruas")
            st.latex(fr"x = {fungsi(hasil)}")

    if muncul_2:
        st.write('## **Grafik**')

        jarak = -5
        batas = 5
        ukuran = 0.01

        plt.style.use('seaborn-whitegrid')

        x = np.arange(jarak, batas + 1e-14, ukuran)
        plt.figure(figsize=(10,10))

        y1 = a*x + b
        plt.plot(x,y1,lw=5,color='blue')

        y2 = 0*x + c
        plt.plot(x,y2,lw=5,color='green')

        plt.xlabel("x",)
        plt.ylabel("y",)
        #plt.title("Grafik Penyelesaian", size=20)
        plt.legend([ruas_kiri, ruas_kanan])

        plt.savefig('Preview.png')
        img = Image.open('Preview.png')
        st.image(img, width=500)

if persamaan == persamaan_list[1]:
    st.latex(r"ax + by = c\\dx + ey = f")
    # st.latex(r"a \neq 0, a \neq 0, a \neq 0, d \neq 0")
    st.sidebar.write('### Masukkan angka')
    a = float(st.sidebar.text_input("a (Default: 1)", value=2))
    b = float(st.sidebar.text_input("b (Default: 1)", value=1))
    c = float(st.sidebar.text_input("c (Default: 5)", value=5))
    d = float(st.sidebar.text_input("d (Default: 3)", value=3))
    e = float(st.sidebar.text_input("e (Default: -2)", value=-2))
    f = float(st.sidebar.text_input("f (Default: 4)", value=4))

    st.write('### **Hasil Persamaan**')

    ruas_kiri_1 = fr"{fungsi4(fungsi(a))}x {fungsi4(fungsi2(fungsi(b)))}y"
    ruas_kanan_1 = fungsi(c)
    ruas_kiri_2 = fr"{fungsi4(fungsi(d))}x {fungsi4(fungsi2(fungsi(e)))}y"
    ruas_kanan_2 = fungsi(f)
    persamaan_1 = fr"{ruas_kiri_1} = {ruas_kanan_1}"
    persamaan_2 = fr"{ruas_kiri_2} = {ruas_kanan_2}"
    persamaan = fr"{persamaan_1}\\{persamaan_2}"
    st.latex(persamaan)

    st.write('### **Hasil Penyelesaian**')

    try:
        hasil_y = (d * c - a * f) / (d * b - a * e)
        hasil_x = (c - b * hasil_y) / a
        st.latex(fr"(x, y) = ({fungsi(hasil_x)}, {fungsi(hasil_y)})")

        muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)
        muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)
    except:
        st.write("Ada yang bermasalah pada input persamaan")

        muncul_1 = False
        muncul_2 = False

    if muncul_1:
        st.write('### **Langkah Penyelesaian**')

        jenis_list = ["Eliminasi", "Subsitusi", "Determinan"]
        jenis = st.selectbox("Pilih cara langkah penyelesaian:", jenis_list)

        if jenis == jenis_list[0]:
            nomor = 1
            st.write(f"### {nomor}")
            st.latex(fr"{persamaan}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Di Persamaan 1, kalikan kedua ruas dengan {fungsi(d)}")
            st.write(f"Di Persamaan 2, kalikan kedua ruas dengan {fungsi(a)}")
            st.latex(fr"{fungsi4(fungsi(d * a))}x {fungsi4(fungsi2(fungsi(d * b)))}y = {fungsi(d * c)}\\{fungsi4(fungsi(a * d))}x {fungsi4(fungsi2(fungsi(a * e)))}y = {fungsi(a * f)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write("Kurangkan persamaan atas dengan bawah")
            st.latex(fr"{fungsi4(fungsi(d * b))}y - {fungsi4(fungsi3(fungsi(a * e)))}y = {fungsi(d * c)} - {fungsi3(fungsi(a * f))}")
            st.latex(fr"{fungsi4(fungsi(d * b - a * e))}y = {fungsi(d * c - a * f)}")
            if fungsi(d * b - a * e) != 1:
                st.latex(fr"""\frac{{{fungsi(d * b - a * e)}}}{{{fungsi(d * b - a * e)}}} y = \frac{{{fungsi(d * c - a * f)}}}{{{fungsi(d * b - a * e)}}}""")
                st.latex(fr"y = {fungsi(hasil_y)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Subsitusikan y = {fungsi(hasil_y)} ke Persamaan 1")
            st.latex(fr"{fungsi4(fungsi(a))}x + {fungsi3(fungsi(b))} \times {fungsi3(fungsi(hasil_y))} = {fungsi(c)}")
            st.latex(fr"{fungsi4(fungsi(a))}x {fungsi2(fungsi(b * hasil_y))} = {fungsi(c)}")
            st.latex(fr"{fungsi4(fungsi(a))}x + {fungsi3(fungsi(b * hasil_y))} - {fungsi3(fungsi(b * hasil_y))} = {fungsi(c)} - {fungsi3(fungsi(b * hasil_y))}")
            st.latex(fr"{fungsi4(fungsi(a))}x = {fungsi(c - b * hasil_y)}")
            st.latex(fr"\frac{{{fungsi(a)}}}{{{fungsi(a)}}} x = \frac{{{fungsi(c - b * hasil_y)}}}{{{fungsi(a)}}}")
            st.latex(fr"x = {fungsi(hasil_x)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"(x, y) = ({fungsi(hasil_x)}, {fungsi(hasil_y)})")

        if jenis == jenis_list[1]:
            nomor = 1
            st.write(f"### {nomor}")
            st.latex(fr"{persamaan}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"{fungsi4(fungsi(a))}x {fungsi4(fungsi2(fungsi(-a)))}x {fungsi4(fungsi2(fungsi(b)))}y = {fungsi4(fungsi(-a))}x {fungsi2(fungsi(c))}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"{fungsi4(fungsi(b))}y = {fungsi4(fungsi(-a))}x {fungsi2(fungsi(c))}")
            if fungsi(b) != 1:
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"\frac{{{fungsi(b)}}}{{{fungsi(b)}}}y = \frac{{{fungsi(-a)}}}{{{fungsi(b)}}}x {fungsi5(c)} \frac{{{fungsi(abs(c))}}}{{{fungsi(b)}}}")
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"y = {fungsi4(fungsi(-a / b))}x {fungsi2(fungsi(c / b))}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Subsitusikan y ke Persamaan 2")
            st.latex(fr"{fungsi4(fungsi(d))}x {fungsi4(fungsi2(fungsi(e)))}({fungsi4(fungsi(-a / b))}x {fungsi2(fungsi(c / b))}) = {fungsi(f)}")
            st.latex(fr"{fungsi4(fungsi(d))}x {fungsi4(fungsi2(fungsi(e * -a / b)))}x {fungsi2(fungsi(e * c / b))} = {fungsi(f)}")
            st.latex(fr"{fungsi4(fungsi(d + e * -a / b))}x {fungsi2(fungsi(e * c / b))} = {fungsi(f)}")
            st.latex(fr"{fungsi4(fungsi(d + e * -a / b))}x {fungsi2(fungsi(e * c / b))} {fungsi2(fungsi(-e * c / b))} = {fungsi(f)} {fungsi2(fungsi(-e * c / b))}")
            st.latex(fr"{fungsi4(fungsi(d + e * -a / b))}x = {fungsi(f - e * c / b)}")
            if fungsi4(fungsi(d + e * -a / b)) != 1:
                st.latex(fr"\frac{{{fungsi(d + e * -a / b)}}}{{{fungsi(d + e * -a / b)}}}x = \frac{{{fungsi(f - e * c / b)}}}{{{fungsi(d + e * -a / b)}}}")
                st.latex(fr"x = {fungsi(hasil_x)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Subsitusikan x = {fungsi(hasil_x)} ke Persamaan 1")
            st.latex(fr"y = {fungsi3(fungsi(-a / b))} \times {fungsi3(fungsi(hasil_x))} {fungsi2(fungsi(c / b))}")
            st.latex(fr"y = {fungsi(-a / b * hasil_x)} {fungsi2(fungsi(c / b))}")
            st.latex(fr"y = {fungsi(hasil_y)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"(x, y) = ({fungsi(hasil_x)}, {fungsi(hasil_y)})")

        if jenis == jenis_list[2]:
            nomor = 1
            st.write(f"### {nomor}")
            st.latex(fr"{persamaan}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Ubah bentuk persamaan menjadi determinan")
            # st.latex(r"D = \begin{bmatrix}a & b\\c & d\end{bmatrix}")
            st.latex(fr"D = \begin{{bmatrix}}{fungsi(a)} & {fungsi(b)}\\{fungsi(d)} & {fungsi(e)}\end{{bmatrix}}")
            st.latex(fr"D_1 = \begin{{bmatrix}}{fungsi(c)} & {fungsi(b)}\\{fungsi(f)} & {fungsi(e)}\end{{bmatrix}}")
            st.latex(fr"D_2 = \begin{{bmatrix}}{fungsi(a)} & {fungsi(c)}\\{fungsi(d)} & {fungsi(f)}\end{{bmatrix}}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Gunakan rumus determinan")
            # st.latex(rf"D = ad - bc")
            st.latex(rf"D = {fungsi3(fungsi(a))} \times {fungsi3(fungsi(e))} - {fungsi3(fungsi(b))} \times {fungsi3(fungsi(d))}")
            st.latex(rf"D_1 = {fungsi3(fungsi(c))} \times {fungsi3(fungsi(e))} - {fungsi3(fungsi(b))} \times {fungsi3(fungsi(f))}")
            st.latex(rf"D_2 = {fungsi3(fungsi(a))} \times {fungsi3(fungsi(f))} - {fungsi3(fungsi(c))} \times {fungsi3(fungsi(d))}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Hitungkan")
            st.latex(rf"D = {fungsi(a * e)} {fungsi2(fungsi(-b * d))}")
            st.latex(rf"D_1 = {fungsi(c * e)} {fungsi2(fungsi(-b * f))}")
            st.latex(rf"D_2 = {fungsi(a * f)} {fungsi2(fungsi(-c * d))}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Hitungkan")
            st.latex(rf"D = {fungsi(a*e-b*d)}")
            st.latex(rf"D_1 = {fungsi(c*e-b*f)}")
            st.latex(rf"D_2 = {fungsi(a*f-c*d)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Gunakan rumus persamaan dan determinan")
            st.latex(rf"x = \frac{{D_1}}{{D}} = \frac{{{fungsi(c*e-b*f)}}}{{{fungsi(a*e-b*d)}}}")
            st.latex(rf"y = \frac{{D_2}}{{D}} = \frac{{{fungsi(a*f-c*d)}}}{{{fungsi(a*e-b*d)}}}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Hitungkan")
            st.latex(rf"x = {fungsi(hasil_x)}")
            st.latex(rf"y = {fungsi(hasil_y)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Penyelesaian x dan y")
            st.latex(fr"(x, y) = ({fungsi(hasil_x)}, {fungsi(hasil_y)})")

            # st.latex(r"a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)")
            # st.latex(rf"a + ar + a r^2 + a r^3 + \cdots + a r^{12-1} = \sum_{13}^{12-1} ar^k = a \left(\frac{31}{13}\right)")

    if muncul_2:
        st.write('### **Grafik**')

        jarak = hasil_x - 5
        batas = hasil_x + 5
        ukuran = 0.01

        plt.style.use('seaborn-whitegrid')

        x = np.arange(jarak, batas + 1e-14, ukuran)
        plt.figure(figsize=(10,10))

        y1 = -a/b*x + c/b
        plt.plot(x,y1,lw=5,color='blue')

        y2 = -d/e*x + f/e
        plt.plot(x,y2,lw=5,color='green')

        plt.xlabel("x", size=20, )
        plt.ylabel("y",)
        plt.legend([persamaan_1, persamaan_2])

        plt.savefig('Preview.png')
        img = Image.open('Preview.png')
        st.image(img, width=500)

if persamaan == persamaan_list[2]:
    st.latex(r"ax^2 + bx + c = 0")
    st.latex(r"a \neq 0")
    st.sidebar.write('### **Masukkan angka**')
    a = float(st.sidebar.text_input("a (Default: 1)", value=1))
    b = float(st.sidebar.text_input("b (Default: 3)", value=3))
    c = float(st.sidebar.text_input("c (Default: 2)", value=2))

    st.write('### **Hasil Persamaan**')

    ruas_kiri = fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(b)))}x {fungsi2(fungsi(c))}"
    ruas_kanan = "0"

    hasil_persamaan = fr"{ruas_kiri} = {ruas_kanan}"

    st.latex(hasil_persamaan)

    st.write('### **Hasil Penyelesaian**')

    try:
        # Hasil Penyelesaian
        d = b ** 2 - 4 * a * c

        # Hasil 2 Solusi
        hasil_x1 = (-b + d ** 0.5) / (2 * a)
        hasil_x2 = (-b - d ** 0.5) / (2 * a)

        # Mencari Jumlah Solusi
        if d > 0: e = 2
        elif d == 0: e = 1
        elif d < 0: e = 0

        # Titik Puncak
        f1 = -b / (2*a)
        f2 = -b**2 / (4*a) + c

        # Solusi
        if d < 0:
            st.write("x = Tidak ada")
        else:
            if fungsi(hasil_x1) == fungsi(hasil_x2):
                st.latex(fr"x = {fungsi(hasil_x1)}")
            else:
                st.latex(fr"x_1 = {fungsi(hasil_x1)}")
                st.latex(fr"x_2 = {fungsi(hasil_x2)}")
        
        st.write(f"Diskriminan = {fungsi(d)}")
        st.write(f"Jumlah Solusi = {fungsi(e)}")
        st.write(f"Titik Puncak = ({fungsi(f1)}, {fungsi(f2)})")
        st.write("")

        muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)
        muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)
    except:
        st.write("Ada yang bermasalah pada input persamaan")

        muncul_1 = False
        muncul_2 = False

    if muncul_1:
        st.write('### **Langkah Penyelesaian**')

        jenis_list = ["Selesaikan persamaan kuadrat", "Hitung diskriminan", "Jumlah solusi", "Titik puncak"]
        jenis = st.selectbox("Pilih jenis langkah penyelesaian:", jenis_list)

        if jenis == jenis_list[0]:
            jenis_2_list = ["Rumus kuadrat", "Kuadrat sempurna"]
            jenis_2 = st.selectbox("Pilih cara langkah penyelesaian:", jenis_2_list)

            if jenis_2 == jenis_2_list[0]:
                g1 = fr"\sqrt{{{fungsi3(fungsi(b))}^2 - 4 \times {fungsi3(fungsi(a))} \times {fungsi3(fungsi(c))}}}"
                g2 = fr"\sqrt{{{fungsi(b ** 2)} {fungsi2(fungsi(-4 * a * c))}}}"
                g3 = fr"\sqrt{{{fungsi(d)}}}"

                nomor = 1
                st.write(f"### {nomor}")
                st.latex(fr"{hasil_persamaan}")
                nomor += 1
                st.write(f"### {nomor}")
                st.write(f"Gunakan rumus persamaan kuadrat")
                st.latex(fr"x_1 = \frac{{-{fungsi3(fungsi(b))} + {g1}}}{{2 \times {fungsi3(fungsi(a))}}}")
                st.latex(fr"x_2 = \frac{{-{fungsi3(fungsi(b))} - {g1}}}{{2 \times {fungsi3(fungsi(a))}}}")
                nomor += 1
                st.write(f"### {nomor}")
                st.write(f"Hitungkan")
                st.latex(fr"x_1 = \frac{{{fungsi(-b)} + {g2}}}{{{fungsi(2 * a)}}}")
                st.latex(fr"x_2 = \frac{{{fungsi(-b)} - {g2}}}{{{fungsi(2 * a)}}}")
                nomor += 1
                st.write(f"### {nomor}")
                st.write(f"Hitungkan")
                st.latex(fr"x_1 = \frac{{{fungsi(-b)} + {g3}}}{{{fungsi(2 * a)}}}")
                st.latex(fr"x_2 = \frac{{{fungsi(-b)} - {g3}}}{{{fungsi(2 * a)}}}")
                if fungsi(d) >= 0:
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.write(f"Hitung akar")
                    st.latex(fr"x_1 = \frac{{{fungsi(-b)} + {fungsi(d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                    st.latex(fr"x_2 = \frac{{{fungsi(-b)} - {fungsi(d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.write(f"Hitungkan")
                    st.latex(fr"x_1 = \frac{{{fungsi(-b + d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                    st.latex(fr"x_2 = \frac{{{fungsi(-b - d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.write(f"Hasil")
                    st.latex(fr"x_1 = {fungsi(hasil_x1)}")
                    st.latex(fr"x_2 = {fungsi(hasil_x2)}")
                    if fungsi(hasil_x1) == fungsi(hasil_x2):
                        nomor += 1
                        st.write(f"### {nomor}")
                        st.write(f"Hasil")
                        st.latex(fr"x = {fungsi(hasil_x1)}")
                else:
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.write(f"Hasil")
                    st.latex(r"x \notin \R")
                    st.write("x = Tidak ada")

            if jenis_2 == jenis_2_list[1]:
                nomor = 1
                st.write(f"### {nomor}")
                st.latex(fr"{hasil_persamaan}")
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(b)))}x {fungsi2(fungsi(c))} {fungsi2(fungsi(-c))} = 0 {fungsi2(fungsi(-c))}")
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(b)))}x = {fungsi(-c)}")
                if a != 1:
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.latex(fr"\frac{{{fungsi(a)}}}{{{fungsi(a)}}}x^2 {fungsi5(b)} \frac{{{fungsi(abs(b))}}}{{{fungsi(a)}}}x = \frac{{{fungsi(-c)}}}{{{fungsi(a)}}}")
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.latex(fr"x^2 {fungsi4(fungsi2(fungsi(b / a)))}x = {fungsi(-c / a)}")
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"x^2 {fungsi4(fungsi2(fungsi(b / a)))}x + {fungsi(b**2 / (4*a**2))} = {fungsi(-c / a)} + {fungsi(b**2 / (4*a**2))}")
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"(x {fungsi2(fungsi(b / (2*a)))})^2 = {fungsi(-c / a + b**2 / (4*a**2))}")
                if fungsi(d) > 0:
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.latex(fr"x_1 {fungsi2(fungsi(b / (2*a)))} = {fungsi((-c / a + b**2 / (4*a**2))**0.5)}")
                    st.latex(fr"x_2 {fungsi2(fungsi(b / (2*a)))} = {fungsi(-(-c / a + b**2 / (4*a**2))**0.5)}")
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.latex(fr"x_1 {fungsi2(fungsi(b / (2*a)))} {fungsi2(fungsi(-b / (2*a)))} = {fungsi((-c / a + b**2 / (4*a**2))**0.5)} {fungsi2(fungsi(-b / (2*a)))}")
                    st.latex(fr"x_2 {fungsi2(fungsi(b / (2*a)))} {fungsi2(fungsi(-b / (2*a)))} = {fungsi(-(-c / a + b**2 / (4*a**2))**0.5)} {fungsi2(fungsi(-b / (2*a)))}")
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.latex(fr"x_1 = {fungsi(hasil_x1)}")
                    st.latex(fr"x_2 = {fungsi(hasil_x2)}")
                elif fungsi(d) == 0:
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.latex(fr"x {fungsi2(fungsi(b / (2*a)))} = 0")
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.latex(fr"x {fungsi2(fungsi(b / (2*a)))} {fungsi2(fungsi(-b / (2*a)))} = 0 {fungsi2(fungsi(-b / (2*a)))}")
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.latex(fr"x = {fungsi(hasil_x1)}")
                else:
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.latex(r"x \notin \R")
                    st.write("x = Tidak ada")

        if jenis == jenis_list[1]:
            nomor = 1
            st.write(f"### {nomor}. Siapkan inputnya")
            st.latex(fr"   {hasil_persamaan}")
            nomor += 1
            st.write(f"### {nomor}. Gunakan rumus diskriminan")
            st.latex(fr"D = {fungsi(b)} ^ 2 - 4 \times {fungsi(a)} \times {fungsi(c)}")
            nomor += 1
            st.write(f"### {nomor}. Sederhanakan")
            st.latex(fr"D = {fungsi(b ** 2)} - {4 * fungsi(a) * fungsi(c)}")
            nomor += 1
            st.write(f"### {nomor}. Kurangkan")
            st.latex(fr"D = {fungsi(d)}")

        if jenis == jenis_list[2]:
            nomor = 1
            st.write(f"### {nomor}. Siapkan inputnya")
            st.latex(fr"{hasil_persamaan}")
            nomor += 1
            st.write(f"### {nomor}. Gunakan rumus diskriminan")
            st.latex(fr"D = {fungsi(b)} ^ 2 - 4 \times {fungsi(a)} \times {fungsi(c)}")
            nomor += 1
            st.write(f"### {nomor}. Sederhanakan")
            st.latex(fr"D = {fungsi(b ** 2)} - {4 * fungsi(a) * fungsi(c)}")
            nomor += 1
            st.write(f"### {nomor}. Kurangkan")
            st.latex(fr"D = {fungsi(d)}")
            # st.write("Jika D > 0: Jumlah ")
            nomor += 1
            st.write(f"### {nomor}")
            if fungsi(d) > 0: st.write("Jumlah solusi = 2")
            elif fungsi(d) == 0: st.write("Jumlah solusi = 1")
            else: st.write("Jumlah solusi = 0")

        if jenis == jenis_list[3]:
            nomor = 1
            st.write(f"### {nomor}. Siapkan inputnya")
            st.latex(fr"{hasil_persamaan}")
            nomor += 1
            st.write(f"### {nomor}. Gunakan rumus untuk mencari titik puncak untuk x")
            st.latex(fr"x = \frac{{{fungsi(-b)}}}{{2 \times {fungsi(a)}}}")
            nomor += 1
            st.write(f"### {nomor}. Sederhanakan")
            st.latex(fr"x = \frac{{{fungsi(-b)}}}{{2 \times {fungsi(a)}}}")
            nomor += 1
            st.write(f"### {nomor}. Bagikan")
            st.latex(fr"x = {fungsi(f1)}")
            nomor += 1
            st.write(f"### {nomor}. Gunakan rumus untuk mencari titik puncak untuk y")
            st.latex(fr"y = -\frac{{{fungsi(b)} ^ 2 - 4 \times {fungsi(a)} \times {fungsi(c)}}}{{4 \times {fungsi(a)}}}")
            nomor += 1
            st.write(f"### {nomor}. Sederhanakan")
            st.latex(fr"y = -\frac{{{fungsi(b ** 2)} - {4 * fungsi(a) * fungsi(c)}}}{{{fungsi(4 * a)}}}")
            nomor += 1
            st.write(f"### {nomor}. Bagikan")
            st.latex(fr"y = -\frac{{{fungsi(d)}}}{{{fungsi(4 * a)}}}")
            nomor += 1
            st.write(f"### {nomor}. Bagikan")
            st.latex(fr"y = {fungsi(f2)}")
            nomor += 1
            st.write(f"### {nomor}. Titik puncak")
            st.latex(fr"({fungsi(f1)}, {fungsi(f2)})")

            # st.latex(r"""\[ \int\limits_0^1 x^2 + y^2 \ dx \]""")

    if muncul_2:
        st.write('### **Grafik**')

        jarak = f1 - 5
        batas = f1 + 5
        ukuran = 0.01

        plt.style.use('seaborn-whitegrid')

        x = np.arange(jarak, batas + 1e-14, ukuran)
        plt.figure(figsize=(10,10))

        y1 = a*x**2 + b*x + c
        plt.plot(x,y1,color='blue',lw=5)

        y2 = 0*x + 0
        plt.plot(x,y2,color='green',lw=5)

        plt.xlabel("x", size=20,)
        plt.ylabel("y",)
        plt.legend(['hehe', ruas_kanan])

        plt.savefig('Preview.png')
        img = Image.open('Preview.png')
        st.image(img, width=500)


    
