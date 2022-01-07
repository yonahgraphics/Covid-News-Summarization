from imports import* 
import pickle

#Saving the model
with open('model_pickle','wb') as file:
    pickle.dump(model,file)

#Loading the model
with open('model_pickle','rb') as file:
    mp = pickle.load(file)