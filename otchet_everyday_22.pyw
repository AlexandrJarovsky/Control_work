import time
import glob
import os
from tkinter import *
from tkinter.scrolledtext import ScrolledText  # or PP4E.Gui.Tour.scrolledtext
from tkinter import ttk
from datetime import datetime, timedelta
#import threading


def buckup_data(dir, dat=[]):
    start = time.perf_counter()
#    global text3
    count = 1

    dat1 = str(datetime.now()).split()[0].split('-')
    y = dat1[0]
    if not dat:
        d = dat1[2]
        m = dat1[1]
    else:
        d = dat[0]
        m = dat[1]

 #   print(d, m, y, glob.glob(dir + '\\' + '*' + d + m + y + '*'))

    text3.delete(1.0, END)

    lbl = Label(text3, text=str(time.asctime()))
    lbl.grid(row=0, column=0, padx=5, pady=5)

    text3.window_create(END, window=lbl)  # embed a photo
    text3.insert(END, '\n')
    text3.tag_add('centr', "1.0", "2.0")  # tag 'is'
    text3.tag_config('centr', justify='center')  # change colors in tag

    if glob.glob(dir + '\\' + '*' + d + m + y + '*'):

        texts = open(glob.glob(dir + '\\' + '*' + d + m + y + '*')[0], 'r').readlines()

        for line in texts:
#            if line != '\n':
            if 'non' in line:
                text3.insert(END, line)  # insert six lines
                text3.tag_add('demo', str(count + 1) + ".0", str(count + 1) + "." + str(len(line)))  # tag 'is'
                text3.tag_config('demo', background='purple')  # change colors in tag
                text3.tag_config('demo', foreground='white')  # not called bg/fg here
                count += 1
            elif len(line) < 25 and 'Кол' not in line:
                text3.insert(END, line)  # insert six lines
                text3.tag_add('demo1', str(count + 1) + ".0", str(count + 1) + "." + str(len(line)))  # tag 'is'
                text3.tag_config('demo1', background='blue')  # change colors in tag
                text3.tag_config('demo1', foreground='white')  # not called bg/fg here
                count += 1
            else:
                text3.insert(END, line)  # insert six lines
                count += 1

    else:
        text3.insert(END, 'Не найден файл.\n')  # insert six lines

    text3.pack(side=LEFT, expand=YES, fill=X)
    #  text3.grid(row=0, column=0)
    text3.insert(END, str(time.perf_counter() - start))


def report_asutp(dir, dat=[]):
    start = time.perf_counter()
#    global text

    dat1 = str(datetime.now()).split()[0].split('-')
    y = dat1[0]
    if not dat:
        d = dat1[2]
        m = dat1[1]
    else:
        d = dat[0]
        m = dat[1]

    count1 = 1

    text.delete(1.0, END)

    lbl = Label(text, text=str(time.asctime()))
    lbl.grid(row=0, column=0, padx=5, pady=5)

    text.window_create(END, window=lbl)  # embed a photo
    text.insert(END, '\n')

    lbl = Label(text, text='Выделен путь, в котором отсутствует отчет')
    lbl.grid(row=1, column=0, padx=5, pady=5)

    text.window_create(END, window=lbl)  # embed a photo
    text.insert(END, '\n')
    text.tag_add('centr', "1.0", "3.0")  # tag 'is'
    text.tag_config('centr', justify='center')  # change colors in tag

    if glob.glob(dir + '\\' + '*' + d + m + y + '*'):

        texts = open(glob.glob(dir + '\\' + '*' + d + m + y + '*')[0], 'r').readlines()
#        texts = open(glob.glob(dir + '\\' + '*' + d + m + y + '*')[0], 'r').readlines()

        for line in texts:
            if line != '\n':

                if 'non' in line or 'empty' in line:
                    text.insert(END, line)  # insert six lines
                    text.tag_add('demo', str(count1 + 2) + ".0", str(count1 + 2) + "." + str(len(line)))  # tag 'is'
                    text.tag_config('demo', background='purple', foreground='white')  # change colors in tag
                    count1 += 1
                elif ('c:' not in line and 'e:' not in line):
#                elif (':' not in line) and ('-' not in line):
                    text.insert(END, '\n')  # insert six lines
                    text.insert(END, line)  # insert six lines
                    text.tag_add('demo1', str(count1 + 3) + ".0", str(count1 + 3) + "." + str(len(line)))  # tag 'is'
                    text.tag_config('demo1', background='blue', foreground='white')  # change colors in tag
                    count1 += 2
                else:
                    if ('kupm' in line):
                        text.insert(END, line)  # insert six lines
#                        text.insert(END, line[38:len(line)-2] + '\n')  # insert six lines
                    elif ('gobkk' in line):
                        text.insert(END, line)  # insert six lines
#                        text.insert(END, line[39:len(line)-1] + '\n')  # insert six lines
                    else:
#                        text.insert(END, line)  # insert six lines
                        text.insert(END, line[35:len(line)-2] + '\n')  # insert six lines
                    count1 += 1

    else:
        text.insert(END, 'Не найден файл.\n')  # insert six lines

#    print(count1)

    #  text.grid(row=0, column=0)
    text.pack(side=LEFT, expand=YES, fill=X)
    text.insert(END, str(time.perf_counter() - start))


def restart_mb(dir):
    #  global root3
    start = time.perf_counter()
    count2 = 1

    text1.delete(1.0, END)

    lbl = Label(text1, text=str(time.asctime()))
    lbl.grid(row=0, column=0, padx=5, pady=5)

    text1.window_create(END, window=lbl)  # embed a photo
    text1.insert(END, '\n')
    text1.tag_add('centr', "1.0", "2.0")  # tag 'is'
    text1.tag_config('centr', justify='center')  # change colors in tag

    if os.path.exists(dir):
        texts = open(dir, 'r').readlines()

        for line in texts:
            if line != '\n':
                text1.insert(END, line)  # insert six lines
                if 'file:' in line or 'WinError' in line:
                    text1.tag_add('demo', str(count2) + ".0", str(count2 + 1) + "." + str(len(line)))  # tag 'is'
                    text1.tag_config('demo', background='purple')  # change colors in tag
                    text1.tag_config('demo', foreground='white')  # not called bg/fg here
                    lbl.config(bg="red")
#                count2 += 1
                elif '(' in line:
#                    text1.insert(END, line)  # insert six lines
                    text1.tag_add('demo1', str(count2 + 1) + ".0", str(count2 + 1) + "." + str(len(line)))  # tag 'is'
                    text1.tag_config('demo1', background='blue')  # change colors in tag
                    text1.tag_config('demo1', foreground='white')  # not called bg/fg here
                count2 += 1

    else:
        text1.insert(END, 'Не найден файл.\n')  # insert six lines

    #  text1.grid(row=0, column=0, sticky=W+E+S+N)
    # lbl.config(bg="red")
    def leftclick(event):
        lbl.config(bg="white")
    lbl.bind('<Button-1>', leftclick)
    text1.pack(side=RIGHT, expand=NO, fill=X)
    text1.insert(END, str(time.perf_counter() - start))


def archiv_mb_table1(dir):
    start = time.perf_counter()
    #  global root4

#    dat = str(datetime.now()).split()[0].split('-')
    count2 = 1

    text2 = ScrolledText(f_bot, height=19)
    text2.config(font=('courier', 11, 'normal'), bg='green', fg='white')  # set font for all

    lbl = Label(text2, text=str(time.asctime()))
    lbl.grid(row=0, column=0, padx=5, pady=5)

    text2.window_create(END, window=lbl)  # embed a photo
    text2.insert(END, '\n')
    text2.tag_add('centr', "1.0", "2.0")  # tag 'is'
    text2.tag_config('centr', justify='center')  # change colors in tag

    if os.path.exists(dir):
        texts = open(dir, 'r').readlines()

        for line in texts:
            if line != '\n':

                if ':' not in line:
                    if '=' not in line:
                        text2.insert(END, '\n')  # insert six lines
                        text2.insert(END, line)  # insert six lines
                        text2.tag_add('demo1', str(count2 + 2) + ".0",
                                      str(count2 + 2) + "." + str(len(line)))  # tag 'is'
                        text2.tag_config('demo1', background='blue', foreground='white')  # change colors in tag
                        count2 += 1
                    else:
                        text2.insert(END, line)  # insert six lines
                else:
                    text2.insert(END, line)  # insert six lines

                if 'архив отсутствует' in line:
                    text2.tag_add('demo', str(count2 + 1) + ".0", str(count2 + 1) + "." + str(len(line)))  # tag 'is'
                    text2.tag_config('demo', background='purple', foreground='white')  # change colors in tag

                count2 += 1

    else:
        text2.insert(END, 'Не найден файл.\n')  # insert six lines

    #  text2.grid(row=0, column=0)
    text2.pack(side=LEFT, expand=YES, fill=X)
    text2.insert(END, str(time.perf_counter() - start))


def vost_archiv(dir):
    start = time.perf_counter()
    #  global root6

#    dat = str(datetime.now()).split()[0].split('-')
    count2 = 1

#    text5 = ScrolledText(root6, height=15, width=80)
    lbl = Label(text5, text=str(time.asctime()))
    lbl.grid(row=0, column=0, padx=5, pady=5)

    text5.window_create(END, window=lbl)  # embed a photo
    text5.insert(END, '\n')
    text5.tag_add('centr', "1.0", "2.0")  # tag 'is'
    text5.tag_config('centr', justify='center')  # change colors in tag

    if os.path.exists(dir):
        texts = open(dir, 'r').readlines()

        for line in texts:

            #      if 'sozdan' in line or 'Python' in line or 'net' in line:
#            if 'sozdan' in line:
            if 'sozdan' in line or '\\' in line:
                text5.insert(END, line)  # insert six lines
                text5.tag_add('demo1', str(count2 + 1) + ".0", str(count2 + 1) + "." + str(len(line)))  # tag 'is'
                text5.tag_config('demo1', background='purple', foreground='white')  # change colors in tag
                count2 += 1
            else:
                #        text5.insert(END, line)   # insert six lines
                if (':' not in line) and ('=' not in line) and (line != ''):
                    text5.insert(END, line)  # insert six lines
                    text5.tag_add('demo', str(count2 + 1) + ".0", str(count2 + 1) + "." + str(len(line)))  # tag 'is'
                    text5.tag_config('demo', background='blue', foreground='white')  # change colors in tag
                    count2 += 1
                else:
                    text5.insert(END, line)  # insert six lines
                    count2 += 1

    #      count2+=1
    else:
        text5.insert(END, 'Не найден файл.\n')  # insert six lines
    #    open(os.curdir+'\\report_error.txt' , 'a' ).write( 'Не найден файл конфигурации: ' + datetime.today().strftime("%d.%m.%Y %H:%M:%S") + '\n' )

    #  text5.grid(row=0, column=0)
    text5.pack(side=LEFT, expand=YES, fill=X)
    text5.insert(END, str(time.perf_counter() - start))


if __name__ == '__main__':

    try:

        def tick_opros():
            # lbl_chenge_hour.after(60000, tick_opros)
            but.after(60000, tick_opros)
            if datetime.now().minute == 5:
                restart_mb(r'\\10.100.120.99\d$\MB_TEP\python\python_on_22\\error_serv\otchet_serv_error.txt')

        os.popen(r'cmd /c net use \\10.100.120.99\d$ google3519google /user:administrator')

        dat = str(datetime.now()).split()[0].split('-')
        d = dat[2]
        m = dat[1]
        y = dat[0]

        root = Tk()
#        root.geometry('900x600+50+50')
        root.geometry('+50+0')

        f_top = LabelFrame(root, height=100, bg='green', fg='white', text="Бэкапы баз и Отчеты перезапуска ТЭП и МБ")
        f_top.config(relief=RAISED, borderwidth=1, font=('courier', 12, 'normal'))

        f_bot = LabelFrame(root, height=30, bg='green', fg='white',
                           text="Отчеты на сервере АСУТП и Отчет формирования архивов таблиц ТЭП и МБ")
        f_bot.config(relief=RAISED, borderwidth=1, font=('courier', 12, 'normal'))

        root6 = LabelFrame(root, height=15, bg='green', fg='white',
                           text="Отчет восстановленных архивов таблиц ТЭП и МБ")
        root6.config(relief=RAISED, borderwidth=1, font=('courier', 12, 'normal'))

        f_top.pack(expand=YES, fill=BOTH)
        f_bot.pack(expand=YES, fill=BOTH)
#        root6.pack(expand=YES, fill=BOTH)

        root5 = Frame(root)
        root5.pack(side=BOTTOM, expand=YES, fill=BOTH)

        root.title('Суточные отчеты')

        text3 = ScrolledText(f_top, height=30, width=90)
        text3.config(font=('courier', 11, 'normal'), bg='green', fg='white')  # set font for all

        text = ScrolledText(f_bot, height=30, width=90)
        text.config(font=('courier', 11, 'normal'), bg='green', fg='white')  # set font for all

        text1 = ScrolledText(f_top, height=30, width=90)
        text1.config(font=('courier', 11, 'normal'), bg='green', fg='white')  # set font for all

        text5 = ScrolledText(f_bot, height=30, width=90)
        text5.config(font=('courier', 11, 'normal'), bg='green', fg='white')  # set font for all

        start = time.perf_counter()
        buckup_data(r'\\10.100.120.99\d$\MB_TEP\python\python_on_22\\Arch_databeses\Backup_tepmb')
        report_asutp(r'\\10.100.120.99\d$\MB_TEP\python\python_on_22\\Arch_databeses\Otchet_tepmb')
        restart_mb(r'\\10.100.120.99\d$\MB_TEP\python\python_on_22\\error_serv\otchet_serv_error.txt')
#        archiv_mb_table1(r'\\10.100.120.22\c$\Python34\My\Arch_tabl\otchet_table_arch.txt')
        vost_archiv(r'\\10.100.120.99\d$\MB_TEP\python\python_on_22\\Vost_arch\otchet_vost_arch.txt')

        # t1=threading.Thread(target=buckup_data, args=(r'\\10.100.120.22\c$\Python34\My\Arch_databeses\Backup_tepmb',))
        # t1.start()
        # t2=threading.Thread(target=report_asutp, args=(r'\\10.100.120.22\c$\Python34\My\Arch_databeses\Otchet_tepmb',))
        # t2.start()
        # t3=threading.Thread(target=restart_mb, args=(r'\\10.100.120.22\c$\Python34\My\error_serv\otchet_serv_error.txt',))
        # t3.start()
        # t4=threading.Thread(target=archiv_mb_table1, args=(r'\\10.100.120.22\c$\Python34\My\Arch_tabl\otchet_table_arch.txt',))
        # t4.start()
        # t5=threading.Thread(target=vost_archiv, args=(r'\\10.100.120.22\c$\Python34\My\Vost_arch\otchet_vost_arch.txt',))
        # t5.start()

        but = Button(root5, text="Update backup", width=13, height=1, bg="white", fg="black",
                     command=lambda: buckup_data(r'\\10.100.120.99\d$\MB_TEP\python\python_on_22\\Arch_databeses\Backup_tepmb',
                                                 [listbox1.get(), listbox2.get()]))
        but.pack(side=LEFT, padx=5)

        list1 = []
        for i in range(1, 32):
            list1.append(str(i))
        listbox1 = ttk.Combobox(root5, height=1, width=15, values=list1)

        list1 = []
        for i in range(1, 13):
            if i in range(1, 10):
                list1.append('0' + str(i))
            else:
                list1.append(str(i))
        listbox2 = ttk.Combobox(root5, height=1, width=15, values=list1)

        listbox1.set(d)
        listbox2.set(m)
        listbox1.pack(side=LEFT, padx=5)
        listbox2.pack(side=LEFT, padx=5)

        but = Button(root5, text="Update otchet", width=13, height=1, bg="white", fg="black",
                     command=lambda: report_asutp(r'\\10.100.120.99\d$\MB_TEP\python\python_on_22\\Arch_databeses\Otchet_tepmb',
                                                  [listbox1.get(), listbox2.get()]))
        but.pack(side=LEFT, padx=5)

        but = Button(root5, text="Update restart", width=13, height=1, bg="white", fg="black",
                     command=lambda: restart_mb(r'\\10.100.120.99\d$\MB_TEP\python\python_on_22\\error_serv\otchet_serv_error.txt'))
        but.pack(side=RIGHT, padx=5)
        but.after_idle(tick_opros)

        menubar = Menu(root)
        root.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu1 = Menu(fileMenu)

        fileMenu.add_command(label="Exit", command=root.destroy)

#        fileMenu1.add_command(label="otchet2_off", command=lambda: root4.grid_remove())
#        fileMenu1.add_command(label="otchet2_on", command=lambda: root4.grid())

        menubar.add_cascade(label="File", menu=fileMenu)

#        fileMenu.add_cascade(label="otchet2", menu=fileMenu1)

#        print(root.grid_size())
        lbl = Label(root5, text=str(time.perf_counter() - start))
        lbl.pack(side=LEFT, padx=5)

        # lbl_chenge_hour = Label()
        # lbl_chenge_hour.pack()
        # lbl_chenge_hour.after_idle(tick_opros)

        root.mainloop()

    except Exception as Er:
        open(os.curdir + '\\report_error.txt', 'a').write(
            'Ошибка: ' + str(Er) + ': ' + datetime.today().strftime("%d.%m.%Y %H:%M:%S") + '\n')
