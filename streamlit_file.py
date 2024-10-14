import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import re


st.title("Study Smart Web App")

#tools for app ->

def graphing_tool():
    st.title("Graphing Tool")

    # Selectbox for choosing a mathematical function
    function_options = {
        "x^2": "x**2",
        "sin(x)": "np.sin(x)",
        "cos(x)": "np.cos(x)",
        "tan(x)": "np.tan(x)",
        "e^x": "np.exp(x)",
        "1/x": "1/x",
    }
    
    selected_function = st.selectbox("Choose a function to graph:", list(function_options.keys()))
    function_input = function_options[selected_function]

    # User input for the x-range
    x_min = st.number_input("Enter the minimum x value", -10)
    x_max = st.number_input("Enter the maximum x value", 10)

    # Generate x values
    x = np.linspace(x_min, x_max, 400)

    # Calculate y values based on user input
    try:
        y = eval(function_input)

        # Create a figure and plot
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(x, y, label=f'y = {selected_function}', color='blue')
        ax.set_title("Graph of the Function")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.axhline(0, color='black', lw=0.5, ls='--')
        ax.axvline(0, color='black', lw=0.5, ls='--')
        ax.grid()
        ax.legend()

        # Render the plot in Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        return None

    st.title("Graphing Tool")

    # User input for the function
    function_input = st.text_input("Enter a mathematical function (e.g., x**2, np.sin(x))", "x**2")

    # User input for the x-range
    x_min = st.number_input("Enter the minimum x value", -10)
    x_max = st.number_input("Enter the maximum x value", 10)

    # Generate x values
    x = np.linspace(x_min, x_max, 400)

    # Calculate y values based on user input
    try:
        y = eval(function_input)
        
        # Plotting
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, label=f'y = {function_input}', color='blue')
        plt.title("Graph of the Function")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.grid()
        plt.legend()
        
        # Display the plot
        st.pyplot(plt)
    
    except Exception as e:
        st.error(f"Error: {e}")

def equation_solver():
    st.title("Equation Solver")

    # Input for the equation
    equation = st.text_input("Enter a linear equation (e.g., '2x + 3 = 7'):")

    if st.button("Solve"):
        # Extract coefficients and constants from the equation
        match = re.match(r'([+-]?\d*\.?\d*)x\s*([+-]?\s*\d*\.?\d*)\s*=\s*([+-]?\s*\d*\.?\d*)', equation.replace(" ", ""))
        if match:
            a = float(match.group(1)) if match.group(1) != '' else 1
            b = float(match.group(2).replace(" ", "")) if match.group(2) != '' else 0
            c = float(match.group(3).replace(" ", ""))

            # Solve for x
            try:
                x = (c - b) / a
                st.success(f"The solution for the equation {equation} is: x = {x:.2f}")
            except ZeroDivisionError:
                st.error("Error: Division by zero. The equation has no solution.")
        else:
            st.error("Error: Invalid equation format. Please use the format 'ax + b = c'.")

def unit_converter():
    st.title("Unit Converter")

    # Select conversion type
    conversion_type = st.selectbox("Choose a conversion type:", ["Length", "Weight", "Temperature"])

    if conversion_type == "Length":
        st.subheader("Length Converter")
        length_value = st.number_input("Enter value in meters:")
        length_unit = st.selectbox("Convert to:", ["Kilometers", "Centimeters", "Millimeters", "Miles", "Feet", "Inches"])
        
        if st.button("Convert"):
            if length_unit == "Kilometers":
                result = length_value / 1000
            elif length_unit == "Centimeters":
                result = length_value * 100
            elif length_unit == "Millimeters":
                result = length_value * 1000
            elif length_unit == "Miles":
                result = length_value / 1609.34
            elif length_unit == "Feet":
                result = length_value * 3.28084
            elif length_unit == "Inches":
                result = length_value * 39.3701
            
            st.success(f"{length_value} meters = {result:.4f} {length_unit}")

    elif conversion_type == "Weight":
        st.subheader("Weight Converter")
        weight_value = st.number_input("Enter value in kilograms:")
        weight_unit = st.selectbox("Convert to:", ["Grams", "Pounds", "Ounces", "Stones"])

        if st.button("Convert"):
            if weight_unit == "Grams":
                result = weight_value * 1000
            elif weight_unit == "Pounds":
                result = weight_value * 2.20462
            elif weight_unit == "Ounces":
                result = weight_value * 35.274
            elif weight_unit == "Stones":
                result = weight_value * 0.157473

            st.success(f"{weight_value} kilograms = {result:.4f} {weight_unit}")

    elif conversion_type == "Temperature":
        st.subheader("Temperature Converter")
        temp_value = st.number_input("Enter value in Celsius:")
        temp_unit = st.selectbox("Convert to:", ["Fahrenheit", "Kelvin"])

        if st.button("Convert"):
            if temp_unit == "Fahrenheit":
                result = (temp_value * 9/5) + 32
            elif temp_unit == "Kelvin":
                result = temp_value + 273.15

            st.success(f"{temp_value}°C = {result:.2f} {temp_unit}")




#home page

def home():
    st.write("Welcome To Study Smart App Which Makes Your Education Simple")
    
    current_class = st.selectbox("Choose Your Current Class",["None" , "Class 9th" , "Class 10th" , "Class 11th" , "Class 12th"])

    if current_class == "Class 9th":
        subject = st.selectbox("Choose The Subject",["None" , "Science" , "Social Study" , "Maths"])

        if subject == "Science":
            chapter = st.selectbox("Select The Chapter",["None" , "Matter In Our Surrounding" , "Is Matter Around Us Pure" , "Atoms And Molecules" , "Structure Of Atom" , "The Fundamental Unit Of Life" , "Tissues" , "Diversity in Living Organisms" , "Motion" , "Force and Laws of Motion" , "Gravitation" , "Work, Power And Energy" , "Sound" , "Why Do we Fall Ill" , "Natural Resources" , " Improvement in Food Resources"])


            if chapter == "Matter In Our Surrounding":
                tab1,tab2,tab3 = st.tabs(["All Topics" , "Notes" , "Question Blank"])

                with tab1:
                    topic = st.selectbox("Choose Your Topic",["None" , "Definition of Matter" , "Characteristics of Matter" , "hree states of matter: Solid, Liquid, and Gas" , "Comparison of the characteristics of these states" , "Interconversion of States of Matter"])

                with tab2:
                    st.markdown("[Full Complete Notes](https://drive.google.com/file/d/1rPXrZVSAVF103m-jeTaGoXI6gZooIZ9_/view)")

def about():
    st.markdown("**About Study Smarter**")
    st.write("Welcome to *Study Smarter* – your go-to platform for smarter, more efficient learning. "
              "Our web app is designed to empower students and lifelong learners by providing the tools, "
              "resources, and techniques needed to optimize study habits and boost productivity. Whether "
              "you're preparing for exams, mastering new skills, or simply looking to stay organized, "
              "*Study Smarter* has you covered.")

    st.markdown("**Created By**")
    st.write("*Study Smarter* is developed by Samarth Taneja, along with a passionate team of educators "
              "and tech enthusiasts dedicated to transforming the way you study. We are committed to "
              "continuous improvement and innovation, ensuring our platform remains at the forefront of "
              "educational technology.")

    st.markdown("**Theme: Computational Thinking**")
    st.write("Our app incorporates the principles of computational thinking to enhance learning. "
              "By breaking down complex problems, recognizing patterns, and developing systematic solutions, "
              "*Study Smarter* helps you become a more effective and analytical learner.")

def tools():
    st.write("Get Almost All The Essential Tools Here")
    tool_type = st.selectbox("Choose The Tool",["None" , "Quadratic Equation Solver" , "Graphing Tool" , "Linear Equation Solver" , "Unit Converter"])

    if tool_type == "Quadratic Equation Solver":
        st.title("Quadratic Equation Solver")
        st.write("Enter the coefficients of the quadratic equation in the form of ax² + bx + c = 0")

        a = st.number_input("Enter coefficient a (non-zero)", min_value=-100.0, max_value=100.0, value=1.0)
        b = st.number_input("Enter coefficient b", min_value=-100.0, max_value=100.0, value=0.0)
        c = st.number_input("Enter coefficient c", min_value=-100.0, max_value=100.0, value=0.0)

        if st.button("Solve"):
            if a == 0:
               st.error("Coefficient 'a' cannot be zero. Please enter a valid value.")
            else:
                roots = solve_quadratic(a, b, c)
                if roots is None:
                   st.write("The equation has no real roots.")
                elif len(roots) == 1:
                    st.write(f"The equation has one real root: x = {roots[0]}")
                else:
                    st.write(f"The equation has two real roots: x₁ = {roots[0]}, x₂ = {roots[1]}")

    elif tool_type == "Graphing Tool":
        graphing_tool()
    
    elif tool_type == "Linear Equation Solver":
        equation_solver()
    
    elif tool_type == "Unit Converter":
        unit_converter()



#sidebar
st.sidebar.header("Overview")
page = st.sidebar.selectbox("Choose a page", ["Home", "My Work", "About App" , "Resources" , "Tools"])
st.sidebar.markdown("[VIDEO TUTORIAL](https://www.youtube.com)")

if page == "Home":
    home()
elif page == "About App":
    about()
elif page == "Tools":
    tools()

else:
    st.write("Contact us at: example@example.com")