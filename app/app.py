import gradio as gr

def greet(name):
    if not name.strip():
        return "Please enter your name!"
    return f"Hello, {name}! Welcome to MLOps CI/CD Practice! 🚀"

# Create Gradio interface with better styling
iface = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(placeholder="Enter your name here...", label="Your Name"),
    outputs=gr.Textbox(label="Greeting"),
    title="🤖 MLOps CI/CD Practice App",
    description="This is a simple Gradio app deployed via GitHub Actions to Hugging Face Spaces!",
    theme=gr.themes.Soft(),
    examples=[["Alice"], ["Bob"], ["Charlie"]]
)

if __name__ == "__main__":
    iface.launch()