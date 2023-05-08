import requests
import base64
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="MY REN ", page_icon=":heart:", layout="wide")

img= Image.open("us.jpg")
fb= Image.open("FB.png")
ig= Image.open("IG.png")
gh= Image.open("GH.png")
gm= Image.open("GM.png")
cvo= Image.open("Cv1.JPG")
cvt= Image.open("Cv2.JPG")
cert= Image.open("Cert.JPG")

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

hide_st_style="""
        <style>
        #MainMenu {visibility:hidden;}
        header {visibility:hidden;}
        footer {visibility:hidden;}
        </style>
        """   
st.markdown(hide_st_style, unsafe_allow_html=True)
lottie_coding =load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_wZSMXs0yM6.json")

lottie1 =load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_9wzu5dlu.json")
lottie2 =load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_cvi9bg1a.json")
lottie3 =load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_xohcppgz.json")
lottie4 =load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_vuxwscfi.json")
lottie5 =load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_hwcplx4x.json")

selected = option_menu(
    menu_title=None,
    options=["About","Document","Contacts"],
    icons=["person","book","envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding":"0!important","background-color":None},
        "icon": {"color":None,"font-size":"25px"},
        "nav-link": {
            "font-size":"25px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#D6594F ",
        },
    }
    )

if selected == "About":
    with st.container():
        extral, left, right, extrar = st.columns((1,2,2,2))
        
        with extral:
            st.markdown("")

        with left:
            st.markdown("")
            st.markdown("""<h1>Hi Ren, Hi Laloves ko!💘</h1>""", unsafe_allow_html=True)

        with right:
            st_lottie(lottie2, height=250, key="wave")

        with extrar:
            st.markdown("")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.markdown("")
            st.markdown("")
            st.header("Everyday ILoveYou💘 ")
            st.markdown("")
            st.subheader("Nandito Lang Ako Palagi Para Sayo Mahal💘 ")
            st.markdown("")
            st.subheader("I Will Always Be Your Sigurado, Payapa At Pahinga 💘💘💘")
            st.markdown("")
            st.subheader("I'm Yours Only Ren💘")
        with right_column:
            st.image(img, width= 450)

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown("")
            st_lottie(lottie_coding, height=300, key="coding")


        with right_column:
            st.header("Dates To Remember")
            st.markdown("")
            st.markdown("")
            st.subheader(":large_blue_diamond: 01/21/23 :beginner:")
            st.markdown("")
            st.subheader(":large_blue_diamond: 02/18/23 :heart:")
            st.markdown("")
    with st.container():
        st.write("---")

if selected == "Document":
    st.write("---")
    st.markdown("")
    st.markdown("")
    left,center, right, extra = st.columns((2,1,1,1))
    with left:
        st.write("")
        st_lottie(lottie1, height=300, key="reading")
    with center:
        with open("CV.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="Download CV", 
            data=PDFbyte,
            file_name="Bryan Colis CV.pdf",
            mime='application/octet-stream')

        st.image(cvo, width= 600)
        st.markdown("")
        st.image(cvt, width= 600)

        with open("OJT.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.markdown("")
        st.markdown("")
        st.download_button(label="Download Certificate of Completion in DICT LC3 OJT", 
            data=PDFbyte,
            file_name="Bryan Colis Certificate.pdf",
            mime='application/octet-stream')
        
        st.image(cert, width= 600)
        

    with right:
        st.write("")
    with extra:
        st.write("")
    
    

if selected == "Contacts":
    with st.container():
        left, center, right = st.columns(3)
        with left:
            st_lottie(lottie5, height=150, key="followm")
        with center:
            st_lottie(lottie4, height=200, key="socmed")
        with right:
            st_lottie(lottie3, height=120, key="follow")
    with st.container():
        st.write("---")
        st.markdown("")
        st.markdown("")
        left,center, right_column, extra = st.columns(4)
        with left:
            st.write("")
        with center:
            st.image(fb, width= 150) 
            st.write("---")
            st.markdown("")
            st.markdown("")
            st.image(ig, width= 150)
            st.write("---")
            st.markdown("")
            st.markdown("")
            st.image(gh, width= 150)
            st.write("---")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.image(gm, width= 150)
            st.write("---")
        with right_column:
            st.markdown("")
            st.markdown("")
            st.markdown("""<h1><a href="https://www.facebook.com/bryan.colis.1">[FACEBOOK]</a></h1>""", unsafe_allow_html=True,)
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("""<h1><a href="https://www.instagram.com/bryan_colis/">[INSTAGRAM]</a></h1>""", unsafe_allow_html=True,)
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("""<h1><a href="https://github.com/Bryan-15">[GITHUB]</a></h1>""", unsafe_allow_html=True,)
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("""<h1><a>[colisbryan15@gmail.com]</a></h1>""", unsafe_allow_html=True,)
        with extra:
            st.write("")
