from locust import HttpUser, between, task
import base64

class APIUser(HttpUser):
    wait_time = between(1, 5)

    # Put your stress tests here.
    # See https://docs.locust.io/en/stable/writing-a-locustfile.html for help.
    # TODO
    @task
    def index(self):
        self.client.get("/")
        
        
    @task
    def predict(self):
        with open("stress_test/dog.jpeg", "rb") as image_file:
            image_name = image_file.name
            image_data = image_file.read()
            files = {'file': (image_name, image_data)}
            self.client.post("/predict", files=files)
        

