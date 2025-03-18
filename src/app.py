import streamlit as st
from components.dashboard import display_dashboard
from components.filters import display_filters
from components.header import display_header
from utils.data_loader import get_real_time_rates
from styles.custom_styles import load_custom_styles

def main():
    # Set page config
    st.set_page_config(
        page_title="Bank Interest Rate Dashboard",
        page_icon="🏦",
        layout="wide"
    )
    
    # Load custom styles
    load_custom_styles()
    
    # Initialize session states
    if 'previous_country' not in st.session_state:
        st.session_state.previous_country = None
    
    # Display header with attribution
    display_header()
    
    # Load data
    df = get_real_time_rates()
    
    # Display filters in sidebar
    selected_country, selected_term, selected_banks = display_filters(df)
    
    # Display dashboard content
    display_dashboard(df, selected_country, selected_term, selected_banks)

if __name__ == "__main__":
    main() 