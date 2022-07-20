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

.. code-block:: console

   import pyvisa
   rm = pyvisa.ResourceManager()
   print(rm.list_resources())

| Now you should get a list of resources, eg: ('GPIB0::1::INSTR') - copy the one that corrolates with the oscilloscope and insert it into the next code.
.. code-block:: console

    tds = rm.open_resource('GPIB0::1::INSTR')
    print(tds.query("*IDN?"))
| 
| If you get an answer from the device, everything is ready. Otherwise there might still be a problem with the driver of your converter. Try redownloading a driver from National Instruments. 
| In case you work with an older GPIB to USB converter you might need to install an older version of NI-VISA.


