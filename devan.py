import math
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

#RUMUS
#Bangun Datar

pi = math.pi

def persegi(s):
    keliling = 4*s
    luas = s*s
    diagonal = s*np.sqrt(2)
    return(keliling,luas,diagonal)

def p_panjang(p,l):
    keliling = 2*(p+l)
    luas = p*l
    diagonal = np.sqrt(p**2+l**2)
    return(keliling,luas,diagonal)

def jajar_genjang(a,t): # New!
    luas = a*t
    return(luas)

def trapesium(s_a,s_b,t): # New!
    luas = (s_a+s_b)*t/2
    return(luas)

def lingkaran(r):
    diameter = 2*r
    keliling = 2*math.pi*r
    luas = pi*r*r
    return(diameter,keliling,luas)

def segitiga(a,t):
    s = math.hypot(a,t)
    keliling = a + t + s
    luas = 0.5 * a * t
    return(keliling,luas,s)

#Bangun Ruang
def kubus(s):
    luas = 6*s**2
    volume = s**3
    return(luas,volume)

def balok(p,l,t):
    luas = 2 * (p*l + p*t +l*t)
    volume = p*l*t
    return(luas,volume)

def tabung(r,t):
    luas = 2*pi*r*(r+t)
    volume = pi*r**2*t
    return(luas,volume)

def kerucut(r,t):
    s = math.hypot(r,t)
    diameter = 2*r
    luas = pi*r*(r+s)
    volume = pi*r**2*t/3
    return(diameter,luas,volume,s)

def bola(r):
    diameter = 2*r
    luas = 4*pi*r**2
    volume = 4/3*pi*r**3
    return(diameter,luas,volume)

#Streamlit
st.write("""# Flat Shape and Round Shape Program""")
st.write('** Made by Devan Daniel Nainggolan **')
st.write('')
st.write('## **Input Variabel**')

jenis = st.selectbox("Pilih jenis bangun yang diinginkan: ",['Bangun Ruang','Bangun Datar'])

if jenis=='Bangun Ruang':
    list_bangun = ['Kubus','Balok','Tabung','Kerucut','Bola']

else:
    list_bangun =  ['Persegi','Persegi Panjang','Jajar Genjang','Trapesium','Lingkaran','Segitiga']

bentuk = st.selectbox("\nPilih jenis bentuk: ",list_bangun)

if bentuk=='Persegi' or bentuk=='Kubus':
    s = st.number_input("Sisi (cm)")

    st.write(' ')
    st.write('## **Solution**')
    
    if bentuk=="Persegi":
        img = Image.open('persegi.png')
        st.image(img)

        k, l, d = persegi(s)
        st.markdown(f'Keliling = 4s = 4*{s} = {round(k,2)} cm')
        st.markdown(f'Diagonal = $\sqrt2*s = sqrt(2)*{s}$ = {round(d,2)} cm')
        st.markdown(f'Luas = s^2 = {s}^2 = {round(l,2)} cm^2')
        
    elif bentuk=="Kubus":
        img = Image.open('kubus.png')
        st.image(img)

        l, v = kubus(s)
        st.markdown(f'Luas Permukaan $= 6s^2 = (6)({s})({s}) = {round(l,2)}  cm^2$')
        st.markdown(f'Volume $= s^3 = {s}^3 = {round(v,2) }  cm^3$')


elif bentuk=='Lingkaran' or bentuk=='Bola':
    r = st.number_input("Jari-jari (cm)")

    st.write(' ')
    st.write('## **Solution**')

    if bentuk=="Lingkaran":
        img = Image.open('lingkaran.png')
        st.image(img)

        d, k, l = lingkaran(r)
        st.markdown(f'Diameter $= 2r = (2)({r}) = {round(d,2)} cm$')
        st.markdown(f'Keliling $= 2 \pi r = (2)(\pi)({r}) = {round(k,2)} cm$')
        st.markdown(f'Luas $= \pi r^2 = (\pi)({r})({r}) = {round(l,2)} cm^2$')

    elif bentuk=="Bola":
        img = Image.open('bola.png')
        st.image(img)

        d, l, v = bola(r)
        st.markdown(f'Diameter $= 2r = (2)({r}) = {round(d,2)} cm$')
        st.markdown(f'Luas Permukaan $= 4 \pi r^2 = (4)(\pi)({r}^2) = {round(l,2)} cm^2$')
        st.markdown(f'Volume $= 4/3 \pi r^3 = (4/3)(\pi)({r}^3) = {round(v,2)} cm^3$')
        

elif bentuk=='Tabung' or bentuk=='Kerucut':
    r = st.number_input("Jari-jari alas (cm)")
    t = st.number_input("Tinggi (cm)")

    st.write(' ')
    st.write('## **Solution**')

    if bentuk=="Tabung":
        img = Image.open('tabung.png')
        st.image(img)

        l, v = tabung(r,t)
        st.markdown(f'Luas Permukaan $= 2 \pi r(r+t) = (2)(\pi)({r})({r}+{t}) = {round(l,2)} cm^2$')
        st.markdown(f'Volume $= \pi r^2t = (\pi)({r}^2)({t}) = {round(v,2)} cm^3$')

    elif bentuk=="Kerucut":
        img = Image.open('kerucut.png')
        st.image(img)

        d, l, v, s = kerucut(r,t)
        st.markdown(f'Diameter $= 2r = (2)({r}) = {round(d,2)} cm$')
        st.markdown(f'Luas Permukaan $= \pi r (r+s) = (\pi)({r})({r}+{s}) = {round(l,2)} cm^2$')
        st.markdown(f'Volume $= 1/3\pi r^2t = (1/3)(\pi)({r}^2)({t}) = {round(v,2)} cm^3$')

elif bentuk=='Balok':
    p = st.number_input("Panjang (cm)")
    l = st.number_input("Lebar (cm)")
    t = st.number_input("Tinggi (cm)")

    st.write(' ')
    st.write('## **Solution**')

    img = Image.open('balok.png')
    st.image(img)

    luas, v = balok(p,l,t)
    st.markdown(f'Luas Permukaan $= 2 (pl + pt + lt) = 2 ({p}*{l} + {p}*{t} + {l}*{t}) = {round(luas,2)} cm^2$')
    st.markdown(f'Volume $= plt = ({p})({l})({t}) = {round(v,2)} cm^3$')


elif bentuk=='Persegi Panjang':
    panjang = st.number_input("Panjang (cm)")
    lebar = st.number_input("Lebar (cm)")

    st.write(' ')
    st.write('## **Solution**')

    img = Image.open('persegi panjang.png')
    st.image(img)

    keliling, luas, diagonal = p_panjang(panjang, lebar)
    st.markdown(f'Keliling $= 2 * (panjang + lebar) = 2 * ({panjang} + {lebar}) = {round(keliling, 2)} cm$')
    st.markdown(f'Diagonal = {round(diagonal, 2)} cm')
    st.markdown(f'Luas $= panjang * lebar = {panjang} * {lebar} = {round(luas, 2)} cm^2$')

elif bentuk=='Jajar Genjang': # New!
    alas = st.number_input("Alas (cm)")
    tinggi = st.number_input("Tinggi (cm)")

    st.write(' ')
    st.write('## **Solution**')

    img = Image.open('jajar genjang.png')
    st.image(img)

    luas = jajar_genjang(alas, tinggi)
    st.markdown(f'Luas $= alas * tinggi = {alas} * {tinggi} = {round(luas, 2)} cm^2$')

elif bentuk=='Trapesium': # New!
    sisi_a = st.number_input("Sisi a (cm)")
    sisi_b = st.number_input("Sisi b (cm)")
    tinggi = st.number_input("Tinggi (cm)")

    st.write(' ')
    st.write('## **Solution**')

    img = Image.open('trapesium.png')
    st.image(img)

    luas = trapesium(sisi_a, sisi_b, tinggi)
    st.markdown(f'Luas $= (sisi_a + sisi_b) * tinggi / 2 = ({sisi_a} + {sisi_b}) * {tinggi} / 2 = {round(luas, 2)} cm^2$')

elif bentuk=='Segitiga':
    a = st.number_input("Alas (cm)")
    t = st.number_input("Tinggi (cm)")

    st.write(' ')
    st.write('## **Solution**')

    img = Image.open('segitiga.png')
    st.image(img)

    k, l, s= segitiga(a,t)
    st.markdown(f'Keliling $= a + t + s = {a} + {t} + {s} = {round(k,2)} cm$')
    st.markdown(f'Luas $= at/2 = ({a})({t})/2 = {round(l,2)} cm^2$')

# Menjalankan program
# streamlit run devan.py
