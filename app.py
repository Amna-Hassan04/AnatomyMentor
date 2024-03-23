import streamlit as st



#Main Function 
def main():
    st.set_page_config(page_title="GlucoGuide", layout="wide")
    #st.title("AnatomyMentor")
    st.image("images/image.png")
    st.markdown("*AnatomyMentor* Our anatomy tutoring app is designed to assist medical students in learning complex anatomical concepts with ease. Through interactive lessons, visual aids, and personalized learning features, students can delve into various anatomy topics, such as nerves, muscles, and organs. The app also offers question generation for practice and incorporates image processing capabilities to analyze uploaded anatomical structure images. By leveraging the power of AI, our app aims to provide comprehensive and tailored support to enhance the anatomy learning experience for students.")


    
    #sidebar
    with st.sidebar:
        st.header("Controls")
        anotomay_topic = st.text_area("Please enter the anatomy topic or specific area you would like to learn more about. This could include nerves, muscles, organs, or any other specific anatomical structures or systems. Providing a clear topic will help us tailor the learning content and resources to your specific needs:", height=20)
        anatomy_mcqs = st.text_area("How many multiple-choice questions would you like to generate for practicing anatomy concepts?", height=20)
        anatomy_pic = st.file_uploader("Please upload an image of the anatomical structure you would like to learn more about:")
        

        generate_plan_btn = st.button("Generate analysis and questions")

    col1, col2 = st.columns(2)

    with col1:
        #meal plan
        st.subheader("Anatomy Topic Analysis:")

        # write output in this command st.markdown("") rather than st.text("")
        
        st.divider()

      
        
        

    with col2:
        #Exercise plan
        st.subheader("Question Generation:")
        # write output in this command st.markdown("") rather than st.text("")

        

        st.divider()

        st.subheader("Anatomical Structure Image Analysis and Description:")
        # write output in this command st.markdown("") rather than st.text("")


        st.divider()

        
        


        
        


#Run Main Function 
if __name__ == "__main__":
    main()

                

