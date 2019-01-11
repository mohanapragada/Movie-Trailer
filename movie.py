import fresh_tomatoes
import media
doraemon=media.MovieTrailer("Doraemon","doraemon comes to future robot he saves the boy",
                            "images/doraemon.jpg",
                            "https://www.youtube.com/watch?v=RS7Aecxbyh8")
Toy_Story=media.MovieTrailer("ToyStory","toys can plays with their friends",
                             "images/toystory.jpg",
                             "https://www.youtube.com/watch?v=P9-jf9-c9JM")
harrypotter=media.MovieTrailer("Harry Potter","harry saves their magic school",
                             "images/harrypotter.jpg",
                             "https://www.youtube.com/watch?v=VyHV0BRtdxo")
dinosaur=media.MovieTrailer("The Good Dainosaur","dainosaur can helps the other animals",
                             "images/dinosaur.jpg",
                             "https://www.youtube.com/watch?v=cc6THZw_uuc")
peanuts=media.MovieTrailer("The Peanuts","the animals can fight the peanuts",
                             "images/peanuts.jpg",
                             "https://www.youtube.com/watch?v=8pCoVQDD-OY")
conjuring=media.MovieTrailer("The Conjuring2","the animals can fight the peanuts",
                             "images/conjuring.jpg",
                             "https://www.youtube.com/watch?v=VFsmuRPClr4")
mayamall=media.MovieTrailer("MayaMall","the animals can fight the peanuts",
                             "images/mayamall.jpg",
                             "https://www.youtube.com/watch?v=sXz9u1sHV2w")
movies=[doraemon,Toy_Story,harrypotter,dinosaur,peanuts,conjuring,mayamall]
fresh_tomatoes.open_movies_page(movies)
