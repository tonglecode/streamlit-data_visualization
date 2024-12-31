import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta


class SalesDashboard:
    def __init__(self):
        self.df = self.load_data()

    def load_data(self):
        """샘플 판매 데이터 생성"""
        np.random.seed(0)

        # 날짜 생성
        dates = pd.date_range(
            start='2024-01-01',
            end='2024-12-31',
            freq='D'
        )

        # 제품 목록
        products = ['노트북', '스마트폰', '태블릿', '이어폰']
        regions = ['서울', '부산', '대구', '인천', '광주']

        # 데이터프레임 생성
        data = []
        for date in dates:
            for product in products:
                for region in regions:
                    quantity = np.random.randint(10, 100)
                    price = {
                        '노트북': 1200000,
                        '스마트폰': 800000,
                        '태블릿': 500000,
                        '이어폰': 200000
                    }[product]

                    data.append({
                        '날짜': date,
                        '제품': product,
                        '지역': region,
                        '수량': quantity,
                        '가격': price,
                        '매출': quantity * price
                    })

        return pd.DataFrame(data)

    def run(self):
        st.title("📊 판매 데이터 대시보드")

        # 사이드바 필터
        with st.sidebar:
            st.header("필터 설정")

            # 날짜 범위 선택
            date_range = st.date_input(
                "기간 선택",
                [self.df['날짜'].min(), self.df['날짜'].max()]
            )

            # 제품 선택
            products = st.multiselect(
                "제품 선택",
                self.df['제품'].unique(),
                self.df['제품'].unique()
            )

            # 지역 선택
            regions = st.multiselect(
                "지역 선택",
                self.df['지역'].unique(),
                self.df['지역'].unique()
            )

        # 데이터 필터링
        mask = (
            (self.df['날짜'].dt.date >= date_range[0]) &
            (self.df['날짜'].dt.date <= date_range[1]) &
            (self.df['제품'].isin(products)) &
            (self.df['지역'].isin(regions))
        )

        filtered_df = self.df.loc[mask]

        # 주요 지표
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            total_sales = filtered_df['매출'].sum()
            st.metric("총 매출", f"{total_sales:,.0f}원")

        with col2:
            total_quantity = filtered_df['수량'].sum()
            st.metric("총 판매량", f"{total_quantity:,}개")

        with col3:
            avg_sales = filtered_df.groupby('날짜')['매출'].sum().mean()
            st.metric("일평균 매출", f"{avg_sales:,.0f}원")

        with col4:
            product_count = len(filtered_df['제품'].unique())
            st.metric("제품 수", f"{product_count}개")

        # 차트
        col1, col2 = st.columns(2)

        with col1:
            # 제품별 매출
            sales_by_product = filtered_df.groupby(
                '제품')['매출'].sum().reset_index()
            fig = px.pie(
                sales_by_product,
                values='매출',
                names='제품',
                title='제품별 매출 비중'
            )
            st.plotly_chart(fig)

        with col2:
            # 지역별 매출
            sales_by_region = filtered_df.groupby(
                '지역')['매출'].sum().reset_index()
            fig = px.bar(
                sales_by_region,
                x='지역',
                y='매출',
                title='지역별 매출'
            )
            st.plotly_chart(fig)

        # 시계열 트렌드
        daily_sales = filtered_df.groupby('날짜')['매출'].sum().reset_index()
        fig = px.line(
            daily_sales,
            x='날짜',
            y='매출',
            title='일별 매출 트렌드'
        )
        st.plotly_chart(fig)

        # 상세 데이터
        st.header("상세 데이터")
        st.dataframe(
            filtered_df.style.format({
                '매출': '{:,.0f}원',
                '가격': '{:,.0f}원',
                '수량': '{:,}개'
            })
        )
