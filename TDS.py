import pyvisa
import time
import sys

ch = 1
mathvari = 1
meas = 1

def Channel(channelnumber):
    if channelnumber >= 1 and channelnumber <= 4:
        global ch
        ch = str(channelnumber)
        tds.write('TRIGger:A:COMMunication:SOUrce CH' + str(ch))
        return
    else:
        raise ValueError('Selected channel can only be 1, 2, 3 or 4.')
       
def Header(status='off'):
    if status == 'off':
        tds.write('HDR OFF')
    elif status == 'on':
        tds.write('HDR ON')

def Identify():
    tds.query("*IDN?")

def AutoSet():
    tds.write('AUTOSet EXECute')

def Undo():
    tds.write('AUTOSet UNDo')

def Clear():
    tds.write('*CLS')

def IsDone():
    tds.query('*OPC?')

def Wait():
    tds.write('*WAI')

def Calibration():
    print(tds.write('*CAL?'))

def Recall(storagelocation):
    if storagelocation >= 0 and storagelocation <= 10:
        tds.write('*RCL ' + str(storagelocation))
        return
    else:
        raise ValueError('Storage Location must range from 0 through 10.')

def Save(storagelocation):
    if storagelocation >= 0 and storagelocation <= 10:
        tds.write('*SAV ' + str(storagelocation))
        print('Current state of the oscilloscope was saved to location' + str(storagelocation))
        return
    else:
        raise ValueError('Storage Location must range from 0 through 10.')

def ResetToFactorySettings():
    tds.write('*RST')

def Trig():
    tds.write('*TRG')
    
def Acquisition(acquiremode=None, samplesize=None, WFamount=None, mode=None, stop=None, fast=None):
    if acquiremode:
        if acquiremode == 'sampling':
            tds.write('ACQuire:MODe SAMple')
        elif acquiremode == 'peakdetect':
            tds.write('ACQuire:MODe PEAKdetect') 
        elif acquiremode == 'hires':
            tds.write('ACQuire:MODe HIRes')
        elif acquiremode == 'averaging':
            tds.write('ACQuire:MODe AVErage')
            if WFamount:
                tds.write('ACQuire:NUMAVg ' + str(WFamount))
        elif acquiremode == 'envelope':
            tds.write('ACQuire:MODe ENVelope')
            if WFamount:
                tds.write('ACQuire:NUMENv' + str(WFamount))
        elif acquiremode == 'wfmdb':
            tds.write('ACQuire:MODE WFMDB')
        else:
            raise ValueError('acquiremode must be sampling, peakdetect, hires, averaging, envelope or wfmdb')
    if mode:
        tds.write('ACQuire:SAMPlingmode ' + str(mode)) #RT, IT, ET
    if samplesize:
        tds.write('ACQuire:NUMSAMples ' + str(samplesize)) 
    if stop:
        if stop == 'single':
            tds.query('ACQuire:STOPAfter SEQuence')
        elif stop == 'repeat':
            tds.query('ACQuire:STOPAfter RUNSTop')  
    if fast:
        if fast == 'on':
            tds.write('FASTAcq:STATE ON')
        elif fast == 'off':
            tds.write('FASTAcq:STATE OFF')
        else:
            raise ValueError('Fast only has two valid states: on/off.')
    
def StartAcquisition():
    tds.write('ACQuire:STATE RUN')

def StopAcquisition():
    tds.write('ACQuire:STATE STOP')

def Busy():
    tds.query('BUSY?')

def ProbeCalibration(channel=ch):
    tds.query('CALibrate:CALProbe:CH' + str(channel) + '?')

def ChannelOffset(offsetinmV, channel=ch):
    offset = float(offsetinmV)
    off="{:.2f}".format(offset)
    tds.query('CH'+ str(channel)+ ':OFFSet ' + str(off) + 'E-03')

def Date():
    tds.query('DATE?')
    
def SetDate(day='01', month='01', year='2000'):
    tds.write('DATE "' + str(year) + '-' + str(month) + '-' + str(day) +'"')
    
def Export(filename=None, fileformat=None, inksaver=None, palette=None, fullscreen=None):
    if filename:
        tds.query('EXPort:FILEName "' + str(path) + '"')
    if fileformat:
        if fileformat == 'BMP':
            tds.write('EXPort:FORMat BMP')
        elif fileformat == 'JPEG':
            tds.write('EXPort:FORMat JPEG')
        elif fileformat == 'PNG':
            tds.write('EXPort:FORMat PNG')
        else:
            raise TypeError('File format wrong. Please choose between BMP, JPEG and PNG')
    if inksaver:
        if inksaver == 1:
            tds.write('EXPort:IMAGe NORMal')
        elif inksaver == 2:
            tds.write('EXPort:IMAGe INKSaver')
        elif inksaver == 3:
            tds.write('EXPort:IMAGe ENHANcedwfm')  
    if palette:
        if palette == 'color':
            tds.write('EXPort:PALEtte COLOr')
        elif palette == 'gray':
            tds.write('EXPort:PALEtte GRAYscale')
        elif palette == 'baw':
            tds.write('EXPort:PALEtte BLACKANDWhite')
    if fullscreen:
        if fullscreen == 'off':
            tds.write('EXPort:VIEW GRAticule')
        elif fullscreen == 'on':
            tds.write('EXPort:VIEW FULLSCREEN')        
    tds.write('EXPort STArt')

def Screenshot(filename=None, inksaver=None, palette=None, orientation=None, fullscreen=None):
    if orientation:
        if orientation == 1:
            tds.write('HARDCopy:LAYout PORTRait')
        elif orientation == 2:
            tds.write('HARDCopy:LAYout LANDscape')
    if filename:
        tds.write('HARDCopy:FILEName "' + str(filename) + '"')
    if fullscreen:
        if fullscreen == 'off':
            tds.write('HARDCopy:VIEW GRAticule')
        elif fullscreen == 'on':
            tds.write('HARDCopy:VIEW FULLSCREEN')
    if palette:
        if palette == 'color':
            tds.write('HARDCopy:PALEtte COLOr')
        elif palette == 'gray':
            tds.write('HARDCopy:PALEtte GRAYscale')
        elif palette == 'baw':
            tds.write('HARDCopy:PALEtte BLACKANDWhite')
    if inksaver:
        if inksaver == 1:
            tds.write('HARDCopy:IMAGe NORMal')
        elif inksaver == 2:
            tds.write('HARDCopy:IMAGe INKSaver')
        elif inksaver == 3:
            tds.write('HARDCopy:IMAGe ENHANcedwfm')    
    tds.write('HARDCopy STArt')
                 
def Lock():
    tds.write('LOCk ALL')  
def Unlock():
    tds.write('UNLock ALL')

def Mask(start=True, mask=None, source=None, display=None, counting=None, wfmamount=None,
         highlights=None, inverted=None, margin=None, polatity=None, stoponfailure=None, failthreshold=None, failscreen=None, 
         logfail=None, logwfm=None, repeat=None, delay=None, auto=None, hdelta=None, vdelta=None, digitalfilter=None, 
         beep=None, failbeep=None):
    if mask:
        tds.write('MASK:STANdard ' + str(mask))
    if source:
        tds.write('MASK:SOUrce ' + str(source))
    if display:
        tds.write('MASK:DISplay ' + str(display))
    if counting:
        tds.write('MASK:COUNt:STATE ' + str(counting))
    if highlights:
        tds.write('MASK:HIGHLIGHTHits ' + str(highlights))
    if digitalfilter:
        tds.write('MASK:FILTer ' + str(digitalfilter))
    if failthreshold:
        tds.write('MASK:TESt:SAMple:THReshold ' + str(failthreshold))
        tds.write('MASK:TESt:THReshold ' + str(failthreshold))
    if wfmamount:
        tds.write('MASK:TESt:WAVEform ' + str(wfmamount))
    if failscreen:
        tds.write('MASK:TESt:HARDCOPY ' + str(failscreen))
    if logfail:
        tds.write('MASK:TESt:LOG:FAILure ' + str(logfail))
    if logwfm:
        tds.write('MASK:TESt:SAVEWFM ' + str(logwfm))
    if repeat:
        tds.write('MASK:TESt:REPeat ' + str(repeat))
    if delay:
        tds.write('MASK:TEST:DELay ' + str(delay))
    if margin:
        tds.write('MASK:MARgin:STATE ON')
        tds.write('MASK:MARgin:PERCent ' + str(margin)) #range -50 to +50
    else:
        tds.write('MASK:MARgin:STATE OFF')
    if auto == 'ON':
        if hdelta:
            tds.write('MASK:AUTOAdjust:HDELTA ' + str(hdelta))
        if vdelta:
            tds.write('MASK:AUTOAdjust:VDELTA ' + str(vdelta))
    if auto:
        tds.write('MASK:AUTOAdjust ' + str(auto))
    if inverted:
        tds.write('MASK:INVert ' + str(inverted))
    if beep:
        tds.write('MASK:TESt:BEEP:COMPLetion ' + str(beep))
    if failbeep:
        tds.write('MASK:TESt:BEEP:FAILure ' + str(failbeep))
    if stoponfailure:
        tds.write('MASK:TESt:STOP:FAILure ' + str(stoponfailure))
    if start == True:
        tds.write('MASK:TESt:STATE ON')
        if polarity:
            if polarity == 'negative':
                tds.write('MASK:POLarity NEGAtive')
            elif polarity == 'positive':
                tds.write('MASK:POLarity POSITIVe')
            elif polarity == 'both':
                tds.write('MASK:POLarity BOTh')
            else:
                raise ValueError('Maks polarity may only be 0 (negative), 1 (positive) or 2 (both).')
    else:
        tds.write('MASK:TESt:STATE OFF')
    
def UserMask(seg=None, points=None, amp=None, bit=None, hscale=None, htrigpos=None, patbits=None, 
             presampbits=None, reclength=None, serialtrig=None, trigtosamp=None, voffset=None, vpos=None, vscale=None, width=None):
    if seg:
        if points:
            tds.write('MASK:USER:SEG' + str(seg) + ':POINTS ' + str(points))
    if amp:
        tds.write('MASK:USER:ASMPlitude ' + str(amp))
    if bit:
        tds.write('MASK:USER:BITRate ' + str(bit))
    if hscale:
        tds.write('MASK:USER:HSCAle ' + str(hscale))
    if htrigpos:
        tds.write('MASK:USER:HTRIGPOS ' + str(htrigpos)) #0.0 to 1.0
    if patbits:
        tds.write('MASK:USER:PATTERNBITS ' + str(patbits))
    if presampbits:
        tds.write('MASK:USER:PRESAMPBITS ' + str(presampbits))
    if reclength:
        tds.write('MASK:USER:RECOrdlength ' + str(reclength))
    if serialtrig:
        tds.write('MASK:USER:SERIALTRIG ' + str(serialtrig))
    if trigtosamp:
        tds.write('MASK:USER:TRIGTOSAMP ' + str(trigtosamp))
    if voffset:
        tds.write('MASK:USER:VOFFSet ' + str(voffset))
    if vpos:
        tds.write('MASK:USER:VPOS ' + str(vpos))
    if vscale:
        tds.write('MASK:USER:VSCAle ' + str(vscale))
    if width:
        tds.write('MASK:USER:WIDth' + str(width))
        
def DeleteUserMaskSeg(seg):
    tds.write('MASK:USER:SEG' + str(seg) + ' DELETE')
    
def MaskHit():
    tds.query('MASK:COUNt:TOTal?')
    
def ResetMaskHit():
    tds.write('MASK:COUNt:RESET')

def SetMathStorage(number):
    global mathvari
    mathvari = number
    
def MathVariable(varnumber, varvalue):
    if varnumber >= 1 or varnumber <= 8:
        tds.write('MATHVAR:VAR'+ str(varnumber) + ' ' + str(varvalue))
    else:
        raise ValueError('Variable Number can only range from 1 through 8.')

def Math(math=mathvari, equation=None, y=None, x=None):
    if equation:
        tds.write('MATH' + str(math) + ':DEFine "' + str(equation) + '"')
    if y:
        tds.write('MATH' + str(math) + ':POSition ' + str(y))
    if x:
        tds.write('MATH' + str(math) + ':SCAle ' + str(x))
        
def AllMeasPara():
    tds.query('MEASUrement?')
    
def ImmedMeasPara():
    tds.query('MEASUrement:IMMed?')
    
def ImmedValue():
    tds.query('MEASUrement:IMMed:VALue?')
    
def ImmedUnit():
    tds.query('MEASUrement:IMMed:UNIts?')
    
def ImmedMeasure(m=meas, statistics=None, meastype=None, source=None, source2=None, refmethod=None, 
            high=None, low=None, mid=None, delay=None, edge1=None, edge2=None):
    if source:
        tds.write('MEASUrement:IMMed:SOURCE[1] ' + str(source))
    if source2:
        tds.write('MEASUrement:IMMed:SOURCE[2] ' + str(source))
    if refmethod:
        if refmethod == 'percent':
            if high:
                tds.write('MEASUrement:IMMed:REFLevel:PERCent:HIGH ' + str(high))
            if low:
                tds.write('MEASUrement:IMMed:REFLevel:PERCent:LOW ' + str(low)) 
            if mid:
                tds.write('MEASUrement:IMMed:REFLevel:PERCent:MID[1]' + str(mid))
        if refmethod == 'absolute':
            if high:
                tds.write('MEASUrement:IMMed:REFLevel:ABSolute:HIGH ' + str(high))
            if low:
                tds.write('MEASUrement:IMMed:REFLevel:ABSolute:LOW ' + str(low))    
            if mid:
                tds.write('MEASUrement:IMMed:REFLevel:ABSolute:MID[1]' + str(mid))
    if delay:
        if delay == forwards:
            tds.write('MEASUrement:IMMed:DELay:DIREction FORWards')
        elif delay == backwards:
            tds.write('MEASUrement:IMMed:DELay:DIREction BACKWards')
    if edge1:
        if edge1 == 'rise':
            tds.write('MEASUrement:IMMed:DELay:EDGE[1] RISe')
        if edge1 == 'fall':
            tds.write('MEASUrement:IMMed:DELay:EDGE[1] FALL')
    if edge2:
        if egde2 == 'rise':
            tds.write('MEASUrement:IMMed:DELay:EDGE[2] RISe')
        if edge2 == 'fall':
            tds.write('MEASUrement:IMMed:DELay:EDGE[2] FALL')
    if meastype:
        tds.write('MEASUrement:IMMed:TYPE ' + str(argument)) 
    
def MeasPara(m=meas):
        tds.query('MEASUrement:MEAS' + str(m) + '?')

def GlobalMeas(x):
    global meas
    meas = str(x)
    
def CountMeas(m=meas):
    tds.query('MEASUrement:MEAS' + str(m) + ':COUNt?')

def Maximum(m=meas):
    tds.query('MEASUrement:MEAS' + str(m) + ':MAXimum?')
def Mean(m=meas):
    tds.query('MEASUrement:MEAS' + str(m) + ':MEAN?')
def Minimum(m=meas):
    tds.query('MEASUrement:MEAS' + str(m) + ':MINImum?')
    
def Measure(meastype=None, method=None, m=meas, statistics=None, weightvalue=None, state=None, source=None, source2=None, refmethod=None, 
            high=None, low=None, mid=None, delay=None, edge1=None, edge2=None):
    if source:
        tds.write('MEASUrement:MEAS' + str(m) + ':SOURCE[1] ' + str(source))
    if source2:
        tds.write('MEASUrement:MEAS' + str(m) + ':SOURCE[2] ' + str(source))
    if method:
        if method == 'histogram':
            tds.write('MEASUrement:METHod HIStogram')
        elif method == 'mean':
            tds.write('MEASUrement:METHod MEAN')
        elif method == 'minmax':
            tds.write('MEASUrement:METHod MINMax')
        else:
            raise ValueError('Measure method may only be histogram, mean or minmax')
    if delay:
        if delay == forwards:
            tds.write('MEASUrement:MEAS' + str(m) + ':DELay:DIREction FORWards')
        elif delay == backwards:
            tds.write('MEASUrement:MEAS' + str(m) + ':DELay:DIREction BACKWards')
    if edge1:
        if edge1 == 'rise':
            tds.write('MEASUrement:MEAS' + str(m) + ':DELay:EDGE[1] RISe')
        elif edge1 == 'fall':
            tds.write('MEASUrement:MEAS' + str(m) + ':DELay:EDGE[1] FALL')
    if edge2:
        if egde2 == 'rise':
            tds.write('MEASUrement:MEAS' + str(m) + ':DELay:EDGE[2] RISe')
        elif edge2 == 'fall':
            tds.write('MEASUrement:MEAS' + str(m) + ':DELay:EDGE[2] FALL')
    if refmethod:
        if refmethod == 'percent':
            if high:
                tds.write('MEASUrement:MEAS' + str(m) + ':REFLevel:PERCent:HIGH ' + str(high))
            if low:
                tds.write('MEASUrement:MEAS' + str(m) + ':REFLevel:PERCent:LOW ' + str(low)) 
            if mid:
                tds.write('MEASUrement:MEAS' + str(m) + ':REFLevel:PERCent:MID[1]' + str(mid))
        elif refmethod == 'absolute':
            if high:
                tds.write('MEASUrement:MEAS' + str(m) + ':REFLevel:ABSolute:HIGH ' + str(high))
            if low:
                tds.write('MEASUrement:MEAS' + str(m) + ':REFLevel:ABSolute:LOW ' + str(low))    
            if mid:
                tds.write('MEASUrement:MEAS' + str(m) + ':REFLevel:ABSolute:MID[1]' + str(mid))
    if meastype:
        tds.write('MEASUrement:MEAS' + str(m) + ':TYPE ' + str(argument)) 
    if statistics =='all':
        tds.write('MEASUrement:STATIstics:MODe ALL')
    elif statistics == 'off':
        tds.write('MEASUrement:STATIstics:MODe OFF')
    elif statistics == 'mean':
        tds.write('MEASUrement:STATistics:MODe VALUEMean')
    if weightvalue:
        tds.write('MEASUrement:STATIstics:WEIghting ' + str(weightvalue))
    if state:
        if state == 'off':
            tds.write('MEASUrement:MEAS' + str(m) + ':STATE OFF')   
        elif state == 'on':
            tds.write('MEASUrement:MEAS' + str(m) + ':STATE ON')

def MeasValue():
    tds.query('MEASUrement:MEAS' + str(m) + ':VALue?')
def MeasUnit():
    tds.query('MEASUrement:MEAS' + str(m) + ':UNIts?')
    
def StanDeviation():
    tds.query('MEASUrement:MEAS' + str(m) + ':STDdev?')
    
def ResetStatistics():
    tds.query('MEASUrement:STATIstics:COUNt RESET')
    
def TrigLevel():
    tds.write('TRIGger:A SETLevel')
    
def TriggerB(state=None, source=None, count=None, time=None, level=None, slope=None):
    tds.write('TRIGger:B:EDGE:COUPling ATRIGger')
    if source:
        if source == 'aux':
            tds.write('TRIGger:B:EDGE:SOUrce AUXiliary')
        else:
            tds.write('TRIGger:B:EDGE:SOUrce ') + str(source)
    if time:
        tds.write('TRIGger:B:BY TIMe')
        tds.write('TRIGger:B:TIMe ') + str(time)
    elif count:
        tds.write('TRIGger:B:BY EVENTS')
        tds.write('TRIGger:B:EVENTS:COUNt ') + str(count)
    if level:
        tds.write('TRIGger:B:LEVel ') + str(level)
    if slope:
        if slope == 'rise':
            tds.write('TRIGger:B:EDGE:SLOpe RISe')
        elif slope == 'fall':
            tds.write('TRIGger:B:EDGE:SLOpe FALL')  
    if state:
        tds.write('TRIGger:B:STATE ') + str(state)
    
def Trigger(triggertype=None, mode=None, holdhofftime=None, triggerclass=None, CH1=None, CH2=None, CH3=None, CH4=None, 
            function=None, triggerwhen=None, logicmin=None, logicmax=None, source=None, comm=None, bitrate=None, pulseform=None, eyetype=None, 
            clock=None, clocksource=None, polarity=None, clockthreshold=None, setholdsource=None, threshold=None, 
            settime=None, holdtime=None, width=None, low=None, high=None, edgecoupling=None, standard=None, level=None, 
            CH1TH=None, CH2TH=None, CH3TH=None, CH4TH=None, dataformat=None, datapattern=None, timeouttime=None, deltatime=None, transition=None):
    if mode:
        if mode == 'auto':
            tds.query('TRIGger:A:MODe AUTo')
        elif mode == 'normal':
            tds.query('TRIGger:A:MODe NORMal')
    if holdofftime:
        if holdofftime == 'auto':
            tds.write('TRIGger:A:HOLDoff:BY AUTO')
        elif holdofftime == 'random':
            tds.write('TRIGger:A:HOLDoff:BY RANDOM')
        else:
            tds.write('TRIGger:A:HOLDoff:BY TIMe')
            tds.write('TRIGger:A:HOLDoff:TIMe ' + str(holdofftime))        
    if triggertype:
        if triggertype == 'logic':
            tds.write('TRIGger:A:TYPe LOGIc')
            if CH1:
                tds.write('TRIGger:A:LOGIc:INPut:CH1 ' + str(CH1))
            if CH2:
                tds.write('TRIGger:A:LOGIc:INPut:CH2 ' + str(CH2))
            if CH3:
                tds.write('TRIGger:A:LOGIc:INPut:CH3 ' + str(CH3))
            if function:
                tds.write('TRIGger:A:LOGIc:FUNCtion ' + str(function))
            if CH1TH or CH2TH or CH3TH or CH4TH:
                if CH1TH:
                    tds.write('TRIGger:A:LOGIc:THReshold:CH1 ' + str(CH1TH))
                if CH2TH:
                    tds.write('TRIGger:A:LOGIc:THReshold:CH2 ' + str(CH2TH))
                if CH3TH:
                    tds.write('TRIGger:A:LOGIc:THReshold:CH3 ' + str(CH3TH))
                if CH4TH:
                    tds.write('TRIGger:A:LOGIc:THReshold:CH4 ' + str(CH4TH))
            if triggerclass:
                if triggerclass == 'pattern':
                    tds.write('TRIGger:A:LOGIc:CLAss PATtern')
                    if CH4:
                        tds.write('TRIGger:A:LOGIc:PATtern:INPut:CH4 ' + str(CH4))
                    if triggerwhen:
                        if triggerwhen == 'true':
                            tds.write('TRIGger:A:LOGIc:PATtern:WHEn TRUe')
                        elif triggerwhen == 'false':
                            tds.write('TRIGger:A:LOGIc:PATtern:WHEn FALSe')
                        elif triggerwhen == 'less':
                            tds.write('TRIGger:A:LOGIc:PATtern:WHEn LESSThan')
                        elif triggerwhen == 'more':
                            tds.write('TRIGger:A:LOGIc:PATtern:WHEn MOREThan')
                    if logicmax:
                        tds.write('TRIGger:A:LOGIc:PATtern:WHEn:LESSLimit ' + str(logicmax))
                    if logicmin:
                        tds.write('TRIGger:A:LOGIc:PATtern:WHEn:MORELimit ' + str(logicmin))
                if triggerclass == 'state':
                    tds.write('TRIGger:A:LOGIc:CLAss STATE')
                    if CH4:
                        if CH4 == 'fall':
                            tds.write('TRIGger:A:LOGIc:STATE:INPut:CH4 FALL')
                        if CH4 == 'rise':
                            tds.write('TRIGger:A:LOGIc:STATE:INPut:CH4 RISe')
                    if triggerwhen:
                        if triggerwhen == 'true':
                            tds.write('TRIGger:A:LOGIc:STATE:WHEn TRUe')
                        if triggerwhen == 'false':
                            tds.write('TRIGger:A:LOGIc:STATE:WHEn FALSe')
                if triggerclass == 'sethold':
                    tds.write('TRIGger:A:LOGIc:CLAss SETHold')
                    if setholdsource:
                        tds.write('TRIGger:A:LOGIc:SETHold:DATa:SOUrce CH' + str(setholdsource))
                    if clocksource:
                        tds.write('TRIGger:A:LOGIc:SETHold:CLOCk:SOUrce CH' + str(clocksource))
                    if clock:
                        if clock == 'fall':
                            tds.write('TRIGger:A:LOGIc:SETHold:CLOCk:EDGE FALL')
                        elif clock == 'rise':
                            tds.write('TRIGger:A:LOGIc:SETHold:CLOCk:EDGE RISe')
                    if clockthreshold:
                        tds.write('TRIGger:A:LOGIc:SETHold:CLOCk:THReshold ' + str(clockthreshold))
                    if threshold:
                        tds.write('TRIGger:A:LOGIc:SETHold:DATa:THReshold ' + str(threshold))
                    if settime:
                        tds.write('TRIGger:A:LOGIc:SETHold:SETTime ' + str(settime))
                    if holdtime:
                        tds.write('TRIGger:A:LOGIc:SETHold:HOLDTime ' + str(holdtime))       
        elif triggertype == 'comm':
            tds.write('TRIGger:A:TYPe COMM')
            if source:
                if source >=1 and source <= 4:
                    tds.write('TRIGger:A:COMMunication:SOUrce CH' + str(source))
                else:
                    raise ValueError('Trigger source may only be 1, 2, 3 or 4.')
            if standard:
                tds.write('TRIGger:A:COMMunication:STANdard ' + str(standard))
            if bitrate:
                tds.write('TRIGger:A:COMMunication:BITRate ' + str(bitrate))
            if pulseform and comm:
                tds.write('TRIGger:A:COMMunication:CODe ' + str(comm))
                if pulseform == 'plus':
                    tds.write('TRIGger:A:COMMunication:' + str(comm) + ':PULSEForm PLUSOne')
                if pulseform == 'minus':
                    tds.write('TRIGger:A:COMMunication:' + str(comm) + ':PULSEForm MINUSOne')
                if pulseform == 'eye':
                    tds.write('TRIGger:A:COMMunication:' + str(comm) + ':PULSEForm EYEDiagram')
                    if eyetype:
                        if eyetype == 'data':
                            tds.write('TRIGger:A:COMMunication:SOUrce:TYPe DATA')
                        elif eyetype == 'clock':
                            tds.write('TRIGger:A:COMMunication:SOUrce:TYPe CLOCK')
                        elif eyetype == 'recovered':
                            tds.write('TRIGger:A:COMMunication:SOUrce:TYPe RECOVERED')
                        else:
                            raise TypeError('Eyetype must be data, clock or recovered')
                if pulseform == 'zero':
                    tds.write('TRIGger:A:COMMunication:' + str(comm) + ':PULSEForm ZERO')
            if (low and comm) or (high and comm):
                tds.write('TRIGger:A:COMMunication:CODe ' + str(comm))
                if high:
                    tds.write('TRIGger:A:COMMunication:' + str(comm) + ':THReshold:HIGH ' + str(high))
                if low:
                    tds.write('TRIGger:A:COMMunication:' + str(comm) + ':THReshold:LOW ' + str(low))
            if polarity:
                if polarity == 'rise':
                    tds.write('TRIGger:A:COMMunication:CLOCK:POLarity RISE')
                elif polarity == 'fall':
                    tds.write('TRIGger:A:COMMunication:CLOCK:POLarity FALL')
        elif triggertype == 'edge':
            tds.write('TRIGger:A:TYPe EDGE')
            if edgesource:
                if edgesource == 'AUX':
                    tds.write('TRIGger:A:EDGE:SOUrce AUXiliary')
                elif edgesource == 'line':
                    tds.write('TRIGger:A:EDGE:SOUrce LINE')
                else:
                    tds.write('TRIGger:A:EDGE:SOUrce ' + str(edgesource))
            if edgecoupling:
                tds.write('TRIGger:A:EDGE:COUPling ' + str(edgecoupling))
            if edgeslope:
                if edgeslope == 'rise':
                    tds.write('TRIGger:A:EDGE:SLOpe RISe')
                elif edgeslope == 'fall':
                    tds.write('TRIGger:A:EDGE:SLOpe FALL')
                else:
                    raise TypeError('Edgeslope must be rise or fall.')
        elif triggertype == 'serial':
            tds.write('TRIGger:A:TYPe SERIal')
            if source:
                tds.write('TRIGger:A:Serial:SOUrce ' + str(source))
            if standard:
                tds.write('TRIGger:A:Serial:STANdard ' + str(standard))
            if dataformat:
                if dataformat == 'hex':
                    tds.write('TRIGger:A:Serial:DATa:FORMat HEX')
                elif dataformat == 'binary':
                    tds.write('TRIGger:A:Serial:DATa:FORMat BINary')
            if datapattern:
                tds.write('TRIGger:A:Serial:DATa:PATtern ' + str(datapattern))
            if bitrate:
                tds.write('TRIGger:A:SERial:BITRate ' + str(bitrate))
            if code:
                tds.write('TRIGger:A:Serial:CODe NRZ')
            if clock:
                tds.write('TRIGger:A:Serial:CLOCK:LEVel ' + str(clock))
            if polarity == 'rise':
                tds.write('TRIGger:A:Serial:CLOCK:POLARITY RISe')
            elif polarity == 'fall':
                tds.write('TRIGger:A:Serial:CLOCK:POLARITY FALL')
            if clocksource:
                tds.write('TRIGger:A:Serial:CLOCK:SOUrce ' + str(clocksource))
        elif triggertype == 'pulse':
            tds.write('TRIGger:A:TYPe PULse')
            if source:
                tds.write('TRIGger:A:PULse:SOUrce CH' + str(source))
            if triggerclass:
                if triggerclass == 'glitch':
                    tds.write('TRIGger:A:PULse:CLAss GLItch')
                    if polarity:
                        if polarity == 'positive':
                            tds.write('TRIGger:A:PULse:GLItch:POLarity POSITIVe')
                        elif polarity == 'negative':
                            tds.write('TRIGger:A:PULse:GLItch:POLarity NEGAtive')
                        elif polarity == 'both':
                            tds.write('TRIGger:A:PULse:GLItch:POLarity EITher')
                        else:
                            raise ValueError('Polarity in the glitch class may only be positive, negative or both.')
                    if triggerwhen:
                        if triggerwhen == 'wider':
                            tds.write('TRIGger:A:PULse:GLItch:TRIGIF REJect')
                        if triggwhen == 'narrower':
                            tds.write('TRIGger:A:PULse:GLItch:TRIGIF ACCept')
                    if width:
                        tds.write('TRIGger:A:PULse:GLItch:WIDth ' + str(width))
                elif triggerclass == 'runt':
                    tds.write('TRIGger:A:PULse:CLAss RUNT')
                    if width:
                        tds.write('TRIGger:A:PULse:RUNT:WIDth ' + str(width))
                    if polarity:
                        if polarity == 'positive':
                            tds.write('TRIGger:A:PULse:RUNT:POLarity POSITIVe')
                        elif polarity == 'negative':
                            tds.write('TRIGger:A:PULse:RUNT:POLarity NEGAtive')
                        elif polarity == 'both':
                            tds.write('TRIGger:A:PULse:RUNT:POLarity EITher')
                        else:
                            raise ValueError('Polarity in the runt class may only be positive, negative or both.')
                    if threshold:
                        tds.write('TRIGger:A:PULse:RUNT:THReshold:BOTh ' + str(threshold))
                    if high:
                        tds.write('TRIGger:A:PULse:RUNT:THReshold:HIGH ' + str(high))
                    if low:
                        tds.write('TRIGger:A:PULse:RUNT:THReshold:LOW ' + str(low))
                    if triggerwhen:
                        if triggerwhen == 'any':
                            tds.write('TRIGger:A:PULse:RUNT:WHEn OCCurs')
                        elif triggerwhen == 'greater':
                            tds.write('TRIGger:A:PULse:RUNT:WHEn WIDERthan')
                elif triggerclass == 'width':
                    tds.write('TRIGger:A:PULse:CLAss WIDth')
                    if high:
                        tds.write('TRIGger:A:PULse:WIDth:HIGHLimit ' + str(high))
                    if low:
                        tds.write('TRIGger:A:PULse:WIDth:LOWLIMIT ' + str(low))
                    if polarity:
                        if polarity == 'positive':
                            tds.write('TRIGger:A:PULse:WIDth:POLarity POSITIVe')
                        elif polarity == 'negative':
                            tds.write('TRIGger:A:PULse:WIDth:POLarity NEGAtive')
                        else:
                            raise ValueError('Width polarity must be either positive or negative.')
                    if triggerwhen:
                        if triggerwhen == 'outside':
                            tds.write('TRIGger:A:PULse:WIDth:WHEn OUTside')
                        if triggerwhen == 'within':
                            tds.write('TRIGger:A:PULse:WIDth:WHEn WIThin')
                elif triggerclass == 'transition':
                    tds.write('TRIGger:A:PULse:CLAss TRANsition')
                    if deltatime:
                        tds.write('TRIGger:A:PULse:TRANsition:DELTATime ' + str(deltatime))
                    if polarity:
                        if polarity == 'high':
                            tds.write('TRIGger:A:PULse:TRANsition:POLarity STAYSHigh')
                        elif polarity == 'low':
                            tds.write('TRIGger:A:PULse:TRANsition:POLarity STAYSLow')
                        elif polarity == 'both':
                            tds.write('TRIGger:A:PULse:TRANsition:POLarity EITher')
                        else:
                            raise ValueError('Pulse transition polarity can only be high, low or both.')
                    if threshold:
                        tds.write('TRIGger:A:PULse:TRANsition:THReshold:BOTh ' + str(threshold))
                    if high:
                        tds.write('TRIGger:A:PULse:TRANsition:THReshold:HIGH ' + str(high))
                    if low:
                        tds.write('TRIGger:A:PULse:TRANsition:THReshold:LOW ' + str(low))
                    if triggerwhen:
                        if triggerwhen == 'faster':
                            tds.write('TRIGger:A:PULse:TRANsition:WHEn FASTERthan')
                        elif triggerwhen == 'slower':
                            tds.write('TRIGger:A:PULse:TRANsition:WHEn SLOWERthan')
                elif triggerclass == 'timeout':
                    tds.write('TRIGger:A:PULse:CLAss TIMEOut')
                    if polarity:
                        if polarity == 'high':
                            tds.write('TRIGger:A:PULse:TIMEOut:POLarity STAYSHigh')
                        if polarity == 'low':
                            tds.write('TRIGger:A:PULse:TIMEOut:POLarity STAYSLow')
                        if polarity == 'either':
                            tds.write('TRIGger:A:PULse:TIMEOut:POLarity EITher')
                    if timeouttime:
                        tds.write('TRIGger:A:PULse:TIMEOut:TIMe ' + str(timeouttime))
                    
                else:
                    raise ValueError('Pulse trigger class can only be glitch, runt, width, transition or timeout.')
        else:
            raise TypeError('Triggertype may only be edge, logic, pulse, comm or serial.')
    if level:
        tds.write('TRIGger:A:LEVel ' + str(level))
        
def ResetHistogram():
    tds.write('HIStogram:COUNt RESET')
    
def HistogramData():
    tds.query('HIStogram:DATa?')
        
def Histogram(display=None, source=None, size=None, function=None, state=None, box=None, left=None, top=None, right=None, bottom=None):
    if display:
        if str(display) == 'off':
            tds.write('HIStogram:DISplay OFF')
        elif str(display) == 'log':
            tds.write('HIStogram:DISplay LOG')
        elif str(display) == 'lin':
            tds.write('HIStogram:DISplay LINEAr')
        else:
            raise TypeError('Display argument must be off, log or lin.')
    if state:
        tds.write('HIStogram:STATE ' + str(state))
    if source:
        tds.write('HIStogram:SOUrce ' + str(source))
    if size:
        tds.write('HIStogram:SIZe ' + str(size))#0.1-8 div hor, 0.1+10 vert
    if function:
        if function == 'vertical':
            tds.write('HIStogram:FUNCtion VERTical')
        elif function == 'horizontal':
            tds.write('HIStogram:FUNCtion HORizontal')
    if box and left and top and right and bottom:
        if box == 'coordinates':
            tds.write('HIStogram:Box ' + str(left) + ', '+ str(top) + ', '+ str(right) + ', '+ str(bottom))
        elif box == 'percent':
            tds.write('HIStogram:BOXPcnt ' + str(left) + ', '+ str(top) + ', '+ str(right) + ', '+ str(bottom))
        else:
            raise TypeError('Histogram Box can only be coordinates or percent')
    else:
        raise ValueError('Box argument needs left, top, right and bottom arguments.')

def FastFrame(source=None, count=None, refframe=None, length=None, mode=None, multiframes=None, multisource=None, frameamount=None, start=None):
    if source:
        tds.write('HORizontal:FASTframe:REF:SOUrce ' + str(source))
    if count:
        tds.write('HORizontal:FASTframe:COUNt ' + str(count))
    if refframe:
        tds.write('HORizontal:FASTframe:REF:FRAme ' + str(refframe))
    if length:
        tds.write('HORizontal:FASTframe:LENgth ' + str(length))
    if mode:
        tds.write('HORizontal:FASTframe:TRACk ' + str(mode))
    if multiframes:
        if multiframes == 'off':
            tds.write('HORizontal:FASTframe:MULtipleframes:MODE OFF')
        elif str(mode) == 'on':
            tds.write('HORizontal:FASTframe:MULTipleframes:MODE OVERlay')
            if multisource:
                if frameamount:
                    tds.write('HORizontal:FASTframe:MULTipleframes:NUMFRames:' + str(multisource) + ' '  + str(frameamount))
                if start:
                    tds.write('HORizontal:FASTframe:MULtipleframes:FRAMESTart:' + str(multisource) + ' ' + str(start))
        else:
            raise TypeError('Multiframes mode must be either off or on.')
               
def FastFrameStart():
    tds.write('HORizontal:FASTframe:STATE ON')
def FastFrameStop():
    tds.write('HORizontal:FASTframe:STATE OFF')
        
def TimeDelay(mode='seconds', time='0'):
    if time == '0':
        tds.write ('HORizontal:DELay:MODe OFF')
    elif mode == 'percent':
        if time >= 1 and time <= 99:
            tds.write ('HORizontal:DELay:MODe ON')
            tds.write('HORizontal:DELay:POSition ' + str(time))
        else:
            raise ValueError('Time delay position may only range from 0 to 99.')
    elif mode == 'seconds':
        tds.write ('HORizontal:DELay:MODe ON')
        tds.write('HORizontal:DELay:TIMe ' + str(time))
    else:
        raise TypeError('Time delay mode must be either seconds or percent. Alternatively time can be set to 0.')

def Horizontal(rate=None, scale=None, units=None, position=None, resolution=None, roll=None):
    if rate:
        tds.write('HORizontal:MAIn:SAMPLERate ' + str(rate))
    if scale:
        tds.write('HORizontal:MAIn:SCAle ' + str(scale))
    if units:
        tds.write('HORizontal:MAIn:UNIts ' + str(units))
    if position:
        tds.write('HORizontal:MAIn:POSition ' + str(position))
    if resolution:
        tds.write('HORizontal:RECOrdlength ' + str(resolution))
    if roll:
        tds.write('HORizontal:ROLL ' + str(roll))

def ChannelSetup(channel=ch, coupling=None, deskewtime=None, offset=None, position=None, scale=None):
    if coupling:
        tds.write('CH' + str(channel) + ':COUPling ' + str(coupling))
    if deskewtime:
        tds.write('CH' + str(channel) + ':DESKew ' + str(deskewtime))
    if offset:
        tds.write('CH' + str(channel) + ':OFFSet ' + str(offset))
    if position:
        tds.write('CH' + str(channel) + ':POSition ' + str(position))
    if scale:
        tds.write('CH' + str(channel) + ':SCAle ' + str(scale))
    
def WaveformDisplay(source='CH1', arg = 'ON'):
    tds.write('SELect:' + str(source) + ' ' + str(arg))
    
