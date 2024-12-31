import streamlit as st
import numpy as np
import pandas as pd


def data_filtering():
    st.title("데이터 필터링과 정렬")

    # 데이터 로드
    @st.cache_data
    def load_data():
        # 샘플 데이터 생성
        np.random.seed(0)
        dates = pd.date_range('20240101', periods=100)
        df = pd.DataFrame({
            '날짜': dates,
            '매출': np.random.randint(1000, 10000, 100),
            '비용': np.random.randint(500, 5000, 100),
            '지역': np.random.choice(['서울', '부산', '대구', '인천'], 100)
        })
        df['이익'] = df['매출'] - df['비용']
        return df

    df = load_data()

    # 필터링 컨트롤
    st.sidebar.header("필터 설정")

    # 날짜 범위 선택
    date_range = st.sidebar.date_input(
        "날짜 범위",
        [df['날짜'].min(), df['날짜'].max()]
    )

    # 지역 선택
    selected_regions = st.sidebar.multiselect(
        "지역 선택",
        df['지역'].unique(),
        df['지역'].unique()
    )

    # 최소 매출 선택
    min_revenue = st.sidebar.number_input(
        "최소 매출",
        min_value=int(df['매출'].min()),
        max_value=int(df['매출'].max()),
        value=int(df['매출'].min())
    )

    # 데이터 필터링
    mask = (
        (df['날짜'].dt.date >= date_range[0]) &
        (df['날짜'].dt.date <= date_range[1]) &
        (df['지역'].isin(selected_regions)) &
        (df['매출'] >= min_revenue)
    )

    filtered_df = df.loc[mask]

    # 정렬 옵션
    sort_column = st.selectbox(
        "정렬 기준",
        ['날짜', '매출', '비용', '이익']
    )

    sort_order = st.radio(
        "정렬 순서",
        ['내림차순', '오름차순']
    )

    # 데이터 정렬
    if sort_order == '오름차순':
        filtered_df = filtered_df.sort_values(sort_column)
    else:
        filtered_df = filtered_df.sort_values(sort_column, ascending=False)

    # 결과 표시
    st.header("필터링 및 정렬 결과")
    st.write(f"총 {len(filtered_df)}개의 데이터")
    st.dataframe(filtered_df)

    # 기본 통계
    st.header("기본 통계")
    st.write(filtered_df.describe())
