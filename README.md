# Chasing the ISS! (And streaming data)

<p align="left"><img src= "https://img.shields.io/badge/Status-Constantly%20Updated-brightgreen"></p>

<p align="center"><img src= "https://user-images.githubusercontent.com/92702848/217097355-658b747d-039e-440f-8930-83e8d5d2abc8.jpg"></p>

<p align="center">"Ground Control to Major Tom..."</p>


# 🌌 Briefing

Initially, I thought about ways to start a space trip, but I wasn't sure where to start, so I built a rocket using components that could take me to the ISS.

Jokes aside, the idea of monitoring the ISS seemed like an excellent starting point for the project, both because of the information we have about it and the fact that it is relatively simple to access through the use of APIs. Our goal is to monitor its trajectory around the Earth, which is blue!

The project was based on Object-Oriented Programming, with the aim of providing robustness to the codes and modularizing our objectives, aiming for greater scalability in the future, in case we also want to monitor other space objects that may be valid within the scope of this project.

The "Components" file received this name precisely because it alludes to the components of a rocket, but you will notice that when accessing it, we will see other information closer to "locations" than to a propeller or fuselage.

Beyond creating objects capable of providing information about the ISS and ourselves in relation to the Earth, it is also important to capture and structure this information for future studies, applying, perhaps, Data Science concepts. For this, I created an architecture in Docker, containing a Postgres database and a Debezium connector so that we can transmit the data to Kafka. The objective is both to have a messaging system through the prompt while our Python script runs independently, and to provide streaming data for consumption on other platforms, such as Spark (this part is still being worked on and thought out).

(Note: You can consult the docker-compose through Docker_configurations, where we also have the JSON used to configure the connector.)

# :rocket: APIs

 - Open Notify - International Space Station Current Location: http://open-notify.org/Open-Notify-API/ISS-Location-Now/  
 - NASA -  Astronomy Picture of the Day(APOD): https://api.nasa.gov/ 

# :telescope: POO - Components

 - `My_Location:` get informations about my current position (latitude, longitude and also my city - through the IP).
 - `InternationalSpaceStation:` return informations about the API status, current latitude, longitude and about the astronauts.
 - `Astrolabe:` using the inheritance concept, here, we can chase the ISS with the compass, current country of ISS, and the distance between me and the astronauts. At this point its important to highlight that the distance use the haversine formula, which considers the non-euclidean geometry of the Earth, that's return the distance more accurately.
 - `Image Of Day:` here we can access the NASA's image of the day, if you want you can access it with your personal API key, but if you don't have any key, don't worry, there's a DEMO key (with some requests limits).
 - `IssDataStreaming:` also using the inheritance, here we can start our streaming and send data to Postgres.

 
 

