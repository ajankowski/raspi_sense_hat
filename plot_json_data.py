import matplotlib.pyplot as plt
import numpy as np
import json


if _name_=='_main_':
    
    x = np.arange(100)
    y = x*x
    z = x*x + 10*x
    
    with open('dane.json') as json_file:
        s = json.load(json_file)
        
        
    plt.rcParams.update(s)
    
    plt.plot(x,y,label='Y=x*x');
    plt.plot(x,y,label='Y=x*x+10*x');
    plt.title('dane json');
    plt.legend();
    plt.plot();
    plt.savefig('dane_json.png')