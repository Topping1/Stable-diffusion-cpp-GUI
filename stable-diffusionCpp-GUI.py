import tkinter as tk
from tkinter import filedialog
import subprocess
import os
from PIL import ImageTk, Image

# File path for saving and loading the values
config_file_path = os.path.join(os.path.dirname(__file__), "config.txt")

# Function to save the values to a file
def save_config():
    config_data = {
        "mode" : mode_entry.get() or "",
        "threads" : threads_entry.get() or "",
        "model" : model_entry.get() or "",
        "vae" : vae_model_dir_entry.get() or "",
        "lora_model_dir" : lora_model_dir_entry.get() or "",
        "positive_prompt" : positive_prompt_entry.get() or "",
        "negative_prompt" : negative_prompt_entry.get() or "",
        "cfg_scale" : cfg_scale_entry.get() or "",
        "height" : height_entry.get() or "",
        "width" : width_entry.get() or "",
        "steps" : steps_entry.get() or "",
        "seed" : seed_entry.get() or "",
        "control_model" : control_model_entry.get() or "",
        "control_image" : control_image_entry.get() or "",
        "control_st" : control_st_entry.get() or ""
    }

    with open(config_file_path, "w") as f:
        for key, value in config_data.items():
            f.write(f"{key}: {value}\n")

# Function to load the values from the file
def load_config():
    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as f:
            config_data = {}
            for line in f:
                line = line.strip()
                if line:
                    if ": " in line:
                        key, value = line.split(": ", 1)
                        config_data[key] = value

            mode_entry.delete(0, tk.END)
            mode_entry.insert(0, config_data.get("mode", ""))

            threads_entry.delete(0, tk.END)
            threads_entry.insert(0, config_data.get("threads", ""))

            model_entry.delete(0, tk.END)
            model_entry.insert(0, config_data.get("model", ""))

            vae_model_dir_entry.delete(0, tk.END)
            vae_model_dir_entry.insert(0, config_data.get("vae_model_dir", ""))

            lora_model_dir_entry.delete(0, tk.END)
            lora_model_dir_entry.insert(0, config_data.get("lora_model_dir", ""))

            positive_prompt_entry.delete(0, tk.END)
            positive_prompt_entry.insert(0, config_data.get("positive_prompt", ""))

            negative_prompt_entry.delete(0, tk.END)
            negative_prompt_entry.insert(0, config_data.get("negative_prompt", ""))

            cfg_scale_entry.delete(0, tk.END)
            cfg_scale_entry.insert(0, config_data.get("cfg_scale", ""))

            height_entry.delete(0, tk.END)
            height_entry.insert(0, config_data.get("height", ""))

            width_entry.delete(0, tk.END)
            width_entry.insert(0, config_data.get("width", ""))

            steps_entry.delete(0, tk.END)
            steps_entry.insert(0, config_data.get("steps", ""))

            seed_entry.delete(0, tk.END)
            seed_entry.insert(0, config_data.get("seed", ""))

            control_model_entry.delete(0, tk.END)
            control_model_entry.insert(0, config_data.get("control_model", ""))

            control_image_entry.delete(0, tk.END)
            control_image_entry.insert(0, config_data.get("control_image", ""))

            control_st_entry.delete(0, tk.END)
            control_st_entry.insert(0, config_data.get("control_st", ""))

def run_sd():
    # Save the values before running the program
    save_config()

    mode = mode_entry.get()
    threads = threads_entry.get()
    model = model_entry.get()
    vae = vae_model_dir_entry.get()
    lora_model_dir = lora_model_dir_entry.get()
    positive_prompt = positive_prompt_entry.get()
    negative_prompt = negative_prompt_entry.get()
    cfg_scale = cfg_scale_entry.get()
    height = height_entry.get()
    width = width_entry.get()
    steps = steps_entry.get()
    seed = seed_entry.get()
    control_model = control_model_entry.get()
    control_image = control_image_entry.get()
    control_st = control_st_entry.get()

    command = ['./sd', '-M', mode,'-t', threads, '-m', model, '--lora-model-dir',lora_model_dir, '--vae', vae, '-p', positive_prompt, '-n', negative_prompt, '--cfg-scale', cfg_scale, '-H', height, '-W', width, '--steps', steps,'-s', seed, '--control-net', control_model,'--control-image', control_image,'--control-strength', control_st,'--sampling-method','lcm','-v']

    subprocess.run(command)

def browse_file(entry):
    filename = filedialog.askopenfilename(initialdir='/', title='Select File')
    entry.delete(0, tk.END)
    entry.insert(tk.END, filename)

def browse_directory(entry):
    directory = filedialog.askdirectory(initialdir='/', title='Select Directory')
    entry.delete(0, tk.END)
    entry.insert(tk.END, directory)

def on_hotkey(event):
    if event.keysym == "r" and event.state == 8:  # Check for ALT key
        run_sd()  # Call the button's function

root = tk.Tk()
root.title("Stable-diffusion.cpp simple GUI")

def check_file_modification():
    global photo, last_modified

    # Check if the output image file exists and has been modified
    if os.path.exists(output_image_path) and os.path.getmtime(output_image_path) > last_modified:
        # Load the updated image
        image = Image.open(output_image_path)
        photo = ImageTk.PhotoImage(image)

        # Update the image in the GUI
        image_label.config(image=photo)

        # Update the last modified timestamp
        last_modified = os.path.getmtime(output_image_path)

    # Schedule the next check after a certain interval (in milliseconds)
    root.after(1000, check_file_modification)


output_image_path = "output.png"  # Replace with the actual path of the output image file
photo = None

# Mode
mode_label = tk.Label(root, text="Run mode (txt2img or img2img or convert):")
mode_label.grid(row=0, column=0)
mode_entry = tk.Entry(root)
mode_entry.grid(row=0, column=1)

# Threads
threads_label = tk.Label(root, text="Number of Threads:")
threads_label.grid(row=1, column=0)
threads_entry = tk.Entry(root)
threads_entry.grid(row=1, column=1)

# Model
model_label = tk.Label(root, text="Path to Model:")
model_label.grid(row=2, column=0)
model_entry = tk.Entry(root,width=100)
model_entry.grid(row=2, column=1)

# VAE
vae_model_dir_label = tk.Label(root, text="Path to vae:")
vae_model_dir_label.grid(row=3, column=0)
vae_model_dir_entry = tk.Entry(root,width=100)
vae_model_dir_entry.grid(row=3, column=1)

# LoRa Model Directory
lora_model_dir_label = tk.Label(root, text="LoRa Model Directory:")
lora_model_dir_label.grid(row=4, column=0)
lora_model_dir_entry = tk.Entry(root,width=100)
lora_model_dir_entry.grid(row=4, column=1)

# Prompt
positive_prompt_label = tk.Label(root, text="Prompt:")
positive_prompt_label.grid(row=5, column=0)
positive_prompt_entry = tk.Entry(root,width=100)
positive_prompt_entry.grid(row=5, column=1)

# Negative Prompt
negative_prompt_label = tk.Label(root, text="Negative Prompt:")
negative_prompt_label.grid(row=6, column=0)
negative_prompt_entry = tk.Entry(root,width=100)
negative_prompt_entry.grid(row=6, column=1)

# CFG Scale
cfg_scale_label = tk.Label(root, text="CFG Scale:")
cfg_scale_label.grid(row=7, column=0)
cfg_scale_entry = tk.Entry(root)
cfg_scale_entry.grid(row=7, column=1)

# Height
height_label = tk.Label(root, text="Image Height:")
height_label.grid(row=8, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=8, column=1)

# Width
width_label = tk.Label(root, text="Image Width:")
width_label.grid(row=9, column=0)
width_entry = tk.Entry(root)
width_entry.grid(row=9, column=1)

# Steps
steps_label = tk.Label(root, text="Number of Steps:")
steps_label.grid(row=10, column=0)
steps_entry = tk.Entry(root)
steps_entry.grid(row=10, column=1)

# Seed
seed_label = tk.Label(root, text="Seed:")
seed_label.grid(row=11, column=0)
seed_entry = tk.Entry(root)
seed_entry.grid(row=11, column=1)

# ControlNet model
control_model_label = tk.Label(root, text="ControlNet model:")
control_model_label.grid(row=12, column=0)
control_model_entry = tk.Entry(root,width=100)
control_model_entry.grid(row=12, column=1)

# ControlNet image
control_image_label = tk.Label(root, text="ControlNet image:")
control_image_label.grid(row=13, column=0)
control_image_entry = tk.Entry(root,width=100)
control_image_entry.grid(row=13, column=1)

# ControlNet strength
control_st_label = tk.Label(root, text="ControlNet strength:")
control_st_label.grid(row=14, column=0)
control_st_entry = tk.Entry(root)
control_st_entry.grid(row=14, column=1)

# Run button
run_button = tk.Button(root, text="Run SD", command=run_sd)
run_button.grid(row=15, column=0)
root.bind("<Key>", on_hotkey)  # Bind the hotkey to the root window

# Create a Label widget to display the image
image_label = tk.Label(root)
image_label.grid(row=0, column=2, rowspan=12, padx=20)  # Adjust rowspan and padx as needed

load_config()

# Initialize the last modified timestamp
last_modified = os.path.getmtime(output_image_path) if os.path.exists(output_image_path) else 0

# Start the file modification checking
check_file_modification()

root.mainloop()