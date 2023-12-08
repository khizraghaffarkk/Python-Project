"""
Created on Fri Jul 17 11:23:57 2020
@author: Khizra Ghaffar
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
from tkinter import messagebox

# Natural Language Processing Packages
from nltk_summarization import nltk_summarizer
from spacy_summarization import text_summarizer

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen

# GUI for Text Summerization App
window = Tk()
window.title("Text Summerization App")
window.geometry("820x650")
window.config(background='black')
window.minsize(820,650)

# Create Menu through Notebook
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
# Add Tabs to Our Notebook
tab_control.add(tab1, text=f'{"Add Text":^35s}')
tab_control.add(tab2, text=f'{"File":^35s}')
tab_control.add(tab3, text=f'{"URL-Entry":^35s}')
tab_control.add(tab4, text=f'{"Information ":^35s}')

tab_control.pack(expand=1, fill='both')

############################################# (Start-Add Text-Functions) ###############################################################

# Get Summary Function
def get_summary():
	raw_text = str(entry.get('1.0',tk.END))
	final_text = text_summarizer(raw_text)
	print(final_text)
	result = '\nSummary:{}'.format(final_text)
	tab1_display.insert(tk.END,result)

# Clear Entry Text
def clear_text():
	entry.delete('1.0',END)

# Clear Result Text
def clear_display_result():
	tab1_display.delete('1.0',END)

############################################# (End-Add Text-Functions) ###############################################################

############################################# (Start-File-Functions) ###############################################################

# Open File Function
def openfiles():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file.insert(tk.END,read_text)

# Get Summary Function
def get_file_summary():
	raw_text = displayed_file.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	result = '\nSummary:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)

# Clear Entry Text
def clear_text_file():
	displayed_file.delete('1.0',END)

# Clear Result Text
def clear_text_result():
	tab2_display_text.delete('1.0',END)
    
############################################# (End-File-Functions) ###############################################################

############################################# (Start-URL-Functions) ###############################################################

# Get URL Text
def get_text():
	raw_text = str(url_entry.get())
	page = urlopen(raw_text)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	url_display.insert(tk.END,fetched_text)
    
# Get URL Summary
def get_url_summary():
	raw_text = url_display.get('1.0',tk.END)
	final_text = nltk_summarizer(raw_text)
	result = '\nSummary:{}'.format(final_text)
	tab3_display_text.insert(tk.END,result)	
    
# Clear URL Entry
def clear_url_entry():
	url_entry.delete(0,END)

# Clear Text Entry Which Get From URL
def clear_url_Entry_Text():
	url_display.delete('1.0',END)
    
# Clear Text Result Which Get from URL Text    
def clear_url_display():
	tab3_display_text.delete('1.0',END)
    
############################################# (End-URL-Functions) ###############################################################

# Exit Function
def Exit_window():
    ans=messagebox.askquestion("Exit","Do you really want to close this window?")
    if(ans=='yes'):
        window.destroy()

############################################# (Start-Add Text) ###############################################################

# Label Attached to Home Entry Text Tab
l1=Label(tab1,text="Enter Your Text In this Entry Box to Get Summary of Your Text:- ",font=('Arial',11))
l1.grid(row=1,column=0,padx=5,pady=15)

# Enter Text for Summarize(Home)
entry=ScrolledText(tab1,height=10)
entry.grid(row=2,column=0,columnspan=2,padx=80,pady=5)

# Buttons for Tab (Home)
button1=Button(tab1,text="Reset Text",command=clear_text, width=14,bg='#bd2b2b',fg='#fff',font='Arial 11 bold')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab1,text="Summarize",command=get_summary, width=14,bg='#2cb2be',fg='#fff',font='Arial 11 bold')
button2.grid(row=4,column=1,padx=145,pady=10)

button3=Button(tab1,text="Clear Result", command=clear_display_result,width=14,bg='#c546a6',fg='#fff',font='Arial 11 bold')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab1,text="Close", command=Exit_window, width=14,bg='#2b72a8',fg='#fff',font='Arial 11 bold')
button4.grid(row=5,column=1,padx=10,pady=10)

#Display Screen for Get Summerize Text (Home)
tab1_display = ScrolledText(tab1, height=10)
tab1_display.grid(row=7,column=0, columnspan=3,padx=80,pady=5)

############################################# (End-Add Text) ###############################################################

############################################# (Start-File) ###############################################################

# Label Attached to File Entry Text Tab
l1=Label(tab2,text="Open Your File Here To Summarize the Text:- ",font=('Arial',11))
l1.grid(row=1,column=0,padx=5,pady=15)


# Get File Text for Summarize (File)
displayed_file = ScrolledText(tab2,height=10)
displayed_file.grid(row=2,column=0, columnspan=3,padx=80,pady=5)

# # Buttons for Tab (File)
b0=Button(tab2,text="Open File", width=14,command=openfiles,bg='#29be73', fg='#fff',font='Arial 11 bold')
b0.grid(row=4,column=0,padx=10,pady=10)

b1=Button(tab2,text="Reset Text", width=14,command=clear_text_file,bg='#bd2b2b',fg='#fff',font='Arial 11 bold')
b1.grid(row=4,column=1,padx=10,pady=10)

b2=Button(tab2,text="Summarize", width=14,command=get_file_summary,bg='#2cb2be',fg='#fff',font='Arial 11 bold')
b2.grid(row=5,column=0,padx=10,pady=10)

b3=Button(tab2,text="Clear Result", width=14,command=clear_text_result,bg='#c546a6',fg='#fff',font='Arial 11 bold')
b3.grid(row=5,column=1,padx=10,pady=10)

b4=Button(tab2,text="Close", width=14,command=Exit_window,bg='#2b72a8',fg='#fff',font='Arial 11 bold')
b4.grid(row=6,column=2,padx=10,pady=10)

# Display Screen for Get Summerize Text (File)
tab2_display_text = ScrolledText(tab2,height=10)
tab2_display_text.grid(row=7,column=0, columnspan=3,padx=80,pady=5)



# Allows you to edit
tab2_display_text.config(state=NORMAL)

############################################# (End-File) ###############################################################

############################################# (Start-URL) ###############################################################
# Label Attached to URL Entry Text Tab
l1=Label(tab3,text="Enter Your URL Here for Summarize the Text:- ",font=('Arial',11))
l1.grid(row=1,column=0,padx=5,pady=20)

raw_entry=StringVar()
url_entry=Entry(tab3,textvariable=raw_entry,width=40,font=('Arial',12))
url_entry.grid(row=2,column=1)
# Buttons for Tab (URL)
button1=Button(tab3,text="Clear URL",command=clear_url_entry, width=14,bg='#f26d7d',fg='#fff',font='Arial 11 bold')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab3,text="Get Text",command=get_text, width=14,bg='#29be73', fg='#fff',font='Arial 11 bold')
button2.grid(row=4,column=1,padx=10,pady=10)

button4=Button(tab3,text="Reset Text",command=clear_url_Entry_Text, width=14,bg='#bd2b2b',fg='#fff',font='Arial 11 bold')
button4.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab3,text="Summarize",command=get_url_summary, width=14,bg='#2cb2be',fg='#fff',font='Arial 11 bold')
button4.grid(row=5,column=1,padx=10,pady=10)

button3=Button(tab3,text="Clear Result", command=clear_url_display,width=14,bg='#c546a6',fg='#fff',font='Arial 11 bold')
button3.grid(row=6,column=0,padx=10,pady=10)

button5=Button(tab3,text="Close", width=14,command=Exit_window,bg='#2b72a8',fg='#fff',font='Arial 11 bold')
button5.grid(row=6,column=1,padx=10,pady=10)

# Get URL Text for Summarize (URL)
url_display = ScrolledText(tab3,height=10)
url_display.grid(row=7,column=0, columnspan=3,padx=80,pady=5)

# Display Screen for Get Summerize Text (URL)
tab3_display_text = ScrolledText(tab3,height=10)
tab3_display_text.grid(row=10,column=0, columnspan=3,padx=80,pady=20)

############################################# (End-URL) ###############################################################

############################################# (Start-Information) #################################################################
# Final Tab (Information)
about_label = Label(tab4,text="This is Text Summerization App In NLP\nModules: NLTK & Spacy\nGUI: Tkinter",pady=5,padx=5)
about_label.grid(column=4,row=4,padx=10, pady=50)

button7=Button(tab4,text="Exit", width=14,command=Exit_window,bg='#2b72a8',fg='#fff',font='Arial 11 bold')
button7.grid(row=6,column=5,padx=10,pady=10)

############################################# (End-Information) ###############################################################
window.mainloop()
