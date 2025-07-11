# To run this file we need to install streamlit and also make sure we have python in our system

# To run this in vs code, open the terminal, copy the path of the folder in which you have this python file. then enter -> streamlit run file_name.py

import streamlit as st

st.set_page_config(page_title="To Do List", page_icon="📝") # title of the tab and icon

st.markdown("""
    <style>
        body {
            background-color: black;
        }
        .title {
            color: #ff0000;
            text-align: center;
            font-size: 48px;
        }
        .task-box {
            background-color: #1a1a1a;
            padding: 10px 15px;
            margin-bottom: 10px;
            border-radius: 8px;
            border-left: 4px solid #ff0000;
            color: white;
        }
        .stButton > button {
            background-color: #ff0000;
            color: black;
            border-radius: 8px;
            padding: 0.5em 1em;
            border: solid;
        }
        .stButton > button:hover {
            background-color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📝 To Do List</div>', unsafe_allow_html=True)

if "tasks" not in st.session_state:
    st.session_state.tasks = []

with st.form("task_form", clear_on_submit=True):
    task_input = st.text_input("Add a new Task", "")
    submitted = st.form_submit_button("Add Task")
    if submitted and task_input.strip():
        st.session_state.tasks.append({"task": task_input.strip(), "done": False})

st.subheader("Your Tasks", divider="red")

if not st.session_state.tasks:
    st.info(" No tasks yet!")
else:
    updated_tasks = []
    for i, item in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            done = st.checkbox(
                "Mark done",
                value=item["done"],
                key=f"check_{i}",
                label_visibility="collapsed"
            )
        with col2:
            task_text = f"~~{item['task']}~~" if done else item["task"]
            st.markdown(f'<div class="task-box">{task_text}</div>', unsafe_allow_html=True)
        updated_tasks.append({"task": item["task"], "done": done})

    st.session_state.tasks = updated_tasks

if any(task["done"] for task in st.session_state.tasks):
    if st.button("🗑️ Clear Completed Tasks"):
        st.session_state.tasks = [task for task in st.session_state.tasks if not task["done"]]
        
        st.success("Are you sure you completed the task ? ")
