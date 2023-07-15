import streamlit as stm

stm.set_page_config(page_title = "LLM Assistant")
stm.title("Personalized LLM Assistant")

heading = '<h3 style="font-family:Courier; color:Orange; font-style: italic; font-size: 16px;">Unlock the Secrets of Data Analysis with Your Trusted LLM Assistant</h3>'
stm.markdown(heading, unsafe_allow_html=True)
heading = '<p style="font-family:Sans-Serif; color:gray; font-style: italic; font-size: 14px;">Explore, analyze, and visualize data effortlessly, guided by an intelligent companion that adapts to your unique needs. Discover deeper insights, make informed decisions, and elevate your data-driven strategies to new heights.</p>'
stm.markdown(heading, unsafe_allow_html=True)
gif='''
<style>
    .gif-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
      
        
    }

    .gif-container img {
        max-width: 100%;
        max-height: 100%;
        
    }
</style>

<div class="gif-container">
    <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgQXWoE6YAxVVZtPhmUUj2TDGSOdKYYX9nMWUrBGVmaTtjQ_oqChBnrtemyHCYZKKE6svxZchRJlLj3m1s31NAHoWstSFYL2tQbYQM4UODKN6c7PXXXFUQM45K-FPHbXzagLRrevieIceDUuhGBtULDHbFFO04AIQTbWiWGC6-NAJZHVf9be-2PdvEeg/s1559/LLM4Mobile%201.gif">
</div>'''

stm.markdown(gif, unsafe_allow_html=True)

stm.sidebar.success("Select Any Page from here")