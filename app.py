import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from black_scholes import black_scholes
from implied_volatility import implied_volatility


st.set_page_config(
        page_title="Black–Scholes model & Implied Volatility",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )
st.title("Black-Scholes Option Pricing Model")
main_col, param_col = st.columns([3, 1])

with param_col:
    linkedin_url = "https://www.linkedin.com/in/mikhail-ignatenko-b79876243/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Mikhail Ignatenko`</a>', unsafe_allow_html=True)
    tg_link = "https://t.me/mikhail_lc"
    st.markdown(f'<a href="{tg_link}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/128/2111/2111646.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Mikhail I`</a>', unsafe_allow_html=True)
    github_link = "https://github.com/m-ignatenko"
    st.markdown(f'<a href="{github_link}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/128/14063/14063266.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Mikhail I`</a>', unsafe_allow_html=True)


    st.header("Option parameters")
    S = st.number_input("Price for time t (S)", value=100.0, step=1.0)
    K = st.number_input("Strike price (K)", value=105.0, step=1.0)
    tau = st.number_input("Time to maturity in years(tau)", value=1.0, min_value=0.01, step=0.1)
    r = st.slider("Risk-free rate (r)", 0.0, 0.2, 0.05, 0.01)
    sigma = st.slider("Volatility (σ)", 0.01, 5.0, 0.2, 0.01)

    call_price = black_scholes(S, tau, r, K, sigma)[0]
    put_price = black_scholes(S, tau, r, K, sigma)[1]
    st.metric(label="Call Option Price", value=f"{call_price:.3f}")
    st.metric(label="Put Option Price", value=f"{put_price:.3f}")

with main_col:
    

    T_range = np.linspace(0.01, tau + 2.5, 100)
    call_prices = [black_scholes(S, t, r, K, sigma)[0] for t in T_range]
    put_prices = [black_scholes(S, t, r, K, sigma)[1] for t in T_range]
    current_call = black_scholes(S, tau, r, K, sigma)[0]
    current_put = black_scholes(S, tau, r, K, sigma)[1]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=T_range,
        y=call_prices,
        mode='lines',
        name='Call Option',
        line=dict(color='red')
    ))

    fig.add_trace(go.Scatter(
        x=T_range,
        y=put_prices,
        mode='lines',
        name='Put Option',
        line=dict(color='#81EC7C')
    ))

    fig.add_vline(
        x=tau,
        line=dict(color='green', dash='dash'),
        annotation_text=f'Current Maturity: {tau:.2f} years',
        annotation_position="top right"
    )

    fig.add_trace(go.Scatter(
        x=[tau],
        y=[current_call],
        mode='markers',
        name='Current Call Price',
        marker=dict(color='red', size=10)
    ))

    fig.add_trace(go.Scatter(
        x=[tau],
        y=[current_put],
        mode='markers',
        name='Current Put Price',
        marker=dict(color='#81EC7C', size=10)
    ))

    fig.update_layout(
        title='Option Prices vs Time to Maturity',
        xaxis_title='Time to Maturity (years)',
        yaxis_title='Option Price',
        hovermode='x unified',
        showlegend=True,
        template='plotly_white',
        height=500
    )
    st.markdown("[Black–Scholes model article](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)")

    st.plotly_chart(fig, use_container_width=True)


    st.header("Implied Volatility (IV) calculation for CALL options")
    C_market = st.number_input('Market price for option (C_market)',value = 10.0, step=1.0)
    S_vol = st.number_input("Current price for option (S_vol)", value=100.0, step=1.0)
    K_vol = st.number_input("Strike price (K_vol)", value=100.0, step=1.0)
    tau_vol = st.number_input("Time to maturity in years (tau_vol)", value=1.0, min_value=0.01, step=0.1)
    r_vol = st.slider("Risk-free rate (r_vol)", 0.0, 0.2, 0.05, 0.01)

    sigma_vol = implied_volatility(C_market,S_vol,K_vol,tau_vol,r_vol)
    st.metric(label="Calculated Volatility", value=f"{sigma_vol:.4f}")  