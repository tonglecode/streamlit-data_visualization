import streamlit as st
import pandas as pd


def pandas_basics():
    st.title("Pandas 기초와 Streamlit")

    # 샘플 데이터 생성
    data = {
        '이름': ['김철수', '이영희', '박민수', '정지원', '홍길동'],
        '나이': [25, 28, 21, 30, 35],
        '성적': [85, 92, 78, 95, 88],
        '등급': ['B', 'A', 'C', 'A', 'B']
    }

    df = pd.DataFrame(data)

    # 기본 데이터프레임 표시
    st.header("1. 기본 데이터프레임")
    st.dataframe(df)

    # 정적 테이블로 표시
    st.header("2. 정적 테이블")
    st.table(df)

    # 기술 통계량
    st.header("3. 기술 통계량")
    st.write(df.describe())

    # 필터링 섹션
    st.header("4. 데이터 필터링")

    # 이름 검색 필터 추가
    name_search = st.text_input("이름 검색")
    grade_filter = st.selectbox(
        "등급 선택", ['모두'] + list(df['등급'].unique()))

    # 필터링 로직
    filtered_df = df

    # 이름 검색 필터 적용
    if name_search:
        filtered_df = filtered_df[filtered_df['이름'].str.contains(
            name_search, na=False)]

        # 등급 필터 적용
    if grade_filter != '모두':
        filtered_df = filtered_df[filtered_df['등급'] == grade_filter]

    st.write(filtered_df)
