import customtkinter as ctk
import tkinter as tk
#from PIL import Image
from time import strftime
import time as t
import CTkTable as ctkt
import threading
import pickle


def Home():
    global save_task
    global load_task
    global click
    global refresh
    global load_notes
    global num_pomo
    global master_data
    global username
    global timer_frame
    global home
    global username_label
    global tasks_frame
    global tasks
    global notes

    def save_task():
        title=task_entry.get()
        desc=task_desc.get("1.0",tk.END)
        tasks[title]=desc
        task_window.destroy()
        master_data[username]["tasks"]=tasks
        with open('data.db','wb') as fh:
            pickle.dump(master_data,fh)
        load_task()

    def add_task():
        global task_entry
        global task_desc
        global task_window

        task_window=ctk.CTkToplevel()
        task_window.title("TASK")
        task_window.geometry("410x410")
        task_window.resizable(False,False)

        task_window_frame=ctk.CTkFrame(task_window,fg_color=black,width=400,height=400)    
        task_window_frame.grid(row=0,column=0,padx=5,pady=4,sticky="NSEW")
        task_entry=ctk.CTkEntry(task_window_frame, font=('Avenir',16), width=310,fg_color=orange,placeholder_text="Title Of Task",placeholder_text_color=black)
        task_entry.place(anchor=tk.CENTER, relx=0.5, rely=0.1)
        task_desc=ctk.CTkTextbox(task_window_frame, font=('Avenir',18), width=310, height=250,fg_color=orange,border_color=grey, border_width=2)
        task_desc.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
        save_button=ctk.CTkButton(task_window_frame, text="Save Task",command=save_task,fg_color=lblue,text_color=black, font=('Avenir',16))
        save_button.place(anchor=tk.CENTER, relx=0.5, rely=0.9)
        refresh()
    
    def click(info):
        def edit_task():
            title=edit_task_entry.get()
            desc=edit_task_desc.get("1.0",tk.END)
            if btext==title:
                tasks[title]=desc
                master_data[username]["tasks"]=tasks
            else:
                del tasks[btext]
                tasks[title]=desc
                master_data[username]["tasks"]=tasks
                table.edit_row(info['row'], value=title)
            edit_task_window.destroy()
            with open('data.db','wb') as fh:
                pickle.dump(master_data,fh)

        def remove_task():
            del tasks[btext]
            master_data[username]["tasks"]=tasks
            if tasks=={}:
                tasks_frame2=ctk.CTkScrollableFrame(tasks_frame, width=570, height=250, corner_radius=15,fg_color=grey, scrollbar_button_color=grey, scrollbar_button_hover_color=grey)
                tasks_frame2.place(x=0,y=80)
            else:
                table.delete_row(info['row'])
            edit_task_window.destroy()
            with open('data.db','wb') as fh:
                pickle.dump(master_data,fh)

            
        btext = info["value"]
        edit_task_window=ctk.CTkToplevel()
        edit_task_window.title("TASK")
        edit_task_window.geometry("410x410")
        edit_task_window.resizable(False,False)

        edit_task_window_frame=ctk.CTkFrame(edit_task_window,fg_color=black,width=400,height=400)    
        edit_task_window_frame.grid(row=0,column=0,padx=5,pady=4,sticky="NSEW")
        edit_task_entry=ctk.CTkEntry(edit_task_window_frame, font=('Avenir',16), width=310,fg_color=orange,placeholder_text="Title Of Task",placeholder_text_color=black)
        edit_task_entry.place(anchor=tk.CENTER, relx=0.5, rely=0.1)
        edit_task_entry.insert(0, btext)
        edit_task_desc=ctk.CTkTextbox(edit_task_window_frame, font=('Avenir',18), width=310, height=250,fg_color=orange,border_color=grey, border_width=2)
        edit_task_desc.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
        if tasks[btext]!="":
            edit_task_desc.insert("1.0",tasks[btext])
        edit_button=ctk.CTkButton(edit_task_window_frame, text="Edit Task",command=edit_task,fg_color=lblue,text_color=black, font=('Avenir',16))
        edit_button.place(anchor=tk.CENTER, relx=0.2, rely=0.9)
        remove_button=ctk.CTkButton(edit_task_window_frame, text="Remove Task",command=remove_task,fg_color=lblue,text_color=black, font=('Avenir',16))
        remove_button.place(anchor=tk.CENTER, relx=0.8, rely=0.9)

    def load_task():
        global table
        tasks_frame2=ctk.CTkScrollableFrame(tasks_frame, width=570, height=250, corner_radius=15,fg_color=grey, scrollbar_button_color=grey, scrollbar_button_hover_color=grey)
        tasks_frame2.place(x=0,y=80)
        value=[]
        for i in tasks:
            value.append([i])
        table = ctkt.CTkTable(master=tasks_frame2, values=value, corner_radius=0,command=click,width=520,text_color=black,colors=[lgrey,white],border_width=5,border_color=grey,height=30,font=('Avenir',18))
        table.pack(expand=True, fill="both", padx=20, pady=15)
        

    def save_notes():
        global notes
        text_in_notepad=notepad.get("1.0",tk.END)
        notes=text_in_notepad
        master_data[username]["notes"]=notes
        with open('data.db','wb') as fh:
            pickle.dump(master_data,fh)

    def load_notes():
        global notes
        notepad.insert("1.0",notes)




    username=username_entry.get()
    window.destroy()
    if username in master_data:
        tasks=master_data[username]["tasks"]
        notes=master_data[username]["notes"]
        is_new_user=False
    else:
        is_new_user=True
        tasks={}
        notes=""
        master_data[username]={"tasks":tasks,"notes":notes}
        with open('data.db','wb') as fh:
            pickle.dump(master_data,fh)

    home=ctk.CTk()
    home.title("POMODORO")
    width,height=1220,770
    v_dim=str(width)+'x'+str(height)
    home.geometry(v_dim)
    home.minsize(1220,770)
    home.maxsize(1220,770)
    #refresh()

    mainframe=ctk.CTkFrame(master=home, width=1220, height=770, fg_color=grey)
    mainframe.place(x=0,y=0)

    timer_frame=ctk.CTkFrame(master=mainframe, width=600, height=760, corner_radius=15, fg_color=grey)
    timer_frame.grid(row=0,column=0,padx=5,pady=4,sticky="NSEW")

    tasks_frame=ctk.CTkFrame(master=mainframe, width=600, height=760, corner_radius=15, fg_color=grey)
    tasks_frame.grid(row=0,column=1,padx=5,pady=4,sticky="NSEW") 

    title_label=ctk.CTkLabel(tasks_frame, font=('Avenir',30,"bold"), text="Tasks", text_color=white)
    title_label.place(anchor=tk.CENTER, relx=0.14, rely=0.05)  

    desg=ctk.CTkFrame(tasks_frame,width=500,height=2,fg_color=white)
    desg.place(anchor=tk.CENTER, relx=0.5, rely=0.1)  

    add_button=ctk.CTkButton(tasks_frame, text="+", command=add_task, text_color=white,font=('Avenir',40,"bold"), cursor="hand2", corner_radius=5, width=30,height=30,border_width=0,fg_color="transparent",hover="disable")
    add_button.place(anchor=tk.CENTER, relx=0.88, rely=0.05)

    ntitle_label=ctk.CTkLabel(tasks_frame, font=('Avenir',30,"bold"), text="Notepad", text_color=white)
    ntitle_label.place(anchor=tk.CENTER, relx=0.14, rely=0.5)  

    ndesg=ctk.CTkFrame(tasks_frame,width=500,height=2,fg_color=white)
    ndesg.place(anchor=tk.CENTER, relx=0.5, rely=0.55)

    notepad=ctk.CTkTextbox(tasks_frame, font=('Avenir',18), width=500, height=250,fg_color=grey,border_color=white, border_width=2)
    notepad.place(anchor=tk.CENTER, relx=0.5, rely=0.75)

    add_nbutton=ctk.CTkButton(tasks_frame, text="+", command=save_notes, text_color=white,font=('Avenir',40,"bold"), cursor="hand2", corner_radius=5, width=30,height=30,border_width=0,fg_color="transparent",hover="disable")
    add_nbutton.place(anchor=tk.CENTER, relx=0.88, rely=0.5)


    #Timer frame
    username_label=ctk.CTkLabel(timer_frame, font=('Avenir',30,"bold"), text="", text_color=white)
    username_label.place(anchor=tk.CENTER, relx=0.22, rely=0.09)
    refresh()

    def time():
        string = strftime('%H:%M %p \n %d %B')
        time_label.config(text=string)
        time_label.after(1000, time)
        refresh()

    time_label=tk.Label(timer_frame, font=('Avenir',30,"bold"),text="",bg=grey,foreground=white)
    time_label.place(anchor=tk.CENTER, relx=0.8, rely=0.09)

    tdesg=ctk.CTkFrame(timer_frame,width=500,height=2,fg_color=white)
    tdesg.place(anchor=tk.CENTER, relx=0.5, rely=0.17)  
    time()

    def start_timer():
        global is_running, is_paused, timer_thread,pause_button
        pause_button = ctk.CTkButton(countdown_frame, text="Pause", font=('Avenir', 30),text_color=black, command=pause_timer,bg_color=black,fg_color=white,width=150,height=70, hover=False)
        pause_button.place(anchor=tk.CENTER,relx=0.5,rely=0.85)
        
        if not is_running:
            is_running = True
            start_button.configure(state=tk.DISABLED)
            pause_button.configure(state=tk.NORMAL)
            next_button.configure(state=tk.NORMAL)
            timer_thread = threading.Thread(target=timer)
            timer_thread.start()

    def pause_timer():
        global is_paused, timer_thread
        next_button.configure(state="disabled")
        if is_running:
            if not is_paused:
                is_paused = True
                pause_button.configure(text="Resume")
            else:
                is_paused = False
                pause_button.configure(text="Pause")
                resume_timer()

    def resume_timer():
        global timer_thread
        next_button.configure(state="normal")
        if timer_thread and not timer_thread.is_alive():
            timer_thread = threading.Thread(target=timer)
            timer_thread.start()

    def reset_timer():
        start_button = ctk.CTkButton(countdown_frame, text="Start", font=('Avenir', 30),text_color=black, command=start_timer,bg_color=black,fg_color=white,width=150,height=70, hover=False)
        start_button.place(anchor=tk.CENTER,relx=0.5,rely=0.85)
        global is_running, is_paused, remaining_time, timer_thread
        is_running = False
        if is_paused:
            if is_pomo:
                remaining_time = 1501
            elif is_short:
                remaining_time=301
            else:
                remaining_time=901
        else:
            if is_pomo:
                remaining_time = 1500
            elif is_short:
                remaining_time=300
            else:
                remaining_time=900
        is_paused = False
        label.config(text=format_time(remaining_time))
        start_button.configure(state=tk.NORMAL)
        next_button.configure(state=tk.DISABLED)

    def timer():
        global remaining_time, num_pomo
        while remaining_time > 0 and is_running:
            if not is_paused:
                remaining_time -= 1
                label.config(text=format_time(remaining_time))
                t.sleep(1)
        if remaining_time == 0:
            skip()

    def format_time(seconds):
        m, s = divmod(seconds, 60)
        return "{:02}:{:02}".format(m, s)
    
    def skip():
        global num_pomo
        if is_pomo and (num_pomo)%4!=0:
            short_break()
        elif is_pomo and (num_pomo)%4==0:
            long_break()
        elif is_short:
            pomodoro()
            num_pomo+=1
            pomo_label.configure(text="#"+str(num_pomo))
        elif is_long:
            pomodoro()
            num_pomo+=1
            pomo_label.configure(text="#"+str(num_pomo))
        

    countdown_frame=ctk.CTkFrame(master=timer_frame, width=550, height=400, corner_radius=15, fg_color=black)
    countdown_frame.place(anchor=tk.CENTER, relx=0.5, rely=0.48)

    label = tk.Label(countdown_frame, text=format_time(remaining_time), font=('Avenir', 150),background=black,foreground=white)
    label.place(anchor=tk.CENTER,relx=0.5,rely=0.5)

    start_button = ctk.CTkButton(countdown_frame, text="Start", font=('Avenir', 30),text_color=black, command=start_timer,bg_color=black,fg_color=white,width=150,height=70, hover=False)
    start_button.place(anchor=tk.CENTER,relx=0.5,rely=0.85)

    next_button = ctk.CTkButton(countdown_frame, text=">", font=('Avenir', 30),text_color=white, command=skip,bg_color=black,fg_color=black,width=50,height=70, hover=False,text_color_disabled=black)
    next_button.place(anchor=tk.CENTER,relx=0.85,rely=0.85)
    next_button.configure(state="disabled")

    def short_break():
        global remaining_time, is_pomo, is_short, is_long
        is_pomo=False
        is_short=True
        is_long=False
        remaining_time=300
        pomodoro_button.configure(fg_color="transparent")
        short_break_button.configure(fg_color="black")
        long_break_button.configure(fg_color="transparent")
        reset_timer()

    def long_break():
        global remaining_time, is_pomo, is_short, is_long
        is_pomo=False
        is_short=False
        is_long=True
        remaining_time=900
        pomodoro_button.configure(fg_color="transparent")
        short_break_button.configure(fg_color="transparent")
        long_break_button.configure(fg_color="black")
        reset_timer()

    def pomodoro():
        global remaining_time, is_pomo, is_short, is_long
        is_pomo=True
        is_short=False
        is_long=False
        remaining_time=1500
        pomodoro_button.configure(fg_color="black")
        short_break_button.configure(fg_color="transparent")
        long_break_button.configure(fg_color="transparent")
        reset_timer()

    pomodoro_button=ctk.CTkButton(countdown_frame, text="Pomodoro", font=('Avenir', 25),text_color=white, command=pomodoro,bg_color="transparent",fg_color="transparent",width=100, hover=False)
    pomodoro_button.place(anchor=tk.CENTER, relx=0.2, rely=0.18)
    pomodoro_button.configure(fg_color="black")

    short_break_button=ctk.CTkButton(countdown_frame, text="Short Break", font=('Avenir', 25),text_color=white, command=short_break,bg_color="transparent",fg_color="transparent",width=100, hover=False)
    short_break_button.place(anchor=tk.CENTER, relx=0.5, rely=0.18)

    long_break_button=ctk.CTkButton(countdown_frame, text="Long Break", font=('Avenir', 25),text_color=white, command=long_break,bg_color="transparent",fg_color="transparent",width=100, hover=False)
    long_break_button.place(anchor=tk.CENTER, relx=0.8, rely=0.18)

    pomo_label=ctk.CTkLabel(timer_frame, text="#"+str(num_pomo), font=('Avenir', 25),text_color=white)
    pomo_label.place(anchor=tk.CENTER, relx=0.5, rely=0.8)

    focus_label=ctk.CTkLabel(timer_frame, text="Time to Focus!", font=('Avenir', 25),text_color=white)
    focus_label.place(anchor=tk.CENTER, relx=0.5, rely=0.85)

    if tasks!={}:
        load_task()
    if notes!="":
        load_notes()
    home.resizable(False,False)
    home.mainloop()

def refresh():
    global home,username_label
    cur=t.localtime()
    if cur.tm_hour<12 and cur.tm_hour>=0:
        username_label.configure(text="Good Morning"+",\n"+username)
    elif cur.tm_hour>=12 and cur.tm_hour<18:
        username_label.configure(text="Good Afternoon"+",\n"+username)
    elif cur.tm_hour>=18:
        username_label.configure(text="Good Evening"+",\n"+username)

with open('data.db',"rb") as fh:
    master_data=pickle.load(fh)

window=ctk.CTk()
window.title("POMODORO")
window.geometry('900x600')

orange="#DC5F00"
black="#373A40"
grey="#686D76"
white="#EEEEEE"
lblue="#8AAAE5"
lgrey="#CACFD2"

fr=ctk.CTkFrame(master=window, width=900, height=600, fg_color=grey)
fr.place(x=0,y=0)

frame=ctk.CTkFrame(master=fr, width=320, height=250, corner_radius=15, fg_color=black)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label=ctk.CTkLabel(master=frame, text="POMODORO", font=('Avenir', 30), text_color=lblue, corner_radius=1000)
label.place(x=60, y=45)

username_entry=ctk.CTkEntry(master=frame, placeholder_text="Username", width=220, fg_color=grey,placeholder_text_color=lblue)
username_entry.place(x=50, y=120)

entry_button=ctk.CTkButton(master=frame, width=90, text="Enter",corner_radius=10, cursor='hand2', command=Home, font=('Avenir',15), text_color=black,fg_color=lblue)
entry_button.place(x=120, y=200)

is_running = False
is_paused = False
timer_thread = None
num_pomo=1
is_pomo=True
is_short=False
is_long=False
is_new_user=None

if is_pomo:
    remaining_time = 1500
elif is_short:
    remaining_time=300
else:
    remaining_time=900

window.resizable(False,False)
window.mainloop()

