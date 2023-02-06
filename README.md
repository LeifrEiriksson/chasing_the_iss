# Chasing the ISS!
<p align="left"><img src= "https://img.shields.io/badge/Status-Constantly%20Updated-brightgreen"></p>

A simple Python project about space, especially the ISS. The objective is to calculate the distance between you and the ISS and get some information about it, such as who is on it, what country it is flying over.

<p align="center"><img src= "https://user-images.githubusercontent.com/92702848/217097355-658b747d-039e-440f-8930-83e8d5d2abc8.jpg"></p>

# 🌌 Briefing

This project starts with my curiosity about the space, so, if you think about it you can travel through your ideas in a infinite trip like the universe. 
But I needed a starting point, instead of trying to keep with a pretentious project, I prefer to make simple code with few objects(POO) that give me the position on the ISS and who is inside.
The first step was the searching about APIs that give me the localization of the ISS and more (like the famous NASA's Picture of the day), so, I got it!

# :rocket: APIs

 - Open Notify - International Space Station Current Location: http://open-notify.org/Open-Notify-API/ISS-Location-Now/  
 - NASA -  Astronomy Picture of the Day(APOD): https://api.nasa.gov/ 

# :telescope: POO - Components

 - `Where Am I?:` get informations about my current position (latitude, longitude and also my city).
 - `ISS:` return informations about the API status, current latitude, longitude and about the astronauts.
 - `Astrolabe:` using the inheritance concept, here, we can chase the ISS with the compass, current country of ISS, and the distance between me and the astronauts. At this point its important to highlight that the distance use the haversine formula, which considers the non-euclidean geometry of the Earth, that's return the distance more accurately.
 - `Image Of Day:` here we can access the NASA's image of the day, if you want you can access it with your personal API key, but if you don't have any key, don't worry, there's a DEMO key (with some requests limits).
 
 # 🌃 But what about JUPYTER NOTEBOOK? 
 It's my sandbox ( ͡° ͜ʖ ͡°)
 
 

