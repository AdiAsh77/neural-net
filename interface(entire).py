import customtkinter as ctk
import tkinter as tk
import numpy as np
import math
import random
# ctk.set_widget_scaling(0.8)

global x
arr = [6]
oval = None
smallov = []
c = 0

def slider_event(value):
    print(int(float(value)))
    arr[0] = int(float(value))



def create_weights(slider_frame, a, b, slider_array, low, high, step):
    slider_array.clear()

    for i in range(b):
        sl = []
        for i in range(a):
            slider = ctk.CTkSlider(slider_frame, from_=low, to=high, number_of_steps=step)
            slider.pack(pady=7)
            slider.set(round(random.uniform((0.25*low), (0.25*high)), 2))
            sl.append(slider)
        slider_array.append(sl)


def create_baises(slider_frame, a, slider_array, low, high, step):
    slider_array.clear()

    for i in range(a):
        slider = ctk.CTkSlider(slider_frame, from_=low, to=high, number_of_steps=step)
        slider.pack(pady=7)
        slider.set(round(random.uniform((0.25*low), (0.25*high)), 2))
        slider_array.append(slider)


randinput = 0
def randominput():
    global randinput
    randinput = round(random.uniform(-3, 3), 2)
    button_event(randinput)

def showRate(event):
    learnlable.configure(text=f"Learn Rate is: {round(event,2)}")
def showepoch(event):
    epochlable.configure(text=f"Epoch is: {int(event)}")


def button_event(event):
    # label_S.configure(text=f"Value: {sliderx.get()}, {slidery.get()}")
    Slope(event)
    global oval
    global smallov
    
    if oval is not None:
        canvas.delete(oval)

    pointx = event
    pointy = function(pointx)
    x=515 + (65 * pointx)
    y=700 - (65 * pointy)

    # print("button pressed", x, y)
    r=10
    # oval2 = canvas.create_oval(x-(r-4), y-(r-4), x+(r-4), y+(r-4), fill="white")
    oval = canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")
    # smallov.append(oval2)
    
def Restart():
    button_event(randinput)
    for ov in smallov:
        canvas.delete(ov)

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


def function(x):
    y = (0.2 * math.pow(x,4)) + (0.1 * math.pow(x,3)) - math.pow(x,2) + 2
    return y
def FunctionDerivative(x):
    y = (0.8 * math.pow(x,3)) + (0.3 * math.pow(x,2)) - (2*x)
    return y

def Slope(x):
    # h = 0.0000000001
    # delta = function(h+x) - function(x)
    slope = round(FunctionDerivative(x),3)
    slopelable.configure(text=f"Slope is: {slope}")

def learn():
    global randinput
    rate = round(sliderlearn.get(),2)
    print("input random is: ", randinput)

    h = 0.0000000001
    delta = function(h+randinput) - function(randinput)
    slope = round(delta/h,3)

    randinput -= slope * rate
    button_event(randinput)


## need to store Activations,   WeightedInput,   


def Learn():
    h = 0.0001
    learnrate = round(sliderlearn.get(),2)
    originalCost = Cost(data)
    # print("original: ",originalCost)

    weights = [   slider3, slider5   ]
    baises = [   slider4, slider6  ]
    
    for layno in range(len(lay)):
        numNodesIn = lay[layno][0]
        numNodesOut = lay[layno][1]

        #COSTGRADIENT FOR WEIGHTS:
        for nodeout in range(numNodesOut):

            for nodein in range(numNodesIn):
                weights[layno][nodeout][nodein].set( weights[layno][nodeout][nodein].get() + h)
                deltaCost = Cost(data) - originalCost
                weights[layno][nodeout][nodein].set( weights[layno][nodeout][nodein].get() - h )
                costGradientW[layno][nodeout][nodein] = deltaCost/h

        #COSTGRADIENT FOR Baises:
        for nodeout in range(numNodesOut):
            baises[layno][nodeout].set( baises[layno][nodeout].get() + h )
            deltaCost = Cost(data) - originalCost
            baises[layno][nodeout].set( baises[layno][nodeout].get() - h )
            costGradientB[layno][nodeout] = deltaCost/h
    # print(costGradientW)
    # print(costGradientB)
    ApplyGradient(learnrate, costGradientW, costGradientB)


def ApplyGradient(learnrate, costGradientW, costGradientB):
    weights = [   slider3, slider5   ]
    baises = [   slider4, slider6  ]
    # weights[0][0][0].set(0.6)

    for layno in range(len(lay)):
        numNodesIn = lay[layno][0]
        numNodesOut = lay[layno][1]

        for nodeOut in range(0,numNodesOut):
            baises[layno][nodeOut].set( baises[layno][nodeOut].get() - (costGradientB[layno][nodeOut] * learnrate) )
            for nodein in range(0,numNodesIn):
                weights[layno][nodeOut][nodein].set( weights[layno][nodeOut][nodein].get() - (costGradientW[layno][nodeOut][nodein] * learnrate) )


## layer is same as calculateOutputs for video understanding
weighInpVal = []
# activationnVal = []
def Layer(numNodesIn, numNodesOut, inputs, layno):
    weights = [   slider3, slider5   ]
    baises = [   slider4, slider6  ]
    global weighInpVal
    # global activationnVal

    # weights = [   [ [1,2], [5,6], [7,8] ], [ [2,3,1], [5,8,9] ]   ]
    # baises = [   [1,4,7], [6,7]   ]

    weightedInputs = []
    activations = []
    for nodeOut in range(0,numNodesOut):
        weightinp = baises[layno][nodeOut].get()
        for nodein in range(0,numNodesIn):
            weightinp += ( inputs[nodein] * weights[layno][nodeOut][nodein].get())
        activations.append(Activation(weightinp))
        weightedInputs.append(weightinp)
    # print(weightedInputs)
    weighInpVal.append(weightedInputs)
    # activationnVal.append(activations)
    # print(activations)
    # print("\n")
    return activations

def Activation(weightedinp):
    # if (weightedinp > 0):
    #     return 1
    # else:
    #     return 0
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

def titi():
    datapoint = data[0]
    datapoint2 = data[1]
    titi(datapoint)
    clearAllGrad()
    titi(datapoint2)

def starprocess():
    print("the machine is starting to learn:---")
    # epoch = 300
    x = 0
    i = 1
    epoch = int(sliderepoch.get())
    # for i in range(9000):
    while(Cost(data)>0.03):
        NewLearn()
        print(i)
        i+=1
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
    # global weighInpVal
    # datapoint = data[0]
    # print(datapoint["input"])
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
    # print(costGradientW)
    # print(costGradientB)
    # print("\n")



def CalOutputLayerNodeVal(activation, weightinp, expectedOut):
    nodeValue = []
    for i in range(len(expectedOut)):
        nodecostderi = NodeCOstDerivative(activation[i], expectedOut[i])
        activeDeri = ActivationDerivative(weightinp[i])
        nodeValue.append( nodecostderi * activeDeri ) 
    return nodeValue

def CalHiddenLayerNodeVal(weightinp, OldLayer, OldNodeVal):
    weights = [   slider3, slider5   ]
    # print("weights:")
    # print(OldLayer[0], len(OldNodeVal))
    NewnodeValue = []
    for newnode in range(OldLayer[0]):
        nodeVal = 0
        for oldnode in range(len(OldNodeVal)):
            weghtedInpDeri = weights[lay.index(OldLayer)][oldnode][newnode].get()
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

label = ctk.CTkLabel(app, text="hello world", fg_color="transparent")
label.pack()

###########################################################....... FRAME1

# frame = ctk.CTkFrame(master=app, width=300, height=250)
# frame.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=10)
# frame.place(x=width)
# frame.pack_propagate(False)

# button = ctk.CTkButton(frame, text="CTkButton", command=button_event)
# button.pack(pady=30, padx=20)


# sliderx = ctk.CTkSlider(frame, from_=0, to=10, number_of_steps=10)
# sliderx.pack(pady=20, padx=20)
# sliderx.set(0)

# slidery = ctk.CTkSlider(frame, from_=0, to=10, number_of_steps=10)
# slidery.pack(pady=10, padx=20)
# slidery.set(0)


# label_S = ctk.CTkLabel(frame, text="slider value", fg_color="transparent")
# label_S.pack(pady=20, padx=20)




##########################################################...... FRAME 2

# frame2 = ctk.CTkFrame(master=app, width=300, height=250)
# frame2.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=270)
# # frame.place(x=width)
# frame2.pack_propagate(False)

# lable2 = ctk.CTkLabel(frame2, text="Draw the line: y=mx+c", fg_color="transparent")
# lable2.pack(pady=20, padx=20)

# slid1frame2 = ctk.CTkSlider(frame2, from_=-10, to=10, number_of_steps=10)
# slid1frame2.pack(pady=10, padx=20)
# slid1frame2.set(0)

# slid2frame2 = ctk.CTkSlider(frame2, from_=-10, to=10, number_of_steps=10)
# slid2frame2.pack(pady=10, padx=20)
# slid2frame2.set(0)

# buttonline = ctk.CTkButton(frame2, text="Drwa Line", command=lineDraw)
# buttonline.pack(pady=20, padx=20)

# eq = ctk.CTkLabel(frame2, text="y = mx + c", fg_color="transparent")
# eq.pack(pady=0, padx=20)


##########################################################......... OptionMenu

def switchFrame(choice):
    global horizontal
    if choice == "Frame 1":
        frameslope.place_forget()

        frame3.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=30)

        frame4.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=255)

        frame5.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=390)

        frame6.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=625)

        # canvas.delete(horizontal)
        # horizontal = canvas.create_line(60, 730, 60, 40, fill="white", width=3)

    elif choice == "Frame 2":
        frame4.place_forget()
        frame5.place_forget()
        frame6.place_forget()
        frame3.place_forget()
        frameslope.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=30)
        framelearn.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=160)
        # canvas.delete(horizontal)
        # horizontal = canvas.create_line(515, 730, 515, 40, fill="white", width=3)


option_menu = ctk.CTkOptionMenu(app, values=["Frame 1", "Frame 2"], command=switchFrame)
option_menu.place(relx=1.0, rely=0.0, anchor="ne", x=-100, y=0)


##########################################################......... slopeslider

frameslope = ctk.CTkFrame(master=app, width=300, height=120)
# frameslope.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=10)
frameslope.pack_propagate(False)

sliderslope = ctk.CTkSlider(frameslope, from_=-3.2, to=3.0, number_of_steps=150, command=button_event)
sliderslope.pack(pady=20)
sliderslope.set(0)
slopelable = ctk.CTkLabel(frameslope, text="Slope is: ", fg_color="transparent", font=("Arial", 16, "bold"))
slopelable.pack(padx=20)




##########################################################......... LeranFrame

framelearn = ctk.CTkFrame(master=app, width=300, height=280)
# frameslope.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=10)
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

Random = ctk.CTkButton(framelearn, text="Random", command=randominput)
Random.pack(pady = 7, padx=20)

restart = ctk.CTkButton(framelearn, text="Restart", command=Restart)
restart.pack(pady = 7, padx=20)



##########################################################......... FRAME 3

frame3 = ctk.CTkFrame(master=app, width=300, height=220)
frame3.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=30)
frame3.pack_propagate(False)

lable3 = ctk.CTkLabel(frame3, text="WEIGHTS 1", fg_color="transparent")
lable3.pack(padx=20)
slider3 = []
create_weights(frame3, 2, 3, slider3, -2, 2, 40000)

# buttonline = ctk.CTkButton(frame3, text="Drwa Line", command=showcase)
# buttonline.pack(pady=20, padx=20)

# eq = ctk.CTkLabel(frame3, text="y = mx + c", fg_color="transparent")
# eq.pack(pady=0, padx=20)



##########################################################......... FRAME 4

frame4 = ctk.CTkFrame(master=app, width=300, height=130)
frame4.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=255)
frame4.pack_propagate(False)

lable4 = ctk.CTkLabel(frame4, text="BAISES 1", fg_color="transparent")
lable4.pack(padx=20)

slider4 = []
create_baises(frame4, 3, slider4, -10, 10, 200000)




##########################################################......... FRAME 5

frame5 = ctk.CTkFrame(master=app, width=300, height=230)
frame5.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=390)
frame5.pack_propagate(False)

lable5 = ctk.CTkLabel(frame5, text="WEIGHTS 1", fg_color="transparent")
lable5.pack(pady=5, padx=20)

slider5 = []
create_weights(frame5, 3, 2, slider5, -10, 10, 200000)





##########################################################......... FRAME 6

frame6 = ctk.CTkFrame(master=app, width=300, height=110)
frame6.place(relx=1.0, rely=0.0, anchor="ne", x=-20, y=625)
frame6.pack_propagate(False)

lable6 = ctk.CTkLabel(frame6, text="BAISES 1", fg_color="transparent")
lable6.pack(padx=20)

slider6 = []
create_baises(frame6, 2, slider6, -5, 5, 100000)



switchFrame("Frame 2")
Drawline = ctk.CTkButton(app, text="Drwa 0Line", command=starprocess)
Drawline.place(relx=1.0, rely=0.0, anchor="ne", x=-100, y=735)


graph = ctk.CTkFrame(master=app, width=1100, height=700)
graph.place(x=35, y=30)
# frame.place(x=width)
graph.pack_propagate(False)

canvas = tk.Canvas(graph, bg="#333333", width=1300, height=900, highlightthickness=0)
canvas.pack(padx=40, pady=40)
canvas.pack_propagate()

vertical = canvas.create_line(40, 700, 1200, 700, fill="white", width=3)
horizontal = canvas.create_line(60, 730, 60, 40, fill="white", width=3)

costval = ctk.CTkLabel(app, text="COST IS: false", font=("Arial", 20, "bold"))
costval.place(x=50, y=740)


for i in range(0,11):
    canvas.create_text(
        40, 
        700-(i*65), 
        text=f"{i}", 
        fill="white", 
        font=("Helvetica", 14, "bold")
    )
c = 0
for i in range(0,15):
    canvas.create_text(
        60+(i*65), 
        730, 
        text=f"{c+i}", 
        fill="white", 
        font=("Helvetica", 14, "bold")
    )

# d = [6]
# arr[0] = 6

# x=60 + (65 * arr[0])
# y=700 - (65 * arr[0])
# r=10
# oval = canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")

# point = [[1,2], [2,4], [1,5], [2,7], [8,8], [4,6], [5,1], [9,1], [10, 10], [0.5, 0.5]]

point = [[3.7, 2.07], [8.14, 3.86], [3.71, 6.56], [9.15, 8.83], [6.31, 5.72], [6.02, 7.95], [7.31, 6.4], [5.13, 0.9], [7.04, 9.12], [5.01, 1.56], [5.38, 9.11], [4.86, 2.45], [1.19, 1.51], [2.54, 8.43], [4.6, 1.29], [7.06, 5.75], [2.86, 1.56], [7.69, 9.58], [6.2, 1.57], [2.0, 1.57], [9.99, 1.99], [1.74, 9.96], [0.87, 4.01], [6.51, 4.38], [0.72, 5.99], [7.19, 1.02], [4.13, 9.19], [1.51, 3.08], [3.16, 4.97], [7.75, 5.03], [0.16, 1.19], [6.91, 4.29], [7.38, 7.51], [3.93, 0.33], [6.3, 0.93], [8.61, 6.17], [3.25, 4.79], [5.02, 8.5], [3.07, 0.91], [6.94, 2.94], [6.45, 4.25], [5.55, 8.87], [9.07, 9.51], [3.56, 6.07], [4.7, 4.34], [7.63, 5.06], [3.29, 1.3], [7.26, 0.6], [0.4, 4.39], [2.45, 3.62], [3.86, 2.78], [8.39, 9.49], [8.13, 3.81], [6.71, 2.24], [7.6, 0.61], [2.1, 1.73], [1.03, 4.35], [9.59, 4.65], [1.38, 9.15], [8.42, 4.19], [4.87, 7.95], [1.91, 9.09], [4.45, 2.45], [5.83, 3.07], [6.08, 0.85], [4.07, 3.89], [3.93, 2.64], [6.01, 6.08], [2.78, 9.39], [0.36, 4.42], [8.08, 4.66], [1.1, 5.43], [3.25, 8.67], [8.0, 7.15], [9.5, 7.11], [8.55, 5.24], [7.19, 3.76], [4.98, 0.45], [8.66, 4.04], [5.82, 7.77], [0.56, 2.55], [5.26, 2.28], [4.16, 9.8], [4.67, 8.33], [2.88, 4.39], [2.67, 2.28], [5.65, 7.48], [0.0, 8.66], [3.17, 5.09], [9.75, 0.55], [3.94, 4.99], [9.39, 2.38], [6.38, 6.37], [7.85, 1.15], [0.83, 1.98], [5.37, 2.6], [6.84, 7.16], [8.1, 8.44], [4.24, 1.33], [5.16, 1.72]]
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


lo = [[4, 7], [8,10]]

def line(pon):
    x1 = 515 + (pon[0][0] * 65)
    y1 = 700 - (pon[0][1] * 65)
    
    x2 = 515 + (pon[1][0] * 65)
    y2 = 700 - (pon[1][1] * 65)

    # x1 = 515 - (0 * 65)
    # y1 = 700 + (0 * 65)
    
    # x2 = 515 + (-1 * 65)
    # y2 = 700 - (1 * 65)
    
    canvas.create_line(x1, y1, x2, y2, fill="yellow", width=3)

# lineEq(lo)

def lineEq():
    lin = []
    for i in np.arange(-3.2, 10.0, 0.1):
        x = round(i, 1)
        # y = float((m*x) + c)

        y = function(x)

        lin.append([x,y])
        if (y > 10.2):
            continue
        elif(len(lin) > 1):
            # print("ghghghghgh",lin)
            line(lin[int(x*10)+31:])


# line([[-1,6],[0,2]])
# lineEq()

# global wx1,wx2, wy1, wy2

# wx1= 0.7
# wx2= -0.4
# wy1= -0.6
# wy2 = 0.9

d = {}
val = []
# d.update({2:[4,8]})
# d.update({9:[4,8]})
# print(":", d)


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




# for i in np.arange(0.0, 1.0, 0.1):
#     x = round(i, 1)
#     print(x)
safes = [[3.7, 2.07], [5.13, 0.9], [5.01, 1.56], [4.86, 2.45], [1.19, 1.51], [4.6, 1.29], [2.86, 1.56], [6.2, 1.57], [2.0, 1.57], [0.87, 4.01], [1.51, 3.08], [0.16, 1.19], [3.93, 0.33], [6.3, 0.93], [3.07, 0.91], [3.29, 1.3], [0.4, 4.39], [2.45, 3.62], [3.86, 2.78], [2.1, 1.73], [1.03, 4.35], [4.45, 2.45], [6.08, 0.85], [4.07, 3.89], [3.93, 2.64], [0.36, 4.42], [4.98, 0.45], [0.56, 2.55], [5.26, 2.28], [2.88, 4.39], [2.67, 2.28], [0.83, 1.98], [5.37, 2.6], [4.24, 1.33], [5.16, 1.72]]
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
print(len(data))

# Run the application
# print("here is dic\n", d)
# print("\n\nhere is dic\n", val)
# print("end")
app.after(0, maximize)
app.mainloop()
