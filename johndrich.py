
import streamlit as st
from streamlit_option_menu import option_menu
from views import home, projects, team, jda
import time as time
from PIL import Image

img_logo = Image.open("images/jdlogo.jpg")
img_logo2 = Image.open("images/jdlogo2.png")
clar = Image.open("images/transparent1.png")

# -- Sidebar --

menu=["Home", "Projects", "The Team", "OJT", "Content"]

with st.sidebar:
    st.image(img_logo2, width=200)

    st.header("Menu")

    selected = option_menu(
        menu_title=None,
        options=menu,
        icons=["house", "box-seam", "chat-right-quote", "mouse", "collection-play"],
        menu_icon="menu-down",
        default_index=0,
        orientation= "vertical"
    )
# ------------------------------ 1st Page -------------------------------------- #
if selected=="Home":
    import requests
    import streamlit as st
    from streamlit_lottie import st_lottie
    from PIL import Image

    # -- Website for emojis : https://www.webfx.com/tools/emoji-cheat-sheet/ --

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    # -- Images --

    img_logo = Image.open("images/jdlogo.jpg")


    # -- Local CSS Files --
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style/style.css")

    # -- Animations --
    lottie_drawing = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_brpdhwlm.json")
    lottie_computer = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_rdhvjhkp.json")
    lottie_tablet = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_dqr7Sj.json")

    # -- Caching --

    # -- HEADER --
    with st.container():
        image_column, text_column = st.columns((3, 5))
        with image_column:
            st.image(img_logo)
        with text_column:
            st.title("Welcome to :blue[JohnDrich IT Services]")
            st.subheader("A home for HUION, Wacom Drawing Tablets and other IT products.")
            st.write(" ")  # blankspace
            st.write("📘" " [Visit the Facebook Page >](https://www.facebook.com/johndrich.its)")

    # -- 1st Part of Page --
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("🤼" " About us")
            st.write("##")
            st.write(
                """
                In JohnDrich IT services we are the gateway for people who:

                • Want the best deals for drawing tablets and IT products.

                • Want to expand their knowledge in the field of IT.

                • Are aspiring artists with a dream.

                • Are upcoming Engineers, Architects, and Programmers.

                • Are having problems about starting their I.T. career.
                """)
            st.write("##")
            st.write("""

                If this sounds like you, then make sure to contact our [Facebook page](https://www.facebook.com/johndrich.its)
                 and visit our [Showroom](https://goo.gl/maps/5dDCpr5RApJCiF4Y7).
                """
                     )

        with right_column:
            st.write("###")
            st.image(clar)

    # -- 2nd Part of Page --

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        st.markdown("""
        <h3 style='text-align: center; color: black;'>🛒 Shop more at the <a href="https://shopee.ph/johndrich524?categoryId=100644&entryPoint=ShopByPDP&itemId=7854714539">JohnDrich Shopee Page</h3></a>    
        """,
                 unsafe_allow_html=True)

        with left_column:
            st.header("💻" " Our Products")
            st_lottie(lottie_computer, height=380, key="computer")

        with right_column:
            st.header(" ")  # blank space
            st.header(" ")  # blank space
            st.header("HUION")

            st.write(
                "• [HUION Inspiroy RTS300 (H642)](https://shopee.ph/Huion-Inspiroy-RTS300(H642)-i.36626678.667421887?sp_atk=36a33e45-cc55-438c-a94f-f00022fc980e&xptdk=36a33e45-cc55-438c-a94f-f00022fc980e) - ₱2,490")
            st.write(
                "• [HUION Inspiroy RTP700 (H1162)](https://shopee.ph/Huion-Inspiroy-RTP700(H1162)-i.36626678.1349966312?sp_atk=9a2eee78-5a70-45e9-ab9b-f970d2cd8ba8&xptdk=9a2eee78-5a70-45e9-ab9b-f970d2cd8ba8) - ₱5,290")
            st.write(
                "• [HUION Kamvas 13](https://shopee.ph/Huion-Kamvas-13-Without-Stand-i.36626678.8718200755?sp_atk=d953f64d-2637-4b3f-9ee9-a7cf8f45cff3&xptdk=d953f64d-2637-4b3f-9ee9-a7cf8f45cff3) - ₱12,690")
            st.write(
                "• [HUION Kamvas 22 Plus](https://shopee.ph/HUION-KAMVAS-22-PLUS--i.36626678.1755479490?sp_atk=15bb2cb9-1624-4b3c-a887-c4541f5dd0eb&xptdk=15bb2cb9-1624-4b3c-a887-c4541f5dd0eb) - ₱25,190")
            st.write(
                "• [HUION Pro 24 4k Drawing Tablet](https://shopee.ph/Huion-Pro-24-4k-Drawing-Tablet-i.36626678.7854714539?sp_atk=81d64c45-b6e9-4e65-90f0-f5dd9562c57a&xptdk=81d64c45-b6e9-4e65-90f0-f5dd9562c57a) - ₱68,590")

            with left_column:
                st.header("Wacom")
                st.write(
                    "• [One by Wacom Drawing Tablet](https://shopee.ph/One-by-Wacom-Medium-Drawing-Tablet-i.36626678.1349860432?sp_atk=de81fad1-adff-41d8-bb99-30cba408b216&xptdk=de81fad1-adff-41d8-bb99-30cba408b216) - ₱4,990")
                st.write(
                    "• [Wacom Intuos Small](https://shopee.ph/Wacom-Intuos-Small-Wireless-i.36626678.1349484651?sp_atk=7c323772-adee-4eea-a216-fae46657cec6&xptdk=7c323772-adee-4eea-a216-fae46657cec6) - ₱6,390")
                st.write(
                    "• [Wacom Intuos Pro Medium](https://shopee.ph/WACOM-INTUOS-PRO-MEDIUM-i.36626678.1552168074?sp_atk=2be86b0a-1ed2-427b-a032-2956fe3bc2c0&xptdk=2be86b0a-1ed2-427b-a032-2956fe3bc2c0) - ₱22,290")
                st.write(
                    "• [Wacom Cintiq 16 HD](https://shopee.ph/Wacom-Cintiq-16HD--i.36626678.1958517091?sp_atk=e3ab5970-ccb1-48c3-b9b1-1f28de3f4c5c&xptdk=e3ab5970-ccb1-48c3-b9b1-1f28de3f4c5c) - ₱37,890")
                st.write(
                    "• [Wacom Cintiq Pro 16DTH167](https://shopee.ph/WACOM-CINTIQ-PRO-16DTH167-i.36626678.19421304925?sp_atk=7e6693f0-e8ed-435f-80df-c731e5044af5&xptdk=7e6693f0-e8ed-435f-80df-c731e5044af5) - ₱99,590")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")

            with right_column:
                st.header(" ")  # blankspace
                st.header(" ")  # blankspace
                st.header(" ")  # blankspace
                st.header(" ")  # blankspace
                st.header(" ")  # blankspace
                st_lottie(lottie_tablet, height=380, key="tablet")
        st.write("---")

    # -- Contact Us --
    with st.container():
        st.header("💬 Get In Touch With Us")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/zachada.yawa@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="Name" placeholder="Your Name" required>
         <input type="email" name="e=Email" placeholder="Your Email" required>
         <textarea name="Message" placeholder="Your Message" required> </textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

# ----------------------- End of 1st Page ----------------------------- #

if selected=="Projects":
    import requests
    import streamlit as st
    from streamlit_lottie import st_lottie
    from PIL import Image
    import streamlit.components.v1 as components

    img_logo = Image.open("images/jdlogo.jpg")
    img_showroom = Image.open("images/showroom.jpg")
    img_gather = Image.open("images/gather.jpg")

    basewidth = 700
    img_ad = Image.open("images/ad.jpg")
    wpercent = (basewidth / float(img_ad.size[0]))
    hsize = int((float(img_ad.size[1]) * float(wpercent)))
    img_ad = img_ad.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    img_ad.save("images/ad.jpg")


    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/zoom.css")

    with st.container():
        col1, col2, col3 = st.columns((3, 5, 3))
        with col1:
            st.write('')
        with col2:
            st.image(img_logo)
        with col3:
            st.write('')
        st.write("---")
    with st.container():
        components.iframe("https://www.youtube.com/embed/WTsokIo1gQ8", width=float(700), height=float(400))
        col1, col2, col3 = st.columns((1, 5, 1))
        with col1:
            st.write('')
        with col2:
            st.subheader(":blue[JohnDrich] - To you, 100 Years From Now")
            st.write("<h6 style='text-align: center; color: black;'> An advertisement for JohnDrich IT Services made by the OJT workers of batch 2023</h6>",
                     unsafe_allow_html=True, )
        with col3:
            st.write('')

    with st.container():
        padding = 0
        st.markdown(f""" <style>
            .reportview-container .main .block-container{{
                padding-top: {padding}rem;
                padding-right: {padding}rem;
                padding-left: {padding}rem;
                padding-bottom: {padding}rem;
            }} </style> """, unsafe_allow_html=True)

        st.write("---")
        st.title(":blue[JohnDrich] Projects")
        col1, col2, col3 = st.columns((5, 5, 3))
        with col1:
            st.markdown("""
            <div class="img">
            <a href="#bisakol1"><img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t1.15752-9/345739577_626996546142879_1109488999167297136_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeFkBh7WEGx2M_6LKauFsI-EHLhiIWciJ4YcuGIhZyInhq935ZfhSYxC6GgQudJ4QclifPA80BavtPqq0_ctPOg2&_nc_ohc=HSujK4ttDuwAX9hkkes&_nc_ht=scontent.fmnl9-3.fna&oh=03_AdSVReyrHLEfSlzJPGJuNmD0YB1VjPJBAXgKU2alVR1P6A&oe=64816CBC" width="250" height="400" style="border:3px solid #000000; padding:0px; margin:0px">/</a>
            """, unsafe_allow_html=True,
                        )
        with col2:
            st.markdown("""
            <div class="img">
             <a href="#bisakol2"><img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t1.15752-9/345760105_758105239286649_6416624952447299925_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHQwDBrjUjMRDx4aaNdsqPCVxTAH2TsHbtXFMAfZOwduzwlwzC3IOgLsVyqpTR97v_KUAScAx-CWp_AGNzelrHH&_nc_ohc=WtNzU9wGnqkAX-69G5Z&_nc_ht=scontent.fmnl9-3.fna&oh=03_AdTN_9GgGNtyvmDcdAC9HK40M0k0QetHYE38tUb5Pznc4A&oe=6481859F" width="250" height="400" style="border:3px solid #000000; padding:0px; margin:0px">/</a>
             """, unsafe_allow_html=True,
                        )
        with col3:
            st.markdown("""
            <div class="img">
             <a href="#bisakol3"><img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t1.15752-9/345863078_779389020566112_5843879216779392104_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeFlxUw9o5EDbLhCgHbqMhkUXfX0b8XWHoJd9fRvxdYego7pNmAtSUe7MTlFGrW1zATb1blPyZQtk8J4avVCPSBP&_nc_ohc=srgk9vM92DYAX9T6UG6&_nc_ht=scontent.fmnl9-3.fna&oh=03_AdTzqeqtmSv5VpCjKhmIKBCI5PmKUYyq2TPpJYcD9EUSmg&oe=648164A7" width="250" height="400" style="border:3px solid #000000; padding:0px; margin:0px">/</a>
             """, unsafe_allow_html=True,
                        )

    with st.container():
        st.markdown("""
        <img id="bisakol1" src="https://user-images.githubusercontent.com/28086837/61171212-0f84e580-a5a7-11e9-91da-3642d1d42ecc.png" width="1" height="1"></a>
        """, unsafe_allow_html=True, )
        st.write("---")
        st.markdown("""
                <h1>🏠Our Showroom</h1>

        <h5>The Home of JohnDrich IT Services.</h5>
        <div class="table">
            <div class="table-inner">
                <input class="table-open" type="radio" id="table-1" name="table" aria-hidden="true" hidden="" checked="checked">
                <div class="table-item">
                    <img src="https://scontent.fmnl9-2.fna.fbcdn.net/v/t1.15752-9/346068406_762523385578142_5457390876778526509_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHq5C0WvrMBCFCNjvEyPxb_HQR2hur9kNodBHaG6v2Q2j3wFpv9L9KbhuZ00f6bY_jI_PspbW5nNWE38DaDXKc-&_nc_ohc=fAanx6jlOyYAX88FRKj&_nc_ht=scontent.fmnl9-2.fna&oh=03_AdRX8gTqSxWCU56aJ_d4SBdeKWADeOrJH6zaqO-qcSzmvg&oe=648EDA05">
                </div>
                <input class="table-open" type="radio" id="table-2" name="table" aria-hidden="true" hidden="" checked="checked">
                <div class="table-item">
                    <img src="https://scontent.fmnl9-2.fna.fbcdn.net/v/t1.15752-9/346053548_1305958183605835_5674481828595390411_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHL5VhjXdioohO6J73q88uG0rR2nZ2b86nStHadnZvzqdFPqNoA2QpO2TPAJi-5Xdj5UM4e4Ul50VTPllZwtWwU&_nc_ohc=HBz3ogavZM8AX9d1GF7&_nc_ht=scontent.fmnl9-2.fna&oh=03_AdRUiXGtGi8uQR7mVkmVcIkO5rzuChUkGeFCM82INszk1w&oe=648EA985">
                </div>
                <input class="table-open" type="radio" id="table-3" name="table" aria-hidden="true" hidden="" checked="checked">
                <div class="table-item">
                    <img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t1.15752-9/345967434_1397300811062012_1128121003778787622_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGtAYIiv0QewMMOGlWIY80T92grtvUdUYP3aCu29R1Rg6XrTFI6J-wZUCKOFEn3kAED1UXIHc1jtRxfBcNBuB65&_nc_ohc=DHZ5vyEiAUUAX8v_nVD&_nc_ht=scontent.fmnl9-3.fna&oh=03_AdRw8UEJdDRgYvlPs6YG-RqOEdSaP36m5_KRiLnUXc76Zw&oe=648ECAD6">
                </div>
                <input class="table-open" type="radio" id="table-4" name="table" aria-hidden="true" hidden="" checked="checked">
                <div class="table-item">
                    <img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t1.15752-9/346051294_159617943506339_1565967623981802964_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeG0Ji7bmNukQgAOKmm1psRMqEHN1_ZkyYeoQc3X9mTJh0pVBD3KmrJV6GveQxi8Rdt1D2ITi97nBKdo7s9ytkn0&_nc_ohc=DgBlMw8Ixa4AX9O0TOZ&_nc_ht=scontent.fmnl9-3.fna&oh=03_AdTdkRUsTO6C4INlLBHZZe7xNiIeZSjIbjTzfCwUQ4bsdg&oe=648EDB1E">
                </div>
                <label for="table-4" class="table-control next control-3">›</label>
                <label for="table-3" class="table-control prev control-4">‹</label>
                <label for="table-2" class="table-control next control-1">›</label>
                <label for="table-1" class="table-control prev control-2">‹</label>
                <label for="table-4" class="table-control prev control-1">‹</label>
                <label for="table-3" class="table-control next control-2">›</label>
                <label for="table-2" class="table-control prev control-3">‹</label>
                <label for="table-1" class="table-control next control-4">›</label>
                <ol class="table-indicators">
                    <li>
                        <label for="table-1" class="table-bullet">•</label>
                    </li>
                    <li>
                        <label for="table-2" class="table-bullet">•</label>
                    </li>
                    <li>
                        <label for="table-3" class="table-bullet">•</label>
                    </li>
                    <li>
                        <label for="table-4" class="table-bullet">•</label>
                    </li>
                </ol>
            </div>
        </div>
                """, unsafe_allow_html=True, )

        st.write("---")
        st.markdown("""
                      <img id="bisakol2" src="https://user-images.githubusercontent.com/28086837/61171212-0f84e580-a5a7-11e9-91da-3642d1d42ecc.png" width="1" height="1"></a>
                      """, unsafe_allow_html=True, )
        st.markdown("""
                <h1>📆 JohnDrich - The Gathering</h1>

        <h5>JohnDrich Event of November 2019.</h5>
        <div class="carousel">
            <div class="carousel-inner">
                <input class="carousel-open" type="radio" id="carousel-1" name="carousel" aria-hidden="true" hidden="" checked="checked">
                <div class="carousel-item">
                    <img src="https://scontent.fmnl3-4.fna.fbcdn.net/v/t1.6435-9/78177545_3126132127413253_2333111949849526272_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=cdbe9c&_nc_eui2=AeED6L8xD5nWHs_OuXQtbTYMbFu_ymYkd5xsW7_KZiR3nPVaMc3pbMrW2o89OTuEFwkzSv9UVbMwD-g80_6h8GtH&_nc_ohc=AdwFfcTkxJ8AX_AUF4N&_nc_ht=scontent.fmnl3-4.fna&oh=00_AfBU5eAv74qTfEbRPOPHgaGM6QuV-hm9B1ULgE02Ygx3Pg&oe=6492451D">
                </div>
                <input class="carousel-open" type="radio" id="carousel-2" name="carousel" aria-hidden="true" hidden="" checked="checked">
                <div class="carousel-item">
                    <img src="https://scontent.fmnl3-2.fna.fbcdn.net/v/t1.15752-9/346163469_605023208254260_5381969382819487706_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeE6JfT7dGidAWVoYgyjy5OiI9OcJ5Lf1ccj05wnkt_Vx28EQDtJLC_WOdQqebtUASUmf0BpHEnxGrJSNPdzXAlu&_nc_ohc=RvXBl58wzAYAX_jyJbu&_nc_oc=AQm88bhgqtrE1iBGRrTbFgY3VWtpdAiyjKNWvz5tLWjOpXuT8Cyr6nj-LZp6yiSYL9I&_nc_ht=scontent.fmnl3-2.fna&oh=03_AdRqYgDwe9Xc6v_3WMajzEl40847XeAG7ABvy3_33aY8Tw&oe=64924413">
                </div>
                <input class="carousel-open" type="radio" id="carousel-3" name="carousel" aria-hidden="true" hidden="" checked="checked">
                <div class="carousel-item">
                    <img src="https://z-p3-scontent.fmnl25-3.fna.fbcdn.net/v/t1.15752-9/346131879_275744474836742_3745965704671868106_n.png?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeE4qJSbnR1QN9XsLz3eYt47ezhz3zbgNPB7OHPfNuA08BY9LYqvg89OJeGNeJs49omhLF7-ZloVbSHzAGT1Bx1b&_nc_ohc=NN_rMzJUSCkAX-hgQr-&_nc_ht=z-p3-scontent.fmnl25-3.fna&oh=03_AdST2LJ2AGvMW5zHJVOx4rk_PW-oZv3_14CzbelbONVZBg&oe=64925EF9">
                </div>
                <input class="carousel-open" type="radio" id="carousel-4" name="carousel" aria-hidden="true" hidden="" checked="checked">
                <div class="carousel-item">
                    <img src="https://scontent.fmnl3-1.fna.fbcdn.net/v/t1.15752-9/346132765_2450125405169054_399009606626230458_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeEC7SM2i4QnxeWXxY9AD58RvYLe0L_36LW9gt7Qv_fotXom_bk_SjAaMpUuh0ygqUzmrOpRiiecfNFTo6mMiW7H&_nc_ohc=NHBb_O6f6y0AX-YsWWf&_nc_ht=scontent.fmnl3-1.fna&oh=03_AdSq8zBczCK0UKTdWUmysDys9kM0FCz60fiEBZiAq-TmGA&oe=649243B6">
                </div>
                <label for="carousel-4" class="carousel-control next control-3">›</label>
                <label for="carousel-3" class="carousel-control prev control-4">‹</label>
                <label for="carousel-2" class="carousel-control next control-1">›</label>
                <label for="carousel-1" class="carousel-control prev control-2">‹</label>
                <label for="carousel-4" class="carousel-control prev control-1">‹</label>
                <label for="carousel-3" class="carousel-control next control-2">›</label>
                <label for="carousel-2" class="carousel-control prev control-3">‹</label>
                <label for="carousel-1" class="carousel-control next control-4">›</label>
                <ol class="carousel-indicators">
                    <li>
                        <label for="carousel-1" class="carousel-bullet">•</label>
                    </li>
                    <li>
                        <label for="carousel-2" class="carousel-bullet">•</label>
                    </li>
                    <li>
                        <label for="carousel-3" class="carousel-bullet">•</label>
                    </li>
                    <li>
                        <label for="carousel-4" class="carousel-bullet">•</label>
                    </li>
                </ol>
            </div>
        </div>
                """, unsafe_allow_html=True, )
        st.write("###")
        components.iframe("https://drive.google.com/file/d/1urcuNQYnDhiMU7UE1Gqk0REVgTK4cFZz/preview", width=float(700),
                          height=float(350))
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        local_css("style/table.css")

        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        local_css("style/carousel.css")
        st.write("---")
        st.markdown("""
               <img id="bisakol3" src="https://user-images.githubusercontent.com/28086837/61171212-0f84e580-a5a7-11e9-91da-3642d1d42ecc.png" width="1" height="1"></a>
               """, unsafe_allow_html=True, )
        st.markdown("""
                                <h1> 🏋️‍♂️JohnDrich OJT Work Immersion</h1>

                        <h5> OJT Workers of Batch 2023.</h5>
                        <div class="tableojt">
                            <div class="tableojt-inner">
                                <input class="tableojt-open" type="radio" id="tableojt-1" name="tableojt" aria-hidden="true" hidden="" checked="checked">
                                <div class="tableojt-item">
                                    <img src="https://z-p3-scontent.fmnl25-3.fna.fbcdn.net/v/t1.15752-9/341958343_914615619594761_8476305713564202027_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeENthTS8QiGp2stOF8UdZwkKf1ThLR5m-gp_VOEtHmb6BKW8pJl4bQrFQfoeQKpG9ZjHfL9kes1_6AWQ_uVyDoC&_nc_ohc=rgopjvySv4AAX_OK79K&_nc_ht=z-p3-scontent.fmnl25-3.fna&oh=03_AdQc9-HzDVLRWq4Kx_asD-rY2FN0dYpZnc63wGCZvJEydQ&oe=649298C5">
                                </div>
                                <input class="tableojt-open" type="radio" id="tableojt-2" name="tableojt" aria-hidden="true" hidden="" checked="checked">
                                <div class="tableojt-item">
                                    <img src="https://z-p3-scontent.fmnl25-4.fna.fbcdn.net/v/t1.15752-9/346144045_256212797077234_3457793238193450966_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHgV1rMhDs01P4f6SK1EfP4ZOdRP5oRkplk51E_mhGSmeU8AEOiMw_YEZqiqIBjWKIBQ3fVDHPSHCDhiLzt8_tf&_nc_ohc=rVsLaFPFB3YAX94nvbV&_nc_oc=AQk4nIpSZPXB23lYI4y5t8tmQLAYHroFALOaztTs5gPsECvnT46c2R_cp27Vle1C5yY&_nc_ht=z-p3-scontent.fmnl25-4.fna&oh=03_AdRqQcW_TgCHfjx-acdkUIFc3n5Z5dnciTirntJUKXv3ng&oe=6492748D">
                                </div>
                                <input class="tableojt-open" type="radio" id="tableojt-3" name="tableojt" aria-hidden="true" hidden="" checked="checked">
                                <div class="tableojt-item">
                                    <img src="https://z-p3-scontent.fmnl25-4.fna.fbcdn.net/v/t1.15752-9/342891555_183800474549750_973216371791576636_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGwhf_q6nPhzh00WrkvzxYOdyYQh_AWt-Z3JhCH8Ba35r75wH3tE8YsWwlApIXH1SI0AgeKQJM-sCNLm1-UkBig&_nc_ohc=pLzQeinJrygAX-7FiAP&_nc_ht=z-p3-scontent.fmnl25-4.fna&oh=03_AdT4pnP07XJlBrad-Lw0VUAugROor1IHppoQtFaoJ1QAgw&oe=64927529">
                                </div>
                                <input class="tableojt-open" type="radio" id="tableojt-4" name="tableojt" aria-hidden="true" hidden="" checked="checked">
                                <div class="tableojt-item">
                                    <img src="https://z-p3-scontent.fmnl25-1.fna.fbcdn.net/v/t1.15752-9/344602022_206253485544088_7125958233968680124_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeERX1qO5_0EGRn9ew1Inzf_vCcVTj5BzhC8JxVOPkHOENe5GUojWj5Vt0m-QKfmGqVMIP1sdqtDwggxWRDPlSYc&_nc_ohc=dgc4b_SIrSIAX9Q2Ffs&_nc_ht=z-p3-scontent.fmnl25-1.fna&oh=03_AdRfNodVgbWBPqItRal_NlIV9jey89lFa-DGaOiWe7po8Q&oe=64928154">
                                </div>
                                <label for="tableojt-4" class="tableojt-control next control-3">›</label>
                                <label for="tableojt-3" class="tableojt-control prev control-4">‹</label>
                                <label for="tableojt-2" class="tableojt-control next control-1">›</label>
                                <label for="tableojt-1" class="tableojt-control prev control-2">‹</label>
                                <label for="tableojt-4" class="tableojt-control prev control-1">‹</label>
                                <label for="tableojt-3" class="tableojt-control next control-2">›</label>
                                <label for="tableojt-2" class="tableojt-control prev control-3">‹</label>
                                <label for="tableojt-1" class="tableojt-control next control-4">›</label>
                                <ol class="tableojt-indicators">
                                    <li>
                                        <label for="tableojt-1" class="tableojt-bullet">•</label>
                                    </li>
                                    <li>
                                        <label for="tableojt-2" class="tableojt-bullet">•</label>
                                    </li>
                                    <li>
                                        <label for="tableojt-3" class="tableojt-bullet">•</label>
                                    </li>
                                    <li>
                                        <label for="tableojt-4" class="tableojt-bullet">•</label>
                                    </li>
                                </ol>
                            </div>
                        </div>
                                """, unsafe_allow_html=True, )
        st.write("###")
        components.iframe("https://www.youtube.com/embed/wQL_JZtinu0", width=float(700), height=float(400))


        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style/tableojt.css")
        st.write("---")

if selected=="The Team":
    import streamlit as st
    from streamlit.components.v1 import html

    st.title("👬 Meet the Team")
    st.write("---")
    st.subheader("• Strategic Planning Department")
    st.write("###")
    st.markdown("""
        <div class="row">
      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl25-5.fna.fbcdn.net/v/t39.30808-6/342351110_613525214018213_5981432779924882055_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeH7UxxaZuWnOIZXBX2r5-Tw9v51pqnUunP2_nWmqdS6c8ESfe-3ZcrmtAT30vEmJDoSXao4PtodVr6xdKlDB-m9&_nc_ohc=mX3XYv6jgB0AX8WEaSw&_nc_zt=23&_nc_ht=scontent.fmnl25-5.fna&oh=00_AfBcNcsWeoS2oaWABf5CZxvXlJIXTb9VicmPljXpx5l0EQ&oe=647021A0" alt="Jane" style="width:100%">
          <div class="container">
            <h3 class="nameAljohn"> Aljohn "Work Ethics" Gutierrez</strong></h3> </h3>
            <p class="title">Leader/ Supervisor</p>
            <p> Babawasan ka ng points pag di ka umayos</p>
            <p><a href="https://web.facebook.com/aljohnpeter.gutierrez?_rdc=1&_rdr"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>

    <div class="row">
      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t39.30808-6/322498088_535354225323963_3135976692610434405_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeHMikTlDK_J21cPtG0PapOIstGA4BBgtBey0YDgEGC0F4LGuAbb1HPqrBtXghwgvff3etcKWW5fz1qMBMse1R4F&_nc_ohc=sOQJ9pPH5N0AX8_yngC&_nc_oc=AQm87iUAGq09RTkRgHZgefMHUJ_T-BqFaRRWBTHmtR2Bg1SCJApEPqMiJenB_iItCXJ59ogWfAdAT_8chN1XFQNh&_nc_ht=scontent.fmnl9-3.fna&oh=00_AfDj6_TwMhXInMtEulS1-TJmRVUUd5kop27M87ICRKpaaA&oe=6471C81A" alt="Jane" style="width:100%">
          <div class="container">
            <h3 class="nameClar">Clarence "Penge ng GF" <strong>Delrosario</strong></h3>
            <p class="title">Leader/Artist</p>
            <p>Wala paring girlfriend hanggang ngayon</p>
            <p><a href="https://www.facebook.com/clarence30.delrosario"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>

      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl33-4.fna.fbcdn.net/v/t1.6435-9/132208412_3892036127528902_7097265032218286629_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeEiu7hrIYCSrNUoQfm8bYlwma8PPgIQVC6Zrw8-AhBULhNBLa0FILRRFYN5w-pW38G5Cr9Vi2CjdBhsHoKMf8or&_nc_ohc=M5VRdf9M204AX__8mfe&_nc_ht=scontent.fmnl33-4.fna&oh=00_AfBz64sSOAi5qb7d2V6Np677ohrjYTfDhiit6vyH7_p6ZA&oe=6483BEF2" alt="Jane" style="width:100%">
          <div class="container">
            <h4 class="nameCarl2">Carl "Gusto ko na Umuwi" Mangune</h4>
            <p class="title">Leader/Architect</p>
            <p>Ok lang yan kahit di pantay, di naman mapapansin</p>
            <p><a href="https://www.facebook.com/illinoiss.fe"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>
      
    <div class="row">
      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t39.30808-6/320591777_650210293464318_3620581362099258986_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeF5_lm3a3_7iiPuE9sbUe_NcyIcUaL-qQVzIhxRov6pBfxxyqzflGD0K_Ab0M5wobQhJkeD_Maimvn7vuWla6-f&_nc_ohc=HJ8CJZhf41YAX_t89Mi&_nc_oc=AQkChszScsNA_KmWp-jqFQlruyO2K86g56mFZ4QgQC8BKCHRMCWTsX--p1G4ezTQDqmiJ9n3rQN_-GdtlrmnpEW4&_nc_ht=scontent.fmnl9-3.fna&oh=00_AfA94RmHGu50fa5YItOafiYll2fjnXqLW2QsMGkosSRA7w&oe=6472096E" alt="Jane" style="width:95%">
          <div class="container">
            <h4 class="nameCarl">Jacob "2 Hours Biyahe" David</h4>
            <p class="title">Leader/Architect</p>
            <p>Pre pls umuwi na tayo 5 na gagabihin ako</p>
            <p><a href="https://www.facebook.com/Scriptlinx"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>
              <div class="row">
      <div class="column">
        <div class="card">
          <img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/343749927_568507501934028_33051919848196045_n.jpg?stp=dst-jpg_s403x403&_nc_cat=101&ccb=1-7&_nc_sid=aee45a&_nc_eui2=AeHKi59uPp_64Qd2_qZngtgE-KAe0bLBqfL4oB7RssGp8tcWhBB4rWn30vccFVXmvxJYkKgYhbAnxh5Xszd5ckz6&_nc_ohc=GnTjmadyCxwAX-QqC8a&_nc_oc=AQlPlMrxHbr6WuEHXH-mKcEHiwYwgtOVU1_MH_ZycTE8cfzfdFkeWwhBv_-7UIPoLVCSm46edFreMnY94NRwpB6M&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRuAuEm9LIQ5MRH8uDwyAbFL47F8Cp0t2g_JLvCWTAB0w&oe=6484042F" alt="Jane" style="width:95%">
          <div class="container">
            <h4 class="nameBrian">Brian "Lover Boy" Dilig</h4>
            <p class="title">Leader/ IT</p>
            <p>Nag-iiba personality pag inlove</p>
            <p><a href="https://www.facebook.com/brian.dilig"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>
        """, unsafe_allow_html=True, )
    st.write("---")
    st.subheader("• Animation Department")
    st.write("###")
    st.markdown("""
    <div class="row">
  <div class="column">
    <div class="card">
      <img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t39.30808-6/322498088_535354225323963_3135976692610434405_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeHMikTlDK_J21cPtG0PapOIstGA4BBgtBey0YDgEGC0F4LGuAbb1HPqrBtXghwgvff3etcKWW5fz1qMBMse1R4F&_nc_ohc=sOQJ9pPH5N0AX8_yngC&_nc_oc=AQm87iUAGq09RTkRgHZgefMHUJ_T-BqFaRRWBTHmtR2Bg1SCJApEPqMiJenB_iItCXJ59ogWfAdAT_8chN1XFQNh&_nc_ht=scontent.fmnl9-3.fna&oh=00_AfDj6_TwMhXInMtEulS1-TJmRVUUd5kop27M87ICRKpaaA&oe=6471C81A" alt="Jane" style="width:100%">
      <div class="container">
        <h3 class="nameClar">Clarence "Penge ng GF" <strong>Delrosario</strong></h3>
        <p class="title">Leader/Artist</p>
        <p>Wala paring girlfriend hanggang ngayon</p>
        <p><a href="https://www.facebook.com/clarence30.delrosario"><button class="button">Contact</button></p></a>
      </div>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t39.30808-6/329006041_574903844573794_6957607425541989308_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeHjaDtrZ5-4At6TVVbY68RavulE2oYSFae-6UTahhIVp33SQqm6ELQ36MAJiFYNYbWOfLzo_k6uzSaZ1iPHt9sE&_nc_ohc=i4TUuyWi0C4AX_4i9qT&_nc_ht=scontent.fmnl9-3.fna&oh=00_AfCvBU43iQMKdQW7shAhyDkmoKtvFLHOpafrqhWem3FQGA&oe=64721F2E" alt="Mike" style="width:100%">
      <div class="container">
        <h4 class="nameKyle">Kyle "Pa-order ng Siomai Rice" Fernandez</h4>
        <p class="title">Animator</p>
        <p>7 Piece Siomai ulit. wag mo kalimutan yung gulaman</p>
        <p><a href="https://www.facebook.com/kylecedrick.fernandez.50"><button class="button">Contact</button></p></a>
      </div>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <img src="https://scontent.fmnl9-2.fna.fbcdn.net/v/t39.30808-6/251136930_910674186226832_6441802131631541053_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeFvaxVV0I_wANis5W-mfmZZI9jaMDRjtTEj2NowNGO1Mae77MhPlEInUk3ucEoY9o_bPyROGclgJU1kuZGUOTEr&_nc_ohc=ufOfMm9DCUcAX9YSOHU&_nc_oc=AQnVscO3fzQjBNj8vyq-6kHxdWTyULN8P6j3lsYZ99DTB1gwSEdgqn6U2g34sneGKyZys9BZYx_8njLUXJTzYRA1&_nc_ht=scontent.fmnl9-2.fna&oh=00_AfBhDyG8J-XBAIQ3WeK7W4DY8-5-Dz-pduaqMgBZ9jKqkw&oe=647267C1" alt="John" style="width:100%">
      <div class="container">
        <h4>Franchesca "Lumipat ng IT" Gubat </h4>
        <p class="title">Architect</p>
        <p>Nag-aaral na mag HTML at CSS </p>
        <p><a href="https://www.facebook.com/franchesca.gubat"><button class="button">Contact</button></p></a>
      </div>
    </div>
  </div>
</div>
 <div class="column">
    <div class="card">
      <img src="https://scontent.fmnl33-3.fna.fbcdn.net/v/t1.6435-9/200940879_1744991429041803_2005675647221889139_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeFMYBeNrjl3UxhSe_L4LAKv1C5r2wCb8aLULmvbAJvxov3TCeFaf5uiB5oz_B07utuSVAu8bAHK2YTU9Nl1fzwK&_nc_ohc=cMwYOoKgo1kAX-zfB1r&_nc_ht=scontent.fmnl33-3.fna&oh=00_AfBwfmV2yVH9EQ97wu86nZkSnc1qOb59MB2rmHlXMt7CdA&oe=6483B38C" alt="John" style="width:100%">
      <div class="container">
        <h4>Althe "Na-stress sa Autocad" Sosing</h4>
        <p class="title">Marketer</p>
        <p>Ayaw na mag Autocad</p>
        <p><a href="https://www.facebook.com/althesosing05"><button class="button">Contact</button></p></a>
      </div>
    </div>
  </div>
</div>
    """, unsafe_allow_html=True, )
    st.write("---")
    st.subheader("• JG Builders")
    st.write("###")
    st.markdown("""
        <div class="row">
      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl33-4.fna.fbcdn.net/v/t1.6435-9/132208412_3892036127528902_7097265032218286629_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeEiu7hrIYCSrNUoQfm8bYlwma8PPgIQVC6Zrw8-AhBULhNBLa0FILRRFYN5w-pW38G5Cr9Vi2CjdBhsHoKMf8or&_nc_ohc=M5VRdf9M204AX__8mfe&_nc_ht=scontent.fmnl33-4.fna&oh=00_AfBz64sSOAi5qb7d2V6Np677ohrjYTfDhiit6vyH7_p6ZA&oe=6483BEF2" alt="Jane" style="width:100%">
          <div class="container">
            <h4 class="nameCarl">Carl "Gusto ko na Umuwi" Mangune</h4>
            <p class="title">Leader/Architect</p>
            <p>Ok lang yan kahit di pantay, di naman mapapansin</p>
            <p><a href="https://www.facebook.com/illinoiss.fe"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>

      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t39.30808-6/269893599_1092177584888664_579414072975544248_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeGjT7omag0VS-nCoXTHeBmB0BrM4gVNZn3QGsziBU1mfdyG5SaSF47MMTiaiY9dfzkSeeXvmEji5sb3Zacc_4n5&_nc_ohc=8y26Ns6Trw4AX8AEzmX&_nc_ht=scontent.fmnl9-3.fna&oh=00_AfD3S5AHjDjK06Cm_H38udV51P3wjUbRzb_V0kvQTea4yw&oe=6471CD48" alt="Mike" style="width:100%">
          <div class="container">
            <h4 class="nameDulay">Adrian "May Natapakan" Dulay</h4>
            <p class="title">Architect/ IT</p>
            <p>Pa-tanong nalang kung ano yung natapakan nya</p>
            <p><a href="https://www.facebook.com/adrianpaul.dulay.7"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>

      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl3-2.fna.fbcdn.net/v/t1.15752-9/345956623_1527430371120117_8484625550281575720_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGxiutpAxgpk5LPK1xdldHggVuix1yMbxiBW6LHXIxvGCPneX8k1helitdhR6HnL352VCgrmGDf8dknfY-9-Vof&_nc_ohc=ZWQLtgpv1EQAX-qwAqm&_nc_ht=scontent.fmnl3-2.fna&oh=03_AdTN1FmJ7WVj5XVVP_Rlh_0Jg1kx5_19SFiJvOwlSAJM3Q&oe=6483F16F" alt="John" style="width:100%">
          <div class="container">
            <h4 class="nameBondal">Jeremy "Barako"Bondal</h4>
            <p class="title">Engineer/ Marketing</p>
            <p>Ang pait ng kape. Ayaw mag creamer</p>
            <p><a href="https://www.facebook.com/jeremy.bondal"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>
    </div>
     <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl9-4.fna.fbcdn.net/v/t39.30808-6/333516627_1257188091549435_7697713599624126804_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeH0rzDa5FyVE2u6-t1IF-_-GOMgbRaPzUEY4yBtFo_NQSs-SC8YtIqME7Mgso-8VjFpzTEnSuii0-A8ktnq8fBf&_nc_ohc=3zQb_snRU9gAX-morDx&_nc_ht=scontent.fmnl9-4.fna&oh=00_AfBHULcl6PEukbA3ZUbXy6nI2qvG9aOIm_El2fY6WamjOw&oe=647106F1" alt="John" style="width:100%">
          <div class="container">
            <h4>Zach "Python Lang" Adaya</h4>
            <p class="title">IT</p>
            <p>Akala ko python lang? Bat nag-aaral na ako ng javascript?!</p>
            <p><a href="https://www.facebook.com/zahcpogi"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>
    </div>
        """, unsafe_allow_html=True, )
    st.write("---")
    st.subheader("• System Development")
    st.write("###")
    st.markdown("""
        <div class="row">
      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl9-3.fna.fbcdn.net/v/t39.30808-6/320591777_650210293464318_3620581362099258986_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeF5_lm3a3_7iiPuE9sbUe_NcyIcUaL-qQVzIhxRov6pBfxxyqzflGD0K_Ab0M5wobQhJkeD_Maimvn7vuWla6-f&_nc_ohc=HJ8CJZhf41YAX_t89Mi&_nc_oc=AQkChszScsNA_KmWp-jqFQlruyO2K86g56mFZ4QgQC8BKCHRMCWTsX--p1G4ezTQDqmiJ9n3rQN_-GdtlrmnpEW4&_nc_ht=scontent.fmnl9-3.fna&oh=00_AfA94RmHGu50fa5YItOafiYll2fjnXqLW2QsMGkosSRA7w&oe=6472096E" alt="Jane" style="width:95%">
          <div class="container">
            <h4 class="nameCarl">Jacob "2 Hours Biyahe" David</h4>
            <p class="title">Leader/Architect</p>
            <p>Pre pls umuwi na tayo 5 na gagabihin ako</p>
            <p><a href="https://www.facebook.com/Scriptlinx"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>

      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl3-2.fna.fbcdn.net/v/t1.15752-9/346110530_195949536713042_8690722925843117388_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGWffQpz2VPtCWC2YRyvLw2uXxS0JVmS6O5fFLQlWZLo4upPlnidBaImXUINCZCMBw-WL4vAWo5rIPqA1yMuSvq&_nc_ohc=ed05z_qDcfYAX9K3T2e&_nc_ht=scontent.fmnl3-2.fna&oh=03_AdRu8dRKs_nSwiXPAaAzDbp0PbStXZBtZojpeisYteCTBg&oe=6483CD5B" alt="Mike" style="width:100%">
          <div class="container">
            <h4 class="nameJayson">Jayson "Breakdown" Alcano</h4>
            <p class="title"> IT</p>
            <p>Hindi ko nagugustuhan ang pangyayari</p>
            <p><a href="https://www.facebook.com/profile.php?id=100059818312663"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>

      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl3-1.fna.fbcdn.net/v/t1.15752-9/346009413_258146373260499_5925647481914794308_n.png?_nc_cat=108&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeF1thKLSiBD-x2UFVgxzRwLG6PLqZOHM1Ybo8upk4czVqTszORjKUuJkri513Ffk70PN-c38mvFrQ-pTojmha5D&_nc_ohc=kAcDZgl9X9YAX93t39x&_nc_ht=scontent.fmnl3-1.fna&oh=03_AdQo4sMqRgedX-zJjOIvD6jSjbfKy6Wrw6DECyWH-5wnOA&oe=64841E7B" alt="John" style="width:99%">
          <div class="container">
            <h4 class="nameBondal">Natasha "Nag Code na rin" Paguirigan</h4>
            <p class="title">Architecture/ Engineering</p>
            <p>Ano department mo? Depende</p>
            <p><a href="https://www.facebook.com/profile.php?id=100056190421822"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>
    </div>
     <div class="column">
        <div class="card">
          <img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/346094783_913684296393109_2796429124695029669_n.jpg?stp=dst-jpg_s403x403&_nc_cat=108&ccb=1-7&_nc_sid=aee45a&_nc_eui2=AeHxMiekMEX_HlZgnheyMcVJRScvdEAVfFtFJy90QBV8W56TqYdmV2_kB1E0FBf9gc_BS8c85dWbhv8jCNtd2zpQ&_nc_ohc=gWRR8Fa8qSQAX8u70S2&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdTmpkcDC4OyXveVjDmlEB7wQ7ok8c_Ip2c0OMqOjK709Q&oe=64841A75" alt="John" style="width:100%">
          <div class="container">
            <h4> Angela "Architect God" Almodovar</h4>
            <p class="title">Architect</p>
            <p>Wala ako malagay AHHAHA grabe nginawngaw yung architecture</p>
            <p><a href="https://www.facebook.com/gela.almodovar"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>
    </div>
        """, unsafe_allow_html=True, )

    st.write("---")
    st.subheader("• IT Training Center")
    st.write("###")
    st.markdown("""
        <div class="row">
      <div class="column">
        <div class="card">
          <img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/343749927_568507501934028_33051919848196045_n.jpg?stp=dst-jpg_s403x403&_nc_cat=101&ccb=1-7&_nc_sid=aee45a&_nc_eui2=AeHKi59uPp_64Qd2_qZngtgE-KAe0bLBqfL4oB7RssGp8tcWhBB4rWn30vccFVXmvxJYkKgYhbAnxh5Xszd5ckz6&_nc_ohc=GnTjmadyCxwAX-QqC8a&_nc_oc=AQlPlMrxHbr6WuEHXH-mKcEHiwYwgtOVU1_MH_ZycTE8cfzfdFkeWwhBv_-7UIPoLVCSm46edFreMnY94NRwpB6M&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRuAuEm9LIQ5MRH8uDwyAbFL47F8Cp0t2g_JLvCWTAB0w&oe=6484042F" alt="Jane" style="width:95%">
          <div class="container">
            <h4 class="nameBrian">Brian "Lover Boy" Dilig</h4>
            <p class="title">Leader/ IT</p>
            <p>Nag-iiba personality pag inlove</p>
            <p><a href="https://www.facebook.com/brian.dilig"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>

      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl3-1.fna.fbcdn.net/v/t1.15752-9/345967441_758017682446201_4362207776001777646_n.png?_nc_cat=108&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHRxXQTXDRWUdHGyoLo7-Ceovp-y9Tfg9Si-n7L1N-D1CD90GXd43eXmw7z-5vuV9VkmmYMq1g-KWdmtSDSEZPi&_nc_ohc=yZzL2ANELjgAX94XKKh&_nc_ht=scontent.fmnl3-1.fna&oh=03_AdTwVnPaLSPPfqoJ3Rg_KdgdmTD01NVRvdfRAbJl3d5KHQ&oe=648410FC" alt="Mike" style="width:88%">
          <div class="container">
            <h4 class="nameJayson">Julius "Tinapay" Reynosa </h4>
            <p class="title">IT</p>
            <p>I love Sibuyas and Onion and tinapay</p>
            <p><a href="https://www.facebook.com/reyus.kazuki.3"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>

      <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl9-1.fna.fbcdn.net/v/t39.30808-6/333692994_159877390237948_3278638485997279866_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=174925&_nc_eui2=AeF0Eb6O5ZAyMtpnG0ea5QcEeHj74UcZ8vZ4ePvhRxny9jVdnj-6cm81rbJ-qECe27GbI6_GgLx5x0QrtHxJDM97&_nc_ohc=K-7_SeZaLx4AX_XsWpW&_nc_ht=scontent.fmnl9-1.fna&oh=00_AfDY82JqbmGbm-4PevPIcmXpGUI2oz_1Es-hwOPd_lfPHQ&oe=6472323D" alt="John" style="width:100%">
          <div class="container">
            <h4 class="nameBondal">Rheayln "LeBron" Narsico</h4>
            <p class="title">IT</p>
            <p>Titiktokan ka neto pag di ka tumigil</p>
            <p><a href="https://www.facebook.com/rhlynnrsc"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>
    </div>
     <div class="column">
        <div class="card">
          <img src="https://scontent.fmnl25-4.fna.fbcdn.net/v/t1.15752-9/346030771_1335156053716112_8995745933584428986_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeFTqM4okn6sUYHvtyZQOYvYzasiursXxZbNqyK6uxfFlq9BTOSRowJ60KqV3ZJq7qBCBjBBt6Q5wJMrQ2zog48P&_nc_ohc=wayrpiUGSgAAX9fWyUj&_nc_ht=scontent.fmnl25-4.fna&oh=03_AdQkWezMPgamUghEnsJX4zL-zXMpnRi-xMjFmotDCEYUzg&oe=648D5ABE" alt="John" style="width:100%">
          <div class="container">
            <h4> Vincent "R. Papa" Cubay</h4>
            <p class="title">Engineering</p>
            <p>Si Papa, si Mama, si Kuya, si Ate, si Baby </p>
            <p><a href="https://www.facebook.com/vincentcubs"><button class="button">Contact</button></p></a>
          </div>
        </div>
      </div>
    </div>
        """, unsafe_allow_html=True, )

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style/team.css")

if selected=="OJT":
    import streamlit.components.v1 as components

    with st.container():
        col1, col2, col3 = st.columns((3, 5, 3))
        with col1:
            st.write('')
        with col2:
            st.image(img_logo)
        with col3:
            st.write('')
    with st.container():
        option = st.selectbox(
            'Projects of the OJT Workers',
            ('Overview', 'Animation', 'Architecture', 'Engineering', 'IT',))

        if option == 'Overview':
            col1, col2, = st.columns((3, 3))
            with col1:
                    IT = st.markdown("""
    <div class="card">
      <img src="https://scontent.fmnl3-4.fna.fbcdn.net/v/t1.15752-9/346097733_588560343098490_4371486048026542471_n.png?_nc_cat=106&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGpp897TK_MXUBdbI5174o1BEtTZumcrQQES1Nm6ZytBHnBciDCbSepUlqYYvXsgQy5IYY7sPRsTjSeSAFTMpW3&_nc_ohc=WgkEZ39PRVYAX_8SQsZ&_nc_ht=scontent.fmnl3-4.fna&oh=03_AdT0i_qTp4qHaHMpgAyCohVfn4BHJmdcvDJiPCFepM6lGg&oe=64922AF9" alt="picture" style="width:100%">
      <div class="container">
        <h4><b> Zach Adaya </b></h4>
        <p> JohnDrich Homepage </p>
      </div>
    </div>
            """, unsafe_allow_html=True, )
                    st.write("###")
                    st.markdown("""
                <div class="card">
                  <img src="https://scontent.fmnl3-2.fna.fbcdn.net/v/t1.15752-9/346097719_628297549185312_686228450946917231_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHfpF01FhhqVrD65jHdmD4_YhbjhhfmpWJiFuOGF-alYmyyVBBQmZv5j3WejJf9EoUt7reO_SmKNh-sVKm7VRvf&_nc_ohc=c8jPGb36F-cAX8lX-H2&_nc_ht=scontent.fmnl3-2.fna&oh=03_AdTXb2nyMxTyZKmHQQPu3KLo04N4sHR8NY_v8v68HQT-uw&oe=6492299C" alt="picture" style="width:100%">
                  <div class="container">
                    <h4><b> Adrian Dulay </b></h4>
                    <p> 3D Model for JohnDrich Advertisement </p>
                  </div>
                </div>
                        """, unsafe_allow_html=True, )
                    st.write("###")
                    st.markdown("""
                                <div class="card">
                      <img src="https://scontent.fmnl3-1.fna.fbcdn.net/v/t1.15752-9/346170596_783144809877793_2472374460963357945_n.png?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHr1kDhj-OFaQsyPdFyJFg0HDj_4IzpXOkcOP_gjOlc6cCXPaMmf6DCRSE2ZLxB9kK_LcmvXHEPUTHq9IBE3Ra8&_nc_ohc=5g8xz4FrKQYAX9f6Nda&_nc_ht=scontent.fmnl3-1.fna&oh=03_AdSLuYf7rl3-em3Cr5KIcqjCmSPirEPs61BOJZX9c9cKmg&oe=64925988" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Brian Dilig </b></h4>
                	<p>Snake Game using JavaScript</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )
            st.write("###")
            with col1:
                st.write("###")
                st.markdown("""
                            <div class="card">
                  <img src="https://z-p3-scontent.fmnl25-4.fna.fbcdn.net/v/t1.15752-9/346143793_762849448637200_6025935652302890780_n.png?_nc_cat=107&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGjzeXYm4zH2KZ6wS_waEet8mX7rzzND8fyZfuvPM0Pxw0V7eN7ysC_3l8Y-R2s2Y71_2OwUcuYD_XglUkhLNne&_nc_ohc=C0UUf0dJXoQAX8m4lCk&_nc_ht=z-p3-scontent.fmnl25-4.fna&oh=03_AdTcIk5aTaYZlOUmuqPlCnVN7IhgZ-he2ANrKnADJw8DNg&oe=6492510F" alt="picture" style="width:100%">
                  <div class="container">
                    <h4><b> Jayson Alcano </b></h4>
            	<p>JohnDrich Inventory Management System</p>
                  </div>
                </div>
                            """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                <div class="card">
                  <img src="https://z-p3-scontent.fmnl4-1.fna.fbcdn.net/v/t1.15752-9/348384003_1200910960568140_6105979749304360080_n.png?_nc_cat=103&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHjtMw7mq3N82XITxHL5k-jH8ZsTv6JUFofxmxO_olQWvVD80nDcNVTJ420RWQgLszMbv1hZYSdQch3UaATQosT&_nc_ohc=JKGZpItd37UAX96JenL&_nc_ht=z-p3-scontent.fmnl4-1.fna&oh=03_AdRS8H8HgPB2n6vofFQNL2TD0wzegDI0jKVZMFUqhMcp4A&oe=6493DDE9" alt="picture" style="width:100%">
                  <div class="container">
                    <h4><b> Vincent Cubay </b></h4>
                    <p> 3D Model for JohnDrich Advertisement </p>
                  </div>
                </div>
                        """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                <div class="card">
                  <img src="https://z-p3-scontent.fmnl9-2.fna.fbcdn.net/v/t1.15752-9/346163467_819035072887551_2442225496154377094_n.png?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeH1DTUSkWf9sBw40u0AymN3DtAXhM8_QnUO0BeEzz9CdebYVklhopcxQnPUaf6ekaejlHwWr54o2T30qVWlhkdk&_nc_ohc=dGODlX8vNv0AX_BGfQr&_nc_ht=z-p3-scontent.fmnl9-2.fna&oh=03_AdQ0Slz-ZnNE_lCEklJ4zIJetMGtoerPmWBXoU-9K_qhhQ&oe=6493D8B3" alt="picture" style="width:100%">
                  <div class="container">
                    <h4><b> Jeremy Bondal </b></h4>
                    <p> CSCQC Annex Building Replica </p>
                  </div>
                </div>
                        """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                <div class="card">
                  <img src="https://z-p3-scontent.fmnl4-5.fna.fbcdn.net/v/t1.15752-9/346167392_795161055568827_629110725519539396_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeF0Sw4Hcc4arIcpm6dpF4AdcKpOusgSCVpwqk66yBIJWlXJ61EInUc6zGngjFsKQ-j9BRSI7yHndzbBZISUq1AW&_nc_ohc=5YH_PPQWSwEAX8VcU0G&_nc_ht=z-p3-scontent.fmnl4-5.fna&oh=03_AdRv1taUokadTDX0cZ6oSUqwH4Fmao0SPPcA5SCjai1ELA&oe=6493B846" alt="picture" style="width:100%">
                  <div class="container">
                    <h4><b> Franchesca Gubat </b></h4>
                    <p> Task 1 in Architecture Department </p>
                  </div>
                </div>
                        """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://z-p3-scontent.fmnl4-4.fna.fbcdn.net/v/t1.15752-9/346150930_919200109351377_6993920090590505412_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeEGR1fKlp_H-uQy90PqtRcGf4ravHJMAIV_itq8ckwAhU2EWa0HU9vuS8Geyrt3fTOEQNMobee-HB566xS8bj6V&_nc_ohc=Y7qJxYqH6mcAX8PxII_&_nc_ht=z-p3-scontent.fmnl4-4.fna&oh=03_AdQlImfc487obXkUFhVAAwsGizv6m8st5NiO2kdvF39M1Q&oe=6493E20D" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Angela Almodovar </b></h4>
                    <p> StarBugz Model for Architecture Department</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://scontent.fmnl33-3.fna.fbcdn.net/v/t1.15752-9/346151601_1449993472523445_7844539721065315777_n.png?_nc_cat=109&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeECFI9ELYcNd5DWDt76OuCGb-heaL2QZhJv6F5ovZBmElXY_v35ZDzZRa1YZpFpZ8O6Sx6yRWrGASamIK_hFTQ8&_nc_ohc=nQ2BZmJlhIEAX9brtvR&_nc_ht=scontent.fmnl33-3.fna&oh=03_AdQmiN_rOjHlD_z2EO--TU6qhwFQSjnKN_k3ysp5U70Dyw&oe=6496202E" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Kyle Fernandez </b></h4>
                    <p> JohnDrich Poster</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )


            with col2:
                st.markdown("""
                              <div class="card">
                    <img src="https://z-p3-scontent.fmnl25-2.fna.fbcdn.net/v/t1.15752-9/346143803_262081782992245_6487055084944521155_n.png?_nc_cat=111&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeFn2eUIG4A18zBspdSJ2vVAV2MDOvdTAEJXYwM691MAQnP41j4ZArl7hGP6A5mXn75BXXlYaz7kVin5XMB9QQXX&_nc_ohc=J7YutCkgmjIAX_wTcii&_nc_ht=z-p3-scontent.fmnl25-2.fna&oh=03_AdQ00kizrJpFAk577pDI2xsPyIlaeOjaPRVwJ5_n2K4fGg&oe=64927579" alt="picture" style="width:100%">
                    <div class="container">
                      <h4><b> Clarence Del Rosario </b></h4>
                  <p>JohnDrich Original Collection</p>
                    </div>
                  </div>
                              """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://scontent.fmnl3-1.fna.fbcdn.net/v/t1.15752-9/346112782_1907918516233349_2746521026658801295_n.png?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGCgkkv4tOGB_nT2X3lZzd1tiWBX6eTwhK2JYFfp5PCEt7gF_xb04xirbAZu8flmR74N_pjZ8S5ruAZ8cO2uSs_&_nc_ohc=LPK_6F0MDX4AX9NNoSK&_nc_ht=scontent.fmnl3-1.fna&oh=03_AdSiVuJos6J2ru1L8FxfZ3RX_uIs4KyJ1WgPrRNA6-98Pg&oe=6492479A" alt="picture" style="width:98%">
                      <div class="container">
                        <h4><b> Jacob David </b></h4>
                    <p>Time in Time Out System using C#</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://scontent.fmnl3-2.fna.fbcdn.net/v/t1.15752-9/346144035_617278393788426_3627556121246575266_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHETXTqrHJZCKO4YWPDDi0jpdhO28HTFN2l2E7bwdMU3SD6Yx64pw-JYyBD_fs79-6ajDfwNglPXqDFmLayeUpw&_nc_ohc=6D-WeuPD1cYAX91raji&_nc_oc=AQm6JiqvguxDXEGKWBAIw49DHWJXXUaEj2fuOM20OSYkVQrTmP_pgyyvh6kXNFzjoPI&_nc_ht=scontent.fmnl3-2.fna&oh=03_AdRE1kbO-sF-V2ScXB18mJMGziJRIwb-_nmr0gtc8fv1DA&oe=64926DA2" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Julius Reynosa </b></h4>
                    <p>Space Invaders Game using JavaScript</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://z-p3-scontent.fmnl25-4.fna.fbcdn.net/v/t1.15752-9/346164523_216776141123569_2113876097435611111_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHnNrhC90y-5NFp832xJsKjAWpa3b_P46EBalrdv8_joRIelJ9bUi9FzC-Y7aM8fLoA8qEJPY34woih3mEtpB3W&_nc_ohc=GeN70JUbjL4AX-RPmO0&_nc_ht=z-p3-scontent.fmnl25-4.fna&oh=03_AdQkqF26j-54GvaQGQxclMWPbdjCQmAQetYS43hRcDo_vw&oe=64927323" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Kyle Fernandez </b></h4>
                    <p> Animation of JD Character</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://scontent.fmnl9-4.fna.fbcdn.net/v/t1.15752-9/348364989_6434521813237710_3566802568854561342_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGYGaIGTzv1nwexO5RJh3uqJcDozY85WZElwOjNjzlZkRGa6zUQBiZ-ycx-Nd_ppiH0VjH9WJnN_W9cYnrx9pt_&_nc_ohc=Maa340FN_LwAX-Gz5YL&_nc_ht=scontent.fmnl9-4.fna&oh=03_AdT1dLZ4rtQ6UWqbX0yvGuPfARxrkxtMKta4xzRO6H8Lyw&oe=6494592F" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Rhealyn Narsico </b></h4>
                    <p> JohnDrich Login System</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/346153809_1450729045742038_5619667044859868279_n.jpg?stp=dst-jpg_p403x403&_nc_cat=100&ccb=1-7&_nc_sid=aee45a&_nc_eui2=AeEZJeluMvWCDReQoeyOWSL5Ne2-Gdgltsg17b4Z2CW2yC6NiD6WMHyYl8Nkm0tFMLTk4bV7BvQzC74w4jdM5glF&_nc_ohc=TxbAI9JQtpMAX_95MpP&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRZPmwHZj0LOWJpBMHOTW6Pg1ibZtJZc2kFazJ8VsTeaw&oe=649367A3" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Althe Sosing </b></h4>
                    <p> 3D Modeling Task 1</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                <div class="card">
                  <img src="https://z-p3-scontent.fmnl4-6.fna.fbcdn.net/v/t1.15752-9/346106529_3586133368369826_7818880301153848583_n.png?_nc_cat=107&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeFZtBmowkAYtTOuZ4ps1WUVx0hs5_wBrw3HSGzn_AGvDdcUifbzYB4_8NRZO3bO_tKRy2UNZTO2Dvi8UjXZMe66&_nc_ohc=mKonohnCmNgAX-JDzzY&_nc_ht=z-p3-scontent.fmnl4-6.fna&oh=03_AdQ8D9hjHVMY2k3eLjRsiD1Wo2G6-aJ9hLSKjGSyuvIeqw&oe=6493DC26" alt="picture" style="width:100%">
                  <div class="container">
                    <h4><b> Natasha Paguirigan </b></h4>
                    <p> Task 2 in Engineering Department </p>
                  </div>
                </div>
                        """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://scontent.fmnl33-3.fna.fbcdn.net/v/t1.15752-9/349330753_500522878867280_6505519772706413242_n.png?_nc_cat=109&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHCb-RTdwp0ITf_9h0w0Bo-2FGapq_3DH3YUZqmr_cMfQqVsWVxKX3BXsnknJhoDPEFV_T2kkxeHS9LNKFJvcLW&_nc_ohc=46QDRYdNmHgAX9he0WN&_nc_ht=scontent.fmnl33-3.fna&oh=03_AdRMeUl8IO2v6UKdjlTDA6Dwgd7JEyUKnEo3iVmTX6MyFA&oe=64961F8B" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Carl Mangune </b></h4>
                    <p> JohnDrich Showroom 3D Model</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )

        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style/team1.css")

        with col2:
            st.write("###")

        if option == 'Animation':
            col1, col2, = st.columns((3, 3))
            with col1:
                st.markdown("""
                                <div class="card">
                      <img src="https://z-p3-scontent.fmnl25-4.fna.fbcdn.net/v/t1.15752-9/346164523_216776141123569_2113876097435611111_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHnNrhC90y-5NFp832xJsKjAWpa3b_P46EBalrdv8_joRIelJ9bUi9FzC-Y7aM8fLoA8qEJPY34woih3mEtpB3W&_nc_ohc=GeN70JUbjL4AX-RPmO0&_nc_ht=z-p3-scontent.fmnl25-4.fna&oh=03_AdQkqF26j-54GvaQGQxclMWPbdjCQmAQetYS43hRcDo_vw&oe=64927323" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Kyle Fernandez </b></h4>
                    <p> Animation of JD Character</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://scontent.fmnl33-3.fna.fbcdn.net/v/t1.15752-9/346151601_1449993472523445_7844539721065315777_n.png?_nc_cat=109&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeECFI9ELYcNd5DWDt76OuCGb-heaL2QZhJv6F5ovZBmElXY_v35ZDzZRa1YZpFpZ8O6Sx6yRWrGASamIK_hFTQ8&_nc_ohc=nQ2BZmJlhIEAX9brtvR&_nc_ht=scontent.fmnl33-3.fna&oh=03_AdQmiN_rOjHlD_z2EO--TU6qhwFQSjnKN_k3ysp5U70Dyw&oe=6496202E" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Kyle Fernandez </b></h4>
                    <p> JohnDrich Poster</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )

            with col2:
                st.markdown("""
                              <div class="card">
                    <img src="https://z-p3-scontent.fmnl25-2.fna.fbcdn.net/v/t1.15752-9/346143803_262081782992245_6487055084944521155_n.png?_nc_cat=111&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeFn2eUIG4A18zBspdSJ2vVAV2MDOvdTAEJXYwM691MAQnP41j4ZArl7hGP6A5mXn75BXXlYaz7kVin5XMB9QQXX&_nc_ohc=J7YutCkgmjIAX_wTcii&_nc_ht=z-p3-scontent.fmnl25-2.fna&oh=03_AdQ00kizrJpFAk577pDI2xsPyIlaeOjaPRVwJ5_n2K4fGg&oe=64927579" alt="picture" style="width:100%">
                    <div class="container">
                      <h4><b> Clarence Del Rosario </b></h4>
                  <p>JohnDrich Original Collection</p>
                    </div>
                  </div>
                              """, unsafe_allow_html=True, )

        if option == 'Architecture':
            col1, col2, = st.columns((3, 3))
            with col1:
                st.markdown("""
                                <div class="card">
                      <img src="https://scontent.fmnl33-3.fna.fbcdn.net/v/t1.15752-9/349330753_500522878867280_6505519772706413242_n.png?_nc_cat=109&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHCb-RTdwp0ITf_9h0w0Bo-2FGapq_3DH3YUZqmr_cMfQqVsWVxKX3BXsnknJhoDPEFV_T2kkxeHS9LNKFJvcLW&_nc_ohc=46QDRYdNmHgAX9he0WN&_nc_ht=scontent.fmnl33-3.fna&oh=03_AdRMeUl8IO2v6UKdjlTDA6Dwgd7JEyUKnEo3iVmTX6MyFA&oe=64961F8B" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Carl Mangune </b></h4>
                    <p> JohnDrich Showroom 3D Model</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                <div class="card">
                  <img src="https://z-p3-scontent.fmnl4-6.fna.fbcdn.net/v/t1.15752-9/346106529_3586133368369826_7818880301153848583_n.png?_nc_cat=107&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeFZtBmowkAYtTOuZ4ps1WUVx0hs5_wBrw3HSGzn_AGvDdcUifbzYB4_8NRZO3bO_tKRy2UNZTO2Dvi8UjXZMe66&_nc_ohc=mKonohnCmNgAX-JDzzY&_nc_ht=z-p3-scontent.fmnl4-6.fna&oh=03_AdQ8D9hjHVMY2k3eLjRsiD1Wo2G6-aJ9hLSKjGSyuvIeqw&oe=6493DC26" alt="picture" style="width:100%">
                  <div class="container">
                    <h4><b> Natasha Paguirigan </b></h4>
                    <p> Task 2 in Engineering Department </p>
                  </div>
                </div>
                        """, unsafe_allow_html=True, )

            with col2:
                st.markdown("""
                <div class="card">
                  <img src="https://z-p3-scontent.fmnl4-5.fna.fbcdn.net/v/t1.15752-9/346167392_795161055568827_629110725519539396_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeF0Sw4Hcc4arIcpm6dpF4AdcKpOusgSCVpwqk66yBIJWlXJ61EInUc6zGngjFsKQ-j9BRSI7yHndzbBZISUq1AW&_nc_ohc=5YH_PPQWSwEAX8VcU0G&_nc_ht=z-p3-scontent.fmnl4-5.fna&oh=03_AdRv1taUokadTDX0cZ6oSUqwH4Fmao0SPPcA5SCjai1ELA&oe=6493B846" alt="picture" style="width:100%">
                  <div class="container">
                    <h4><b> Franchesca Gubat </b></h4>
                    <p> Task 1 in Architecture Department </p>
                  </div>
                </div>
                        """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://z-p3-scontent.fmnl4-4.fna.fbcdn.net/v/t1.15752-9/346150930_919200109351377_6993920090590505412_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeEGR1fKlp_H-uQy90PqtRcGf4ravHJMAIV_itq8ckwAhU2EWa0HU9vuS8Geyrt3fTOEQNMobee-HB566xS8bj6V&_nc_ohc=Y7qJxYqH6mcAX8PxII_&_nc_ht=z-p3-scontent.fmnl4-4.fna&oh=03_AdQlImfc487obXkUFhVAAwsGizv6m8st5NiO2kdvF39M1Q&oe=6493E20D" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Angela Almodovar </b></h4>
                    <p> StarBugz Model for Architecture Department</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )


        if option == 'Engineering':
                    col1, col2, = st.columns((3, 3))
                    with col1:
                        st.markdown("""
                        <div class="card">
                          <img src="https://z-p3-scontent.fmnl4-1.fna.fbcdn.net/v/t1.15752-9/348384003_1200910960568140_6105979749304360080_n.png?_nc_cat=103&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHjtMw7mq3N82XITxHL5k-jH8ZsTv6JUFofxmxO_olQWvVD80nDcNVTJ420RWQgLszMbv1hZYSdQch3UaATQosT&_nc_ohc=JKGZpItd37UAX96JenL&_nc_ht=z-p3-scontent.fmnl4-1.fna&oh=03_AdRS8H8HgPB2n6vofFQNL2TD0wzegDI0jKVZMFUqhMcp4A&oe=6493DDE9" alt="picture" style="width:100%">
                          <div class="container">
                            <h4><b> Vincent Cubay </b></h4>
                            <p> 3D Model for JohnDrich Advertisement </p>
                          </div>
                        </div>
                                """, unsafe_allow_html=True, )
                        st.write("###")
                        st.markdown("""
                        <div class="card">
                          <img src="https://scontent.fmnl3-2.fna.fbcdn.net/v/t1.15752-9/346097719_628297549185312_686228450946917231_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHfpF01FhhqVrD65jHdmD4_YhbjhhfmpWJiFuOGF-alYmyyVBBQmZv5j3WejJf9EoUt7reO_SmKNh-sVKm7VRvf&_nc_ohc=c8jPGb36F-cAX8lX-H2&_nc_ht=scontent.fmnl3-2.fna&oh=03_AdTXb2nyMxTyZKmHQQPu3KLo04N4sHR8NY_v8v68HQT-uw&oe=6492299C" alt="picture" style="width:100%">
                          <div class="container">
                            <h4><b> Adrian Dulay </b></h4>
                            <p> 3D Model for JohnDrich Advertisement </p>
                          </div>
                        </div>
                                """, unsafe_allow_html=True, )
                        st.write("###")

                    with col2:
                        st.markdown("""
                                        <div class="card">
                              <img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/346153809_1450729045742038_5619667044859868279_n.jpg?stp=dst-jpg_p403x403&_nc_cat=100&ccb=1-7&_nc_sid=aee45a&_nc_eui2=AeEZJeluMvWCDReQoeyOWSL5Ne2-Gdgltsg17b4Z2CW2yC6NiD6WMHyYl8Nkm0tFMLTk4bV7BvQzC74w4jdM5glF&_nc_ohc=TxbAI9JQtpMAX_95MpP&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRZPmwHZj0LOWJpBMHOTW6Pg1ibZtJZc2kFazJ8VsTeaw&oe=649367A3" alt="picture" style="width:100%">
                              <div class="container">
                                <h4><b> Althe Sosing </b></h4>
                            <p> 3D Modeling Task 1</p>
                              </div>
                            </div>
                                        """, unsafe_allow_html=True, )
                        st.write("###")
                        st.markdown("""
                <div class="card">
                  <img src="https://z-p3-scontent.fmnl9-2.fna.fbcdn.net/v/t1.15752-9/346163467_819035072887551_2442225496154377094_n.png?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeH1DTUSkWf9sBw40u0AymN3DtAXhM8_QnUO0BeEzz9CdebYVklhopcxQnPUaf6ekaejlHwWr54o2T30qVWlhkdk&_nc_ohc=dGODlX8vNv0AX_BGfQr&_nc_ht=z-p3-scontent.fmnl9-2.fna&oh=03_AdQ0Slz-ZnNE_lCEklJ4zIJetMGtoerPmWBXoU-9K_qhhQ&oe=6493D8B3" alt="picture" style="width:100%">
                  <div class="container">
                    <h4><b> Jeremy Bondal </b></h4>
                    <p> CSCQC Annex Building Replica </p>
                  </div>
                </div>
                        """, unsafe_allow_html=True, )



        if option == 'IT':
            col1, col2, = st.columns((3, 3))
            with col1:
                st.markdown("""
            <div class="card">
            <img src="https://z-p3-scontent.fmnl25-4.fna.fbcdn.net/v/t1.15752-9/346143793_762849448637200_6025935652302890780_n.png?_nc_cat=107&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGjzeXYm4zH2KZ6wS_waEet8mX7rzzND8fyZfuvPM0Pxw0V7eN7ysC_3l8Y-R2s2Y71_2OwUcuYD_XglUkhLNne&_nc_ohc=C0UUf0dJXoQAX8m4lCk&_nc_ht=z-p3-scontent.fmnl25-4.fna&oh=03_AdTcIk5aTaYZlOUmuqPlCnVN7IhgZ-he2ANrKnADJw8DNg&oe=6492510F" alt="picture" style="width:100%">
                <div class="container">
                    <h4><b> Jayson Alcano </b></h4>
                        <p>JohnDrich Inventory Management System</p>
                </div>
                </div>
                        """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                    <div class="card">
                      <img src="https://scontent.fmnl3-4.fna.fbcdn.net/v/t1.15752-9/346097733_588560343098490_4371486048026542471_n.png?_nc_cat=106&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGpp897TK_MXUBdbI5174o1BEtTZumcrQQES1Nm6ZytBHnBciDCbSepUlqYYvXsgQy5IYY7sPRsTjSeSAFTMpW3&_nc_ohc=WgkEZ39PRVYAX_8SQsZ&_nc_ht=scontent.fmnl3-4.fna&oh=03_AdT0i_qTp4qHaHMpgAyCohVfn4BHJmdcvDJiPCFepM6lGg&oe=64922AF9" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Zach Adaya </b></h4>
                        <p> JohnDrich Homepage </p>
                      </div>
                    </div>
                            """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                                <div class="card">
                                      <img src="https://scontent.fmnl3-1.fna.fbcdn.net/v/t1.15752-9/346170596_783144809877793_2472374460963357945_n.png?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHr1kDhj-OFaQsyPdFyJFg0HDj_4IzpXOkcOP_gjOlc6cCXPaMmf6DCRSE2ZLxB9kK_LcmvXHEPUTHq9IBE3Ra8&_nc_ohc=5g8xz4FrKQYAX9f6Nda&_nc_ht=scontent.fmnl3-1.fna&oh=03_AdSLuYf7rl3-em3Cr5KIcqjCmSPirEPs61BOJZX9c9cKmg&oe=64925988" alt="picture" style="width:100%">
                                      <div class="container">
                                        <h4><b> Brian Dilig </b></h4>
                                	<p>Snake Game using JavaScript</p>
                                      </div>
                                    </div>
                                                """, unsafe_allow_html=True, )


            with col2:
                st.markdown("""
                                <div class="card">
                      <img src="https://scontent.fmnl3-2.fna.fbcdn.net/v/t1.15752-9/346144035_617278393788426_3627556121246575266_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeHETXTqrHJZCKO4YWPDDi0jpdhO28HTFN2l2E7bwdMU3SD6Yx64pw-JYyBD_fs79-6ajDfwNglPXqDFmLayeUpw&_nc_ohc=6D-WeuPD1cYAX91raji&_nc_oc=AQm6JiqvguxDXEGKWBAIw49DHWJXXUaEj2fuOM20OSYkVQrTmP_pgyyvh6kXNFzjoPI&_nc_ht=scontent.fmnl3-2.fna&oh=03_AdRE1kbO-sF-V2ScXB18mJMGziJRIwb-_nmr0gtc8fv1DA&oe=64926DA2" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Julius Reynosa </b></h4>
                    <p>Space Invaders Game using JavaScript</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://scontent.fmnl3-1.fna.fbcdn.net/v/t1.15752-9/346112782_1907918516233349_2746521026658801295_n.png?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGCgkkv4tOGB_nT2X3lZzd1tiWBX6eTwhK2JYFfp5PCEt7gF_xb04xirbAZu8flmR74N_pjZ8S5ruAZ8cO2uSs_&_nc_ohc=LPK_6F0MDX4AX9NNoSK&_nc_ht=scontent.fmnl3-1.fna&oh=03_AdSiVuJos6J2ru1L8FxfZ3RX_uIs4KyJ1WgPrRNA6-98Pg&oe=6492479A" alt="picture" style="width:98%">
                      <div class="container">
                        <h4><b> Jacob David </b></h4>
                    <p>Time in Time Out System using C#</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )
                st.write("###")
                st.markdown("""
                                <div class="card">
                      <img src="https://scontent.fmnl25-1.fna.fbcdn.net/v/t1.15752-9/348364989_6434521813237710_3566802568854561342_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_eui2=AeGYGaIGTzv1nwexO5RJh3uqJcDozY85WZElwOjNjzlZkRGa6zUQBiZ-ycx-Nd_ppiH0VjH9WJnN_W9cYnrx9pt_&_nc_ohc=Maa340FN_LwAX8Qflq8&_nc_ht=scontent.fmnl25-1.fna&oh=03_AdSINoYC36Mq0i_0q9-KGee5TJyQSRS4zm8bWh0LWYTn6Q&oe=6493782F" alt="picture" style="width:100%">
                      <div class="container">
                        <h4><b> Rhealyn Narsico </b></h4>
                    <p> JohnDrich Login System</p>
                      </div>
                    </div>
                                """, unsafe_allow_html=True, )



if selected == "Content":
    import streamlit.components.v1 as components

    with st.container():
        col1, col2, col3 = st.columns((3, 5, 3))
        with col1:
            st.write('')
        with col2:
            st.image(img_logo)
        with col3:
            st.write('')
    st.write("---")
    st.title("Animation Department")
    components.iframe("https://www.youtube.com/embed/jepq2sIeDU8", width=float(700), height=float(400))
    st.write("---")
    st.title("JG Builders")
    components.iframe("https://drive.google.com/file/d/1-R5CL0FIY5NSzpfaqpY8vi-HokHxCymb/preview", width=float(700), height=float(400))
    st.write("---")
    st.title("System Development")
    components.iframe("https://www.youtube.com/embed/2CPYUAn9haQ", width=float(700), height=float(400))
    st.write("---")
    st.title("IT Training Center")
    components.iframe("https://drive.google.com/file/d/1AW4-KDaJ0DLjSYMAtxHKbPPE04PXV0i-/preview", width=float(700), height=float(400))
