"""
Ready Set Comply — v1

A simple Streamlit app that generates a Cyber Essentials Plus
prep checklist so SME owners don't have to start from a blank page
when audit time comes round.

Run locally with: streamlit run app.py
"""

import streamlit as st
from ce_plus_data import CE_PLUS_CONTROLS

st.set_page_config(page_title="Ready Set Comply", page_icon="🛡️", layout="centered")

st.title("🛡️ Ready Set Comply")
st.caption("Audit prep, without the panic.")
st.write(
    "Generate a plain-English Cyber Essentials Plus prep checklist — "
    "what you need, what auditors will ask for, and where SMEs usually "
    "get caught out."
)

st.divider()

company_name = st.text_input("Company name (optional, just for your generated runbook)")

st.write("### Generate your runbook")
if st.button("Generate CE+ Runbook", type="primary"):
    st.divider()
    heading = f"Ready Set Comply — Runbook for {company_name}" if company_name else "Ready Set Comply — Runbook"
    st.header(heading)

    for theme, details in CE_PLUS_CONTROLS.items():
        with st.expander(f"📋 {theme}", expanded=True):
            st.write(details["description"])

            st.markdown("**Evidence you'll likely need to show:**")
            for item in details["required_evidence"]:
                st.checkbox(item, key=f"{theme}-{item}")

            if details["panic_points"]:
                st.markdown("**Where SMEs commonly get caught out:**")
                for point in details["panic_points"]:
                    st.warning(point)

    st.divider()
    st.info(
        "This is a v1 focused on Cyber Essentials Plus. More standards "
        "(GDPR, ISO 27001, ISO 42001) are planned next, based on feedback "
        "from this version."
    )

st.divider()
st.caption(
    "Built by Arohi Bhate, grounded in dissertation research into cyber "
    "law and compliance burden for SMEs. Feedback welcome via GitHub issues."
)
