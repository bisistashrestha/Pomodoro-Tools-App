master_data={"Bisista Shrestha":
             {"tasks":{"Morning Run":"","Walking the Dog":"","Cleaing the Closet":"","Gym":"","Cooking Dinner":"","Sleeping":""},
              "notes":"Mitochondria is the powerhouse of the cell."}}
import pickle
#with open('data.db','wb') as fh:
    #pickle.dump(master_data,fh)
    
with open('data.db','rb') as fh:
    print(pickle.load(fh))
