import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def plotly_charts():
    st.title("Plotly 차트")

    # 샘플 데이터 생성
    df = px.data.iris()

    # 산점도
    st.header("1. 산점도")
    fig = px.scatter(
        df,
        x='sepal_width',
        y='sepal_length',
        color='species',
        title='붓꽃 데이터 산점도'
    )
    st.plotly_chart(fig)

    # 박스 플롯
    st.header("2. 박스 플롯")
    fig = px.box(
        df,
        x='species',
        y='sepal_length',
        title='종별 꽃받침 길이 분포'
    )
    st.plotly_chart(fig)

    # 히스토그램
    st.header("3. 히스토그램")
    fig = px.histogram(
        df,
        x='sepal_length',
        color='species',
        title='꽃받침 길이 분포'
    )
    st.plotly_chart(fig)
