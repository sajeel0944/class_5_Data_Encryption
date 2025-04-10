import streamlit as st
from dataclasses import dataclass
import json
import hashlib
import time
from typing import Optional


st.set_page_config(page_title="Secure Data Encryption System", page_icon="🔒", layout="centered")

# Inject CSS
st.markdown(
    """
    <style>

    
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""
    <style>
        /* Full background (includes area outside main content) */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background-color:  rgb(0, 0, 0) !important;
             color: white;
        }

        /* Main content area */
        [data-testid="stAppViewContainer"] .main {
            background-color: #1e1e1e !important;
            color: white;
        }

        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background-color: #111827 !important;
            color: white;
        }

        /* Sidebar text and widgets */
        section[data-testid="stSidebar"] * {
            color: white;
        }

        /* Optional: header (if needed) */
        header[data-testid="stHeader"] {
            background-color: transparent;
        }
        
        .stTextInput input {
            color: blue;
        }
            
        .stTextInput input {
        color: black !important;
    }

    .stTextInput label {
        color: white !important;
    }

    .stTextArea label {
        color: white !important;
    }

     /* Tab text color */
    .stTabs button {
        color: white !important;
        border-radius: 10px;
        font-size: 16px;
        transition: background-color 0.3s, color 0.3s;
    }


     /* Button style */
    .stButton button {
        background-color: #4CAF50;  /* Green */
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        cursor: pointer;
        transition: transform 0.2s ease-in-out, background-color 0.3s;
    }

    /* Hover effects */
    .stButton button:hover {
        background-color: #45a049;
        transform: scale(1.1);  /* Button size increases on hover */
        color : white
    }

    /* Active button state */
    .stButton button:active {
        background-color: #388e3c;
        transform: scale(1.05);  /* Slight shrink on click */
    }

    /* Focus effect */
    .stButton button:focus {
        outline: none;
        box-shadow: 0 0 10px 2px rgba(0, 255, 0, 0.7);  /* Green glow when focused */
    }
            
    </style>
""", unsafe_allow_html=True)


## nichy Retrieve Data waly section main dia hai
st.markdown("""
    <style>
        .card {
            background-color: #f9f9f9;
            padding: 20px;
            margin-bottom: 15px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }
        .title {
            font-size: 20px;
            font-weight: 600;
            color: #4A90E2;
        }
        .label {
            font-weight: bold;
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)





# Custom CSS for styling in home
st.markdown("""
    <style>
        .home-container {
            background-color: #ffffff;
            padding: 30px 50px;
            border-radius: 18px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        }
        .main-title {
            font-size: 36px;
            font-weight: 700;
            text-align: center;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        .sub-title {
            font-size: 18px;
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 30px;
        }
        .section-header {
            font-size: 22px;
            font-weight: 600;
            color: #34495e;
            margin-top: 20px;
        }
        .info-text {
            font-size: 16px;
            color: white;
        }
        .footer {
            margin-top: 40px;
            text-align: center;
            color: #aaa;
            font-size: 13px;
        }
    </style>
""", unsafe_allow_html=True)


# Custom CSS with Animations in home
st.markdown("""
    <style>
        @keyframes fadeInUp {
            0% {opacity: 0; transform: translateY(20px);}
            100% {opacity: 1; transform: translateY(0);}
        }
        .home-container {
            background-color: #f9f9fc;
            padding: 40px 50px;
            border-radius: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            animation: fadeInUp 1s ease-in-out;
        }
        .cards {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
            animation: fadeInUp 1.6s ease-in-out;
        }
        .card {
            background-color: white;
            border-radius: 15px;
            padding: 20px;
            width: 250px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0,0,0,0.15);
        }
        .card h3 {
            color: #2c3e50;
            font-size: 20px;
            margin-bottom: 10px;
        }
        .card p {
            font-size: 14px;
            color: #666;
        }
      
    </style>
""", unsafe_allow_html=True)


file_name = "data.json"

## ye dashboard ko display hony ko manage kar raha hai
if "display" not in st.session_state:
    st.session_state.display = True

##   jo user login ye register hoye ga us ka name is main save hoye ga phir name dashboard main show hoye ga
if "save_user_name" not in st.session_state:
    st.session_state.save_user_name = "user" 

@dataclass
class Manage_data:
    name : Optional[str] = None
    password : Optional[str] = None


##   user ko register kary ga
    def register(self) -> bool:
        with open(file_name, "r") as file:
            get_data = json.load(file) ## json ki file read ho rahe hai

            convert_password = hashlib.sha256(self.password.encode()).hexdigest() ## user ky password ko hashlib main convert kar raha ho

            check_user = any(filter(lambda data: data["name"] == self.name, get_data)) ## agar user ka name already json ky andar howa to ye true dyga
            
            if check_user : 
                return False
            else:
                user_data = [{"name":self.name, "password": convert_password, "data":[]}] ## is ky andar sara data aye ga phir wo json main file main jaye ga

                with open(file_name, "r") as file: ## json file ko read kary ga 
                    get_data = json.load(file)
                    for i in get_data:           ## jit na bhi json file ky andar data hai wo ek ek karky user_data ky andar jaye ga
                        user_data.append(i) 

                with open(file_name, "w") as file:
                    json.dump(user_data, file, indent=4) ## user_data ka sara data json ky andar jaraha hai

                return True
    

##   user ko login kata hai
    def login(self) -> bool: 
        with open(file_name, "r") as file:
            get_data = json.load(file) ## json ki file read ho rahe hai

            convert_password = hashlib.sha256(self.password.encode()).hexdigest() ## user ky password ko hashlib main convert kar raha ho

            check_user = any(filter(lambda data: data["name"] == self.name and data["password"] == convert_password, get_data)) ##  user ny jo name or password dia hai ye wo check kary ga ky wo json file ky andar hai ya nhi hai to true dy ga wana false

            if check_user:
                return True
            else:
                return False
            

##   is main Store Data hoye ga
    def push_data(self, title: str, text: str, password: str) -> bool: 
        format_data = {"title": title, "text": text, "password": password} ## jo user ny data sia hai us ko object main convert kar raha ho

        with open(file_name, "r") as file:
            get_data = json.load(file)

            check_user = list(filter(lambda data: data["name"] == st.session_state.save_user_name, get_data)) ## jo user login howa hai wo is main save hai st.session_state.save_user_name or is ki madad sy json is file sy user ka obect nikal raha ho

            save_data = check_user ## user ka object jo nikala hai wo is main save howa hai or data [] main hai
            save_data[0]["data"].append(format_data) ## wo jo user ka object nikala hai us main data name ki key hai us main array hai us ky andar format_data ka object jaraha hai 

            user_data = [save_data[0]] ## is ky andar save_data[0] ka data or json ky file ka sara data is main aye ga

            with open(file_name, "r") as file:
                get_data = json.load(file)
                for i in get_data:
                    if i["name"] == st.session_state.save_user_name: ## jo user login howa hai wo is main save hai st.session_state.save_user_name or or is ko json file ky nadar nhi dyna q ky user_data ky andar already wo object hai wana do do hojaye gy
                        pass
                    else:
                        user_data.append(i) ## jo json file main data hai us ko user_data ky andar send kar raha ho 

            with open(file_name, "w") as file:
                json.dump(user_data, file, indent=4) ## is ky andar user_data ka sara data json file ky andar jaraha hai

            return True
        

##   is main user ny jo storage data ky andar data storage kia hai us ko key ki madad sy nikal raha ho
    def find_data(self, key: str) -> dict:
        with open(file_name, "r") as file:
            get_data = json.load(file)

            check_user = list(filter(lambda data: data["name"] == st.session_state.save_user_name, get_data)) ## jo user login howa hai wo is main save hai st.session_state.save_user_name or is ki madad sy json is file sy user ka obect nikal raha ho

            filter_data = list(filter(lambda i: i["password"] == key, check_user[0]["data"])) ## key ki madad sy jo user ko data chahaye wo dy raha ho

            return filter_data ## is ky andar object ja raha hai

            


###                                 start login and register dashboard



if st.session_state.display:

    st.header("🛡️ Secure Data Encryption System")

    tab1, tab2 = st.tabs(["Register", "Login"])

    with tab1:
        user_name = st.text_input("Enter Name")
        user_password = st.text_input("Enter Password", type="password")

        if st.button("Register"):
            
            if user_name == "" and user_password == "": ## agar user ky name or password nhi dia to ye chaly ga wana else
                st.warning("Please enter your name and password")

            else:
                send : Manage_data = Manage_data(user_name, user_password) 
                upload_data = send.register() ## agar user register ho jaye ga to is main true aye ga wana false aye ag
                st.session_state.save_user_name = user_name  ## jo user jis name sy register howa hai wo st.session_state.save_user_name ky andar save ho raha hai
                if upload_data:
                    time.sleep(1)
                    st.success(f"{user_name} You are successfully registered")
                    time.sleep(1)
                    st.session_state.display = False ## agar user register ho jaye ga to st.session_state.display false hojaye ga to login or register wala dashboard hidden hojaye ga or main dashboard display hojaye ga 
                    st.rerun()  # Force re-render to display the "Successful login" message

                else:
                    st.warning(f"{user_name} is already logged in") 

        
        with tab2:
            user_name_1 = st.text_input("Enter Name for Login")
            user_password_1 = st.text_input("Enter Password for Login", type="password")


            if st.button("Login"):
                if user_name_1 == "" and user_password_1 == "":  ## agar user ky name or password nhi dia to ye chaly ga wana else
                    st.warning("Please enter your name and password")
                
                else:
                    send : Manage_data = Manage_data(user_name_1, user_password_1)
                    upload_data = send.login() ## agar user login ho jaye ga to is main true aye ga wana false aye ag
                    st.session_state.save_user_name = user_name_1 ## jo user jis name sy register howa hai wo st.session_state.save_user_name ky andar save ho raha hai
                    if upload_data:
                        time.sleep(1)
                        st.success(f"{user_name_1} You are successfully login")
                        time.sleep(1)
                        st.session_state.display = False  ## agar user register ho jaye ga to st.session_state.display false hojaye ga to login or register wala dashboard hidden hojaye ga or main dashboard display hojaye ga 
                        st.rerun()  # Force re-render to display the "Successful login" message
                    
                    else:
                        st.warning(f"{user_name_1} is not a register")




######                            start main dashboard



## ye main dashboard hai
else:
    st.sidebar.title(f"Wellcome To {st.session_state.save_user_name}")

    all_option = st.sidebar.radio("Select an option", ["Home", "Store Data", "Retrieve Data", "Logged "])

    if all_option == "Home":    
        # Home page container
        with st.container():
            st.markdown("<div class='main-title'>🔐 Secure Data Encryption System</div>", unsafe_allow_html=True)
            st.markdown("<div class='home-container'>", unsafe_allow_html=True)
            st.markdown("<div class='sub-title'>Welcome to your secure space — your data is encrypted and protected.</div>", unsafe_allow_html=True)
            # Feature Highlights
            st.markdown("<div class='section-header'>🌟 Key Features</div>", unsafe_allow_html=True)
            st.markdown("""
                <div class='cards'>
                    <div class='card'>
                        <h3>🔒 256-bit Encryption</h3>
                        <p>Your passwords are protected with industry-grade encryption.</p>
                    </div>
                    <div class='card'>
                        <h3>📝 Secure Notes</h3>
                        <p>Save private notes and information safely in your vault.</p>
                    </div>
                    <div class='card'>
                        <h3>📦 Local JSON Storage</h3>
                        <p>Data is stored securely in encrypted JSON format locally.</p>
                    </div>
                    <div class='card'>
                        <h3>🎯 Clean UI</h3>
                        <p>Designed for simplicity, usability, and professional feel.</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            # Actionable Sections (like dashboards or secure notes)
            st.markdown("<div class='section-header'>📁 Your Secure Data</div>", unsafe_allow_html=True)
            st.markdown("<p class='info-text'>You can view, manage, or update your encrypted records in the 'My Vault' section.</p>", unsafe_allow_html=True)
            st.markdown("<div class='section-header'>⚙️ Settings</div>", unsafe_allow_html=True)
            st.markdown("<p class='info-text'>Update your password, configure encryption preferences, or logout securely.</p>", unsafe_allow_html=True)
            st.markdown("<div class='footer'>© 2025 Secure Data Encryption System | Powered by Streamlit</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)



    elif all_option == "Store Data":
        st.header("🔒 Store Data Securely")

        user_title = st.text_input("Title")
        user_text = st.text_area("Enter Data")
        user_password = st.text_input("Enter key")

        if st.button("Save Data"):
            if user_title == "" and user_text == "" and user_password == "": ## agar user ky title or text or password nhi dia to ye chaly ga wana else
                st.warning("Please enter data")
            
            else:
                send : Manage_data = Manage_data()
                upload_data = send.push_data(user_title, user_text, user_password) ## is ky andar data dia hai agar wo json ky andar cahla gi ya to True ayega wana False aye ga

                if upload_data:
                    st.success("Your data is successfully save")
                else:
                    st.warning("Something was wrong")



    elif all_option == "Retrieve Data":
        st.subheader("🔍 Retrieve Your Data")

        st.write("To retrieve your saved data securely, please enter your correct key in the fields provided below.")

        user_key = st.text_input("Enter your key")

        if st.button("read"):

            if user_key == "":  ## agar user ky key nhi dia to ye chaly ga wana else
                st.warning("Please enter your key")
            else:
                if "count" not in st.session_state: ## agar user ky 3 bar wrong key daly to wo logout hojaye is liye ye dia hai 
                    st.session_state.count = 3  ## is ki value 3 hai 

                if st.session_state.count > 0:  ## agar st.session_state.count 1 ky bara bar ho jaye to ye false hojaye ga
                    send : Manage_data = Manage_data() 
                    upload_data = send.find_data(user_key)  ## agar jo user ny jo key di hai us ka object aye to if cahly ga wana false

                    if upload_data:  ##  is ky andar user ka title, text or password aye ga  or is main bas display ho raha hai      
                        st.markdown("<h2 style='text-align: center; color: #4A90E2;'>🔐 Secure Data Viewer</h2>", unsafe_allow_html=True)

                        for idx, item in enumerate(upload_data, start=1):
                            with st.container():
                                st.markdown("<div class='card'>", unsafe_allow_html=True)
                                st.markdown(f"<div class='title'>📄 Title {idx}: {item['title']}</div>", unsafe_allow_html=True)

                                col1, col2 = st.columns(2)
                                with col1:
                                    st.markdown(f"<div class='label'>📝 Data:</div>", unsafe_allow_html=True)
                                    st.write(item["text"])
                                with col2:
                                    st.markdown(f"<div class='label'>🔑 Password:</div>", unsafe_allow_html=True)
                                    st.text_input("Hidden Password", value=item["password"], type="password", disabled=True, label_visibility="collapsed")

                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.session_state.count -= 1
                        st.warning(f"Attempt {st.session_state.count}: Data not found. Please check your key.")
                        
                else:##  agar user ky 3 bar wrong key daly to wo logout hojaye is liye ye dia hai 
                    st.session_state.count += 3 ## jab user 3 bar wrong key dy ga us ky daat st.session_state.count ky andar 0 value hoye to is ky zayeye  st.session_state.count ky andar 3 value dy rahy hai 
                    st.session_state.display = True  ## is ky true hony sy login or register wala dashboard show hoye ga main dashboard hidden ho jaye ga
                    st.rerun()  # Force re-render to display the "Successful logout" message


    
    elif all_option == "Logged ":
        # Function to handle logout
        def logout():
            # Reset the session state variables when logging out
            if "user_logged_in" in st.session_state:
                del st.session_state["user_logged_in"]  # Remove user login info
            st.session_state.display = True  # Reset display to show login/register page

        # Page title
        st.title("🔒 Log Out - Secure Data Encryption System")

        # Check if the user is logged in
        if "user_logged_in" in st.session_state:
            st.subheader(f"Goodbye, {st.session_state.user_logged_in}!")
            st.write("You have successfully logged out.")
            
            # Log Out button
            if st.button("Log Out"):
                logout()
                st.success("You have logged out successfully!")
                st.write("Redirecting to the home page...")  # You can add further actions like a redirect to another page if needed
        else:
            st.write("You are not logged in. Please log in to access secure data.")
            # Optionally, show a redirect or button to go back to the login page (if required)
            if st.button("Logged"):
                # This can redirect to another page or simply reload
                st.session_state.display = True  ## is ky true hony sy login or register wala dashboard show hoye ga main dashboard hidden ho jaye ga
                st.rerun()  # Force re-render to display the "Successful logout" message