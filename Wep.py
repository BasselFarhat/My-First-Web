import streamlit as st

# 1. Initialize our post storage with style and alignment settings
if "my_posts" not in st.session_state:
    st.session_state.my_posts = [] 

# --- Sidebar: Admin Control Panel ---
st.sidebar.title("🛠️ Admin Dashboard")
password = st.sidebar.text_input("Admin Password:", type="password")

if password == "1234":
    st.sidebar.success("Edit Mode Active")
    
    # --- SECTION A: ADD NEW POST ---
    st.sidebar.subheader("➕ Add New Post")
    new_content = st.sidebar.text_area("Write here:", key="new_post_input")
    
    # Styling for the new post
    col_a, col_b = st.sidebar.columns(2)
    with col_a:
        new_size = st.sidebar.slider("Font Size:", 10, 80, 24, key="new_size")
        new_align = st.sidebar.selectbox("Alignment:", ["left", "center", "right"], key="new_align")
    with col_b:
        new_color = st.sidebar.color_picker("Text Color:", "#FFFFFF", key="new_color")
    
    if st.sidebar.button("Post to Website"):
        if new_content:
            st.session_state.my_posts.append({
                "text": new_content,
                "size": new_size,
                "color": new_color,
                "align": new_align
            })
            st.rerun()

    # --- SECTION B: EDIT/DELETE EXISTING ---
    if st.session_state.my_posts:
        st.sidebar.markdown("---")
        st.sidebar.subheader("📝 Edit/Delete Posts")
        
        post_indices = range(len(st.session_state.my_posts))
        selected_index = st.sidebar.selectbox("Select Post:", post_indices, format_func=lambda x: f"Post #{x+1}")
        
        current_post = st.session_state.my_posts[selected_index]
        
        # Edit inputs
        edit_text = st.sidebar.text_area("Edit Text:", current_post["text"])
        edit_size = st.sidebar.slider("Edit Size:", 10, 80, current_post["size"])
        edit_color = st.sidebar.color_picker("Edit Color:", current_post["color"])
        edit_align = st.sidebar.selectbox("Edit Alignment:", ["left", "center", "right"], index=["left", "center", "right"].index(current_post.get("align", "left")))
        
        col1, col2 = st.sidebar.columns(2)
        with col1:
            if st.button("Update Post"):
                st.session_state.my_posts[selected_index] = {
                    "text": edit_text,
                    "size": edit_size,
                    "color": edit_color,
                    "align": edit_align
                }
                st.rerun()
        with col2:
            if st.button("🗑️ Delete"):
                st.session_state.my_posts.pop(selected_index)
                st.rerun()

# --- Main Display Section ---
st.title("Bassel's Custom Blog 📝")
st.write("Control your content and layout directly from the dashboard.")

for i, post in enumerate(st.session_state.my_posts):
    # محاذاة النص تتم عبر خاصية text-align في الـ div المحيط
    st.markdown(
        f"""
        <div style="
            border: 1px solid #444; 
            padding: 20px; 
            border-radius: 12px; 
            margin-bottom: 15px;
            text-align: {post.get('align', 'left')};
        ">
            <p style="color: grey; font-size: 12px; margin-bottom: 5px;">Post #{i+1}</p>
            <p style="
                font-size:{post['size']}px; 
                color:{post['color']};
                margin: 0;
                line-height: 1.4;
            ">
                {post['text']}
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )