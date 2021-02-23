from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import random
import seaborn as sns

kWhperm2 = {
  "Andhra Pradesh": 5.6,
  "Arunachal Pradesh": 5.6,
  "Assam": 4.5,
  "Bihar": 5.5,
  "Chhattisgarh": 4.8,
  "Goa": 5.6,
  "Gujarat": 6,
  "Haryana": 5.7,
  "Himachal Pradesh": 5.1,
  "Jammu and Kashmir": 5.2,
  "Jharkhand": 4.8,
  "Karnataka": 5.2,
  "Kerala": 5.4,
  "Madhya Pradesh": 5.6,
  "Maharashtra": 5.7,
  "Manipur": 5.0,
  "Meghalaya": 4.9,
  "Mizoram": 5.0,
  "Nagaland": 5.0,
  "Odisha": 5.4,
  "Punjab": 5.6,
  "Rajasthan": 6.2,
  "Sikkim": 5.0,
  "Tamil Nadu": 5.8,
  "Telangana": 5.4,
  "Tripura": 5.0,
  "Uttar Pradesh": 5.4,
  "Uttarakhand": 5.3,
  "West Bengal": 5.1
}

# A-> Area of solar panels in m2: to be entered by user
# r-> Solar Panel Yield: dependent on type of panel
# state -> used to calculate H-> avg annual solar radiation in kWh/m2
# eta -> effeciency of solar installation: assumed by us
# function gives output in kWh
def calcEnergyOutput(A,r,state,eta):
    return (float(A[0])*r*float(kWhperm2[state])*eta)

# latitude -> latitude
# d -> day of the year. eg. Feb 4 = 35 
def calcAzimuth(latitude, d):
    return ( 90 - latitude + (23.45)*np.sin(360/365*(284+d)))

# Sh -> calculated using function calcEnergyOutput
# theta -> azimuth, calculated using calcAzimuth function
# beta -> angle of solar panel with ground: to be entered by user
def calcActualOutput(Sh, theta, beta):
    return Sh*np.sin(np.radians(theta+beta))/np.sin(np.radians(theta))

# gives day of year when you enter year month and day 
def calcDayOfYear(year, month, day):
    x = datetime.datetime(year, month, day)
    return x.timetuple().tm_yday

# rateOfBillGrowth => [0,1]
def returnPlot2(costOfInstall, currElecBill, rateOfBillGrowth):

    cummBill = list()
    
    cummBill = [0] * 20
    cummBill[0] = currElecBill
    crossPoint = 0
    for i in range(1,20):
        cummBill[i] = (1+rateOfBillGrowth)*cummBill[i-1]
    
    for i in range(1,20):
        cummBill[i] += cummBill[i-1]
        if (cummBill[i] > costOfInstall) and (crossPoint == 0):
            crossPoint = i
    
    plt.figure(figsize=(10,6))  # CHANGE TO GET PREFERRED SIZE
    # plt.title("SAVINGS PLOT", fontsize=20)  
    marks = [crossPoint]
    plt.plot(np.arange(0,20), cummBill, "-rD", markevery=marks)
    plt.axhline(y=costOfInstall, color='g')
    plt.ylabel("Cost(INR)")
    plt.legend(['Cummulative Electricity Bill Cost', 'Initial Solar Investment'])
    plt.text(crossPoint + 0.5, cummBill[crossPoint] - 6000, f"You recoup the investment atleast by {crossPoint} years", 
                    color='g', fontsize=8, style='italic')
    plt.savefig('static/pictures/output_2.png', bbox_inches='tight', pad_inches=.1)   # keep some padding cuz it ensures whole fig comes

    return crossPoint

def returnEnergyPlot(A,r,eta):
    
    dayNo = 1
    sunData = 5.80
    sunDataList = list()    # defining the array
    # JANUARY
    for i in range(20):
        sunData = 5.80 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(10):
        sunData = 6.46 + (random.random()/1.5)*-1
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    # FEBRUARY
    for i in range(21):
        sunData = 6.46 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(7):
        sunData = 6.83 + (random.random()/1.5)*-1
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    # MARCH
    for i in range(24):
        sunData = 6.83 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(7):
        sunData = 6.24 + (random.random()/1.5)
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    # APRIL
    for i in range(23):
        sunData = 6.24 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(7):
        sunData = 5.57 + (random.random()/1.5)
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    # MAY
    for i in range(22):
        sunData = 5.57 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(9):
        sunData = 4.83 + (random.random()/1.5)
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    # JUNE
    for i in range(23):
        sunData = 4.83 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(7):
        sunData = 4.91 + (random.random()/1.5)*-1
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)

    # JULY
    for i in range(24):
        sunData = 4.91 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(7):
        sunData = 5.26 + (random.random()/1.5)*-1
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    # AUGUST
    for i in range(24):
        sunData = 5.26 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(7):
        sunData = 5.74 + (random.random()/1.5)*-1
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    # SEPTEMBER
    for i in range(23):
        sunData = 5.74 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(7):
        sunData = 5.24 + (random.random()/1.5)
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    # OCTOBER
    for i in range(24):
        sunData = 5.24 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(7):
        sunData = 4.94 + (random.random()/1.5)
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    # NOVEMBER
    for i in range(23):
        sunData = 4.94 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(7):
        sunData = 5.30 + (random.random()/1.5)*-1
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    # DECEMBER
    for i in range(22):
        sunData = 5.30 + (random.random()/4)*random.choice([1,-1])  # adds or subs unto 0.25
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)
    
    for i in range(9):
        sunData = 5.8 + (random.random()/1.5)
        dayNo+=1
        sunDataList.append(sunData* A * r * eta)

    plt.figure(figsize=(10,6))  # CHANGE TO GET PREFERRED SIZE
    # plt.title("DAILY SOLAR ENERGY PRODUCTION", fontsize=20)  

    plt.ylabel("Potential for Energy Production (kWh)")
    plt.xticks(np.arange(15,365,30), ['January', 'February', 'March', 'April', 'May',
                                'June', 'July', 'August', 'September', 'October',
                                'November', 'December'], rotation=30) 
    plt.plot(np.arange(1,365), sunDataList, color ="green")
    if(A<=7 and A>=3.5):
        plt.axhspan(2, 3, color='y', alpha=0.2, lw=0)
        plt.text(185, 2.03, "Avg electricity consumption per household ranges between 2-3kWh", 
                    color='g', fontsize=8, style='italic')
    elif(A<3.5):
        plt.axhspan(2, 3, color='y', alpha=0.2, lw=0)
        plt.text(145, 2.97, "Avg electricity consumption per household ranges between 2-3kWh", 
                    color='g', fontsize=8, style='italic')

    plt.savefig('static/pictures/output_1.png', bbox_inches='tight', pad_inches=.1)   # keep some padding cuz it ensures whole fig comes