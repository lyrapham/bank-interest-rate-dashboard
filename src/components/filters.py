import streamlit as st

def display_filters(df):
    st.sidebar.markdown("## 📊 Filter Options")
    
    # Country selection
    selected_country = st.sidebar.selectbox(
        "Select Country",
        options=['All'] + list(df['Country'].unique()),
        help="Choose a country to see its banks or 'All' to compare across countries"
    )
    
    # Filter available terms based on country
    filtered_df = df
    if selected_country != 'All':
        filtered_df = df[df['Country'] == selected_country]
    
    # Term selection
    selected_term = st.sidebar.selectbox(
        "Select Term",
        options=sorted(filtered_df['Term_Months'].unique()),
        format_func=lambda x: f"{x} month{'s' if x > 1 else ''}",
        help="Choose the deposit term period"
    )
    
    # Get available banks based on country selection
    term_filtered_df = filtered_df[filtered_df['Term_Months'] == selected_term]
    available_banks = term_filtered_df['Bank'].unique()
    bank_help = f"Select banks to compare their {selected_term}-month term deposit rates"
    
    # Bank selection
    selected_banks = st.sidebar.multiselect(
        "Select Banks",
        options=available_banks,
        default=available_banks[:3],
        help=bank_help
    )
    
    # Show selected country's banks
    if selected_country != 'All':
        st.sidebar.markdown("---")
        st.sidebar.markdown(f"### Available Banks in {selected_country}")
        for bank in available_banks:
            st.sidebar.markdown(f"• {bank}")
    
    return selected_country, selected_term, selected_banks 