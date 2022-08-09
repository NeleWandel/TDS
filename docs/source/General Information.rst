General Information
===================

.. toctree::

   General Information

Device Set Up
-------------
| In order for this library to work you need to connect your oscilloscope to your device via GPIB to USB converter. 
| Please make sure that the `PyVisa library <https://pyvisa.readthedocs.io/en/latest/>`_ is properly installed on the device. 
| 
| After you set up your device and connected the oscilloscope, you need to set up remote communication on your oscilloscope. To do this start your oscilloscope, go to ``Utilities`` --> ``GPIB Configuration`` and make sure that it is set to ``Talk/Listen``. In case the configuration is set to ``Off Bus`` you will not be able to communicate with the oscilloscope.
| In case your device doesn't recognise the oscilloscope or the GPIB to USB converter, you need to create a fitting driver from NI-VISA. You can download NI-VISA from the `National Instruments website. <https://www.ni.com/de-de/support/downloads/drivers/download.ni-visa.html#346210>`_
|
| You can make sure that your devices are properly connected with a quick testing code:

      >>> import pyvisa
      >>> rm = pyvisa.ResourceManager()
      >>> print(rm.list_resources())

| Now you should get a list of resources, eg: ('GPIB0::1::INSTR') - copy the one that corrolates with the oscilloscope and insert it into the next code.

       >>> tds = rm.open_resource('GPIB0::1::INSTR')
       >>> print(tds.query("*IDN?"))
| 
| If you get an answer from the device, everything is ready. Otherwise there might still be a problem with the driver of your converter. Try redownloading a driver from National Instruments. 
| In case you work with an older GPIB to USB converter you might need to install an older version of NI-VISA.

Example
-------
| Now that the device is properly set up, it is time to write a code to operate the oscilloscope.

      >>> import pyvisa
      >>> rm = pyvisa.ResourceManager()
      >>> tds = rm.open_resource('GPIB0::1::INSTR')
      
| This short code always needs to be executed first, followed by the command definitions, which can be found   `here. <https://github.com/NeleWandel/TDS/blob/main/TDS.py>`_
| The next important step is to connect your probe to the oscilloscope so that there is data to acquire.
| Afterwards you should be able to set up your device and start acquiring data.

      >>> WaveformDisplay('CH1', 'ON')
      >>> ProbeCalibration('1')
      >>> Wait()
      >>> AutoSet()
      >>> Acquisition('sampling', stop='single')
      >>> StartAcquisition()
      >>> Measure(meastype='AMP', m='IMMed', source='CH1')
      >>> Wait()
      >>> print(Value())
      
| In this example we first turn on the display of our source waveform, then we let the oscilloscope auto calibrate our probe with :meth:`ProbeCalibration`. To ensure that the calibration is fully done before moving on, we use the :meth:`Wait` command.
| Next we let the oscilloscope :meth:`AutoSet` the horizontal, vertical and trigger values, so that we have a stable display of our waveform. The :meth:`Acquisition` command sets the wanted parameters, in this case a single sequence acquisition in sampling mode. :meth:`StartAcquisition` then starts acquiring data. The :meth:`Measure` command then sets the measurement parameters to amplitude measurement in immediate mode on channel 1. 
| The :meth:`Wait` command ensures that all data has been acquired before the actual measurement takes place. 
| Not using the :meth:`Wait` command, might result in unfinished data acquisition, which might lead to a false measurement result.

