def code():
    '''
    Implements an initial table for LZW algorithm
    '''
    table = {}                                                              # Creates and emty dictionary 
    table[1] = 't'                                                          # Adds elements to the dictionary
    table[2] = 'e'                                                          # The table is intialized with these numbers
    table[3] = 's'
    table[4] = 't '
    return table

def encode(message):                                                        # Encoder function utilizes the dictionary above to encode the message
    table = code()
    string = ""
    code_for_string = []
    for byte in message:
        symbol = byte
        if (string + symbol) in table.values():                             
            string = string + symbol                                        
        else:
            for k,v in table.iteritems():                                   # The code finds the symbols that is not contained in the list
                if v == string:
                    code_for_string.append(k)
            table[max(table.keys())+1] = string + symbol                    
            string = symbol
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    print table
    return code_for_string



def test():
    test_message = "unitTest"
    print encode(test_message)

test()                                                                      #end
