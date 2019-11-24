# Debug Exercise 13
import tkinter


class CelsiusGUI:

    def __init__(self):

        # Create the main window
        self.main_window = tkinter.Tk()

       # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        # Create the widgets for the top frame
        self.celsius_prompt = tkinter.Label(self.top_frame, text='Enter the Celsius temperature:')
        self.celsius_entry = tkinter.Entry(self.top_frame, width=10)
        
        # Pack the top frame widgets
        self.celsius_prompt.pack(side='left')
        self.celsius_entry.pack(side='left')

        # Create the widgets for the middle frame
        self.results_label = tkinter.Label(self.mid_frame, text='Fahrenheit temperature: ')

        # Create a blank label
        self.value = tkinter.StringVar()
        self.fahrenheit_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        #Pack the middle frame widgets
        self.results_label.pack(side='left')
        self.fahrenheit_label.pack(side='left')

        # create two buttons in the bottom frame
        self.fahrenheit_button = tkinter.Button(self.bottom_frame, text='Convert to Fahrenheit', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack the widgets into the bottom
        self.fahrenheit_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frame
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the show_info function
    def convert(self):
        # Get the values entered
        celsius = float(self.celsius_entry.get())

        # Calulate fahrenheit
        fahrenheit = 9.0 / 5.0 * float(celsius) + 32

        # Updae the fahrenheit_label
        self.value.set(fahrenheit)

# Create an instance of CelciusGUI
if __name__ == '__main__':
    CelsiusGUI()