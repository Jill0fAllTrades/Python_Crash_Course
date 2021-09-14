def print_models(unprinted_designs, completed_models):
    """Simulates printing designs on t-shirts."""
    while unprinted_designs:
        current_design = unprinted_designs.pop() #removes last item from list
        #stores that last item in current_design
    
        #simulate creating a 3d print from the design.
        print("Printing model:" + current_design) #prints current_design
        completed_models.append(current_design)
        #last line adds current_design to completed_models
        

def show_completed_models(completed_models): #this prints what was added to completed_models
    """show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)