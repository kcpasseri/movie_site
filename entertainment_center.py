import media
import fresh_tomatoes
#Creates Toy Story entry
toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#Creates Avatar entry
avatar = media.Movie("Avatar",
                     "A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#Creates Kingsman: The Secret Service entry
kingsman = media.Movie("Kingsman: The Secret Service",
                       "A spy organization recruits an unrefined, but promising street kid into the agency's ultra-competitive training program, just as a global threat emerges from a twisted tech genius.",
                       "http://ia.media-imdb.com/images/M/MV5BMTkxMjgwMDM4Ml5BMl5BanBnXkFtZTgwMTk3NTIwNDE@._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=m4NCribDx4U")
#Creates Slumdog Millionaire entry
slumdog = media.Movie("Slumdog Millionaire",
                      'A Mumbai teen who grew up in the slums, becomes a contestant on the Indian version of "Who Wants To Be A Millionaire?" He is arrested under suspicion of cheating, and while being interrogated, events from his life history are shown which explain why he knows the answers.',
                      "http://ia.media-imdb.com/images/M/MV5BMTU2NTA5NzI0N15BMl5BanBnXkFtZTcwMjUxMjYxMg@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                      "https://www.youtube.com/watch?v=AIzbwV7on6Q")
#Creates Radio entry
radio = media.Movie("Radio",
                    "The story of a high school coach and the developmentally challenged man whom he took under his wing.",
                    "http://ia.media-imdb.com/images/M/MV5BMTY0NzU0NTY3OV5BMl5BanBnXkFtZTcwNDM2MTYyMQ@@._V1_SX214_AL_.jpg",
                    "https://www.youtube.com/watch?v=IWinwCMRJrc")
#Creates Focus entry
focus = media.Movie("Focus",
                    "In the midst of veteran con man Nicky's latest scheme, a woman from his past - now an accomplished femme fatale - shows up and throws his plans for a loop.",
                    "http://ia.media-imdb.com/images/M/MV5BMTUwODg2OTA4OF5BMl5BanBnXkFtZTgwOTE5MTE4MzE@._V1_SX214_AL_.jpg",
                    "https://www.youtube.com/watch?v=MxCRgtdAuBo")

movies = [toy_story, avatar, kingsman, slumdog, radio, focus]
fresh_tomatoes.open_movies_page(movies)
#movie descriptions from IMDB
