import pickle

with open("student_data.pkl","rb") as file:
    Data = pickle.load(file)
print(Data[0].display())
print(Data[1].display())
print(Data[2].display())
