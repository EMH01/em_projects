import gradio as gr
import requests
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

API_URL = os.getenv("FLOWISE_URL")
headers = {"Authorization": os.getenv("FLOWISE_TOKEN")}
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


def bot_query(message, history):
    """
    Function to call FlowiseAI API using graphQL
    """
    query = f"""
    query {{
        flowise(message: "{message}", history: {[]})
    }}
    """
    try:
        response_flowise = requests.post(
            "https://esthermariamh-graphql.hf.space/", json={"query": query}
        )
        # http Error
        response_flowise.raise_for_status()
        return response_flowise.json()["data"]["flowise"]
    except requests.exceptions.RequestException:
        return """Sorry, I can't connect to the server at the moment.
         Please try again later."""


def conectDB():
    """
    Function to connect to the supabase database.
    """
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def check_auth(username, password):
    """
    Function to check in the database,
    the username and password to log in the app.
    """
    client = conectDB()
    response = (
        client.table("credentials")
        .select("user, password")
        .eq("user", username)
        .eq("password", password)
        .execute()
    )
    return len(response.data) > 0


def create_account(user, password):
    """
    Function to create a new account, and add it to database
    """
    client = conectDB()
    if not user or not password:
        return (
            """<h3 style='color: red;'>User name and password can't be empty.</h3>""",
            "",
            "",
            "",
        )  # Returns the message and empty values for the fields
    try:
        client.table("credentials").insert(
            {"user": user, "password": password}
        ).execute()
        # Indicates that the account was created
        return (
            "<h3 style='color: green;'>Account successfully created</h3>",
            "",
            "",
            "",
        )  # Clears the fields
    except Exception:  # Indicates that an error occurred
        return (
            "<h3 style='color: orange;'>"
            "This user and password already exist."
            "Try again with another combination.</h3>",
            "",
            "",
            "",
        )


def delete_account(user, password, password2):
    """
    Function to delete the account from database
    """
    client = conectDB()
    if password != password2:
        return (
            "<h3 style='color: red;'>It can't be any empty field.</h3>",
            "",
            "",
            "",
        )  # Clears the fields
    response = (
        client.table("credentials")
        .select("user, password")
        .eq("user", user)
        .eq("password", password)
        .execute()
    )
    if response.data:
        client.table("credentials").delete().eq("user", user).eq(
            "password", password
        ).execute()
        return (
            "<h3 style='color: green;'>Account successfully deleted</h3>",
            "",
            "",
            "",
        )
    # Indicates that the account was not found
    return (
        "<h3 style='color: red;'>You wrote a wrong password or account.</h3>",
        "",
        "",
        "",
    )


def login(username, password):
    """
    Function to control the visibility of login and app page.
    Simulating a multipage app
    """
    if check_auth(username, password):
        return (
            "",
            gr.update(visible=False),
            gr.update(visible=True),
            "",
            "",
            "",
        )  # Hides the login page and shows the app, clears all fields
    else:
        return (
            "<h3 style='color: red;'>Invalid username or password.</h3>",
            gr.update(visible=True),
            gr.update(visible=False),
            "",
            "",
            "",
        )  # Error message


def login_page():
    """
    Function to build the components of the app.
    Separating the pages in tabs
    """
    with gr.Blocks(title="Weather Assistant") as demo:
        with gr.Row():
            with gr.Column(
                visible=True
            ) as login_col:  # Login page is visible initially
                with gr.Tab("Create account"):
                    inp_a = gr.Textbox(
                        label="User Name", placeholder="Write the user name"
                    )
                    inp_p = gr.Textbox(
                        label="Password",
                        placeholder="Write the password",
                        type="password",
                    )
                    btn1 = gr.Button("Create")
                    out_create = gr.Markdown()

                with gr.Tab("Delete account"):
                    header = """<h1 style='text-align: left;'>
                     This action is irreversible ⚠️ </h1>"""
                    gr.Markdown(header)
                    inp_ad = gr.Textbox(
                        label="User Name", placeholder="Write the user name"
                    )
                    inp_pd = gr.Textbox(
                        label="Password",
                        placeholder="Write your password",
                        type="password",
                    )
                    inp_pd2 = gr.Textbox(
                        label="Password",
                        type="password",
                        placeholder="Write your password again to be sure",
                    )
                    btn2 = gr.Button("Delete")
                    out_delete = gr.Markdown()

                with gr.Tab("Log in"):
                    inp_user = gr.Textbox(
                        label="User Name", placeholder="Write your user name"
                    )
                    inp_pass = gr.Textbox(
                        label="Password",
                        placeholder="Write your password",
                        type="password",
                    )
                    btn_login = gr.Button("Login")
                    login_output = gr.Markdown()

            # App page is hidden initially
            with gr.Column(visible=False) as app_col:
                header = """<h1 style='text-align: center;'>
                🌤️ Your Personal Weather Assistant 🌤️</h1>"""
                gr.Markdown(header)
                gr.ChatInterface(
                    bot_query,
                    theme="soft",
                    chatbot=gr.Chatbot(
                        placeholder="""<strong>Your Personal Weather Assistant
                        </strong><br>
                        You can ask me about the weather or
                         anything else related"""
                    ),
                    fill_height=True,
                )
                btn_logout = gr.Button("Logout")
                btn_logout.click(
                    fn=lambda: (
                        gr.update(visible=True),
                        gr.update(visible=False),
                    ),
                    outputs=[login_col, app_col],
                )

        # Connect buttons to functions
        btn1.click(
            fn=create_account,
            inputs=[inp_a, inp_p],
            outputs=[out_create, inp_a, inp_p],
        )
        btn2.click(
            fn=delete_account,
            inputs=[inp_ad, inp_pd, inp_pd2],
            outputs=[out_delete, inp_ad, inp_pd, inp_pd2],
        )
        btn_login.click(
            fn=login,
            inputs=[inp_user, inp_pass],
            outputs=[login_output, login_col, app_col, inp_user, inp_pass],
        )

    return demo


# Launches the application
if __name__ == "__main__":
    demo = login_page()
    demo.launch()

