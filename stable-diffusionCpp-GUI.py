import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import os
import sys
from PIL import ImageTk, Image
from tkinter import ttk

if getattr(sys, 'frozen', False):
    # Executable mode
    application_path = os.path.dirname(sys.executable)
else:
    # Script mode
    application_path = os.path.dirname(os.path.abspath(__file__))

# File path for saving and loading the values
config_file_path = os.path.join(application_path, "config.txt")

# Function to save the values to a file
def save_config():
    config_data = {
        "mode" : mode_entry.get() or "",
        "threads" : threads_entry.get() or "",
        "model" : model_entry.get() or "",
        "vae" : vae_model_dir_entry.get() or "",
        "taesd" : taesd_model_dir_entry.get() or "",
        "embeddings" : emb_model_dir_entry.get() or "",
        "upscale_model" : upscale_model_dir_entry.get() or "",
        "type" : type_entry.get() or "",
        "init_image" : init_image_entry.get() or "",
        "output_image" : output_image_entry.get() or "",
        "strength" : strength_entry.get() or "",
        "lora_model_dir" : lora_model_dir_entry.get() or "",
        "positive_prompt" : positive_prompt_entry.get() or "",
        "negative_prompt" : negative_prompt_entry.get() or "",
        "cfg_scale" : cfg_scale_entry.get() or "",
        "height" : height_entry.get() or "",
        "width" : width_entry.get() or "",
        "sampling_method" : sampling_method_entry.get() or "",
        "steps" : steps_entry.get() or "",
        "rng" : rng_entry.get() or "",
        "seed" : seed_entry.get() or "",
        "batch" : batch_entry.get() or "",
        "schedule" : schedule_entry.get() or "",
        "clip_skip" : clip_skip_entry.get() or "",
        "vae_tiling" : vae_tiling_var.get() or "",
        "cnet_cpu" : cnet_cpu_var.get() or "",
        "canny" : canny_var.get() or "",
        "control_model" : control_model_entry.get() or "",
        "control_image" : control_image_entry.get() or "",
        "control_st" : control_st_entry.get() or "",
        "verbose" : verbose_var.get() or ""
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
            vae_model_dir_entry.insert(0, config_data.get("vae", ""))

            taesd_model_dir_entry.delete(0, tk.END)
            taesd_model_dir_entry.insert(0, config_data.get("taesd", ""))

            emb_model_dir_entry.delete(0, tk.END)
            emb_model_dir_entry.insert(0, config_data.get("embeddings", ""))

            upscale_model_dir_entry.delete(0, tk.END)
            upscale_model_dir_entry.insert(0, config_data.get("upscale_model", ""))

            type_entry.delete(0, tk.END)
            type_entry.insert(0, config_data.get("type", ""))

            init_image_entry.delete(0, tk.END)
            init_image_entry.insert(0, config_data.get("init_image", ""))

            output_image_entry.delete(0, tk.END)
            output_image_entry.insert(0, config_data.get("output_image", ""))

            strength_entry.delete(0, tk.END)
            strength_entry.insert(0, config_data.get("strength", ""))

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

            sampling_method_entry.delete(0, tk.END)
            sampling_method_entry.insert(0, config_data.get("sampling_method", ""))

            steps_entry.delete(0, tk.END)
            steps_entry.insert(0, config_data.get("steps", ""))

            rng_entry.delete(0, tk.END)
            rng_entry.insert(0, config_data.get("rng", ""))

            seed_entry.delete(0, tk.END)
            seed_entry.insert(0, config_data.get("seed", ""))

            batch_entry.delete(0, tk.END)
            batch_entry.insert(0, config_data.get("batch", ""))

            schedule_entry.delete(0, tk.END)
            schedule_entry.insert(0, config_data.get("schedule", ""))

            clip_skip_entry.delete(0, tk.END)
            clip_skip_entry.insert(0, config_data.get("clip_skip", ""))

            temp0 = config_data.get("vae_tiling", "")
            temp0 = False if temp0 == "" else True
            vae_tiling_var.set(temp0)            

            temp1 = config_data.get("cnet_cpu", "")
            temp1 = False if temp1 == "" else True
            cnet_cpu_var.set(temp1)

            temp2 = config_data.get("canny", "")
            temp2 = False if temp2 == "" else True
            canny_var.set(temp2)

            control_model_entry.delete(0, tk.END)
            control_model_entry.insert(0, config_data.get("control_model", ""))

            control_image_entry.delete(0, tk.END)
            control_image_entry.insert(0, config_data.get("control_image", ""))

            control_st_entry.delete(0, tk.END)
            control_st_entry.insert(0, config_data.get("control_st", ""))

            temp3 = config_data.get("verbose", "")
            temp3 = False if temp3 == "" else True
            verbose_var.set(temp3)

def run_sd():
    # Save the values before running the program
    save_config()

    mode = mode_entry.get()
    threads = threads_entry.get()
    model = model_entry.get()
    vae = vae_model_dir_entry.get()
    taesd = taesd_model_dir_entry.get()
    emb = emb_model_dir_entry.get()
    upscale = upscale_model_dir_entry.get()
    type_q = type_entry.get()
    init_image = init_image_entry.get()
    output_image = output_image_entry.get()
    strength = strength_entry.get()
    lora_model_dir = lora_model_dir_entry.get()
    positive_prompt = positive_prompt_entry.get()
    negative_prompt = negative_prompt_entry.get()
    cfg_scale = cfg_scale_entry.get()
    height = height_entry.get()
    width = width_entry.get()
    sampling_method = sampling_method_entry.get()
    steps = steps_entry.get()
    rng_rng = rng_entry.get()
    seed = seed_entry.get()
    batch = batch_entry.get()
    schedule = schedule_entry.get()
    clip_skip = clip_skip_entry.get()
    control_model = control_model_entry.get()
    control_image = control_image_entry.get()
    control_st = control_st_entry.get()

    command = ['./sd']

    if len(mode_entry.get()) > 0:
        command.append("-M")
        command.append(mode)

    if len(threads_entry.get()) > 0:
        command.append("-t")
        command.append(threads)

    if len(model_entry.get()) > 0:
        command.append("-m")
        command.append(model)

    if len(lora_model_dir_entry.get()) > 0:
        command.append("--lora-model-dir")
        command.append(lora_model_dir)

    if len(vae_model_dir_entry.get()) > 0:
        command.append("--vae")
        command.append(vae)

    if len(taesd_model_dir_entry.get()) > 0:
        command.append("--taesd")
        command.append(taesd)

    if len(emb_model_dir_entry.get()) > 0:
        command.append("--embd-dir")
        command.append(emb)

    if len(upscale_model_dir_entry.get()) > 0:
        command.append("--upscale-model")
        command.append(upscale)
	
    if type_entry.get() != "default":
        if len(type_entry.get()) > 0:
            command.append("--type")
            command.append(type_q)

    if len(init_image_entry.get()) > 0:
        command.append("--init-img")
        command.append(init_image)

    if len(output_image_entry.get()) > 0:
        command.append("--output")
        command.append(output_image)

    if len(strength_entry.get()) > 0:
        command.append("--strength")
        command.append(strength)

    if len(positive_prompt_entry.get()) > 0:
        command.append("-p")
        command.append(positive_prompt)

    if len(negative_prompt_entry.get()) > 0:
        command.append("-n")
        command.append(negative_prompt)

    if len(cfg_scale_entry.get()) > 0:
        command.append("--cfg-scale")
        command.append(cfg_scale)

    if len(height_entry.get()) > 0:
        command.append("-H")
        command.append(height)

    if len(width_entry.get()) > 0:
        command.append("-W")
        command.append(width)

    if len(sampling_method_entry.get()) > 0:
        command.append("--sampling-method")
        command.append(sampling_method)

    if len(steps_entry.get()) > 0:
        command.append("--steps")
        command.append(steps)

    if len(rng_entry.get()) > 0:
        command.append("--rng")
        command.append(rng_rng)

    if len(seed_entry.get()) > 0:
        command.append("-s")
        command.append(seed)

    if len(batch_entry.get()) > 0:
        command.append("--batch-count")
        command.append(batch)

    if len(schedule_entry.get()) > 0:
        command.append("--schedule")
        command.append(schedule)

    if len(clip_skip_entry.get()) > 0:
        command.append("--clip-skip")
        command.append(clip_skip)

    if len(control_model_entry.get()) > 0:
        command.append("--control-net")
        command.append(control_model)

    if len(control_image_entry.get()) > 0:
        command.append("--control-image")
        command.append(control_image)

    if len(control_st_entry.get()) > 0:
        command.append("--control-strength")
        command.append(control_st)

## boolean variables
    if canny_var.get() == 1:
        command.append("--canny")

    if cnet_cpu_var.get() == 1:
        command.append("--control-net-cpu")

    if vae_tiling_var.get() == 1:
        command.append("--vae-tiling")

    if verbose_var.get() == 1:
        command.append("-v")
    print(command)
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
		
        # Resize the image to fit within the label (e.g., 300x300 pixels)
        image.thumbnail((500, 500),Image.BICUBIC)
		
        photo = ImageTk.PhotoImage(image)

        # Update the image in the GUI
        image_label.config(image=photo)

        # Update the last modified timestamp
        last_modified = os.path.getmtime(output_image_path)

    # Schedule the next check after a certain interval (in milliseconds)
    root.after(1000, check_file_modification)


output_image_path = "output.png"  # Replace with the actual path of the output image file
photo = None

# Tooltip class, start of code
class Tooltip:
    def __init__(self, widget, text=""):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.id = None

        self.widget.bind("<Enter>", self.show)
        self.widget.bind("<Leave>", self.hide)

    def show(self, event):
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + self.widget.winfo_rooty() + 20

        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(self.tooltip_window, text=self.text, justify="left",
                         background="#ffffff", relief="solid", borderwidth=1,
                         font=("TkDefaultFont", "8"))
        label.pack(ipadx=1)

    def hide(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()

## end of tooltip code


options = ["txt2img", "img2img", "convert"]
mode_label = tk.Label(root, text="txt2img or img2img or convert, default: txt2img):")
mode_label.grid(row=0, column=0)
mode_entry = ttk.Combobox(root, values=options)
mode_entry.current(0)  # Sets the default value to the first option in the list
mode_entry.grid(row=0, column=1)


# Threads
threads_label = tk.Label(root, text="Number of threads:")
threads_label.grid(row=1, column=0)
threads_entry = tk.Entry(root)
threads_entry.grid(row=1, column=1)
# Create a tooltip for Threads entry
tooltip = Tooltip(threads_entry, text="Number of threads to use during computation. \nIf threads <= 0, then threads will be set to \nthe number of CPU physical cores (default: -1)")


# Model
model_label = tk.Label(root, text="Path to Model:")
model_label.grid(row=2, column=0)
model_entry = tk.Entry(root,width=100)
model_entry.grid(row=2, column=1)

def browse_model():
    filename = filedialog.askopenfilename(initialdir='/', title='Select Model File')
    model_entry.delete(0, tk.END)
    model_entry.insert(tk.END, filename)
    
model_browse_button = tk.Button(root, text="Browse", command=browse_model)
model_browse_button.grid(row=2, column=2)


# VAE
vae_model_dir_label = tk.Label(root, text="Path to vae:")
vae_model_dir_label.grid(row=3, column=0)
vae_model_dir_entry = tk.Entry(root,width=100)
vae_model_dir_entry.grid(row=3, column=1)

def browse_VAE():
    filename = filedialog.askopenfilename(initialdir='/', title='Select VAE File')
    vae_model_dir_entry.delete(0, tk.END)
    vae_model_dir_entry.insert(tk.END, filename)
    
vae_model_browse_button = tk.Button(root, text="Browse", command=browse_VAE)
vae_model_browse_button.grid(row=3, column=2)


# Taesd
taesd_model_dir_label = tk.Label(root, text="Path to TAESD. Using Tiny AutoEncoder for fast decoding (low quality):")
taesd_model_dir_label.grid(row=4, column=0)
taesd_model_dir_entry = tk.Entry(root,width=100)
taesd_model_dir_entry.grid(row=4, column=1)

def browse_TAESD():
    filename = filedialog.askopenfilename(initialdir='/', title='Select TAESD File')
    taesd_model_dir_entry.delete(0, tk.END)
    taesd_model_dir_entry.insert(tk.END, filename)
    
taesd_model_browse_button = tk.Button(root, text="Browse", command=browse_TAESD)
taesd_model_browse_button.grid(row=4, column=2)


# Embeddings
emb_model_dir_label = tk.Label(root, text="Path to embeddings:")
emb_model_dir_label.grid(row=5, column=0)
emb_model_dir_entry = tk.Entry(root,width=100)
emb_model_dir_entry.grid(row=5, column=1)

def browse_Embeddings():
    filename = filedialog.askopenfilename(initialdir='/', title='Select embeddings File')
    emb_model_dir_entry.delete(0, tk.END)
    emb_model_dir_entry.insert(tk.END, filename)
    
emb_model_browse_button = tk.Button(root, text="Browse", command=browse_Embeddings)
emb_model_browse_button.grid(row=5, column=2)


# Upscale model
upscale_model_dir_label = tk.Label(root, text="Path to upscaling ESRGAN model. Upscale images after generate, just RealESRGAN_x4plus_anime_6B supported by now:")
upscale_model_dir_label.grid(row=6, column=0)
upscale_model_dir_entry = tk.Entry(root,width=100)
upscale_model_dir_entry.grid(row=6, column=1)

def browse_Upscale():
    filename = filedialog.askopenfilename(initialdir='/', title='Select upscaling model')
    upscale_model_dir_entry.delete(0, tk.END)
    upscale_model_dir_entry.insert(tk.END, filename)
    
upscale_model_browse_button = tk.Button(root, text="Browse", command=browse_Upscale)
upscale_model_browse_button.grid(row=6, column=2)


# Weight type
options = ["default","f32", "f16", "q4_0", "q4_1", "q5_0", "q5_1", "q8_0"]
type_label = tk.Label(root, text="Weight type (f32, f16, q4_0, q4_1, q5_0, q5_1, q8_0). If not specified, the default is the type of the weight file:")
type_label.grid(row=7, column=0)
type_entry = ttk.Combobox(root, values=options)
type_entry.grid(row=7, column=1)


# Init image
init_image_label = tk.Label(root, text="Input image for img2img, required by img2img:")
init_image_label.grid(row=8, column=0)
init_image_entry = tk.Entry(root,width=100)
init_image_entry.grid(row=8, column=1)

def browse_InitImg():
    filename = filedialog.askopenfilename(initialdir='/', title='Select input image img2img')
    init_image_entry.delete(0, tk.END)
    init_image_entry.insert(tk.END, filename)
    
init_image_browse_button = tk.Button(root, text="Browse", command=browse_InitImg)
init_image_browse_button.grid(row=8, column=2)


# output image
output_image_label = tk.Label(root, text="Output image filename (default: output.png):")
output_image_label.grid(row=9, column=0)
output_image_entry = tk.Entry(root,width=100)
output_image_entry.grid(row=9, column=1)

def browse_outputimage():
    filename = filedialog.asksaveasfilename(initialdir='/', title='Select output image')
    output_image_entry.delete(0, tk.END)
    output_image_entry.insert(tk.END, filename)
    
output_image_browse_button = tk.Button(root, text="Browse", command=browse_outputimage)
output_image_browse_button.grid(row=9, column=2)


# Strength
strength_label = tk.Label(root, text="Strength for noising/unnoising (default: 0.75):")
strength_label.grid(row=10, column=0)
strength_entry = tk.Entry(root)
strength_entry.grid(row=10, column=1)

# LoRa Model Directory
lora_model_dir_label = tk.Label(root, text="LoRa Model Directory:")
lora_model_dir_label.grid(row=11, column=0)
lora_model_dir_entry = tk.Entry(root,width=100)
lora_model_dir_entry.grid(row=11, column=1)

def browse_Loramodel():
    filename = filedialog.askdirectory(initialdir='/', title='Select LoRa model directory')
    lora_model_dir_entry.delete(0, tk.END)
    lora_model_dir_entry.insert(tk.END, filename)
    
lora_model_browse_button = tk.Button(root, text="Browse", command=browse_Loramodel)
lora_model_browse_button.grid(row=11, column=2)


# Prompt
positive_prompt_label = tk.Label(root, text="Prompt:")
positive_prompt_label.grid(row=12, column=0)
positive_prompt_entry = tk.Entry(root,width=100)
positive_prompt_entry.grid(row=12, column=1)

# Negative Prompt
negative_prompt_label = tk.Label(root, text="Negative Prompt:")
negative_prompt_label.grid(row=13, column=0)
negative_prompt_entry = tk.Entry(root,width=100)
negative_prompt_entry.grid(row=13, column=1)

# CFG Scale
cfg_scale_label = tk.Label(root, text="Unconditional guidance scale (CFG Scale) (default: 7.0):")
cfg_scale_label.grid(row=14, column=0)
cfg_scale_entry = tk.Entry(root)
cfg_scale_entry.grid(row=14, column=1)

# Height
height_label = tk.Label(root, text="Image Height (default: 512):")
height_label.grid(row=15, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=15, column=1)

# Width
width_label = tk.Label(root, text="Image Width (default: 512):")
width_label.grid(row=16, column=0)
width_entry = tk.Entry(root)
width_entry.grid(row=16, column=1)

# Sampling Method
options2 = ["euler", "euler_a", "heun", "dpm2", "dpm++2s_a", "dpm++2m", "dpm++2mv2", "lcm"]
sampling_method_label = tk.Label(root, text="Sampling method {euler, euler_a, heun, dpm2, dpm++2s_a, dpm++2m, dpm++2mv2, lcm}  (default: euler_a):")
sampling_method_label.grid(row=17, column=0)
sampling_method_entry = ttk.Combobox(root, values=options2)
sampling_method_entry.grid(row=17, column=1)


# Steps
steps_label = tk.Label(root, text="Number of sample steps (default: 20):")
steps_label.grid(row=18, column=0)
steps_entry = tk.Entry(root)
steps_entry.grid(row=18, column=1)

options = ["cuda", "std_default"]
rng_label = tk.Label(root, text="RNG {std_default, cuda} (default: cuda):")
rng_label.grid(row=19, column=0)
rng_entry = ttk.Combobox(root, values=options)
rng_entry.grid(row=19, column=1)

# Seed
seed_label = tk.Label(root, text="RNG seed (default: 42, use random seed for < 0):")
seed_label.grid(row=20, column=0)
seed_entry = tk.Entry(root)
seed_entry.grid(row=20, column=1)

# Batch count
batch_label = tk.Label(root, text="Number of images to generate:")
batch_label.grid(row=21, column=0)
batch_entry = tk.Entry(root)
batch_entry.grid(row=21, column=1)

options = ["discrete", "karras","ays"]
schedule_label = tk.Label(root, text="Denoiser sigma schedule {discrete, karras,ays} (default: discrete):")
schedule_label.grid(row=22, column=0)
schedule_entry = ttk.Combobox(root, values=options)
schedule_entry.grid(row=22, column=1)

# Clip Skip
clip_skip_label = tk.Label(root, text="Clip Skip:")
clip_skip_label.grid(row=23, column=0)
clip_skip_entry = tk.Entry(root)
clip_skip_entry.grid(row=23, column=1)
# Create a tooltip for Clip Skip entry
tooltip = Tooltip(clip_skip_entry, text="Ignore last layers of CLIP network; \n1 ignores none, 2 ignores one layer, <= 0 represents unspecified, \nwill be 1 for SD1.x, 2 for SD2.x (default: -1)")

# VAE tiling
vae_tiling_label = tk.Label(root, text="Process vae in tiles to reduce memory usage:")
vae_tiling_label.grid(row=24, column=0)
#vae_tiling_entry = tk.Entry(root)
#vae_tiling_entry.grid(row=24, column=1)
vae_tiling_var = tk.BooleanVar()
vae_tiling_checkbox = tk.Checkbutton(root, text="", variable=vae_tiling_var)
vae_tiling_checkbox.grid(row=24, column=1)

# ControlNet CPU
cnet_cpu_label = tk.Label(root, text="Keep controlnet in cpu (for low vram):")
cnet_cpu_label.grid(row=25, column=0)
#cnet_cpu_entry = tk.Entry(root)
#cnet_cpu_entry.grid(row=25, column=1)
cnet_cpu_var = tk.BooleanVar()
cnet_cpu_checkbox = tk.Checkbutton(root, text="", variable=cnet_cpu_var)
cnet_cpu_checkbox.grid(row=25, column=1)

# Canny
canny_label = tk.Label(root, text="Apply canny preprocessor (edge detection):")
canny_label.grid(row=26, column=0)
canny_var = tk.BooleanVar()
canny_checkbox = tk.Checkbutton(root, text="", variable=canny_var)
canny_checkbox.grid(row=26, column=1)

# ControlNet model
control_model_label = tk.Label(root, text="ControlNet model:")
control_model_label.grid(row=27, column=0)
control_model_entry = tk.Entry(root,width=100)
control_model_entry.grid(row=27, column=1)

def browse_Controlnet():
    filename = filedialog.askopenfilename(initialdir='/', title='Select controlnet model')
    control_model_entry.delete(0, tk.END)
    control_model_entry.insert(tk.END, filename)
    
control_model_browse_button = tk.Button(root, text="Browse", command=browse_Controlnet)
control_model_browse_button.grid(row=27, column=2)


# ControlNet image
control_image_label = tk.Label(root, text="ControlNet image:")
control_image_label.grid(row=28, column=0)
control_image_entry = tk.Entry(root,width=100)
control_image_entry.grid(row=28, column=1)

def browse_Controlimage():
    filename = filedialog.askopenfilename(initialdir='/', title='Select controlnet image')
    control_image_entry.delete(0, tk.END)
    control_image_entry.insert(tk.END, filename)
    
control_image_browse_button = tk.Button(root, text="Browse", command=browse_Controlimage)
control_image_browse_button.grid(row=28, column=2)


# ControlNet strength
control_st_label = tk.Label(root, text="ControlNet strength:")
control_st_label.grid(row=29, column=0)
control_st_entry = tk.Entry(root)
control_st_entry.grid(row=29, column=1)
# Create a tooltip for ControlNet strength entry
tooltip = Tooltip(control_st_entry, text="Strength to apply Control Net (default: 0.9). \n1.0 corresponds to full destruction of information in init image")

# Verbose
verbose_label = tk.Label(root, text="Verbose output:")
verbose_label.grid(row=30, column=0)
verbose_var = tk.BooleanVar()
verbose_checkbox = tk.Checkbutton(root, text="", variable=verbose_var)
verbose_checkbox.grid(row=30, column=1)

# Run button
run_button = tk.Button(root, text="Run SD", command=run_sd)
run_button.grid(row=31, column=0)
root.bind("<Key>", on_hotkey)  # Bind the hotkey to the root window

# Create a Label widget to display the image
image_label = tk.Label(root)
image_label.grid(row=0, column=3, rowspan=30, padx=20)  # Adjust rowspan and padx as needed

load_config()

# Initialize the last modified timestamp
last_modified = os.path.getmtime(output_image_path) if os.path.exists(output_image_path) else 0

# Start the file modification checking
check_file_modification()

root.mainloop()
