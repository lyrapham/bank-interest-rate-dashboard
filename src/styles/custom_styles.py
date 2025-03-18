import streamlit as st

def load_custom_styles():
    st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            border-right: 1px solid #dee2e6;
            padding: 2rem 1rem;
            background-color: #f8f9fa;
        }
        div[data-testid="stSidebarNav"] {
            padding-bottom: 20px;
        }
        .footer {
            font-size: 24px;
            text-align: center;
            color: #666;
            padding: 20px;
        }
        .footer a {
            text-decoration: none;
            color: #0066cc;
        }
        .footer a:hover {
            color: #0052a3;
        }
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0px); }
        }
        .floating {
            display: inline-block;
            animation: float 3s ease-in-out infinite;
        }
        /* Center align dataframe numbers and adjust vertical spacing */
        [data-testid="stDataFrame"] td {
            text-align: center !important;
            padding: 12px 8px !important;
            vertical-align: middle !important;
            font-size: 16px !important;
        }
        [data-testid="stDataFrame"] th {
            text-align: center !important;
            padding: 12px 8px !important;
            vertical-align: middle !important;
            font-size: 16px !important;
            font-weight: 600 !important;
        }
        /* Style sidebar elements */
        [data-testid="stSidebar"] [data-testid="stMarkdown"] {
            padding: 0.5rem 0;
        }
        [data-testid="stSidebar"] .stSelectbox, 
        [data-testid="stSidebar"] .stMultiSelect {
            padding: 0.5rem 0;
        }
        /* Add spacing and styling for section separators */
        .section-separator {
            margin: 1.5rem 0;
            border-top: 1px solid #dee2e6;
            opacity: 0.8;
            width: 100%;
        }
        /* Add spacing for sections */
        .section-content {
            margin: 1rem 0;
        }
        /* Make table borders more visible */
        [data-testid="stDataFrame"] table {
            border-collapse: separate;
            border-spacing: 0;
            width: 100%;
        }
        [data-testid="stDataFrame"] td, 
        [data-testid="stDataFrame"] th {
            border: 1px solid #dee2e6 !important;
        }
    </style>
    """, unsafe_allow_html=True) 