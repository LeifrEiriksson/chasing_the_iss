# Chasing the ISS! (And streaming data)

<p align="left"><img src= "https://img.shields.io/badge/Status-Constantly%20Updated-brightgreen"></p>

<p align="center"><img src= "https://user-images.githubusercontent.com/92702848/217097355-658b747d-039e-440f-8930-83e8d5d2abc8.jpg"></p>

<p align="center">"Ground Control to Major Tom..."</p>


# 🌌 Briefing

This project originated from a simple and personal idea: the desire to explore space! 
I know that the International Space Station is not a celestial body in the proper sense, or what we consider a "natural" celestial body, but it seemed to me an excellent starting point as it is easily trackable through the use of APIs, and for a beginner's project, the challenge seemed satisfactory. 
Initially, I opted for the use of Object-Oriented Programming in Python (OOP) as it seemed like a safe and robust alternative for our studies, and its modularization would allow for greater scalability in the future, in case we intend to expand the scope of our studies to other satellites, for example

# :rocket: APIs

 - Open Notify - International Space Station Current Location: http://open-notify.org/Open-Notify-API/ISS-Location-Now/  
 - NASA -  Astronomy Picture of the Day(APOD): https://api.nasa.gov/ 

# :telescope: POO - Components

 - `Where Am I?:` get informations about my current position (latitude, longitude and also my city).
 - `ISS:` return informations about the API status, current latitude, longitude and about the astronauts.
 - `Astrolabe:` using the inheritance concept, here, we can chase the ISS with the compass, current country of ISS, and the distance between me and the astronauts. At this point its important to highlight that the distance use the haversine formula, which considers the non-euclidean geometry of the Earth, that's return the distance more accurately.
 - `Image Of Day:` here we can access the NASA's image of the day, if you want you can access it with your personal API key, but if you don't have any key, don't worry, there's a DEMO key (with some requests limits).

 
 

