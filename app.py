
import streamlit as st
import pandas as pd
import io

st.title("엑셀 자동 통합 프로그램")

st.write("📂 여러 엑셀 파일을 하나로 통합합니다.")
st.write("✅ 파일명은 '위험성평가_이름_날짜.xlsx' 형태를 추천합니다.")
st.write("---")

uploaded_files = st.file_uploader("엑셀 파일 여러개 업로드하기", accept_multiple_files=True, type=["xlsx"])

if uploaded_files:
    dfs = []
    for uploaded_file in uploaded_files:
        df = pd.read_excel(uploaded_file)
        df['파일명'] = uploaded_file.name  # 파일명도 기록
        dfs.append(df)
    
    if dfs:
        merged_df = pd.concat(dfs, ignore_index=True)
        st.success("✅ 통합이 완료되었습니다!")

        # 수정된 다운로드용 코드
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            merged_df.to_excel(writer, index=False)
        output.seek(0)

        st.download_button(
            label="📥 통합된 엑셀파일 다운로드 (위험성평가_통합본.xlsx)",
            data=output,
            file_name="위험성평가_통합본.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
