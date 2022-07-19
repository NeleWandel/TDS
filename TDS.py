#!/usr/bin/env python

import pyvisa
import time
import sys

rm = pyvisa.ResourceManager()
print(rm.list_resources())
tds = rm.open_resource('GPIB0::1::INSTR')

channel = 1
math = 1
m = 1

def Channel(channelnumber):
    if channelnumber >= 1 and channelnumber <= 4:
        global channel
        channel = str(channelnumber)
        tds.write('TRIGger:A:COMMunication:SOUrce CH' + str(channel))
        return
    else:
        sys.exit('Error: Selected channel can only be 1, 2, 3 or 4.')
        
def Identify():
    print(tds.query("*IDN?"))

def AutoSet():
    tds.write('AUTOSet EXECute')

def Undo():
    tds.write('AUTOSet UNDo')

def Clear():
    tds.write('*CLS')
    
def IsDone():
    tds.query('*OPC')
    tds.query('*OPC?')
    
def Wait():
    tds.write('*WAI')

def Calibration():
    print(tds.write('*CAL?'))

def DefineTrigger(trigger):
    tds.write('*DDT ' + str(trigger))

def Recall(storagelocation):
    if storagelocation >= 0 and storagelocation <= 10:
        tds.write('*RCL ' + str(storagelocation))
        return
    else:
        sys.exit('Error: Storage Location must range from 0 through 10.')

def Save(storagelocation):
    if storagelocation >= 0 and storagelocation <= 10:
        tds.write('*SAV ' + str(storagelocation))
        print('Current state of the oscilloscope was saved to location' + str(storagelocation))
        return
    else:
        sys.exit('Error: Storage Location must range from 0 through 10.')

def ResetToFactorySettings():
    tds.write('*RST')
    
def Trigger():
    tds.write('*TRG')

def ActivateSampleMode():
    tds.query('ACQuire:MODe SAMple')
def ActivatePeakDetect():
    tds.query('ACQuire:MODe PEAKdetect')
def ActivateHiRes():
    tds.query('ACQuire:MODe HIRes')
def ActivateAveraging(WFamount):
    tds.query('ACQuire:NUMAVg ' + str(WFamount))
    tds.query('ACQuire:MODe AVErage')
def ActivateEnvelopeMode(WFamount):
    tds.query('ACQuire:NUMENv' + str(WFamount))
    tds.query('ACQuire:MODe ENVelope')
def ActivateWFMDBMode():
    tds.query('ACQuire:MODE WFMDB')

def ModeInfo():
    tds.query('ACQuire:MODe?')

def SetSampleSize(pointamount):
    tds.query('ACQuire:NUMSAMples ' + str(pointamount))


#sampling modes
def SetRealTimeSampling():
    tds.query('ACQuire:SAMPlingmode RT')

def SetInterpolatedSampling():
    tds.query('ACQuire:SAMPlingmode IT')

def SetEquivalentTimeSampling():
    tds.query('ACQuire:SAMPlingmode ET')


#start/stop acquisition
def StartAcquisition():
    tds.query('ACQuire:STATE RUN')

def StopAcquisition():
    tds.query('ACQuire:STATE STOP')

def AcquisitionState():
    if tds.query('ACQuire:STATE?') == ':ACQUIRE:STATE 0':
        return(0)
    else:
        return(1)
   
def Single():
    tds.query('ACQuire:STOPAfter SEQuence')

def Continually():
    tds.query('ACQuire:STOPAfter RUNSTop')

def Busy():
    tds.query('BUSY?')

def ProbeCalibration():
    tds.query('CALibrate:CALProbe:CH' + str(channel) + '?')
    data = tds.read_raw()
    if data == str(1):
        print('Probe calibration in progress.')
        while data == str(1):
            time.sleep(1)
            data = tds.read_raw()
            if data == str(0):
                print('Probe calibration done for Channel ' + str(channel))
                return
            if data == str(-1):
                print('Probe calibration for Channel ' + str(channel) + ' failed.')
                sys.exit('Programm was terminated because of failed command.')
    else:
        sys.exit('Error: Programm was terminated because of failed command.') 
    
def ProbeCalibration2():
    tds.query('CALibrate:CALProbe:CH' + str(channel) + '?')
    data = tds.query('CALibrate:PROBEstate:CH' + str(channel) + '?')
    if data == ':CALIBRATE:PROBESTATE:CH' + str(channel) + ' 1' or data == ':CALIBRATE:PROBESTATE:CH' + str(channel) + ' 2':
        print('Probe calibration initialized.')
        while data == ':CALIBRATE:PROBESTATE:CH' + str(channel) + ' 1' or data == ':CALIBRATE:PROBESTATE:CH' + str(channel) + ' 2':
            time.sleep(1)
            data = tds.query('CALibrate:PROBEstate:CH' + str(channel) + '?')
            if data == ':CALIBRATE:PROBESTATE:CH' + str(channel) + ' 0':
                print('Probe calibration done for Channel ' + str(channel))
                return
            if data == ':CALIBRATE:PROBESTATE:CH' + str(channel) + ' -1':
                print('Probe calibration for Channel ' + str(channel) + ' failed.')
                sys.exit('Programm was terminated because of failed command.')
    else:
        sys.exit('Error: Programm was terminated because of failed command.')
        return
    return

def ChannelOffset(offsetinmV):
    offset = float(offsetinmV)
    off="{:.2f}".format(offset)
    tds.query('CH'+ str(channel)+ ':OFFSet ' + str(off) + 'E-03')
    
def Date():
    tds.query('DATE?')
    
def SetDate(day, month, year):
    tds.write('DATE "' + str(year) + '-' + str(month) + '-' + str(day) +'"')
    
def Export():
    tds.write('EXPort STArt')
    
def ExportFilePath(path):
    tds.query('EXPort:FILEName "' + str(path) + '"')

def ExportFileFormat(ff):
    if ff == 'BMP':
        tds.write('EXPort:FORMat BMP')
        return
    if ff == 'JPEG':
        tds.write('EXPort:FORMat JPEG')
        return
    if ff == 'PNG':
        tds.write('EXPort:FORMat PNG')
        return
    else:
        sys.exit('Error: File format wrong. Please choose between BMP, JPEG and PNG')
        return
    
def Print():
    tds.write('HARDCopy STArt\n*WAI\n')
                 
def PrintFilePath(path):
    tds.write('HARDCopy:FILEName "' + str(path) + '"')
                 
def Lock():
    tds.write('LOCk')  
def Unlock():
    tds.write('UNLock')

def AutoAdjustMaskOn():
    tds.write('MASK:AUTOAdjust ON')
def AutoAdjustMaskOff():
    tds.write('MASK:AUTOAdjust OFF')

def SetMathStorage(number):
    global math 
    math = number
    print('All future Math commands will save in Math ' + str(math))
    
def MathDefinition():
    tds.query('MATH' + str(channel) + ':DEFine?')

def DefineMath(equation):
    tds.query('MATH' + str(math) + ':DEFine "' + str(equation) + '"')
    
def SetMathPos(y):
    tds.write('MATH' + str(math) + ':POSition ' + str(y) + 'E+00')

#in mV
def SetMathScale(x):
    tds.write('MATH' + str(math) + ':SCAle ' + str(x) + 'E-03')
    
def ShowMathPos():
    tds.write('MATH' + str(math) + ':POSition?')
    
def ShowMathScale():
    tds.write('MATH' + str(math) + ':SCAle?')
    
def DefineMathVariable(varnumber, varvalue):
    if varnumber >= 1 or varnumber <= 8:
        tds.write('MATHVAR:VAR'+ str(varnumber) + ' ' + str(varvalue))
        return
    else:
        sys.exit('Error: Variable Number can only range from 1 through 8.')
        return

def ShowAllMeasPara():
    tds.query('MEASUrement?')
    
def ShowImmediateMeasPara():
    tds.query('MEASUrement:IMMed?')


def MeasImmediateDelayDirect(direction):
    if direction == 1:
        tds.write('MEASUrement:IMMed:DELay:DIREction FORWards')
        return
    if direction == 2:
        tds.write('MEASUrement:IMMed:DELay:DIREction BACKWards')
        return
    else:
        sys.exit('Error: Measurement immediate delay direction can only be 1 (forwards) or 2 (backwards)')
        return

def MeasImmediateDelayEdge1(edge):
    if edge == 1:
        tds.write('MEASUrement:IMMed:DELay:EDGE[1] RISe')
        return
    if edge == 2:
        tds.write('MEASUrement:IMMed:DELay:EDGE[1] FALL')
        return
    else:
        sys.exit('Error: Measurement immediate delay edge 1 can only be 1 (rising edge) or 2 (falling edge)')
        return
    
def MeasImmediateDelayEdge2(edge):
    if edge == 1:
        tds.write('MEASUrement:IMMed:DELay:EDGE[2] RISe')
        return
    if edge == 2:
        tds.write('MEASUrement:IMMed:DELay:EDGE[2] FALL')
        return
    else:
        sys.exit('Error: Measurement immediate delay edge 2 can only be 1 (rising edge) or 2 (falling edge)')
        return
 
def ImmediateRefIsAbsolute():
    tds.query('MEASUrement:IMMed:REFLevel:METHod ABSolute')

def ImmediateRefIsPercent():
    tds.query('MEASUrement:IMMed:REFLevel:METHod PERCent')
    
def ImmediateSetHighRefAbsolute(volt):
    tds.query('MEASUrement:IMMed:REFLevel:ABSolute:HIGH ' + str(volt))
    
def ImmediateSetLowRefAbsolute(volt):
    tds.query('MEASUrement:IMMed:REFLevel:ABSolute:LOW ' + str(volt))
    
def ImmediateSetMidRefAbsolute(volt):
    tds.query('MEASUrement:IMMed:REFLevel:ABSolute:MID[1]' + str(volt))
    
def ImmediateSetHighRefPercent(percent):
    tds.query('MEASUrement:IMMed:REFLevel:PERCent:HIGH ' + str(percent))
    
def ImmediateSetLowRefPercent(percent):
    tds.query('MEASUrement:IMMed:REFLevel:PERCent:LOW ' + str(percent))
    
def ImmediateSetMidRefPercent(percent):
    tds.query('MEASUrement:IMMed:REFLevel:PERCent:MID[1]' + str(percent))
    
def ImmediateChannelAsSource():
    tds.query('MEASUrement:IMMed:SOURCE[1] CH' + str(channel))
def ImmediateMathAsSource():
    tds.query('MEASUrement:IMMed:SOURCE[1] MATH' + str(math))
def ImmediateRefAsSource(waveform):
    tds.query('MEASUrement:IMMed:SOURCE[1] REF' + str(waveform))
def ImmediateHistogramAsSource():
    tds.query('MEASUrement:IMMed:SOURCE[1] HIStogram')
    
def SetImmediateMeasType(argument):
    tds.query('MEASUrement:IMMed:TYPE ' + str(argument))
    
def ImmediateValue():
    tds.query('MEASUrement:IMMed:VALue?')
    
def ImmediateUnit():
    tds.query('MEASUrement:IMMed:UNIts?')

def ShowMeasuremetPara(x):
    if x >= 1 and x <= 8:
        print(tds.query('MEASUrement:MEAS' + str(x) + '?'))
        return
    else:
        sys.exit('Error: Measurement can only be specified to 1 through 8.')
        return

def UseMeasurement(x):
    global m
    m = str(x)
    
def CountMeasures(x):
    if x >= 1 and x <= 8:
        ptds.query('MEASUrement:MEAS' + str(x) + ':COUNt?')
        return
    else:
        sys.exit('Error: Measurement can only be specified to 1 through 8.')
        return
    
def MeasDelayDirect(direction):
    if direction == 1:
        tds.write('MEASUrement:MEAS' + str(m) + ':DELay:DIREction FORWards')
        return
    if direction == 2:
        tds.write('MEASUrement:MEAS' + str(m) + ':DELay:DIREction BACKWards')
        return
    else:
        sys.exit('Error: Measurement immediate delay direction can only be 1 (forwards) or 2 (backwards)')
        return

def MeasDelayEdge1(edge):
    if edge == 1:
        tds.write('MEASUrement:MEAS' + str(m) + ':DELay:EDGE[1] RISe')
        return
    if edge == 2:
        tds.write('MEASUrement:MEAS' + str(m) + ':DELay:EDGE[1] FALL')
        return
    else:
        sys.exit('Error: Measurement immediate delay edge 1 can only be 1 (rising edge) or 2 (falling edge)')
        return
    
def MeasDelayEdge2(edge):
    if edge == 1:
        tds.write('MEASUrement:MEAS' + str(m) + ':DELay:EDGE[2] RISe')
        return
    if edge == 2:
        tds.write('MEASUrement:IMMed:DELay:EDGE[2] FALL')
        return
    else:
        sys.exit('Error: Measurement immediate delay edge 2 can only be 1 (rising edge) or 2 (falling edge)')
        return

def Maximum():
    tds.query('MEASUrement:MEAS' + str(m) + ':MAXimum?')
def Mean():
    tds.query('MEASUrement:MEAS' + str(m) + ':MEAN?')
def Minimum():
    tds.query('MEASUrement:MEAS' + str(m) + ':MINImum?')
    
def RefIsAbsolute():
    tds.query('MEASUrement:MEAS' + str(m) + ':REFLevel:METHod ABSolute')
def RefIsPercent():
    tds.query('MEASUrement:MEAS' + str(m) + ':REFLevel:METHod PERCent')
    
def SetHighRefAbsolute(volt):
    tds.query('MEASUrement:MEAS' + str(m) + ':REFLevel:ABSolute:HIGH ' + str(volt))
def SetLowRefAbsolute(volt):
    tds.query('MEASUrement:MEAS' + str(m) + ':REFLevel:ABSolute:LOW ' + str(volt))    
def SetMidRefAbsolute(volt):
    tds.query('MEASUrement:MEAS' + str(m) + ':REFLevel:ABSolute:MID[1]' + str(volt))
    
def SetHighRefPercent(percent):
    tds.query('MEASUrement:MEAS' + str(m) + ':REFLevel:PERCent:HIGH ' + str(percent))   
def SetLowRefPercent(percent):
    tds.query('MEASUrement:MEAS' + str(m) + ':REFLevel:PERCent:LOW ' + str(percent))   
def SetMidRefPercent(percent):
    tds.query('MEASUrement:MEAS' + str(m) + ':REFLevel:PERCent:MID[1]' + str(percent))
    
def ChannelAsSource():
    tds.query('MEASUrement:MEAS' + str(m) + ':SOURCE[1] CH' + str(channel))
def MathAsSource():
    tds.query('MEASUrement:MEAS' + str(m) + ':SOURCE[1] MATH' + str(math))
def RefAsSource(waveform):
    tds.query('MEASUrement:MEAS' + str(m) + ':SOURCE[1] REF' + str(waveform))
def HistogramAsSource():
    tds.query('MEASUrement:MEAS' + str(m) + ':SOURCE[1] HIStogram')
    
def DisableCalcAndDisplay():
    tds.write('MEASUrement:MEAS' + str(m) + ':STATE OFF')
def EnableCalcAndDisplay():
    tds.write('MEASUrement:MEAS' + str(m) + ':STATE ON')    
    
def SetMeasType(argument):
    tds.query('MEASUrement:MEAS' + str(m) + ':TYPE ' + str(argument))
    
def Value():
    tds.query('MEASUrement:MEAS' + str(m) + ':VALue?')
def Unit():
    tds.query('MEASUrement:MEAS' + str(m) + ':UNIts?')
    
def StanDeviation():
    tds.query('MEASUrement:MEAS' + str(m) + ':STDdev?')
    
def ResetStatistics():
    tds.query('MEASUrement:STATIstics:COUNt RESET')
    
def Level():
    tds.write('TRIGger:A SETLevel')
    
def PulseFormPlusOne():
    tds.write('TRIGger:A:COMMunication:AMI:PULSEForm PLUSOne')
def PulseFormMinusOne():
    tds.write('TRIGger:A:COMMunication:AMI:PULSEForm MINUSOne')
def PulseFormExeDiagram():
    tds.write('TRIGger:A:COMMunication:AMI:PULSEForm EYEDiagram')
    
def SetThresholdHigh(volt):
    tds.query('TRIGger:A:COMMunication:AMI:THReshold:HIGH ' + str(volt) + ' E-2')
def SetThresholdLow(volt):
    tds.query('TRIGger:A:COMMunication:AMI:THReshold:LOW ' + str(volt) + ' E-2')
    
def SetBitrate(rate):
    tds.query('TRIGger:A:COMMunication:BITRate ' + stre(rate))
    
def CMIPulseFormPlusOne():
    tds.write('TRIGger:A:COMMunication:CMI:PULSEForm PLUSOne')
def CMIPulseFormMinusOne():
    tds.write('TRIGger:A:COMMunication:CMI:PULSEForm MINUSOne')
def CMIPulseFormExeDiagram():
    tds.write('TRIGger:A:COMMunication:CMI:PULSEForm EYEDiagram') 
def CMIPulseFormZero():
    tds.write('TRIGger:A:COMMunication:CMI:PULSEForm ZERO')
    
def ClockPolarityRise():
    tds.write('TRIGger:A:COMMunication:CLOCK:POLARITY RISE')
def ClockPolarityFall():
    tds.write('TRIGger:A:COMMunication:CLOCK:POLARITY FALL')
    
def TriggerSourceChannel(ch):
    tds.write('TRIGger:A:COMMunication:SOUrce CH' + str(ch))
    
def TriggerAutoHoldoffTime():
    tds.write('TRIGger:A:HOLDoff:BY AUTO')
#range 250ns through 12s
def TriggerSetHoldoffTime(time):
    tds.write('TRIGger:A:HOLDoff:BY TIMe')
    tds.write('TRIGger:A:HOLDoff:TIMe')
    
def TriggerLogic(logic):
    tds.write('TRIGger:A:LOGIc:FUNCtion ' + str(logic))
    
def WaitForTrigger():
    tds.query('TRIGger:A:MODe NORMal')