import datetime
import time

import psycopg2

from Components.Astrolabe import Astrolabe
from Components.InternationalSpaceStation import Iss
from Components.My_Location import Where_Am_I


class ISS_Monitoring(Astrolabe, Iss):

    def __init__(self):

        super().__init__()

        self.user = None
        self.password = None
        self.host = None
        self.port = None
        self.database = None
        self.connection = None

    def iss_database_connection(self):

        while True:

            self.user = input("Database user:")
            self.password = input("Database password:")
            self.host = input("Database host:")
            self.port = input("Database port:")
            self.database = input("Database:")

            try:

                self.connection = psycopg2.connect(
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    port=self.port,
                    database=self.database
                )

                return "Success!"

            except psycopg2.Error as error:

                print(
                    f"Database connection error! \n-- {error}\nPlease try again!")

            except KeyboardInterrupt:

                print("Interrupted")

    def iss_data_streaming(self):

        self.psql_query = """INSERT INTO iss_monitoring ("iss_lat", "iss_long", "current_country", "iss_time", "current_time", "current_date") VALUES (%s, %s, %s, %s, %s, %s);"""
        self.warning = "Connection database OK!\nStarting the streaming... \nPress CTRL+C to stop."
        self.data = None
        self.data_err = None
        self.cursor = None

        try:

            self.iss_database_connection() if self.connection == None else print(self.warning)

            print(self.warning)

            self.cursor = self.connection.cursor()

            while True:

                if Iss().response['message'] == 'success':

                    self.data = (Iss().position()[0],
                                 Iss().position()[1],
                                 Astrolabe().iss_country(),
                                 Iss().iss_time,
                                 datetime.datetime.now().strftime('%H:%M:%S'),
                                 datetime.datetime.now().strftime('%Y-%m-%d')
                                 )

                    self.cursor.execute(self.psql_query, self.data)

                    self.connection.commit()

                    time.sleep(30)

                else:

                    self.data_err = (
                        None,
                        None,
                        "COMMUNICATION ERROR",
                        None,
                        datetime.datetime.now().strftime('%H:%M:%S'),
                        datetime.datetime.now().strftime('%Y-%m-%d')
                    )

                    self.cursor.execute(self.psql_query, self.data_err)

                    self.connection.commit()

                    print("ISS Communication Error")

                    time.sleep(30)

        except KeyboardInterrupt:

            if self.connection:
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")
            pass
