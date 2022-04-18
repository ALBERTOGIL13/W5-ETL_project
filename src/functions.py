def jaleito(row):
    if row['State_Name'] in top_states:
        
        val = True
    else:
        val = False
        
    return val



def racano(row):
    if row['State_Name'] in states_free:
        
        val = True
    else:
        val = False
        
    return val