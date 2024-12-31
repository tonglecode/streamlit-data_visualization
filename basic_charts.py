import streamlit as st
import pandas as pd
import numpy as np


def basic_charts():

    st.title("Streamlit 기본 차트")

    # 샘플 데이터 생성
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )

    # 라인차트
    st.header("1. 라인 차트")
    st.line_chart(chart_data)

    # 영역차트
    st.header("2. 영역 차트")
    st.area_chart(chart_data)

    # 바 차트
    st.header("3. 바 차트")
    st.bar_chart(chart_data)
