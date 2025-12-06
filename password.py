from customtkinter import *
from random import *

def show_diff_pass(value):
    global diff_password
    diff_password = int(value)
    count_password_label.configure(text=f'{int(value)}')

def generate_password():
    global diff_password 
    chars = [char for char in 'qwertyuiopasdfghjklzxcvbnm']
    spec_chars_ = [char for char in '!@#$%^&*()_+']
    available_value = []
    result = ''
    
    if small_chars.get():
        available_value += chars
    if large_chars.get():
        available_value += [char.upper() for char in chars]
    if spec_chars.get():
        available_value += spec_chars_
    if number_chars.get():
        available_value += [str(i) for i in range(0,10)]

    for i in range(diff_password):
        result += choice(available_value)

    password_entry.delete(0,'end')
    password_entry.insert(0,result)
    

diff_password = 34
app = CTk()
app.geometry('400x300')
app.title('Генератор пароля')
app.maxsize(400,300)
#
password_entry = CTkEntry(app, width = 220)
btn_generate = CTkButton(app,text='Генерація', 
                         command=generate_password
                         )

password_entry.grid(row=0,column=0,padx=10,pady=10)
btn_generate.grid(row=0, column = 1, padx = 10)
#setting_left
settings_left = CTkFrame(app, width = 200)
settings_left.grid(row=1,column=0)

small_chars = CTkCheckBox(settings_left,
                          text='Малі літери',
                          width = 220)
large_chars = CTkCheckBox(settings_left,
                          text='Великі літери',
                          width = 220)
spec_chars = CTkCheckBox(settings_left,
                          text='Спеціальні символи',
                          width = 220)
number_chars = CTkCheckBox(settings_left,
                          text='Числа',
                          width = 220)

small_chars.pack(pady=5)
large_chars.pack(pady=5)
spec_chars.pack(pady=5)
number_chars.pack(pady=5)

#setting_right
settings_right = CTkFrame(app)
settings_right.grid(row=1,column=1)

count_password_slider = CTkSlider(settings_right,
                           from_=4, to=64,
                           orientation='vertical',
                           command=show_diff_pass
                           )
count_password_label = CTkLabel(settings_right,text='34',width=80)

count_password_slider.pack(side='right')
count_password_label.pack(side='left')

app.mainloop()