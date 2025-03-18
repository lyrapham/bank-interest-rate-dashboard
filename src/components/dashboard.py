import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def display_dashboard(df, selected_country, selected_term, selected_banks):
    if not selected_banks:
        st.warning("Please select at least one bank to display the rates.")
        return

    # Filter data for selected banks and term
    term_filtered_df = df[df['Term_Months'] == selected_term]
    display_df = term_filtered_df[term_filtered_df['Bank'].isin(selected_banks)]
    latest_date = display_df['Date'].max()
    latest_df = display_df[display_df['Date'] == latest_date]

    # Main dashboard area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        display_trend_chart(df, selected_banks, selected_term)
    
    with col2:
        display_current_rates(latest_df, selected_term)
    
    # Display statistics and insights
    display_statistics(latest_df)
    display_market_analysis(latest_df)
    display_investment_suggestions(latest_df, selected_term)
    display_all_terms_table(df, selected_banks, latest_date)
    display_footer()

def display_trend_chart(df, selected_banks, selected_term):
    st.subheader("Interest Rate Trends Over Time")
    trend_df = df[
        (df['Bank'].isin(selected_banks)) & 
        (df['Term_Months'] == selected_term)
    ]
    
    fig_line = px.line(
        trend_df,
        x='Date',
        y='Interest_Rate',
        color='Bank',
        title=f'Historical Interest Rates ({selected_term}-Month Term)',
        labels={'Interest_Rate': 'Interest Rate (%)', 'Date': 'Month'},
        line_shape='spline',
        hover_data={'Interest_Rate': ':.2f'}
    )
    fig_line.update_traces(mode='lines+markers')
    fig_line.update_layout(
        height=400,
        hovermode='x unified',
        yaxis=dict(range=[
            trend_df['Interest_Rate'].min() - 0.5,
            trend_df['Interest_Rate'].max() + 0.5
        ])
    )
    st.plotly_chart(fig_line, use_container_width=True)

def display_current_rates(latest_df, selected_term):
    st.subheader("Current Rates Comparison")
    fig_bar = go.Figure(data=[
        go.Bar(
            x=latest_df['Bank'],
            y=latest_df['Interest_Rate'],
            text=latest_df['Interest_Rate'].apply(lambda x: f"{x:.2f}%"),
            textposition='auto',
            hovertemplate="Bank: %{x}<br>Rate: %{y:.2f}%<extra></extra>"
        )
    ])
    
    fig_bar.update_layout(
        title=f'Current Interest Rates ({selected_term}-Month Term)',
        xaxis_title='Bank',
        yaxis_title='Interest Rate (%)',
        height=400,
        showlegend=False
    )
    st.plotly_chart(fig_bar, use_container_width=True)

def display_statistics(latest_df):
    st.subheader("Summary Statistics")
    col1, col2, col3 = st.columns(3)
    
    avg_rate = latest_df['Interest_Rate'].mean()
    min_rate = latest_df['Interest_Rate'].min()
    max_rate = latest_df['Interest_Rate'].max()
    
    with col1:
        st.metric("Average Rate", f"{avg_rate:.2f}%")
    with col2:
        st.metric("Minimum Rate", f"{min_rate:.2f}%")
    with col3:
        st.metric("Maximum Rate", f"{max_rate:.2f}%")

def display_market_analysis(latest_df):
    st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-content">', unsafe_allow_html=True)
    st.subheader("📊 Market Analysis & Insights")
    
    avg_rate = latest_df['Interest_Rate'].mean()
    min_rate = latest_df['Interest_Rate'].min()
    max_rate = latest_df['Interest_Rate'].max()
    rate_range = max_rate - min_rate
    best_bank = latest_df.loc[latest_df['Interest_Rate'].idxmax(), 'Bank']
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Key Statistics")
        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
        
        with metrics_col1:
            st.metric("Market Average", f"{avg_rate:.2f}%", 
                     delta=f"{(avg_rate - min_rate):.2f}% above lowest")
        with metrics_col2:
            st.metric("Rate Spread", f"{rate_range:.2f}%",
                     help="Difference between highest and lowest rates")
        with metrics_col3:
            st.metric("Best Rate", f"{max_rate:.2f}%", 
                     delta=f"{(max_rate - avg_rate):.2f}% above average")
    
    with col2:
        st.markdown("### Market Position")
        for bank in latest_df['Bank']:
            bank_rate = latest_df[latest_df['Bank'] == bank]['Interest_Rate'].iloc[0]
            position = sum(latest_df['Interest_Rate'] > bank_rate) + 1
            total_banks = len(latest_df)
            st.markdown(f"• **{bank}**: #{position} of {total_banks} ({bank_rate:.2f}%)")
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_investment_suggestions(latest_df, selected_term):
    st.markdown('<div class="section-separator"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-content">', unsafe_allow_html=True)
    st.markdown("### 💡 Investment Suggestions")
    
    max_rate = latest_df['Interest_Rate'].max()
    avg_rate = latest_df['Interest_Rate'].mean()
    rate_range = max_rate - latest_df['Interest_Rate'].min()
    best_bank = latest_df.loc[latest_df['Interest_Rate'].idxmax(), 'Bank']
    
    recommendations = []
    recommendations.append(f"🏆 **Best Rate**: {best_bank} offers the highest rate at {max_rate:.2f}%")
    
    if rate_range > 0.5:
        recommendations.append("📈 **High Spread Alert**: Consider switching banks as there's significant rate variation")
    
    if selected_term >= 12:
        if max_rate > 5.5:
            recommendations.append("🎯 **Long-term Opportunity**: Current long-term rates are attractive for locking in")
        else:
            recommendations.append("⚠️ **Consider Short-term**: Long-term rates might not offer sufficient premium")
    
    if avg_rate > 5.0:
        recommendations.append("📊 **Market Insight**: Current rates are historically favorable")
    
    for rec in recommendations:
        st.markdown(rec)
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_all_terms_table(df, selected_banks, latest_date):
    st.subheader("All Term Periods")
    all_terms_df = df[
        (df['Bank'].isin(selected_banks)) & 
        (df['Date'] == latest_date)
    ].sort_values(['Bank', 'Term_Months'])
    
    pivot_df = all_terms_df.pivot(
        index='Bank',
        columns='Term_Months',
        values='Interest_Rate'
    ).round(2)
    
    pivot_df.columns = [f"{int(col)} Month{'s' if col > 1 else ''}" for col in pivot_df.columns]
    
    styled_df = pivot_df.style.set_properties(**{
        'text-align': 'center'
    }).format("{:.2f}")
    
    st.dataframe(styled_df, use_container_width=True)

def display_footer():
    st.markdown("---")
    
    # Randomly decide whether to show piggy banks
    if np.random.random() < 0.3:  # 30% chance to show piggy banks
        piggy_left = '<span class="floating">🐷</span>'
        piggy_right = '<span class="floating" style="animation-delay: 1s">🐷</span>'
    else:
        piggy_left = ''
        piggy_right = ''
    
    st.markdown(
        f"""
        <div class="footer">
        {piggy_left} By <a href="https://www.linkedin.com/in/lyrapham/" target="_blank">Lyra Pham</a> 😚 - Jan 2025 {piggy_right}<br>
        <span style="font-size: 18px;">Check my profile to see other projects! :) Thank you!</span>
        </div>
        """,
        unsafe_allow_html=True
    ) 