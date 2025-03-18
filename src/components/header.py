import streamlit as st
from datetime import datetime

def display_header():
    # Author attribution at the top
    st.markdown(
        f"""
        <div class="footer" style="margin-bottom: 20px;">
        <span class="floating">🐷</span> By <a href="https://www.linkedin.com/in/lyrapham/" target="_blank">Lyra Pham</a> 😚 - Jan 2025 <span class="floating" style="animation-delay: 1s">🐷</span>
        </div>
        <div style='text-align: center; color: #666; font-size: 16px;'>
        Data last updated: {datetime.now().strftime('%B %d, %Y')}
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Title and welcome message
    st.title("🏦 Bank Interest Rate Dashboard")
    st.markdown("""
    ### Welcome to the Banking Interest Rate Analysis Platform!
    
    This dashboard provides interactive visualization of interest rates across major banks in Vietnam and Canada.
    Select a country to see its banks, or choose 'All' to compare across countries.
    
    Data shown includes various term deposits:
    - 1 month to 36 months
    - Hover over the charts for detailed information
    - Real-time data updates (when available)
    """) 