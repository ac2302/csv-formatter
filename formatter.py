import tkinter
import tkinter.filedialog


def format(input_path='input.csv', output_path='output.csv'):
    sep_ = sep.get()
    with open(input_path, 'r') as f:
        data = f.read()
    with open(output_path, 'w') as f:
        f.write(data.replace(sep_, ','))


def convert():
    input_path = tkinter.filedialog.askopenfilename(filetypes=[('comma seperated veriables file', '.csv')])
    if input_path:
        output_path = tkinter.filedialog.asksaveasfilename(initialfile='output.csv', filetypes=[('comma seperated veriables file', '.csv')])
        if output_path:
            format(input_path, output_path)

root = tkinter.Tk()
root.title('csv formatter')

tkinter.Label(root, font='default 20', text='seperator ').grid(row=0, column=0)
sep = tkinter.Entry(root, font='default 20')
sep.insert(tkinter.END, ';')
sep.grid(row=0, column=1)

tkinter.Button(root, command=convert, font='default 20', bg='red', text='Convert').grid(row=1, column=0, columnspan=2)

root.mainloop()