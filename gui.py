import tkinter as tk
from tkinter import filedialog
from prediction import Prediction
 
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Visits Prediction")
 
        self.predictor = Prediction("client_data.db")
 
        self.load_button = tk.Button(self.root, text="Load CSV Data", command=self.load_data)
        self.load_button.pack()
 
        self.predict_button = tk.Button(self.root, text="Predict", command=self.run_prediction)
        self.predict_button.pack()
 
    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.predictor.run(file_path)
 
    def run_prediction(self):
        self.predictor.run("client_data.csv")
 
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()