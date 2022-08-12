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

def Scan(scanrate, resolution=None):
    if scanrate:
        sp.write(str(scanrate) + ' NM/MIN')
        time.sleep(0.1)
    sp.write(str(wavelength) + ' NM')


#initialises the monochromator to default values
def Reset():
    sp.write('HELLO')

#sets initialisation wavelength 
def InitialWavelength(wavelength):
    sp.write(str(wavelength) + ' INIT-WAVELENGTH')

def InitialScanrate(scanrate):
    sp.write(str(scanrate) + ' INIT-SRATE')
