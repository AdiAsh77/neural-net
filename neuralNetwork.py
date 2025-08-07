import customtkinter as ctk
import tkinter as tk
import numpy as np
import math
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# ctk.set_widget_scaling(0.8)

global x
arr = [6]
oval = None
smallov = []
c = 0

def slider_event(value):
    print(int(float(value)))
    arr[0] = int(float(value))


def create_weights(a, b):
    slider_array = []
    for i in range(b):
        sl = []
        for i in range(a):
            sl.append(round(random.uniform(1.224, -1.224), 3))
        slider_array.append(sl)
    return slider_array


def create_baises(a):
    slider_array = []

    for i in range(a):
        # slider = ctk.CTkSlider(slider_frame, from_=low, to=high, number_of_steps=step)
        # slider.pack(pady=7)
        # slider.set(round(random.uniform((0.25*low), (0.25*high)), 2))
        slider_array.append(0)
    return slider_array



def showRate(event):
    learnlable.configure(text=f"Learn Rate is: {round(event,2)}")
def showepoch(event):
    epochlable.configure(text=f"Epoch is: {int(event)}")


def pointsafe(pointx, pointy):
    x=60 + (65 * pointx)
    y=700 - (65 * pointy)
    r=5
    oval = canvas.create_oval(x-r, y-r, x+r, y+r, fill="grey")
def pointpois(pointx, pointy):
    x=60 + (65 * pointx)
    y=700 - (65 * pointy)
    r=5
    oval = canvas.create_oval(x-r, y-r, x+r, y+r, fill="yellow")
def pointer(pointx, pointy):
    x=60 + (65 * pointx)
    y=700 - (65 * pointy)
    r=5
    oval = canvas.create_oval(x-r, y-r, x+r, y+r, fill="green", outline="green")
def pointer2(pointx, pointy):
    x=60 + (65 * pointx)
    y=700 - (65 * pointy)
    r=5
    oval = canvas.create_oval(x-r, y-r, x+r, y+r, fill="red", outline="red")

# def lineDraw():
#     m = slid1frame2.get()
#     c = slid2frame2.get()
#     eq.configure(text=f"y = {m}x + {c}")
#     lineEq(m,c)

# def update_label(value):
    # global oval

    # Delete the previous circle if it exists
    # if oval is not None:
    #     canvas.delete(oval)


    # label_S.configure(text=f"Value: {value}")
    # x=int(float(value))
    # # x=0
    # y=700
    # r=80
    # oval = canvas.create_oval(x, y, x+r, y+r, fill="blue")
    # canvas.delete(oval)

def print_window_size():
    width = app.winfo_width()
    height = app.winfo_height()
    print(f"Window size: {width}x{height}")

c = 1


def showcase():
    Cost(data)
    # lable7.configure(text="processing")
    c =0 

    for i in np.arange(0.1, 10.1, 0.1):
        x = round(i, 1)
        for j in np.arange(0.1, 10.1, 0.1):
            y = round(j, 1)
            inp = [x,y]
            # outputs(x,y,c, weight, baises)
            out = Network(inp)
            # print(out)
            if(out[0]>out[1]):
                pointer(x, y)
            else:
                # print("kdbhfuyzdfvugyc")
                pointer2(x, y)
    pointeres()
    #         c+=1
    # inp = [4,5]
    # print(Network(inp))



# def trying():
#     weight = [slide_wx1.get(), slide_wy1.get(), slide_wx2.get(), slide_wy2.get()]
#     print(weight)

# w = [   [ [1,2], [5,6], [7,8] ], [ [2,3,1], [5,8,9] ]   ]
# b = [   [1,4,7], [6,7]   ]

def NodeCost(actual, expected):
    error = actual - expected
    return (error * error)

# this function is del(C) / del(An)
def NodeCOstDerivative(actual, expected):
    error = 2 * (actual - expected)
    return error

def individualCost(datapoint):
    outputs = Network(datapoint["input"])
    # print("hello: ",outputs)
    cost = 0
    for nodeout in range(len(outputs)):
        cost += NodeCost(outputs[nodeout], datapoint["output"][nodeout])
    return cost

def Cost(data):
    totalcost = 0
    for datapoint in data:
        totalcost += individualCost(datapoint)
    costval.configure(text=f"Cost is: {(totalcost/len(data))}")
    return (totalcost/len(data))


## need to store Activations,   WeightedInput,   


def ApplyGradient(learnrate, costGradientW, costGradientB):
    # weights = [   slider3, slider5   ]
    # baises = [   slider4, slider6  ]
    # weights[0][0][0].set(0.6)

    for layno in range(len(lay)):
        numNodesIn = lay[layno][0]
        numNodesOut = lay[layno][1]

        for nodeOut in range(0,numNodesOut):
            # baises[layno][nodeOut].set( baises[layno][nodeOut].get() - (costGradientB[layno][nodeOut] * learnrate) )
            baises[layno][nodeOut] = baises[layno][nodeOut] - (costGradientB[layno][nodeOut] * learnrate) 
            for nodein in range(0,numNodesIn):
                # weights[layno][nodeOut][nodein].set( weights[layno][nodeOut][nodein].get() - (costGradientW[layno][nodeOut][nodein] * learnrate) )
                weights[layno][nodeOut][nodein] = weights[layno][nodeOut][nodein] - (costGradientW[layno][nodeOut][nodein] * learnrate)


## layer is same as calculateOutputs for video understanding
weighInpVal = []
# activationnVal = []
def Layer(numNodesIn, numNodesOut, inputs, layno):
    # weights = [   slider3, slider5   ]
    # baises = [   slider4, slider6  ]
    global weighInpVal

    weightedInputs = []
    activations = []

    for nodeOut in range(0,numNodesOut):
        # weightinp = baises[layno][nodeOut].get()
        weightinp = baises[layno][nodeOut]
        for nodein in range(0,numNodesIn):
            # weightinp += ( inputs[nodein] * weights[layno][nodeOut][nodein].get())
            weightinp += ( inputs[nodein] * weights[layno][nodeOut][nodein])
        activations.append(Activation(weightinp))
        weightedInputs.append(weightinp)
        
    weighInpVal.append(weightedInputs)
    return activations

def Activation(weightedinp):
    return 1/(1+math.pow(math.e,-weightedinp))

# this function is del(An) / del(Zn), where z is weighted input
def ActivationDerivative(weightedinp):
    activation = Activation(weightedinp)
    activeDeri = activation * (1 - activation)
    return activeDeri

activationnVal = []

def Network(input):
    
    global activationnVal
    global weighInpVal
    activationnVal = []
    weighInpVal = []
    activationnVal.append(input)
    for i in range(0,len(lay)):
        input = Layer(lay[i][0], lay[i][1], input, i)
        activationnVal.append(input)
    #     print(input)
    # print("\n")
    return input

def starprocess():
    print("the machine is starting to learn:---")
    # epoch = 300
    x = 0
    i = 1
    epoch = int(sliderepoch.get())
    # for i in range(500):
    file = open("cost.txt", "a")
    while(True):
        gg = Cost(data)
        if(gg > 0.03):
            NewLearn()
            if(i%10 == 0):
                file.write(f"{round(gg,5)}\n")
            print(i)
            i+=1
        else:
            file.write(f"{gg}\n")
            break
    file.close()
    print(weights)
    print(baises)

    # while True:
    #     if i == x:
    #         cos = Cost(data)
    #         i += 100
    #         if(cos < 0.04):
    #             print("The value of x is: ", x)
    #             break
    #     NewLearn()
    #     x+=1
    # check = 900
        # if (i+1 == check):
        #     print(check//90,"%")
        #     check += 900


def NewLearn():
    learnrate = round(sliderlearn.get(),2)

    for datapoint in data:
        Tester(datapoint)
    
    ApplyGradient(learnrate/len(data), costGradientW, costGradientB)
    clearAllGrad()


def Tester(datapoint):
    # layno = lay.index(lay[-1])
    # print(lay[layno])
    # numNodesIn = lay[-1][0]
    # numNodesOut = lay[-1][1]
    Network(datapoint["input"])
    # print(weighInpVal)
    # weighInpVal = []
    # print("activations: ")
    # print(activationnVal)
    outputLay = lay.index(lay[-1])

    # print("NodalValue of output Layer: ")
    nodeValue = CalOutputLayerNodeVal(activationnVal[outputLay+1], weighInpVal[outputLay], datapoint["output"])
    # print(nodeValue)
    UpdateGradient(lay[outputLay], nodeValue, activationnVal[outputLay+1-1])
    # print(costGradientW)
    # print(costGradientB)
    nodeValue = CalHiddenLayerNodeVal(weighInpVal[outputLay-1], lay[outputLay], nodeValue)
    # print(nodeValue)
    # print("Most probably error:--")
    UpdateGradient(lay[outputLay-1], nodeValue, activationnVal[outputLay+1-2])




def CalOutputLayerNodeVal(activation, weightinp, expectedOut):
    nodeValue = []
    for i in range(len(expectedOut)):
        nodecostderi = NodeCOstDerivative(activation[i], expectedOut[i])
        activeDeri = ActivationDerivative(weightinp[i])
        nodeValue.append( nodecostderi * activeDeri ) 
    return nodeValue

def CalHiddenLayerNodeVal(weightinp, OldLayer, OldNodeVal):
    # weights = [   slider3, slider5   ]
    # print("weights:")
    # print(OldLayer[0], len(OldNodeVal))
    NewnodeValue = []
    for newnode in range(OldLayer[0]):
        nodeVal = 0
        for oldnode in range(len(OldNodeVal)):
            # weghtedInpDeri = weights[lay.index(OldLayer)][oldnode][newnode].get()
            weghtedInpDeri = weights[lay.index(OldLayer)][oldnode][newnode]
            nodeVal += weghtedInpDeri * OldNodeVal[oldnode]
        
        nodeVal *= ActivationDerivative(weightinp[newnode])
        NewnodeValue.append(nodeVal)

    return NewnodeValue


def UpdateGradient(layer, nodeValue, input):
    numNodeIn = layer[0]
    numNodeOut = layer[1]
    for nodeout in range(numNodeOut):
        for nodein in range(numNodeIn):
            CostDerivativewrtW = input[nodein] * nodeValue[nodeout]
            costGradientW[lay.index(layer)][nodeout][nodein] += CostDerivativewrtW

        CostDerivativewrtB = 1 * nodeValue[nodeout]
        costGradientB[lay.index(layer)][nodeout] += CostDerivativewrtB


def clearAllGrad():
    for layno in range(len(lay)):
        numNodesin = lay[layno][0]
        numNodesout = lay[layno][1]
        for i in range(numNodesout):
            costGradientB[layno][i] = 0
            for j in range(numNodesin):
                costGradientW[layno][i][j] = 0


# Maximize the window on start
def maximize():
    app.state('zoomed')

# Set appearance mode and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Create the main window
app = ctk.CTk()
app.title("Maximized CustomTkinter Window")
app.geometry("500x500")
width = app.winfo_width()
height = app.winfo_height()

# label = ctk.CTkLabel(app, text="hello world", fg_color="transparent")
# label.pack()

def plot_graph():
    # Get the input and convert to float list
    file = open("cost.txt", "r")
    nr = file.read().split("\n")
    file.close()

    numbers = []
    for i in range(len(nr)):
        if (i%5 == 0):
            numbers.append(float(nr[i]))
    x_values = list(range(len(numbers)))

    # Clear previous plot if any
    ax.clear()

    # Plot without markers
    ax.plot(x_values, numbers, linestyle='-', color="b")
    ax.set_facecolor('#333333')  # or any other color
    fig.patch.set_facecolor('#333333')  # or '#f0f0f0', etc.
    ax.tick_params(axis='x', labelcolor='white', labelsize=10)
    ax.tick_params(axis='y', labelcolor='white', labelsize=10)


    ax.set_xlabel("Index", color='white', fontsize=12)
    ax.set_ylabel("Value", color='white', fontsize=12)
    ax.set_title("Index vs Value Plot", color='white', fontsize=12)
    ax.grid(True)

    # Update the canvas
    Costcanvas.draw()

def switchFrame(choice):
    global horizontal
    if choice == "Frame 1":
        Costgraph.place_forget()
        graph.place(x=35, y=35)
        # frame.place(x=width)
        graph.pack_propagate(False)

    elif choice == "Frame 2":
        graph.place_forget()
        Costgraph.place(x=35, y=35)
        Costgraph.pack_propagate(False)

option_menu = ctk.CTkOptionMenu(app, values=["Frame 1", "Frame 2"], command=switchFrame)
option_menu.place(x=35, y=0)

##########################################################......... LeranFrame

framelearn = ctk.CTkFrame(master=app, width=300, height=280)
framelearn.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=30)
framelearn.pack_propagate(False)

sliderlearn = ctk.CTkSlider(framelearn, from_=0, to=1, number_of_steps=100, command=showRate)
sliderlearn.pack(pady=(10,0))
sliderlearn.set(0)

learnlable = ctk.CTkLabel(framelearn, text="Learn rate is: ", fg_color="transparent", font=("Arial", 16, "bold"))
learnlable.pack(padx=10, pady=8)

sliderepoch = ctk.CTkSlider(framelearn, from_=100, to=1000, number_of_steps=10, command=showepoch)
sliderepoch.pack(pady=(10,0))
sliderepoch.set(100)

epochlable = ctk.CTkLabel(framelearn, text="epoch is: ", fg_color="transparent", font=("Arial", 16, "bold"))
epochlable.pack(padx=20, pady=8)

learn = ctk.CTkButton(framelearn, text="Test", command=showcase)
learn.pack(pady = 7, padx=20)

CostPlot = ctk.CTkButton(framelearn, text="CostPlot", command=plot_graph)
CostPlot.pack(pady = 7, padx=20)

# restart = ctk.CTkButton(framelearn, text="Restart", command=Restart)
# restart.pack(pady = 7, padx=20)


# switchFrame("Frame 2")
Drawline = ctk.CTkButton(app, text="Drwa 0Line", command=starprocess)
Drawline.place(relx=1.0, rely=0.0, anchor="ne", x=-100, y=735)

Costgraph = ctk.CTkFrame(master=app, width=1100, height=700)
Costgraph.place(x=35, y=35)
Costgraph.pack_propagate(False)

graph = ctk.CTkFrame(master=app, width=1100, height=700)
graph.place(x=35, y=35)
# frame.place(x=width)
graph.pack_propagate(False)

canvas = tk.Canvas(graph, bg="#333333", width=1300, height=900, highlightthickness=0)
canvas.pack(padx=40, pady=40)
canvas.pack_propagate()

vertical = canvas.create_line(40, 700, 1200, 700, fill="white", width=3)
horizontal = canvas.create_line(60, 730, 60, 40, fill="white", width=3)



fig = Figure(figsize=(14, 6), dpi=100)
ax = fig.add_subplot(111)
ax.tick_params(axis='x', labelcolor='white', labelsize=11)
ax.tick_params(axis='y', labelcolor='white', labelsize=11)

ax.set_facecolor('#333333')  # or any other color
fig.patch.set_facecolor('#333333') 
fig.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.08)

# Costcanvas = tk.Canvas(Costgraph, bg="#333333", width=1300, height=900, highlightthickness=0)
Costcanvas = FigureCanvasTkAgg(fig, master=Costgraph)
Costcanvas.get_tk_widget().place(x=40, y=10, width=1300, height=850)
# Costcanvas.get_tk_widget().pack(padx=40, pady=40)
# Costcanvas.get_tk_widget().pack_propagate()

costval = ctk.CTkLabel(app, text="COST IS: false", font=("Arial", 20, "bold"))
costval.place(x=50, y=740)


def XY(x,y, canvas):
    for i in range(0,x):
        canvas.create_text(
            40, 
            700-(i*65), 
            text=f"{i}", 
            fill="white", 
            font=("Helvetica", 14, "bold")
        )
    c = 0
    for i in range(0,y):
        canvas.create_text(
            60+(i*65), 
            730, 
            text=f"{c+i}", 
            fill="white", 
            font=("Helvetica", 14, "bold")
        )
XY(11,15,canvas)

# point = [[1,2], [2,4], [1,5], [2,7], [8,8], [4,6], [5,1], [9,1], [10, 10], [0.5, 0.5]]

point = [[3.7, 2.07], [8.14, 3.86], [3.71, 6.56], [9.15, 8.83], [6.31, 5.72], [6.02, 7.95], [7.31, 6.4], [5.13, 0.9], [7.04, 9.12], [5.01, 1.56], [5.38, 9.11], [4.86, 2.45], [1.19, 1.51], [2.54, 8.43], [4.6, 1.29], 
        [7.06, 5.75], [2.86, 1.56], [7.69, 9.58], [6.2, 1.57], [2.0, 1.57], [9.99, 1.99], [1.74, 9.96], [0.87, 4.01], [6.51, 4.38], [0.72, 5.99], [7.19, 1.02], [4.13, 9.19], [1.51, 3.08], [3.16, 4.97], [7.75, 5.03],
        [0.16, 1.19], [6.91, 4.29], [7.38, 7.51], [3.93, 0.33], [6.3, 0.93], [8.61, 6.17], [3.25, 4.79], [5.02, 8.5], [3.07, 0.91], [6.94, 2.94], [6.45, 4.25], [5.55, 8.87], [9.07, 9.51], [3.56, 6.07], [4.7, 4.34], 
        [7.63, 5.06], [3.29, 1.3], [7.26, 0.6], [0.4, 4.39], [2.45, 3.62], [3.86, 2.78], [8.39, 9.49], [8.13, 3.81], [6.71, 2.24], [7.6, 0.61], [2.1, 1.73], [1.03, 4.35], [9.59, 4.65], [1.38, 9.15], [8.42, 4.19], 
        [4.87, 7.95], [1.91, 9.09], [4.45, 2.45], [5.83, 3.07], [6.08, 0.85], [4.07, 3.89], [3.93, 2.64], [6.01, 6.08], [2.78, 9.39], [0.36, 4.42], [8.08, 4.66], [1.1, 5.43], [3.25, 8.67], [8.0, 7.15], [9.5, 7.11], 
        [8.55, 5.24], [7.19, 3.76], [4.98, 0.45], [8.66, 4.04], [5.82, 7.77], [0.56, 2.55], [5.26, 2.28], [4.16, 9.8], [4.67, 8.33], [2.88, 4.39], [2.67, 2.28], [5.65, 7.48], [0.0, 8.66], [3.17, 5.09], [9.75, 0.55], 
        [3.94, 4.99], [9.39, 2.38], [6.38, 6.37], [7.85, 1.15], [0.83, 1.98], [5.37, 2.6], [6.84, 7.16], [8.1, 8.44], [4.24, 1.33], [5.16, 1.72]]
# print(point)

# specifying the layers of the neural Network here:---------

node = [2,3,2]
lay = []
for i in range(0,len(node)-1):
    lay.append([node[i], node[i+1]])

costGradientW = []
costGradientB = []
for layno in range(len(lay)):
    numNodesin = lay[layno][0]
    numNodesout = lay[layno][1]
    costGradientB.append([])
    costGradientW.append([])
    for i in range(numNodesout):
        costGradientB[layno].append(0)
        costGradientW[layno].append([])
        for j in range(numNodesin):
            # w[layno].append([])
            costGradientW[layno][i].append(0)


print(costGradientW, "\n")
weights = []
baises = []
for i in lay:
    weights.append(create_weights(i[0], i[1]))
    baises.append(create_baises(i[1]))
print(weights)
print(baises)
print("\n",costGradientB)


file = open("cost.txt", "w")
file.close()

d = {}
val = []

def outputs(inp1, inp2, g, weight, baises):
    out1 = inp1*weight[0] + inp2*weight[1] + baises[0]
    out2 = inp1*weight[2] + inp2*weight[3] + baises[1]
    if(out1>out2):
        pointer(inp1, inp2)
        d.update({g:[[inp1,inp2],0]})
        val.append(0)
    else:
        pointer2(inp1, inp2)
        d.update({g:[[inp1,inp2],1]})
        val.append(1)


safes = [[3.7, 2.07], [5.13, 0.9], [5.01, 1.56], [4.86, 2.45], [1.19, 1.51], [4.6, 1.29], [2.86, 1.56], [6.2, 1.57], [2.0, 1.57], [0.87, 4.01], [1.51, 3.08], 
         [0.16, 1.19], [3.93, 0.33], [6.3, 0.93], [3.07, 0.91], [3.29, 1.3], [0.4, 4.39], [2.45, 3.62], [3.86, 2.78], [2.1, 1.73], [1.03, 4.35], [4.45, 2.45], 
         [6.08, 0.85], [4.07, 3.89], [3.93, 2.64], [0.36, 4.42], [4.98, 0.45], [0.56, 2.55], [5.26, 2.28], [2.88, 4.39], [2.67, 2.28], [0.83, 1.98], [5.37, 2.6], 
         [4.24, 1.33], [5.16, 1.72]]
# safe = []
data = []
def pointeres():
    for i in point:
        if i not in safes:
            pointsafe(i[0], i[1])
            d = {"input":i,"output":[1,0]}
            data.append(d)
        else:
            pointpois(i[0], i[1])
            d = {"input":i,"output":[0,1]}
            data.append(d)
pointeres()
# Cost(data)
    # print(i)
app.after(0, maximize)
app.mainloop()
