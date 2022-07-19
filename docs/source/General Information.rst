General Information
===================

| In order for this library to work you need to connect your oscilloscope to your device via GPIB to USB converter. 
| Please make sure that the `PyVisa library <https://pyvisa.readthedocs.io/en/latest/>`_ is properly installed on the device. 
| 
| 
| After you set up your device and connected the oscilloscope, you need to set up remote communication on your oscilloscope. To do this start your oscilloscope, go to *Utilities* --> *GPIB Configuration* and make sure that it is set to *Talk/Listen*. In case the configuration is set to *Off Bus* you will not be able to communicate with the oscilloscope.
| In case your device doesn't recognise the oscilloscope or the GPIB to USB converter, you need to download or create a fitting driver on the `National Instruments website. <https://www.ni.com/>`_
|
| You can make sure that your devices are properly connected with a quick testing code:
``import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())``
| Now you should get a list of resources, eg: ('GPIB0::1::INSTR') - copy the one that corrolates with the oscilloscope and insert it into the next code.
``tds = rm.open_resource('GPIB0::1::INSTR')
print(tds.query("*IDN?"))``
