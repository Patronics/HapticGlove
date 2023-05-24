# HapticGlove

## A project for HackDavis 2023
Read our Devpost https://devpost.com/software/haptic-hand!
Our project won the award for "Best Hardware Hack" as part of Hack Davis 2023!

## Description

### Inspiration

We wanted to focus on accessibility for our project, as it is a topic we feel needs to be addressed more often when designing technology. We initially thought of creating a multifunctional glove that could act as both a walking stick and could function as a TTS braille translator for those still learning braille through the use of a camera. In the end, we decided to keep our goals realistic and focus on the virtual walking stick aspect of the glove for the duration of the Davis Hackathon.

### What it does

The Haptic Glove helps the visually impaired navigate obstacles in their space by acting as a "virtual walking stick." Unlike a physical walking stick, the haptic glove can be easily aimed to detect obstructions in any direction the user can point their fingers in. Our glove is designed to give the wearer a sense of the distance between them and objects in their path through the use of a vibrating motor in the thumb. The closer the user is to an object, the stronger it vibrates, and the further away the user is, the less intense the vibration becomes. This helps the navigator using the glove determine if an object is in front of them and allow them to tell their relative distance from the object, all without actually touching the object! The distance which the glove can detect can be physically adjusted with the potentiometer in the glove itself, so it can be used by people of various heights, and for other challenging environments and uses!

### How we built it

We decided to utilize an infrared sensor to detect objects about 1.2 meters away. By connecting the sensor to a DC motor and attaching the device to a glove, we made the Haptic Glove. We brought many of the materials ourselves, such as wires and the infrared sensor, but some things, such as the DC motor, velcro, and the glove itself, we needed to get ourselves. We started building the glove by gathering materials to create a device that could cause the motor to adjust its speed based on the distance detected by the sensor. For example, the DC motor we scavenged from a toothbrush, and the glove we bought from Walmart. First, we accessed the distance readings from the sensor and utilized Python to program the motor spin faster when the sensor reads less distance between it an a detected object, and to stop spinning when it cannot detect any objects within a range of 1.2 meters. Then we needed to power the motor controller and attach it to the glove in a compact way that would not impact the user's ability to move too much. We decided to have the raspberry pi pico microcontroller on the back of the hand, the infrared sensor on the tip of the longest finger (to have a better range of motion in pointing the sensor that one would on the palm or the back of the hand), and put the vibration motor on the thumb.

### Challenges we ran into

When prototyping for our project, we started off by connecting all of our components to a raspberry pi pico using a standard breadboard. When it came to mounting our project to our glove and preserving its functionality, we quickly realized that our project would have to take a smaller form in order to fit all of our components and preserve the user's comfort and practicality of the device. In our process to solder all of our components onto a strip board to replace the bulky breadbox, we were tasked with making and discarding many design choices as to how the user would use our device in a real world setting. We also had a couple issues with finding a way to get enough volts to power the motor, and we ended up needing to upgrade from 1 AA battery to 3, on a separate power supply from the pi, which required a battery pack to by carried separate from the glove itself. Finally, we ran into many technical issues in soldering and adjusting the wire lengths to a non-obtrusive size that would be less likely to catch on obstacles and would not obstruct the sensor.

### Accomplishments that we're proud of

We were able to put together a distance-sensitive glove motor within a few hours! The rest of the time was buying materials for the glove and trying to attach the components to the glove in a way that was practical. Additionally, we are very proud of the way the glove looks and feels, very comfortable and sci-fi. We are also very happy with the range of motion the glove and the functionality of the sensor. Finally, we are happy we were able to implement the physically adjustable range of the glove's sensor, which is really useful, especially for challenging environments like stairs.

### What we learned

We learned a lot from this years Hackathon. First of all, we came much better prepared this year than last year. We had the majority of the components we needed to feasibly consider this idea, and spent much less time at the store. Because we came better prepared, we were able to finish the project very quickly, and even get some sleep during the Hackathon!

### What's next for Haptic Hand

In the future, our team wants to implement more functionality in the Haptic Hand, such as adding the brail and English Text-To-Speech feature to make the glove a multifaceted tool. Another goal of ours is to rebuild the glove with better hardware. Currently, our sensor has a max detection range of 1.2 meters. We want to extend that range so that the glove can detect objects that are further away, and thus give our users the option of having more warning. We also would want a motor with more speed control and access to a stronger vibration setting. Most crucially, we want to test our glove out with real-world potential users and obtain feedback from them on how to make the Haptic Glove better.

## Technical Details

### Specs:
Uses a VL53L0X distance sensor to provide haptic input to a user, serving as a virtual cane.
Uses Raspberry Pi Pico running CircuitPython 8
Uses a simple DC motor as the vibration output.
### Dependencies:
From [Adafruit circuitPython bundle](https://github.com/adafruit/circuitpython):
- adafruit_bus_device
- adafruit_motor
- adafruit_motorkit.mpy

Download Seprately:
- [adafruit-circuitpython-vl53l0x-8.x-mpy-3.6.8](https://github.com/adafruit/Adafruit_VL53L0X)

### Resources:


https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html
https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf
