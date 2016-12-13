import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=vwyZH85NQC4")

The_devils_double = media.Movie("The_devils_double",
                                "The story of the son of sadam hussain's body double",
                                "https://upload.wikimedia.org/wikipedia/en/4/4c/The_Devil%27s_Double.jpg",
                                "https://www.youtube.com/watch?v=2-MsGEWFiYg",)

Movie_300 = media.Movie("300",
                  "300 spartans vs an amry of persians",
                  "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
                  "https://www.youtube.com/watch?v=wDiUG52ZyHQ")
            
Ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
Star_Wars_Episode_III = media.Movie("Star_Wars_Episode_III",
                                    "Akin Skywalker goes dark",
                                    "https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",
                                    "https://www.youtube.com/watch?v=5UnjrG_N8hU")

Office_Space = media.Movie("Office_Space ",
                           "A movie about how work sucks",
                           "https://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",
                           "https://www.youtube.com/watch?v=kwQziVIzDeg")
#movies = [toy_story, The_devils_double, 300, Ratatouille, Star_Wars_Episode_III , Office_Space  ]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.valid_ratings)




                        
