import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Grant Writer", page_icon="✍️")
st.title("✍️ AI Grant Proposal Writer")

# Step 1: User Inputs
st.header("1. Enter Grant Details")
organization_name = st.text_input("Organization Name")
project_focus = st.text_input("Project Focus (e.g., after-school STEM program)")
funding_amount = st.text_input("Requested Funding Amount")
grant_goals = st.text_area("What are the main goals of the project?")
funder_priorities = st.text_area("Funder Priorities (e.g., community impact, innovation)")

# Step 2: Generate Draft
if st.button("Generate Grant Proposal", type="primary"):
    if not organization_name or not project_focus:
        st.warning("Please fill in the Organization Name and Project Focus.")
    else:
        with st.spinner("Drafting your proposal..."):
            
            # Construct the prompt
            prompt = f"""
            You are an expert grant writer. Write a compelling grant proposal for {organization_name}.
            Project Focus: {project_focus}
            Requested Amount: {funding_amount}
            Project Goals: {grant_goals}
            Funder Priorities to address: {funder_priorities}

            The proposal should include:
            1. Executive Summary
            2. Statement of Need
            3. Project Description
            4. Goals and Objectives
            5. Conclusion
            """

            try:
                # Call the OpenAI API
                response = client.chat.completions.create(
                    model="gpt-4o",  # You can also use "gpt-4o-mini" for faster/cheaper results
                    messages=[
                        {"role": "system", "command": "You are an expert, persuasive grant writer."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )

                # Display the results
                st.success("Proposal Generated Successfully!")
                st.subheader("Draft Proposal")
                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error(f"An error occurred: {e}")
