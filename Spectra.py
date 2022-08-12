import pyvisa
from pyvisa.constants import StopBits, Parity
import time
rm = pyvisa.ResourceManager()
print(rm.list_resources())

sp = rm.open_resource('ASRL3::INSTR', read_termination = '\r', 
                      write_termination = '\r', baud_rate = 9600, 
                      data_bits = 8, flow_control = 2, 
                      parity = Parity.none, stop_bits = StopBits.one)

#Go to a designated wavelength at max speed
def Run(wavelength):
    sp.write(str(wavelength) + ' GOTO')

#Go to a designated wavelength at a speed set by scanrate in nm per minute
def Scan(wavelength, scanrate=None):
    if scanrate:
        sp.write(str(scanrate) + ' NM/MIN')
        time.sleep(0.1)
    sp.write(str(wavelength) + ' NM')

#initialises the monochromator to default values
def Restart():
    sp.write('HELLO')

#sets default wavelength in nm, does not change the current wavelength as it only applies after initialising the instrument
def InitialWavelength(wavelength):
    sp.write(str(wavelength) + ' INIT-WAVELENGTH')
    
#sets default scanrate in nm/min, does not change the current scanrate as it only applies after initialising the instrument
def InitialScanrate(scanrate):
    sp.write(str(scanrate) + ' INIT-SRATE')
