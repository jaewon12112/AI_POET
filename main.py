from dotenv import load_dotenv
import os
import streamlit as st
from langchain_openai import ChatOpenAI

# .env 파일 로드
load_dotenv()

# OpenAI API 키 불러오기
api_key = os.getenv("OPENAI_API_KEY")

# LangChain ChatOpenAI 인스턴스 생성
chat_model = ChatOpenAI(api_key=api_key)

# Streamlit UI 구성
st.set_page_config(page_title="AI Poet", page_icon="📝", layout="centered")
st.title("인공지능 시인")
st.markdown("시의 주제를 입력하면 인공지능이 시를 지어드립니다.")

# 사용자 입력
subject = st.text_input(" 시의 주제를 입력해주세요", placeholder="예: 사랑, 자연, 인공지능")

if subject:
    st.write(f"**시의 주제:** {subject}")

# 버튼 클릭 시 시 작성
if st.button("📜 시 작성"):
    with st.spinner("AI 시인이 시를 짓는 중..."):
        try:
            result = chat_model.invoke(f"{subject}에 대한 시를 지어줘.")
            st.success(" 시가 완성되었습니다!")
            st.markdown(f"### AI의 시\n\n{result.content}")
        except Exception as e:
            st.error("❌ 오류가 발생했습니다. API 키 설정 또는 서버 상태를 확인하세요.")
            st.exception(e)