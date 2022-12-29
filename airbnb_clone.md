# API Planning:

### Rooms

GET[X] POST[X] /rooms [X]
GET[X] PUT DELETE /rooms/1 [X]
GET /rooms/1/amenities [X]
GET POST[X] /rooms/1/reviews [X]
GET POST /rooms/amenities [X]
GET PUT DELETE /rooms/amenities/1 [X]
POST /rooms/1/photos [X]
DELETE /rooms/1/photos/2 >>> /medias/photos/1 [X]

### Experiences

GET POST /experiences
GET PUT DELETE /experiences/1
GET /experiences/1/perks
GET POST /experiences/1/bookings
GET PUT DELETE /experiences/1/bookings/2
GET POST /perks [X]
GET PUT DELETE /perks/1 [X]

### Medias

POST /medias
DELETE /medias/1
DELETE /medias/photos/1 [X]

### Users

### Categories

GET POST /categories [X]
GET(Rooms) PUT DELETE /categories/1 [X]
