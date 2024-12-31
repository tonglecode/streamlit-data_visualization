import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def dataframe_styling():
    st.title("DataFrame 스타일링")

    # 시드 설정으로 재현 가능한 난수 생성
    np.random.seed(0)
    df = pd.DataFrame(
        np.random.randn(10, 4),
        columns=['A', 'B', 'C', 'D']
    )

    # 기본 스타일링
    st.header("1. 기본 스타일링")
    st.dataframe(df.style.highlight_max(axis=0))

    # 빨강, 노랑, 초록, 핑크 컬러맵 생성
    colors = ['#FF0000', '#FFFF00', '#00FF00', '#FF69B4']  # 빨강, 노랑, 초록, 핑크
    n_bins = 256  # 색상 구간 수
    custom_cmap = LinearSegmentedColormap.from_list(
        "custom", colors, N=n_bins)

    # 기본컬러맵
    camp = plt.cm.get_cmap('RdYlGn')

    # 조건부 스타일링
    st.header("2. 조건부 스타일링")
    styled_df = df.style.format("{:.2f}").\
        background_gradient(
            cmap=camp,
            subset=df.columns  # 모든 열에 그라데이션 적용
    )

    st.dataframe(styled_df)
