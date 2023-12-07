# Event-Driven-Architecture-with-RabbitMQ

![download](https://github.com/dev-jaswanthraj/Event-Driven-Architecture-with-RabbitMQ/assets/64518811/837f8cb8-98b8-4662-a345-649937cfe78e)
🛠 Developed the "Event Driven Architecture" for Microservices with the help of :
1. Rabbit MQ - Messaging Broker ✉ 
2. Django API - Service 1 ⚙ 
3. Flask API - Service 2 ⚙ 

🖌 Design of the Services :
🌐 Django: 
 💿 Product DB (Title, Image URL, Likes)
 💿 User DB (Pk)
 📌 The Django API will Publish the Message to the Queue 1 when the Product is Created , Updates and Deleted then consumed by the Flask API. 
 📌 Also Django API will Provide User Data to the Flask API for "Like (Like Option to the Product)" Service.
 📌 Django Application Subscribed to Queue 2 to get the Like Event.

🌐 Flask:
 📀 Product DB (Title, Image URL, Likes)
 📀 ProductUser DB(user_id {from django API}, product_id)
 📌 The Flask Application will Consume the Message from Queue 1 to store the Product item.
 📌 While the Product gets the Like the Flask Application will Publish the Message to Queue 2 then consumed by Django API.
 📌 When Product gets Like, Flask Application will hit the Django Endpoint to get the user pk.
