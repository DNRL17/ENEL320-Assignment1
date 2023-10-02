<h1>
ENEL320 Assignment 1
</h1>

<h2>
Introduction
</h2>
<h2>
Q1
</h2>

![Q1](/images/Q1_image.JPG)
<h3>
a)
</h3>

![Model Waveform 1](/images/Model_of_Pulse_Doppler_Radar_Waveform.png)

<h3>
b)
</h3>

![Model Waveform 2](/images/Model_of_Pulse_Doppler_Radar_Waveform.png)

<h3>
c)
</h3>

<p>
Fourier Transform expression of the model Pulse Doppler Radar waveform signal:
</p>

![Fourier Transform Expression of Doppler Pulse](/images/Fourier_Transform_Expression_for_Doppler_Pulse.JPG)

<p>
Simplified Fourier Expression by only looking at one pulse, removing the summation from the equation and simplifying the bounds. 
</p>

![Simplified Fourier Expression](/images/Simplfied_Fourier_Transform_Expression.JPG)

<p>
It is worth noting however, that the real world signal is periodic, while the simplified expression only looks at a single period of the ideal signal.
</p>

<h3>
d)
</h3>
<p>
The model from part b models the signal with some AWGN added to the signal to simulate the transmission of a signal through objects (not free-space) as well as any Johnson noise. The model however still relies on a few assumptions that are dificult to count on in practice such as: <br>

- The transmitted frequency is perfect (no variation)
- The impulse response approaches infinity (not possible - only have finite energy in practice)
- The transmitted frequency is 1 Hz, different in practice

To test the model, we can use a signal generator to modulate the two waveforms using the RF function, transmit via a transmission line and measure the response through a medium (the wire) using an oscilloscope. This test should be able to show some of the non-ideal characteristics that influence the waveform in the real-world.

To improve the model adding variation to the frequency can make it more realistic.
</p>

<h2>
Q2
</h2>

![Q2](/images/Q2_image.JPG)

<h3>
a)
</h3>

![Modulated image u=0.5](/images/RX%20and%20Tx%20Design.jpg)
<h3>
b)
</h3>
<p>
  The code for Question 2 can be found in Q2_code.py
</p>
<h3>
c)
</h3>
<p>
  The image below shows the modulated signal shown in Lecture example 5.4 and a u of 0.5.
</p>

![Modulated image u=0.5](/images/mod%20u=0.5.png)
<p>
  The image below shows the demodulated signal shown in Lecture example 5.4 and a u of 0.5.
</p>

![Final message u=0.5](/images/msg%20u%20=%200.5.png)
<p>
  The image below shows the modulated signal shown in Lecture example 5.4 and a u of 1.
</p>

![Modulated image u=1](/images/mod%20u%20=%201.png)
<p>
  The image below shows the demodulated signal shown in Lecture example 5.4 and a u of 1.
</p>

![Final message u=1](/images/msg%20u%20=%201.png)
<h3>
d)
</h3>
<p>
  The demodulator for the model signal did not work for the song. To get the demodulator to <br />
  work for the song I had to implement a band pass filter.<br />
  The song is from the musical Aladin.
</p>
<h3>
e)
</h3>
<p>
  The system can take noise up to around a scale of 0.5 at which point the song can't be heard.<br />
  The measurement of the haywireness in the system is a value along a normal distribution where 50 <br />
  is the mean and 0 is the minimum.
</p>

<h2>
Q3
</h2>

![Q3](/images/Q3_image.JPG)

<h3>
b)
</h3>
<p>
  The following image shows the waterfall of a French AM radio at the frequiencie 17864.46 kHz and was found<br />
  at 6:10pm on the 5/9/23. 
</p>

![French AM radio](/images/AM%20signal%20Fench%2017864.46.png)
<p>
  The next image is shows the waterfall of a LSB Radio at 7157.03 kHz and was found at 6:00pm on 5/9/23.
</p>

![LSB Radio](/images/LSB%20radio%207157.03.png)
<p>
  The folling image is a waterfall of a morse code signal found at 14027 kHz at 8:00pm on the 5/9/23.
</p>

![Morse code](/images/Morse%20Code%2014027.png)
<p>
  the next waterfall is a fax signal at 13988.50 kHz and was found at 8:30pm
</p>

![Japan metro fax](/images/Weird%20signal%2013988.50.png)
