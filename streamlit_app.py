import streamlit as st
from datetime import datetime
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Load the CSS file
css_file = Path(__file__).parent / "style.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Portfolio", "Skills", "Contact"])

# Home Page
if page == "Home":
    st.markdown('<div class="main-header">James Ewican</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">BS Computer Science Student</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("2x2.jpg", caption="Professional Photo", width='stretch')
    
    st.markdown("---")
    
    st.markdown("""
    ### Welcome to My Autobiography/Portfolio!
    
    I'm currently a 3rd Year BS Computer Science student in CIT-U. From understanding how computers work at a low level to building
    applications with frameworks, I use what I learn to build solutions for problems.
    
    Explore my portfolio to learn more about my journey, projects, and skills.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Year", "3")
    with col2:
        st.metric("Projects Completed", "10+")
    with col3:
        st.metric("Programming Languages", "5+")

# About Me Page
elif page == "About Me":
    st.markdown('<div class="section-header">About Me</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("2x2.jpg", width='stretch')
    
    with col2:
        st.markdown("""
        ### My Story

        Hello! I'm James Ewican, an aspiring software developer with a love for creating 
        elegant solutions to complex problems. My fascination with technology started at a
        young age when I found just how fast computers can be at solving certain problems.

        Currently, I'm pursuing a Bachelor's degree in Computer Science so that I can make my
        passion into a living. I've had passionate and capable instructors walk me through the
        fundamentals of programming, web and app development, and data analysis.
        """)
    
    st.markdown("---")
    
    st.markdown("### Education")
    st.markdown("""
    - **Bachelor of Science in Computer Science** - Cebu Institute of Technology - University (2023-Current)
      - Top 7 Computer Science Student (A.Y. 2024-2025)
    
    - **Senior High School - STEM Strand** - Colegio de Sto. Tomas-Recoletos, Inc. (2021-2023)
      - Graduated With High Honors
      - Ranked 34th out of 201 Students
    """)
    
    
    st.markdown("### Personal Interests")
    st.markdown("""
    When I'm not coding, you can find me running around the city, hanging out
    in coffee shops, or online playing games. I like to expand my skill set, 
    so I often participate in tech events.
    """)

# Portfolio Page
elif page == "Portfolio":
    st.markdown('<div class="section-header">My Portfolio</div>', unsafe_allow_html=True)
    st.markdown("Here are some of my recent projects that showcase my skills and experience:")

    # Project 1
    st.markdown("""
    <div class="project-card">
        <h3>EduGrade</h3>
        <p>A mobile app for calculating grades from test and exam scores.</p>
        <p><strong>Technologies:</strong> Kotlin, Firebase</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>User authentication and authorization</li>
            <li>GWA Calculation with user-defined weights</li>
            <li>Simple scores input</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Project 2
    st.markdown("""
    <div class="project-card">
        <h3>FSM Designer</h3>
        <p>An interactive canvas for creating and testing deterministic finite automata</p>
        <p><strong>Technologies:</strong> Python</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Adding and removing states</li>
            <li>Defining transitions between states</li>
            <li>Evaluating strings with DFA</li>
            <li>Save and load functionality</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Project 3
    st.markdown("""
    <div class="project-card">
        <h3>Structs and Algos</h3>
        <p>An isometric board game showcasing a custom framework for block-based games.</p>
        <p><strong>Technologies:</strong> Java, FXGL</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Simple board game with special tiles</li>
            <li>Fully manipulable blocks as objects for game development</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Project 4
    st.markdown("""
    <div class="project-card">
        <h3>Sustaina</h3>
        <p>An AI-powered platform that crowdsources and visualizes environmental issues in real-time.</p>
        <p><strong>Technologies:</strong> Kotlin, Firebase</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Gamification for engagement</li>
            <li>Real-time reports of environmental issues through crowdsourcing</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Skills Page
elif page == "Skills":
    st.markdown('<div class="section-header">Technical Skills</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Programming Languages")
        skills = ["C", "C++", "Java", "Python", "Kotlin", "Shell"]
        badges_html = ''.join([f'<span class="skill-badge">{skill}</span>' for skill in skills])
        st.markdown(badges_html, unsafe_allow_html=True)
        
        st.markdown("### Web Development")
        skills = ["HTML/CSS", "Spring Boot", "Django", "REST APIs"]
        badges_html = ''.join([f'<span class="skill-badge">{skill}</span>' for skill in skills])
        st.markdown(badges_html, unsafe_allow_html=True)
        
        st.markdown("### Databases")
        skills = ["PostgreSQL", "MySQL", "Firebase"]
        badges_html = ''.join([f'<span class="skill-badge">{skill}</span>' for skill in skills])
        st.markdown(badges_html, unsafe_allow_html=True)

    with col2:
        st.markdown("### Data Science & ML")
        skills = ["Pandas", "NumPy", "Matplotlib"]
        badges_html = ''.join([f'<span class="skill-badge">{skill}</span>' for skill in skills])
        st.markdown(badges_html, unsafe_allow_html=True)
        
        st.markdown("### Tools & Platforms")
        skills = ["Git", "Docker", "AWS", "Linux", "Jupyter", "VS Code"]
        badges_html = ''.join([f'<span class="skill-badge">{skill}</span>' for skill in skills])
        st.markdown(badges_html, unsafe_allow_html=True)
        
    st.markdown("---")

# Contact Page
elif page == "Contact":
    st.markdown('<div class="section-header">Get In Touch</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        I'm always interested in hearing about new opportunities, collaborations, 
        or just connecting with fellow tech enthusiasts. Feel free to reach out!
        """)
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=150)
            
            submitted = st.form_submit_button("Send Message")
            if submitted:
                st.success("Thank you for your message! I'll get back to you soon. 🎉")
    
    with col2:
        st.markdown("### Contact Information")
        st.markdown("""
        📧 **Email:**  
        james.ewican@cit.edu
        
        📱 **Phone:**  
        +63 977 123 4567
        
        🔗 **LinkedIn:**  
        linkedin.com/in/james-ewican
                    
        💻 **GitHub:**  
        github.com/jewican
        """)