import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Descargar datos de SPY (ETF del S&P 500), BTC (Bitcoin), URTH (MSCI World) y QQQ (Nasdaq 100)
spy = yf.download('SPY', start='2020-01-01', end='2024-11-11')
btc = yf.download('BTC-USD', start='2020-01-01', end='2024-11-11')
msci = yf.download('URTH', start='2020-01-01', end='2024-11-11')
nasdaq = yf.download('QQQ', start='2020-01-01', end='2024-11-11')

# Normalizar los datos para la comparación (todos comienzan en 100)
spy['Normalized'] = (spy['Adj Close'] / spy['Adj Close'].iloc[0]) * 100
btc['Normalized'] = (btc['Adj Close'] / btc['Adj Close'].iloc[0]) * 100
msci['Normalized'] = (msci['Adj Close'] / msci['Adj Close'].iloc[0]) * 100
nasdaq['Normalized'] = (nasdaq['Adj Close'] / nasdaq['Adj Close'].iloc[0]) * 100

# Crear un gráfico interactivo para los cuatro activos
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=spy.index, y=spy['Normalized'], mode='lines', name='SPY (S&P 500 ETF)'))
fig1.add_trace(go.Scatter(x=btc.index, y=btc['Normalized'], mode='lines', name='Bitcoin (BTC)'))
fig1.add_trace(go.Scatter(x=msci.index, y=msci['Normalized'], mode='lines', name='URTH (MSCI World)'))
fig1.add_trace(go.Scatter(x=nasdaq.index, y=nasdaq['Normalized'], mode='lines', name='QQQ (Nasdaq 100)'))

fig1.update_layout(title='Comparación del rendimiento de SPY, Bitcoin, MSCI World y Nasdaq 100',
                   xaxis_title='Fecha',
                   yaxis_title='Rendimiento Normalizado',
                   template='plotly_dark')

# Crear un gráfico interactivo para SPY, MSCI World y Nasdaq 100
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=spy.index, y=spy['Normalized'], mode='lines', name='SPY (S&P 500 ETF)'))
fig2.add_trace(go.Scatter(x=msci.index, y=msci['Normalized'], mode='lines', name='URTH (MSCI World)'))
fig2.add_trace(go.Scatter(x=nasdaq.index, y=nasdaq['Normalized'], mode='lines', name='QQQ (Nasdaq 100)'))

fig2.update_layout(title='Comparación del rendimiento de SPY, MSCI World y Nasdaq 100',
                   xaxis_title='Fecha',
                   yaxis_title='Rendimiento Normalizado',
                   template='plotly_dark')

# Mostrar ambos gráficos
fig1.show()
fig2.show()
