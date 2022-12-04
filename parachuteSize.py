import PySimpleGUI as sg
import numpy as np

sg.theme('LightBlue3')
default = "0.00"
sz = 18
iSize = 30


calculateAreaLayout = (
    [sg.Text("Calculate Area of Parachute")],
    [sg.Text("Force: ", size = sz),         sg.Input(default, key = "FORCE", size = iSize), sg.Push(),          sg.Text("N", key = "forceUnit")], 
    [sg.Text("Fluid Density: ", size = sz), sg.Input("0.4349", key = "FLUIDDENSITY", size = iSize), sg.Push(),  sg.Text("kg/m^3", key = "FluidUnit")], 
    [sg.Text("Velocity: ", size = sz),      sg.Input(default, key = "VELOCITY", size = iSize), sg.Push(),       sg.Text("m/s", key = "velocityUnit")], 
    [sg.Text("Cd: ", size = sz),            sg.Input("1.4", key = "Cd", size = iSize)], 
    [sg.Text("Area: ", size = sz),          sg.Input(default, key = "aAREA", size = iSize), sg.Push(),          sg.Text("m^2", key = "areaUnit")], 
    [sg.Push(), sg.Button('Calculate Area')]
)

caclulateDiameterLayout =  (
    [sg.Text("Calculate Parachute Diameter")],
    [sg.Text("Area: ", size = sz),      sg.Input(default, key = "dArea", size = iSize)],
    [sg.Text("Diameter: ", size = sz),  sg.Input(default, key = "dDiameter", size = iSize)],
    [sg.Push(), sg.Button('Calculate Diameter')]
)

calculateForceLayout = (
    [sg.Text("Calculate Force")],
    [sg.Text("Mass: ", size = sz),          sg.Input(default, key = "fMass", size = iSize), sg.Text("kg")],
    [sg.Text("Acceleration: ", size = sz),  sg.Input("9.81", key = "fAcc", size = iSize),   sg.Text("m/s^2")],
    [sg.Text("Force: ", size = sz),         sg.Text(default, key = "fForce", size = iSize), sg.Text("N")],
    [sg.Push(), sg.Button('Calculate Force')]
)

convertVelocityLayout = (
    [sg.Text("Convert ft/s to m/s")],
    [sg.Text("Velocity (ft/s): ", size = sz),   sg.Input(default, key = "inVelocity", size = iSize), sg.Text("ft/s")],
    [sg.Text("Velocity (m/s): ", size = sz),    sg.Text(default, key = "outVelocity", size = iSize), sg.Text("m/s")],
    [sg.Push(), sg.Button('Convert Velocity')]
)

convertDiameterLayout = (
    [sg.Text("Convert meters to feet")],
    [sg.Text("In Length: ", size = sz),     sg.Input(default, key = "inLength", size = iSize), sg.Text("meters")],
    [sg.Text("Out Length: ", size = sz),    sg.Text(default, key = "outLength", size = iSize), sg.Text("feet")],
    [sg.Push(), sg.Button('Convert Length')]
)

layout = [
    convertVelocityLayout,
    calculateForceLayout,
    calculateAreaLayout,
    caclulateDiameterLayout,
    convertDiameterLayout,
]

window = sg.Window('Parachute Area Calculator', layout)

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break 

    if event == 'Calculate Area':
        rho = float(values["FLUIDDENSITY"])
        F = float(values["FORCE"])
        V = float(values["VELOCITY"])
        Cd = float(values["Cd"])
        A = float(values["aAREA"])

        area = 2*F / (Cd * rho * V * V) 
        window["aAREA"].Update(area)
        window["dArea"].Update(area)

    if event == 'Calculate Force':
        m = float(values["fMass"])
        a = float(values["fAcc"])
        
        f = m * a
        window["fForce"].Update(f)
        window["FORCE"].Update(f)

    if event == 'Calculate Diameter':
        A = float(values["dArea"])
        D = np.sqrt((4 * A)/ np.pi)

        window["dDiameter"].Update(D)
        window["inLength"].Update(D)

    if event == 'Convert Velocity':
        inV = float(values["inVelocity"])
        outV = inV * 0.3048

        window["outVelocity"].Update(outV)
        window["VELOCITY"].Update(outV)

    if event == 'Convert Length':
        inLen = float(values["inLength"])
        outLen = inLen / 0.3048

        window["outLength"].Update(outLen)

    




window.close()

