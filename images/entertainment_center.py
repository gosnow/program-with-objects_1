import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

frequencies = media.Movie("Frequencies",
                          "In a parallel world two people have divergent frequencies.",
                          "http://ia.media-imdb.com/images/M/MV5BMjIwMDM1MzgxMF5BMl5BanBnXkFtZTgwNzE0MjE4MTE@._V1_SX214_AL_.jpg",
                          "https://www.youtube.com/watch?v=pmSfzixf314")

fearless = media.Movie("Fearless",
                       "After surviving a plane crash, a man seemingly becomes invincible.",
                       "http://www.impawards.com/1993/posters/fearless_ver2.jpg",
                       "https://www.youtube.com/watch?v=Tm5jBa4LzxQ")


#avatar.show_trailer()
#print(avatar.storyline)

movies = [toy_story, avatar, frequencies, fearless]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
