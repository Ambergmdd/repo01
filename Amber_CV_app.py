"Old Streamlit version. Run in amber_css2026"

import streamlit as st
import pandas as pd
import numpy as np
import os 
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    """,
    unsafe_allow_html=True)


# Set page title
st.set_page_config(page_title="Overview", layout="wide", initial_sidebar_state="collapsed")


# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Overview", "Education", "Work experience", "Skills", "Additional studies", "Volunteering", "Other interests", "Contact"])


# Sections based on menu selection

# -------------------------
# Overview Section
# -------------------------

if menu == "Overview":
    st.markdown(
        """
        <div style="position: relative; text-align: right; color: black;">
            <img src="https://raw.githubusercontent.com/Ambergmdd/repo01/main/IMG_2946-EDIT.jpg"
                 style="width: 100%; 
                 height: auto;">
            <div style="
                position: absolute; 
                top: 30%; 
                left: 60%; 
                transform: translate(-50%, -50%);
                width: 700px;
                text-align: right;
            ">
                <h1 style="margin: 0; font-size: 60px;">Amber De Decker</h1>
                <h2 style="margin: 0; font-size: 40px;">Curriculum Vitae</h2>
            </div>
        </div>
        """,
        unsafe_allow_html=True)

    st.markdown(
        "<p style='font-size: 28px; text-align: center; color: blue; font-family: Montserrat, sans-serif; font-weight: 700; margin-top: 30px;'>Mathematician, Mountain walking guide, Teacher, Musician, Coder</p>",
        unsafe_allow_html=True)
    
    st.markdown(
    """
    <p style='text-align: center; color: black; margin-top: 20px; font-family: Montserrat, sans-serif;'>
        <span style='font-size: 26px; font-weight: 700; color: black; letter-spacing: 0.5px;'>Welcome to my CV!</span><br>
        <span style='font-size: 20px;'>I coded this interactive web app myself, allowing you to easily view the facets of my CV relevant to you, and more if you wish!</span><br>
        <span style='font-size: 18px;'>Click the arrows on the top left to explore the various pages.</span>
    </p>
    """,
    unsafe_allow_html=True)

    
    email = "agm.dedecker@gmail.com"
    number = "+27 78 063 8908"


    st.markdown(
        f"""
        <p style="margin: 0; text-align: center">
            <strong>Email: </strong>  {email}
        </p>
        <p style="margin: 0; text-align: center">
            <strong>Phone: </strong>  {number}
        </p>
        """,
        unsafe_allow_html=True)


elif menu == "Education":
    st.header("Education")

        # University of Cape Town
    st.markdown(
        """
        <p style="font-size: 25px; font-weight: bold; margin: 25px 0 0 0;">University of Cape Town</p>
    
        <p style="margin: 0;"><strong>BSc (Honours) in Mathematics (cum laude)</strong> — 2024</p>
    
        <p style="font-size: 18px; font-style: italic; margin: 10px 0 0 0;">Extra modules</p>
        <p style="margin: 0;">Third-year Mathematics - 85% (2023)</p>
        <p style="margin: 0;">Second-year Physics - 65% (2023)</p>
        <p style="margin: 0;">First-year Computer Science (2024)</p>
        <p style="margin: 0;">Third-year General Relativity (2024)</p>
        <p style="margin: 0;">First-year French (2025)</p>
        <p style="margin: 0;">Attended Honours-level General Relativity (2025)</p>
        <p style="margin: 0;">Coding Summer School (2026)</p>
        """,
        unsafe_allow_html=True)

    
   # Stellenbosch University
    st.markdown(
        """
        <p style="font-size: 25px; font-weight: bold; margin: 25px 0 0 0;">Stellenbosch University</p>
    
        <p style="margin: 0;"><strong>BA Music with a major in Mathematics</strong> — 2022</p>
        <p style="margin: 0;">Degree average: 75%</p>
    
        <p style="font-size: 18px; font-style: italic; margin: 10px 0 0 0;">Extra modules</p>
        <p style="margin: 0;">First-year Physics (89%)</p>
        <p style="margin: 0;">Third-year Practical Violin Performance (distinction)</p>
        <p style="margin: 0;">Short course in Leadership</p>
        """,
        unsafe_allow_html=True)



    # Herschel Girls’ School
    st.markdown(
        """
        <p style="font-size: 25px; font-weight: bold; margin: 25px 0 0 0;">Herschel Girls’ School</p>
        <p style="margin: 0;">National Senior Certificate — 96% average</p>
        """,
        unsafe_allow_html=True
    )
    
    # Rustenburg Girls’ Junior School
    st.markdown(
        """
        <p style="font-size: 25px; font-weight: bold; margin: 25px 0 0 0; margin-top: 15px;">Rustenburg Girls’ Junior School</p>
        <p style="margin: 0;">Primary education</p>
        """,
    unsafe_allow_html=True)


elif menu == "Work experience":
    st.header("Work Experience")

    # ---------------- Professional guiding career ----------------
    st.markdown(
    """
    <p style="font-size: 25px; font-weight: bold; margin: 25px 0 0 0;">Professional guiding career</p>

    <img src="https://raw.githubusercontent.com/Ambergmdd/repo01/main/awol_hike_pic.jpg" 
         style="float: right; width: 200px; border: 0.5px solid black; margin: -27px 0 10px 20px;">

    <ul style="margin-top:0px; font-size:18px;">
        <li>Professional freelance hiking guide on Table Mountain, South Africa, working for several Cape Town-based tour companies</li>
        <li>Qualified and registered with the South African Department of Tourism to guide day- and overnight hikes, on- and off-trail</li>
        <li>Qualified first-aider level three</li>
    </ul>
    """,
    unsafe_allow_html=True)

    # ---------------- Teaching career ----------------
    st.markdown(
        """
        <p style="font-size: 25px; font-weight: bold; margin: 25px 0 0 0;">Teaching career</p>
        <ul style="margin-top:0px; font-size:18px;">
            <li>Private tutor in mathematics, physics, English and music theory to pupils aged 7–20</li>
            <li>University-level mathematics tutor (Stellenbosch University 2020, University of Cape Town 2024)</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

  # ---------------- Musical career ----------------
    st.markdown(
    """
    <p style="font-size: 25px; font-weight: bold; margin: 25px 0 0 0;">Musical career</p>

    <img src="https://raw.githubusercontent.com/Ambergmdd/repo01/main/me_and_violin.jpg"
         style="float: left; width: 200px; border: 0.5px solid black; margin: 20px 50px 20px 0px;">

    <ul style="margin-top:0px; font-size:18px;">
    <li>Violin teacher at Music Dimensions, Boston Private Primary School (2023-2025)</li>
    <li>Offered beginner violin lessons during music degree and adult tuition</li>
    <li>Performed in professional orchestral projects:
        <ul style="margin-left: 225px;"> 
            <li>Stellenbosch University Camerata (2023)</li>
            <li>Winelands Philharmonic Orchestra (2022)</li>
            <li>UCT Symphony Orchestra (2025)</li>
            <li>Stellenbosch International Chamber Music Festival Alumni Orchestra (2025)</li>
            </ul>
        </li>
    </ul>
    """,
        unsafe_allow_html=True
    )
    


    # ---------------- Other casual employment ----------------
    st.markdown(
        """
        <p style="font-size: 25px; font-weight: bold; margin: 25px 0 0 0;">Other casual employment</p>
        <ul style="margin-top:0px; font-size:18px;">
            <li>Vertigo Gear store: casual staff member in outdoor equipment sales (2023)</li>
            <li>GIC Scientific: ad-hoc work to calculate costing of products sold by GIC Scientific using MS Excel (2025-2026)</li>
        </ul>
      <img src="https://raw.githubusercontent.com/Ambergmdd/repo01/main/nels_cave_morning.jpeg" 
     style="width:100%; max-width:500px; height:auto; border: 0.5px solid black; display:block; margin:10px auto;">

     
        """,
        unsafe_allow_html=True
    )

        
elif menu == "Skills":
    st.title("Skills")

    st.markdown('''
    <ul style="font-size:18px;">
        <li>Experience working in tourism and holding engaging conversations with clients from diverse backgrounds</li>
        <li>Strong interpersonal and communication skills</li>
        <li>Highly reliable and organised</li>
        <li>Good administrative and time management skills</li>
        <li>Comfortable with diverse age groups</li>
        <li>Able to provide engaging, creative teaching for children aged 7–20</li>
    </ul>
    ''', unsafe_allow_html=True)
    
elif menu == "Additional studies":
    st.title("Additional studies")
    

   
    st.markdown('''
    <b>Stellenbosch University</b>
    <ul style="font-size:18px;">
        <li>Short-course in leadership (2020) </li>
        <li>First-year physics module (2022) – 89%</li>
        <li>practical violin performance module (2022) – Distinction</li>
    </ul>
    
    <b>University of Cape Town</b>
    <ul style="font-size:18px;">
        <li>Second-year physics module (2023) – 65%</li>
        <li>Third-year mathematics module (2023) – 85%</li>
        <li>First-year computer science  (2024) – Distinction</li>
        <li>First-year French module (2025)</li>
        <li>CHPC/NITheCS Coding Summer School on data analysis and machine learning(2026)</li>
       
       
    </ul>
    ''', unsafe_allow_html=True)

            
elif menu == "Volunteering":
    st.header("Volunteering")

    
    st.markdown("""
    <div style="margin-bottom: 5px;">
      <h3 style="margin-bottom: 2px;">The Heli-Hack Initiative</h3>
      <p style="margin-top: 0px; margin-bottom: 10px;">
        Volunteer clearing invasive alien pine trees in the Western Cape mountain regions (ongoing involvement)
      </p>
    </div>
    
    <div style="margin-bottom: 5px;">
      <h3 style="margin-bottom: 2px;">Siyafunda Programme – Stellenbosch University</h3>
      <p style="margin-top: 0px; margin-bottom: 10px;">
        Taught English and Mathematics to junior school learners (2020-2021)
      </p>
    </div>
    
    <div style="margin-bottom: 5px;">
      <h3 style="margin-bottom: 2px;">Outreach Maths & Outreach Science Clubs</h3>
      <p style="margin-top: 0px; margin-bottom: 10px;">
        Volunteered as a tutor during high school (2018)
      </p>
    </div>
    
    <div style="margin-bottom: 5px;">
      <h3 style="margin-bottom: 2px;">Autumn Classical Music Concert</h3>
      <p style="margin-top: 0px; margin-bottom: 10px;">
        Volunteer performer at fundraising concerts for school children in need (2023-2024)
      </p>
    </div>
    """, unsafe_allow_html=True)

    
        

 

elif menu == "Other interests":
     st.title("Other interests")
     st.markdown('''
    <ul style="font-size:18px;">
        <li>Rock-climbing, hiking, trail running</li>
        <li>Arts and crafts, including painting, lino-cutting and origami</li>
        <li>Baking</li>
        <li>Playing chamber music and playing my violin</li>
        <li>Visiting museums and cultural heritage sights</li>
    </ul>
    ''', unsafe_allow_html=True)
     
  
elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "agm.dedecker@gmail.com"
    number = "+27 78 063 8908"
    st.write("You can reach me at:")


    st.markdown(
        f"""
        <p style="margin: 0;">
            <strong>Email: </strong>  {email}
        </p>
        <p style="margin: 0;">
            <strong>Phone: </strong>  {number}
        </p>
        """,
        unsafe_allow_html=True)

    
    
    #include my uni transcripts
    #include my honours project
    #include all the blurbs ive written about different roles 
    #eventually include a portfolio of coding projects 
    #include some guiding reviews 
    #eventually include some music projects 
    #include my high school achievements CV 
    #include my science expo 
    #include funding received - bursary and MCSA, and trip report, and both articles 
    #languages 
    #include CSS!
    #include any relevant certificates to download 
    #include some pics of my art! 
    #include modules in my maths honours 