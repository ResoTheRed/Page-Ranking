import random;
import os;
import copy

#dictionary for tracking number of pages connecting to each node
connections = {};
connect_from = {};
connect_to = list();


#function creates a random adjacency list with 5-25 nodes
# each connection is unique in the list of the node
#layout id, <number of connections>, connection list 
def adj_list():
    name = name_ui();
    try:
        os.remove(name);
    except OSError:
        pass;

    num = random.randint(5,25);
    file_handler = open(name,'a+');
    for i in range(num):
        size = random.randint(3,num);
        q = list();
        q.append(-1);
        q.append(-1);
        for j in range(2,size):
            while True:
                temp = random.randint(0,num-1);
                if temp not in q:
                    q.append(temp);
                    break;
        q[0] = i;#each node id
        q[1] = len(q)-2;#amount connections
        file_handler.write(set_str(str(q))+'\n');
    file_handler.close();

#get the name of the file to run.
def name_ui():
    name = 'adj_list.txt';
    print('Welcome to the page rank finder.');
    print("1. Enter custom file name an adjacency list to run.");
    print('2. Create a random list ')
    choice = input();
    if int(choice) == 1:
        name = input('Enter the file name.');
    return name;

#remove symbols
def set_str(s):
    s = s.replace('[','');
    s = s.replace(']','');
    s = s.replace(',','');
    return s;
    
#reads in adjacency list file and adds nodes to dictionary
#and add each node list as an array
def setup_data_structs(name='adj_list.txt'):
    file_handler = open(name,'r');
    line = file_handler.readline();

    while line:
        arr = line.split(' ');
        connections[arr[0]] = 0; #establish key values for each node
        w = list();
        connect_from[arr[0]] = w; 
        connect_to.append(arr);
        line = file_handler.readline();

    file_handler.close();
    pages = len(connections);

#logs all connections to each node
def find_connections():
    for i in range(len(connect_to)):
        for j in range(2,len(connect_to[i])):
            b = str(connect_to[i][j]).replace('\n','');
            connections[b] +=1;
            connect_from[b].append(str(i));

#set each page value to 1/n
def set_r():
    r = list();
    pages = len(connections);
    for i in range(pages):
        r.append(round(1/pages,5));
    return r;

#find rt+1 for r
def get_r_new(old):
    #cycle though each nodes connections
    new = list();
    for k,v in connect_from.items():
        summation = 0
        for j in range(len(v)):
            #sum up each page pointing to current page old + (old pointer/pages)1 + ... n
            summation += (round(old[int(v[j])]  / int(connect_to[int(v[j])][1]),5));
        new.append(summation);
    return new;

#produces googles formula with B = 0.85
def google_formula(old):
    B = 0.85;
    n = len(old);
    new = list()
    for k,v in connect_from.items():
        sm = 0;
        for j in range(len(v)):
            sm += B*(round(old[int(v[j])]  / int(connect_to[int(v[j])][1]),5)) + (1-B)*(1/n);
        new.append(sm);
    return new
            
#detect if change is less than 5% from old to new r
def detect_change(new, old):
    for i in range(len(new)):
        v1 = abs(new[i]-old[i]);
        v2 = (new[i]+old[i])/2;
        if v2 == 0:
            return False;
        change = (v1/v2)*100;
        if change > 5:
            return True;
    return False;

#function writes the page rank a specific file
def print_page_rank(page_rank,file_name):
    sm = 0;
    temp = list();
    try:
        os.remove(file_name)
    except OSError:
        pass;
    file_handler = open(file_name,'a+');
    for i in range(len(page_rank)):
        sm += page_rank[i];
        string = str(page_rank[i])+" Page "+str(i)+": "+str(round(page_rank[i],5));
        temp.append(string);
    temp = order_page_rank(temp);
    for j in range(len(temp)):
        #write results to file
        file_handler.write(temp[j]+'\n');
    
#function reoders page-rank result in order of rank.
def order_page_rank(listing):
    listing.sort(reverse=True);
    for i in range(len(listing)):
       arr =  listing[i].split(' ');
       arr[0] = '';
       arr.append(' Ranking: '+str(i+1));
       listing[i] = " ".join(str(x) for x in arr);
    return listing;

#computes the page rank using power iteration
def power_iteration(google=False):
    is_changing = True;
    count = 0;
    r = set_r();
    r_new = list();
    while is_changing and count < 100:
        if google:
            r_new = google_formula(r);
        else:
            r_new = get_r_new(r);
        is_changing = detect_change(r_new, r);
        count+=1;
        r = r_new;
    if count > 99:
        print("Ran 100 iterations.");
    else:
        print('Completed in '+str(count)+' iterations.');
    return r;

#used to navigate to part a or b of the homework
def part_ui():
    print("Would you like to run the standard page rank (part a)\n"
            "or would you like to run Google's formulation. (part b)");
    print('1. Standard Version [part a]');
    print("2. Google's Formulation [part b]");
    choice = input();
    try:
        num = int(choice)
        if num == 1 or num == 2:
            return num;
        else:
            print("\nBad entry. Enter 1 or 2.\n")
            part_ui();
    except ValueError:
        print('\nBad entry. Enter 1 or 2.\n')
        part_ui();
        
#run throught the each step of 
def controller():
    file_name = 'part_a.txt'
    adj_list();
    setup_data_structs();
    find_connections();
    choice = part_ui();
    if choice == 1:
        page_rank = power_iteration();
    else:
        page_rank = power_iteration(google=True);
        file_name = 'part_b.txt';
    print_page_rank(page_rank,file_name);


controller();

