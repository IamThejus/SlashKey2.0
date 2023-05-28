from tkinter import *
from tkinter import messagebox
import json
import threading
import time
import openai
import os


# Engine Threading

module = None

def load_module():
    global module
    import final as mod
    module = mod


threading.Thread(target=load_module).start()


# Functions to start windows


def start_welcome():
    global welcome_win, bn
    welcome_win = Tk()
    welcome_win.title('Welcome User')
    welcome_win.geometry('800x500')
    
    # Get the screen width and height
    screen_width = welcome_win.winfo_screenwidth()
    screen_height = welcome_win.winfo_screenheight()
    
    # Calculate the x and y coordinates for centering the window
    x = int((screen_width / 2) - (800 / 2))
    y = int((screen_height / 2) - (500 / 2))
    
    # Set the window position
    welcome_win.geometry(f'800x500+{x}+{y}')
    
    
    tx = Label(welcome_win, text='Welcome User\nDisease Prediction System', font=('arial',25))
    tx.place(relx=0.5, rely=0.4, anchor='center')
    
    bn = Button(welcome_win, text='START', command=end_wel, font=('arial',15))
    bn.place(relx=0.5, rely=0.6, anchor='center')
    
    welcome_win.mainloop()


def user_info_window():
    # Window formation and geometry
    global i_name, i_age, i_height, i_weight, window
    window = Tk()
    window.title('User Meta Data')
    window.geometry('800x500')

    # Creating Widgets
    t_name = Label(window, text='Name')
    t_age = Label(window, text='Age')
    t_height = Label(window, text='Height')
    t_weight = Label(window, text='Weight')

    i_name = Text(window, width=10, height=1)
    i_age = Text(window, width=10, height=1)
    i_height = Text(window, width=10, height=1)
    i_weight = Text(window, width=10, height=1)

    enter_button = Button(window, width=10, text='Click', command=read_text)

    # Widgets Positioning
    t_name.grid(row=2, column=1, padx=10, pady=10)
    t_age.grid(row=3, column=1, padx=10, pady=10)
    t_height.grid(row=4, column=1, padx=10, pady=10)
    t_weight.grid(row=5, column=1, padx=10, pady=10)

    i_name.grid(row=2, column=2, padx=10, pady=10)
    i_age.grid(row=3, column=2, padx=10, pady=10)
    i_height.grid(row=4, column=2, padx=10, pady=10)
    i_weight.grid(row=5, column=2, padx=10, pady=10)

    enter_button.grid(row=6, column=2, padx=10, pady=10, sticky='e')

    # Center the content
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(7, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(3, weight=1)

    # Running on a mainloop
    window.mainloop()


def main_window():

    # Window creating and geometry

    global main_win, drop, clicked, textbox, submit, selected_tab

    main_win = Tk()
    main_win.geometry('800x500')
    main_win.title('Disease Predition')


    # widgets

    # Dropdown menu options
    options = ['Itching', 'Skin Rash', 'Nodal Skin Eruptions', 'Continuous Sneezing', 'Shivering', 'Chills', 'Joint Pain', 'Stomach Pain', 'Acidity', 'Ulcers On Tongue', 'Muscle Wasting', 'Vomiting', 'Burning Micturition', 'Spotting  Urination', 'Fatigue', 'Weight Gain', 'Anxiety', 'Cold Hands And Feets', 'Mood Swings', 'Weight Loss', 'Restlessness', 'Lethargy', 'Patches In Throat', 'Irregular Sugar Level', 'Cough', 'High Fever', 'Sunken Eyes', 'Breathlessness', 'Sweating', 'Dehydration', 'Indigestion', 'Headache', 'Yellowish Skin', 'Dark Urine', 'Nausea', 'Loss Of Appetite', 'Pain Behind The Eyes', 'Back Pain', 'Constipation', 'Abdominal Pain', 'Diarrhoea', 'Mild Fever', 'Yellow Urine', 'Yellowing Of Eyes', 'Acute Liver Failure', 'Fluid Overload', 'Swelling Of Stomach', 'Swelled Lymph Nodes', 'Malaise', 'Blurred And Distorted Vision', 'Phlegm', 'Throat Irritation', 'Redness Of Eyes', 'Sinus Pressure', 'Runny Nose', 'Congestion', 'Chest Pain', 'Weakness In Limbs', 'Fast Heart Rate', 'Pain During Bowel Movements', 'Pain In Anal Region', 'Bloody Stool', 'Irritation In Anus', 'Neck Pain', 'Dizziness', 'Cramps', 'Bruising', 'Obesity', 'Swollen Legs', 'Swollen Blood Vessels', 'Puffy Face And Eyes', 'Enlarged Thyroid',
               'Brittle Nails', 'Swollen Extremeties', 'Excessive Hunger', 'Extra Marital Contacts', 'Drying And Tingling Lips', 'Slurred Speech', 'Knee Pain', 'Hip Joint Pain', 'Muscle Weakness', 'Stiff Neck', 'Swelling Joints', 'Movement Stiffness', 'Spinning Movements', 'Loss Of Balance', 'Unsteadiness', 'Weakness Of One Body Side', 'Loss Of Smell', 'Bladder Discomfort', 'Foul Smell Of urine', 'Continuous Feel Of Urine', 'Passage Of Gases', 'Internal Itching', 'Toxic Look (typhos)', 'Depression', 'Irritability', 'Muscle Pain', 'Altered Sensorium', 'Red Spots Over Body', 'Belly Pain', 'Abnormal Menstruation', 'Dischromic  Patches', 'Watering From Eyes', 'Increased Appetite', 'Polyuria', 'Family History', 'Mucoid Sputum', 'Rusty Sputum', 'Lack Of Concentration', 'Visual Disturbances', 'Receiving Blood Transfusion', 'Receiving Unsterile Injections', 'Coma', 'Stomach Bleeding', 'Distention Of Abdomen', 'History Of Alcohol Consumption', 'Fluid Overload.1', 'Blood In Sputum', 'Prominent Veins On Calf', 'Palpitations', 'Painful Walking', 'Pus Filled Pimples', 'Blackheads', 'Scurring', 'Skin Peeling', 'Silver Like Dusting', 'Small Dents In Nails', 'Inflammatory Nails', 'Blister', 'Red Sore Around Nose', 'Yellow Crust Ooze']

    # Label Frame for Symptoms
    label_frame = LabelFrame(
        main_win, text="Select Symptoms", padx=10, pady=10)
    label_frame.pack(padx=10, pady=10)

    # Add Symptom Button
    button = Button(label_frame, text='Add Symptom', command=get_name)
    button.grid(row=1, column=1, pady=10)

    # Submit Button
    submit = Button(main_win, text='Submit', command=submit_bn)
    submit.pack(pady=10)


    clicked = StringVar()

    # Create Dropdown Menu
    drop = OptionMenu(label_frame, clicked, *options)
    drop.grid(row=1, column=2, padx=10)

    # Selected Symptoms Textbox
    selected_tab = Text(main_win, width=40, height=5)
    selected_tab.pack(pady=10)

    exit_button=Button(main_win,text='Exit',command=to_exit)
    exit_button.pack(pady=10)


    # Mainloop
    main_win.mainloop()





# Main Functions


def end_wel():
    welcome_win.destroy()


def read_text():
    global window
    name, age, height, weight = i_name.get("1.0", 'end-1c'), i_age.get(
        "1.0", 'end-1c'), i_height.get("1.0", 'end-1c'), i_weight.get("1.0", 'end-1c')
    data = {'name': name,
            'age': age,
            'height': height,
            'weight': weight}
    json_obj = json.dumps(data, indent=4)
    with open('data.json', 'w') as file:
        file.write(json_obj)
    window.destroy()

start_welcome()

try:
    with open('data.json', 'r') as file:
        read_file = file.read()
    data = json.loads(read_file)
except:
    user_info_window()

with open('data.json', 'r') as file:
    read_file = file.read()
data = json.loads(read_file)

def reply(disease):
    chat=f'{disease} what are medicine doctors precsribe in 200 words'
    openai.api_key='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'
    engines = openai.Engine.list()
    input_data=openai.Completion.create(
    model="text-davinci-003",
    prompt=chat,
    max_tokens=250,
    temperature=0
    )
    return input_data['choices'][0]['text']



symptoms = []
slected_text = ''


def to_exit():
    main_win.destroy()

def get_name():
    global symptoms,selected_tab,slected_text
    selected_tab.delete("1.0",END)
    data=clicked.get()
    if data.title() not in symptoms and data.title()!='':
        symptoms.append(data.title())
        slected_text+=str(len(symptoms))+" "+data.title()+'\n'
        selected_tab.insert(END,slected_text)
    else:
        selected_tab.insert(END,slected_text)

def submit_bn():
    global symptoms,selected_tab,slected_text
    print(symptoms)
    resultString = ','.join(symptoms)
    print(resultString)
    disease=module.predictDisease(resultString)
    try:
        d_name=disease.split('(')[0]
    except:
        d_name=disease.split(' ')[0]
    symptoms=[]
    slected_text=''
    threading.Thread(target=find_value,args=(disease,d_name)).start()
    selected_tab.delete("1.0",END)

def find_value(disease,d_name):
    txt=reply(d_name)
    result = messagebox.askyesno("Results","You may have:\n"+disease+'.\nDo you want to know what the AI Doc has to say?')
    if result:
        with open('result.txt','w') as file:
            file.write(txt)
        os.system('notepad result.txt')
    else:
        pass


# Runing


main_window()
