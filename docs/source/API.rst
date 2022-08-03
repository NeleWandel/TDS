API
===

.. toctree::

   API

Acquisition
---------
| With the commands of the acquisition group it is possible to set up the instruments signal aquisition as well as the way signals are processed into waveforms.

.. method:: Acquisition(acquiremode, mode=None, samplesize=None, WFamount=None, stop=None)
| Sets all the options for the acquisition. While it is possible to change these parameters during an ongoing acquisition, it is adviced to change them before starting the acquisition. Starting and stopping an acquisition must be done by :meth:`StartAcquisition` and :meth:`StopAcquisition`.
| 
| All arguments, except ``acquiremode`` are optional. 
| ``acquiremode`` enables the selected mode for aquiring data.
| Valid arguments are:
- :const:`sampling` (Enanbles sampling mode)
- :const:`peakdetect` (Enables peak detect mode)
- :const:`hires` (Enables HiRes mode)
- :const:`averaging` (Enables averaging mode)
- :const:`envelope` (Enables envelope mode)
- :const:`wfmdb` (Enables WFMDB mode)
| 
| ``mode`` sets the wanted samplingmode to either real time (:const:`RT`), interpolated real time (:const:`IT`) or equivalent time (:const:`ET`).
| 
| ``samplesize`` sets the amount of waveform database points that the oscilloscope acquires for a single sequence acquisition. Must be a whole number.
| 
| ``WFamount`` sets the amount of waveforms that will be acquired for averaging and enveloping. Must be a whole number.
| If envelope mode is enabled, a waveform amount of :const:`0` corresponds to infinitely acquisations.
|
| ``stop`` defines whether the acquisition stops after a :const:`single` sequence or :const:`repeat` until stopped with :meth:`StopAcquisition`.
| 
.. method:: StartAcquisition()
| Starts acquiring data. 
| While changes are possible during an acquisition, it is recommended that all acquisition settings are properly set before starting the acquisition.
.. method:: StopAcquisition()
| Stops acquiring data.
.. method:: Wait()
| The oscilloscope waits with the execution of further commands until all acquisitions are done.

Calibration
-----------
| With the commands of the calibration group it is possible to perform self-calibrations as well as probe-calibrations.

.. method:: Calibration()
| Starts the auto calibration. 
.. note:: In order for this command to properly work it is recommended to wait around 20 minutes after turning the oscilloscope on. It might take a long time for the oscilloscope to self-calibrate. No other commands will be executed during this time.
.. method:: ProbeCalibration(channel=ch)
| Starts the auto calibration of the probe defined by ``channel``. The calibration can take up to a minutet and no other commands will be executed during that time.
| ``channel`` may range from :const:`1` through :const:`4`. If no channel is given, the system will use either the default channel 1 or the channel selected by :meth:`Channel` if that command had been used during the session.

Hard Copy and Export
--------------------
| The commands of the hard copy and export group allow the creation of data file copies. Export commands can format waveforms as data files.

.. method:: Export(filename=None, fileformat=None, inksaver=None, palette=None, fullscreen=None)
| Copies a waveform to a file that can be specified by ``filename``.
| 
| All arguments are optional. Defining none of the arguments, exports with either the default settings or the settings used prior in that session.
| If ``filename`` is only the file name and not the directory the file will be saved in the default hard copy directory (usually ``C:\TekScope\Images\yourimage``)
| If ``filename`` is not specified the file will be saved in the default directory with the default name.
| Valid formats for ``fileformat`` are:
- :const:`BMP`
- :const:`JPEG`
- :const:`PNG`
| 
| ``inksaver`` has three valid states:
- :const:`1` (Displays the display in the usual colors)
- :const:`2` (Changes the background to white)
- :const:`3` (Chooses colors that are well visible on a white background)
| 
| ``palette`` has three valid states:
- :const:`color` (The exported file is in color)
- :const:`gray` (The exported file is in grayscale)
- :const:`baw` (The exported file is in black and white)
| 
| ``fullscreen`` has two valid states:
- :const:`off` (Hides all menu areas)
- :const:`on` (Shows all menu areas)

.. method:: Screenshot(filename=None, inksaver=None, palette=None, orientation=None, fullscreen=None)
| Creates a hardcopy screenshot of everything that can currently be seen on the oscilloscopes screen.
| The format is always BMP. Creation of a screenshot might take a few milliseconds, using a timer in between multiple screenshots is recommended.
| All arguments are optional. Defining none of the arguments, takes a screenshot with either the default settings or the settings used prior in that session.
| If ``filename`` is only the file name and not the directory the file will be saved in the default hard copy directory (usually ``C:\TekScope\Images\yourimage``)
| If ``filename`` is not specified the file will be saved in the default directory with the default name.
| 
| ``inksaver`` has three valid states:
- :const:`1` (Displays the display in the usual colors)
- :const:`2` (Changes the background to white)
- :const:`3` (Chooses colors that are well visible on a white background)
| 
| ``palette`` has three valid states:
- :const:`color` (The screenshot is in color)
- :const:`gray` (The screenshot is in grayscale)
- :const:`baw` (The screenshot is in black and white)
| 
| ``orientation`` has two valid states:
- :const:`1` (The screenshot will be captured in portrait mode)
- :const:`2` (The screenshot will be captured in horizontal mode)
| 
| ``fullscreen`` has two valid states:
- :const:`off` (Hides all menu areas)
- :const:`on` (Shows all menu areas)

Histogram
---------

.. method:: Histogram(display=None, source=None, size=None, function=None, state=None, box=None, left=None, top=None, right=None, bottom=None)
| Sets up the histogram, defined by the arguments.
| All arguments are optional. Defining none of the arguments results in this command having no effect.
| ``display`` has three valid states:
- :const:`off` (Disables the display of the histogram, data will still be collected)
- :const:`log` (The histogram display is turned on and set to logarithmic format)
- :const:`lin` (The histogram display is turned on and set to linear format)
| ``source`` sets the source for the histogram. The source may be either CH<x>, MATH<x> or REF<x>. 
| ``size`` is given in devisions and defines the size of the histogram. If the histogram is horizontal, the value may range from 0.1 to 8.0. In case the histogram is vertical, the range is 0.1 to 10.0.
| ``function`` defines whether the histogram is :const:`horizontal` or :const:`vertical`.
| ``state`` defines whether histogram calculations are :const:`ON` or :const:`OFF`.
| ``box`` defines the boundaries of the histogram has two valid arguments:
- :const:`coordinates`
- :const:`percent`
| If ``box`` is used ``left``, ``top``, ``right`` and ``bottom`` must be defined by either the waveform coordinates or the percentage coordinates. 
.. warning::
   Changing the histogram box results in a reset of the histogram data. Make sure to retrieve all wanted data with the :meth:`HistogramData` function before executing changes of the box.

.. method:: HistogramData()
| Returns all histogram data values as an ASCII list, separated by commas.
| A vertical histogram returns 200 values, a horizontal histogram returns 500 values.

.. method:: ResetHistogram()
| Clears all counts and statistics for the histogram.

Horizontal
----------
.. method:: FastFrame(source=None, count=None, refframe=None, length=None, mode=None, multiframes=None, multisource=None, frameamount=None, start=None)
| Sets up all FastFrame (also known as memory segmentation) parameters.
| All arguments are optional. Not defining any of the arguments results in this command being useless.
| ``source`` defines the reference source. Valid sources are CH<x>, MATH<x> and REF<x> with <x> being an number ranging from 1 through 4.
| ``count`` defines how many frames/segments the FastFrame mode acquires.
| ``refframe`` defines the reference frame number which is then used to calculate the time differences for the frames.
| ``length`` may range from :const:`500` through :const:`400000` and defines the record length to the number of data points in each frame.
| ``mode`` can be either :const:`ALL` or :const:`LIVE`. In live mode adjusting a channel waveform leads to adjustment of all channel and math waveforms, as they get locked together. For example changing the reference frame from CH1 to frame 6 results in CH2, CH3, CH4, MATH1, MATH2, MATH3 and MATH 4 also using frame 6 as reference. All mode the same happens, but on top of that all REF waveforms also adjust to the selected frame.
| ``multiframes`` if turned :const:`on` the oscilloscope displays multiple overlaid frames. Turning on multiframe mode gives access to ``multisource``, ``frameamount`` and ``start``.
| ``multisource`` defines the source for the multiframe mode. This needs to be given, in order for ``frameamount`` and ``start`` to be accessible. Valid sources are :const:`CH<x>`, :const:`MATH<x>` and :const:`REF<x>` with <x> being an number ranging from 1 through 4.
| ``frameamount`` defines the number of overlaying frames. 
| ``start`` defines the starting frame.
.. method:: FastFrameStart()
| Starts FastFrame acquisition.
.. method:: FastFrameStop()
| Stops FastFrame acquisition.
.. method:: Horizontal(rate=None, scale=None, units=None, position=None, resolution=None, roll=None)
| Sets the horizontal parameters of the oscilloscope.
| All arguments are optional.
| ``rate`` in samples for second. Sets the horizontal sample rate of the oscilloscope. Adjusting the rate leads to an automatic adjustment of the record length.
| ``scale`` in seconds per devision. Sets the horizontal scale, range is :const:`2E-10` to :const:`40` (200ps to 40s).
| ``units`` as a string. Sets the unit for the time base. 
| ``position`` in percent. Positions the chosen amout of the waveform to the left of the center. 
| ``resolution`` in data points per frame. The minimum is :const:`500`, maximum is :const:`400000` if only one channel is in use, :const:`200000` if two channels are in use and :const:`100000` in case all four channels are in use.
| ``roll`` changes the roll mode status. This can be usefull for observing data samples at slow speeds. It has three valid states:
- :const:`AUTO`
- :const:`OFF`
- :const:`ON`
.. method:: TimeDelay(mode='seconds', time='0')
| Sets the horizontal time delay of the oscilloscope.
| ``mode`` can be either :const:`percent` or :const:`seconds`. 
| If ``mode`` is percent, time can be between :const:`1` and :const:`99`.
| If ``mode`` is seconds, time can be any amount in seconds.
| If ``time`` is :const:`0` time delay is turned off.

Mask
----
| Commands in the mask group allow for comparison of incoming waveforms with standard or user-defined masks. It is possible to set actions that the oscilloscope takes in case the waveform falls inside or outside the mask limits.

.. method:: AutoAdjustMaskOff()
| Turns off automatic optimising of the mask.
.. method:: AutoAdjustMaskOn()
| Turns on automatic optimising of the mask. This feature shifts the mask horizontally and vertically in order to minimise the signal hits.
.. method:: Mask(start=True, mask=None, source='CH1', display='ON', counting=None, wfmamount=None, highlights=None, inverted=None, margin=None, polatity=None, stoponfailure=None, failthreshold=None, failscreen=None, logfail=None, logwfm=None, repeat=None, delay=None, auto=None, hdelta=None, vdelta=None, digitalfilter=None, beep=None, failbeep=None)
| The mask function controlls 
Math
-----
| Commands of the math group allow for the creation of math-based waveforms. Up to four math based waveforms can be stored and displayed at the same time. :meth:`SetMathStorage` regulates which of the four possible math storages will be used by the other commands in the math group.

.. method:: DefineMath(equation)
| Sets a math based waveform. The equation may consist of waveforms (those can be taken from a channel, a reference or another math equation), measurements, scalar sources, functions, operands and numerical constants. The equation may consist of more than 100 characters. The equation will be saved to the place defined by :meth:`SetMathStorage`.
| Changes to any of the operands lead to changes of the output.
| Examples:
| DefineMath(Ch1+Ch2)
| DefineMath((Ch1-Meas1)/Meas2)
| DefineMath(Intg(Ch1-Avg(Ch1))
.. method:: DefineMathVariable(varnumber, varvalue)
| Defines a variable that can be used in :meth:`DefineMath`.
| `varnumber` must be a number ranging from 1 through 8 and defines the storage place of the variable.
| `varvalue` can be any value.
.. method:: MathDefinition()
| Returns the current definition for the math waveform stored in the storage selected by :meth:`SetMathStorage`
.. method:: SetMathPos(y)
| Sets the vertical position of the waveform defined by :meth:`DefineMath`. `y` can be either positive or negative and is given in divisions.
| Please make sure to leave a time of at least 0.5 seconds between computing the math definition and changing the vertical positioning, as autoscaling occurs directly after computing. Autoscaling will override any position changes. 
.. method:: SetMathScale(x)
| Sets the horizontal scale of the waveform defined by :meth:`DefineMath`. `x` can be either positive or negative and is given in volt, amper or watt per divisions.
| Viable ranges are from 100.0E-36 through 100.0E+36.
| Please make sure to leave a time of at least 0.5 seconds between computing the math definition and changing the vertical positioning, as autoscaling occurs directly after computing. Autoscaling will override any position changes. 
.. method:: SetMathStorage(number)
| Sets the storage number for every command in the math group. ``number`` must be either 1, 2, 3 or 4.
| Default storage is 1.
.. method:: ShowMathPos()
| Returns the current position set by :meth:`SetMathPos`.
.. method:: ShowMathScale()
| Returns the current scale set by :meth:`SetMathScale`.

Measurement
-----------
.. method:: Measure(meastype=None, m=meas, statistics=None, weightvalue=None, state=None, source=None, source2=None, refmethod=None, high=None, low=None, mid=None, delay=None, edge1=None, edge2=None)
| ``m`` defines the measurement from :const:`1` to :const:`8`
| 
| ``delay`` sets the starting point and direction for a measurement. It can be either :const:`forwards` (starting at the beginning of the waveform) or :const:`backwards` (starting at the end of the waveform).
| 
| ``meastype`` defines the kind of measurement that takes place in the spot selected by ``m``. 
| Valid options are:
.. tabs::
   .. tab:: AMPlitude
   
      | Measures the amplitude of the selected waveform selected.
      | 
      | Amplitude = High - Low 
   .. tab:: AREa
   
      | Measures the voltage over time for the selected waveform in volt-seconds.
      | Area above the ground is positive, area below the ground is negative.
   .. tab:: BURst
   
      | Measures the duration of a burst.
   .. tab:: CARea
   
      | Measures the voltage over time for the first cycle of the selected waveform in volt-seconds.
      | Area above the reference point is positive, area below the reference point.
   .. tab:: CMEan
   
      | Measures the arithmetic mean for the first cycle of the selected waveform.
   .. tab:: CRMs
   
      | Measures the true root mean square voltage for the first cycle of the selected waveform.
   .. tab:: DELay
   
      | Measures the time between the reference amplitude points of the source and destination waveform.
   .. tab:: DISTDUty
   
      | Measures the time between the falling and rising edge of the eye pattern.
   .. tab:: EXTINCTDB
   
      | Measures the extinction ratio for an optical waveform in dB.
      | This only works for fast acquisition signals.
      | 
      | Extinction dB = 10 x (log 10 (High/Low)
   .. tab:: EXTINCTPCT
   
      | Measures the extinction ratio for an optical waveform in percent.
      | This only works for fast acquisition signals.
      | 
      | Extinction % = 100.0 x (Low/High)
   .. tab:: EXTINCTRATIO
   
      | Measures the extinction ratio for an optical waveform.
      | This only works for fast acquisition signals.
      | 
      | Extinction = (High/Low)
   .. tab:: EYEHeight
   
      | Measures the vertical opening of an eye diagram in volts.
   .. tab:: EYEWidth
   
      | Measures the horizontal opening of an eye diagram in seconds.
   .. tab:: FALL
   
      | Measures the time it takes a falling edge to fall from a high reference value (default 90%) to a low reference value (default 10%).
   .. tab:: FREQuency
   
      | Measures the first cycle of the selected waveform in order to form the frequency in Hz.
   .. tab:: HIGH
   
      | Measures the 100% level reference (topline) of the selected waveform.
   .. tab:: HITS
   
      | Measures the number of hits in/on the histogram box.
   .. tab:: LOW
   
      | Measures the 0% level reference (baseline) of the selected waveform.
   .. tab:: MAXimum
   
      | Measures the maximum amplitude of the selected waveform.
      | 
   .. tab:: MEAN
   
      | 
   .. tab:: MEDian
   
      | 
   .. tab:: MINImum
   
      | 
   .. tab:: NCROss
   
      | 
   .. tab:: NDUty
   
      | 
   .. tab:: NOVershoot
   
      | 
   .. tab:: NWIdth
   
      | 
   .. tab:: PBASe
   
      | 
   .. tab:: PCROss
   
      | 
   .. tab:: PCTCROss
   
      | 
   .. tab:: PDUty
   
      | 
   .. tab:: PEAKHits
   
      | 
   .. tab:: PERIod
   
      | 
   .. tab:: PHAse
   
      | 
   .. tab:: PK2Pk
   
      | 
   .. tab:: PKPKJitter
   
      | 
   .. tab:: PKPKNoise
   
      | 
   .. tab:: POVershoot
   
      | 
   .. tab:: PTOP
   
      | 
   .. tab:: PWIdth
   
      | 
   .. tab:: QFACtor
   
      | 
   .. tab:: RISe
   
      | 
   .. tab:: RMS
   
      | 
   .. tab:: RMSJitter
   
      | 
   .. tab:: RMSNoise
   
      | 
   .. tab:: SIGMA1
   
      | 
   .. tab:: SIGMA2
   
      | 
   .. tab:: SIGMA3
   
      | 
   .. tab:: SIXSigmajit
   
      | 
   .. tab:: SNRatio
   
      | 
   .. tab:: STDdev
   
      | 
   .. tab:: UNDEFINED
   
      | 
   .. tab:: WAVEFORMS
   
      | 

   
| ``m``
| 
| ``statistics``
| 
| ``weightvalue``
| 
| ``state``
| 
| ``source``
| 
| ``source2``
| 
| ``refmethod``
| 
| ``high``
| 
| ``low``
| 
| ``mid``
| 


.. method:: UseMeasurement(x)
| Sets the storage number for every command in the measurement group. ``x`` must range from 1 through 8.
| Default storage is 1.

Trigger
-------
.. method:: Trigger(triggertype=None, mode=None, holdhofftime=None, triggerclass=None, CH1=None, CH2=None, CH3=None, CH4=None, function=None, triggerwhen=None, logicmin=None, logicmax=None, source=None, comm=None, bitrate=None, pulseform=None, eyetype=None, clock=None, clocksource=None, polarity=None, clockthreshold=None, setholdsource=None, threshold=None, settime=None, holdtime=None, width=None, low=None, high=None, edgecoupling=None, standard=None, level=None, CH1TH=None, CH2TH=None, CH3TH=None, CH4TH=None, dataformat=None, datapattern=None, timeout=None, timeouttime=None, deltatime=None, transition=None)

| Allows full controll of the trigger settings. All arguments are optional and not every argument is needed for every trigger type. All arguments ordered by ``triggertype`` can be found in the tabs below.
.. tabs::
   .. tab:: edge
   
      | Turns the trigger type to edge. In this state a trigger event is executed when a signal has a specified voltage level and direction.
      | 
      | ``edgesource`` defines the source. This can be either :const:`CH1`, :const:`CH2`, :const:`CH3`, :const:`CH4`, :const:`AUX` or :const:`line`.
      | AUX specifies that an external trigger is used. This must be connected via the auxiliary trigger input connector on the back of the oscilloscope.
      | line specifies that an AC line voltage is used.
      | 
      | ``edgecoupling`` sets the coupling type. Valid states are:
      - :const:`AC` (AC coupling)
      - :const:`DC` (DC coupling)
      - :const:`HFRej` (Removes high frequency components of the DC signal)
      - :const:`LFRej` (Removes low frequency components of the AC signal)
      - :const:`NOISErej` (Low sensitivity DC coupling. This option needs a higher signal amplitude to minimise false triggers)
      | 
      | ``edgeslope`` defines the slope. Valid states are:
      - :const:`rise` (triggers on a rising/positive signal edge)
      - :const:`fall` (triggers on a falling/negative signal edge)
   .. tab:: logic
   
      | Turns the trigger type to logic. In this state the oscilloscope starts a trigger event in case a defined logical situation occurs.
      | 
      | ``CH1``, ``CH2`` and ``CH3`` sets the logical input can be set to :const:`HIGH`, :const:`LOW` or :const:`x`. This specifies the logic that will be used when the trigger detects the trigger threshold level.
      - :const:`HIGH` specifies the logic high
      - :const:`LOW` specifies the logic low
      - :const:`x` specifies that it doesn't matter
      | 
      | Using the ``CH1TH``, ``CH2TH``, ``CH3TH`` and ``CH4TH`` arguments allow for setting the threshold for the respective channel in Volt.
      | 
      | ``level`` in Volt, sets the trigger level. Valid options are either any Volt amount or the preset trigger levels of :const:`ECL`(-1.3V) or :const:`TTL`(1.4V).
      | 
      | ``triggerclass`` has three valid states each with their own set of arguments:
      .. tabs::
         .. tab:: pattern
         
            | With pattern class activated, the oscilloscope generates a trigger event when the logical combinations of channel 1-4 are met.
            | 
            | ``CH4`` sets the logic input for channel 4. The logical input can be set to :const:`HIGH`, :const:`LOW` or :const:`x`.
            | 
            | ``triggerwhen`` specifies the condition under which the trigger will be generated. 
            | Valid states are:
            - :const:`true` (generates a trigger when the pattern becomes true)
            - :const:`false` (generates a trigger when the pattern becomes false)
            - :const:`less` (generates a trigger when the pattern becomes true for less than the duration set by ``logicmax``)
            - :const:`more` (generates a trigger when the pattern becomes true for longer than the duration set by ``logicmin``)
            | 
            | ``logicmax`` sets the duration in seconds that will be used as the time threshold for ``triggerwhen=less``
            | 
            | ``logicmin`` sets the duration in seconds that will be used as the time threshold for ``triggerwhen=more``
         .. tab:: state
            
            | With state class activated, the oscilloscope generates a trigger event when the channel 4 condition is met first and all of channel 1 through 3 conditions are met afterwards.
            | 
            | ``CH4`` sets the slope for channel 4. This can be either :const:`rise` or :const:`fall`.
            | 
            | ``triggerwhen`` specifies whether the trigger occurs when channel 1 through 3 conditions are met (true) or not met (false). The options are :const:`false` and :const:`true`.
         
         .. tab:: sethold
         
            | With sethold class activated, the oscilloscope generates a trigger event when setup and hold between data source and clock source are violated. 
            | 
            | ``setholdsource`` defines the channel that is used as the sethold data source and must be either :const:`1`, :const:`2`, :const:`3` or :const:`4`.
            | 
            | ``clocksource`` defines the channel that is used as the source of the clock and must be either :const:`1`, :const:`2`, :const:`3` or :const:`4`.
            | 
            | ``clockthreshold`` in Volt, defines the voltage threshold for the clock. 
            | 
            | ``threshold`` in Volt, defines the voltage threshold for the sethold data source.
            | 
            | ``settime`` in seconds, specifies the setup time for sethold violation triggering.
            | 
            | ``holdtime`` in seconds, specifies the hold time for sethold violation triggering.
         
   .. tab:: pulse
   
      | Turns the trigger type to pulse. In this state a trigger event is executed when a specified pulse is found.
      | 
      | ``triggerclass`` has five valid states each with their own set of arguments:
      .. tabs::
         .. tab:: glitch
            
            | With the glitch class activated, the oscilloscope executes a trigger event as soon as a pulse with a specified polarity and width is found.
            | 
            | ``polarity`` defines the polarity the pulse needs to trigger. Valid states are:
            - :const:`positive` (The oscilloscope only triggers when the pulse has a positive polarity)
            - :const:`negative` (The oscilloscope only triggers when the pulse has a negative polarity)
            - :const:`both` (The oscilloscope triggers for both cases)
            | 
            | ``triggerwhen`` defines whether the pulse needs to be :const:`wider` or :const:`narrower` than the defined ``width`` in order to trigger. 
            | 
            | ``width`` in seconds, defines the minimum or maximum width (depending on ``triggerwhen``) the pulse needs to have in order to trigger. 
         .. tab:: runt
            
            | With the runt class activated, the oscilloscope executes a trigger event as soon as a pulse crosses the first voltage threshold two times without crossing the second threshold.
            | 
            | ``width`` in seconds, defines the minimum width for a pulse to trigger, when ``triggerwhen`` is set to :const:`greater`.
            | 
            | ``polarity`` defines the polarity the pulse needs to trigger. Valid states are:
            - :const:`positive` (The oscilloscope only triggers when the pulse crosses the low threshold twice without crossing the high threshold)
            - :const:`negative` (The oscilloscope only triggers when the pulse crosses the high threshold twice without crossing the low threshold)
            - :const:`both` (The oscilloscope triggers for both cases)
            | 
            | ``threshold`` sets the upper and lower threshold to predefined values. The two options are :const:`TTL`, which sets the upper threshold to 1.8V and the lower to 800mV, and :const:`ECL`, which sets the upper threshold to -1.1V and the lower to -1.5V. With the ``high`` and ``low`` arguments, the thresholds can be set to user defined values.
            | 
            | ``high`` in Volt, sets the upper threshold.
            | 
            | ``low`` in Volt, sets the lower threshold.
            | 
            | ``triggerwhen`` defines whether the oscilloscope checks for the width of the pulse. The two valid states are:
            - :const:`any` (A pulse of any width can trigger, as long as the polarity is correct.)
            - :const:`greater` (The pulse must be wider than the amount set with ``width`` in order to trigger.)
         .. tab:: width
            
            | With the width class activated, the oscilloscope executes a trigger event as soon as a pulse with a specified polarity is found inside or outside a defined limit.
            | 
            | ``high`` in seconds, sets the upper trigger limit.
            | 
            | ``low`` in seconds, sets the lower trigger limit.
            | 
            | ``polarity`` specifies whether a pulse needs to be :const:`positive` or :const:`negative` for a trigger event to occur.
            | 
            | ``triggerwhen`` defines wether the the pulse must be detected :const:`outside` or :const:`within` the limit to execute a trigger event.
         .. tab:: transition
            
            | With the transition class activated, the oscilloscope executes a trigger event as soon as a pulse crosses two defined thresholds in the same direction within a defined time span.
            | 
            | ``deltatime`` in seconds, sets the timespan during which the pulse crosses need to occur.
            | 
            | ``polarity`` defines the polarity the pulse needs to trigger. Valid states are:
            - :const:`high` (The oscilloscope only triggers when the pulse first crosses the lower and then the higher threshold.)
            - :const:`low` (The oscilloscope only triggers when the pulse frist crosses the higher and then the lower threshold.)
            - :const:`both` (The oscilloscope triggers for both cases.)
            | 
            | ``threshold`` sets the upper and lower threshold to predefined values. The two options are :const:`TTL`, which sets the upper threshold to 1.8V and the lower to 800mV, and :const:`ECL`, which sets the upper threshold to -1.1V and the lower to -1.5V. With the ``high`` and ``low`` arguments, the thresholds can be set to user defined values.
            | 
            | ``high`` in Volt, sets the upper threshold.
            | 
            | ``low`` in Volt, sets the lower threshold.
            | 
            | ``triggerwhen`` defines whether the crossing of the pulse needs to be :const:`faster` or :const:`slower` than ``deltatime``.
         .. tab:: timeout
            
            | With the timeout class activated, the oscilloscope executes a trigger event as soon as a the pulses stop for a set amount of time.
            | 
            | ``polarity`` defines the polarity the pulse needs to trigger. Valid states are:
            - :const:`high` (The oscilloscope only triggers when the pulse edge stays high/positive during the required time out period.)
            - :const:`low` (The oscilloscope only triggers when the pulse edge stays low/negative during the required time out period.)
            - :const:`either` (The oscilloscope triggers for both cases.)
            | 
            | ``timeouttime`` in seconds, defines the time out period.
   .. tab:: comm
   
      | Turns the trigger type to communitcation. In this state a trigger events is executed when a defined communication signal is found.
      | 
      | ``comm`` defines the communication type. Valid states are:
      - :const:`CMI`
      - :const:`AMI`
      - :const:`HDB3`
      - :const:`B3ZS`
      - :const:`B6ZS`
      - :const:`B8ZS`
      | 
      | ``source`` defines the channel that shall be used as communication source. It must be eihter :const:`1`, :const:`2`, :const:`3` or :const:`4`.
      | 
      | ``standard`` defines the standard that shall be applied for the code and bit rate. A table of all viable standard settings can be found on page 646 in the `Online Programmer Manual <https://download.tek.com/manual/PHP014070web.pdf>`_.
      | 
      | ``bitrate`` defines the bits per seconds. This can be any positive number greater than one.
      | 
      | ``pulseform`` defines the pulseform. Valid states are:
      - :const:`plus` (sets the pulseform to plusone, this means the triggering occurs on a positive mark)
      - :const:`minus` (sets the pulseform to minusone, this means the triggering occurs on a negative mark)
      - :const:`eye` (constructs an eye diagram, this can be further specified by ``eyetype``)
      - :const:`zero` (the triggering occurs on a bit representing zero)
      | 
      | ``eyetype`` sets the source type for creating the eye pattern when pulseform=eye. Valid arguments are:
      - :const:`data` (The oscilloscope triggers and shifts in five units intervalls to form the eye pattern.)
      - :const:`clock` (The oscilloscope triggers randomly with respect to the data channel in order to form the eye pattern. No shifts occur.)
      - :const:`recovered` (The oscilloscope uses a phase locked loop on the recovered clock from the data signal. Triggers are random, no shift occurs.)
      | 
      | ``high`` sets the upper communication threshold.
      | ``low`` sets the lower communication threshold.
      | 
      | ``polarity`` sets the clock polarity to either :const:`rise` or :const:`fall`.

   .. tab:: serial
   
      | Turns the trigger type to serial. In this state a trigger event is executed when NRZ-encoded data providing a 32-bit serial word is found.
      | 
      | ``source`` sets the serial source. Source can be :const:`CH1` through :const:`CH4`.
      | 
      | ``standard`` sets the standard that identifies the code and bit rate. Following standards are valid:
      | :const:`OC1`, :const:`OC3`, :const:`OC12`, :const:`FC133`, :const:`FC266`, :const:`FC531`, :const:`FC1063`, :const:`FW139BS400B`, :const:`FW139BS800B`, :const:`ENET1250`, :const:`CUSTom`, :const:`RIO_500M`, :const:`RIO_750M`, :const:`RIO:1G`, :const:`RIO_SERIAL_1G`, :const:`VSROC192`
      | 
      | ``dataformat`` sets the format in which the serial signals are to be expected. Valid choices are :const:`hex` and :const:`binary`.
      | 
      | ``datapattern`` sets the serial pattern to trigger on. Default is :const:`XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX01`.
      | 
      | ``bitrate`` defines the bits per second. Valid range is :const:`1.5e6` to :const:`1.25e9`.
      | 
      | ``code`` any value other than None sets the signal code to NRZ.
      | 
      | ``clocksource`` defines the source of the clock. Can be either :const:`CH1` to :const:`CH4` or :const:`RECOVered`.
      | 
      | ``clock`` sets the clock level in Volt. Level may range from :const:`-9.9e37` to :const:`9.9e37`.
      | 
      | ``polarity`` sets the polarity of the clock to either :const:`rise` or :const:`fall`.

.. method:: TriggerB(state=None, source=None, count=None, time=None, level=None, slope=None)
| Controlls the secondary trigger.
| 
| ``state`` sets the trigger activity to either :const:`ON` or :const:`OFF`.
| 
| ``source``sets the source for the B trigger. It can be either :const:`AUX` or :const:`CH1` to :const:`CH4`.
| 
| ``count`` sets the amount of :meth:`Trigger` events that must occur before trigger B triggers an event.
| ``time`` sets the time period that must pass after a :meth:`Trigger` event for trigger B to trigger an event. 
| ``time`` and ``count`` cannot be active at the same time.
| 
| ``level`` in Volt, sets the trigger level. Valid options are either any Volt amount or the preset trigger levels of :const:`ECL`(-1.3V) or :const:`TTL`(1.4V).
| 
| ``slope`` sets the slope to either :const:`rise` where the trigger occurs on the rising/positive edge of a signal or :const:`fall` where the trigger occurs on the falling/negative edge of a signal.

Vertical
--------
.. method:: ChannelOffset(offset)
| Sets the vertical offset for the channel specified by :meth:`Channel`. ``offset`` needs to be written in mV.
| Depending on the vertical scale factor the range of the channel offset can be either ±100V, ±10V or ±1V.

Waveform Transfer
-----------------

Miscellaneous
-------------

.. method:: AutoSet()
| Automatically adjusts the vertical, horizontal and trigger controls in order to privide a stable display of the waveform on the oscilloscope.
| These changes can be undone by using the :meth:`Undo` command.
.. method:: Undo()
| Reverses all changes done by :meth:`AutoSet`. This does affect any changes made after the automatic adjustment. 
.. method:: Busy()
| Returns :const:`0` if the oscilloscope is currently not running the :meth:`StartAcquisition` command. Returns :const:`1` if the oscilloscope is acquiring data. 
.. method:: Channel(channelnumber)
| Sets the standard channel for all future commands. ``channelnumber`` may only be :const:`1`, :const:`2`, :const:`3` or :const:`4`.
| Default value is :const:`1`.
.. method:: ChannelAsSource()
| Sets the channel as source for all acquisitions. The channel can be set by :meth:`Channel`
| Other options are: :meth:`MathAsSource`, :meth:`RefAsSource` and :meth:`HistogramAsSource`
.. method:: Clear()
| Clears the ``event queue``, ``standard event status register`` and the ``status byte register``. Does not affect the output queue. 
.. method:: Date()
| Returns the current date of the oscilloscope. 
| The date can be adjusted by using :meth:`SetDate`
.. method:: Identify()
| Prints information and the identifaction code of the oscilloscope.
.. method:: Lock()
| Disables all frontpanel buttons and knobs on the oscilloscope, including the touchscreen.
| The command :meth:`Unlock` enables them again.
.. method:: Recall(storagelocation)
| Sets all oscilloscope settings to a state that was saved via the :meth:`Save` command.
| ``storagelocation`` must range from 1 through 10.
.. method:: ResetToFactorySettings()
| Resets the oscilloscope to the default settings. 
.. method:: Save(storagelocation)
| Saves the current settings of the oscilloscope to a storage location. These settings can be reapplied to the oscilloscope by using the :meth:`Recall` command.
| ``storagelocation`` must range from 1 through 10.
.. method:: SetDate(day, month, year)
| Changes the internal date of the oscilloscope. ``day`` and ``month`` must be two digits, ``year`` must be four digits.
.. method:: Unlock()
| Enables all frontpanel buttons and knobs on the oscilloscope, after they have been locked by :meth:`Lock`
