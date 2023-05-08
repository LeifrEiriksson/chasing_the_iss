from Components import (Astrolabe, ImageOfDay, InternationalSpaceStation,
                        IssDataStreaming, My_Location)

me = My_Location.Where_Am_I()
iss = InternationalSpaceStation.Iss()
astrolabe = Astrolabe.Astrolabe()
data_streaming = IssDataStreaming.ISS_Monitoring()
image = ImageOfDay.ImageOfDay()
