import fresh_tomatoes
import media

""" The creates instances of Movie """

blue_jasmine = media.Movie("Blue Jasmine",
												 "July 26, 2013", 
												 "The story of a rich Manhattan socialite (played by Cate Blanchett) falling into poverty and homelessness",
												 "http://upload.wikimedia.org/wikipedia/en/thumb/3/3f/Blue_Jasmine_poster.jpg/220px-Blue_Jasmine_poster.jpg",
												 "http://www.youtube.com/watch?v=tWLtj4LY5CA")

hunger_games = media.Movie("Hunger Games",
											"2012",
										  "The dystopian nation of Panem consists of a wealthy, glamorous Capitol, ruled by President Snow, ruling twelve poorer districts.",
										  "http://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
										  "http://www.youtube.com/watch?v=4S9a5V9ODuY")

kill_bill = media.Movie("Kill Bill",
											"March 5, 2003",
										  "It stars Uma Thurman as the Bride, who seeks revenge on an assassination squad led by Bill (David Carradine) after they try to kill her and her unborn child.",
										  "http://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Kill_bill_vol_one_ver.jpg/220px-Kill_bill_vol_one_ver.jpg",
										  "http://www.youtube.com/watch?v=ot6C1ZKyiME")

pulp_fiction = media.Movie("Pulp Fiction",
											"September 10, 1994",
										  "American black comedy crime film written and directed by Quentin Tarantino, from a story by Tarantino and Roger Avary.",
										  "http://upload.wikimedia.org/wikipedia/en/thumb/8/82/Pulp_Fiction_cover.jpg/220px-Pulp_Fiction_cover.jpg",
										  "http://www.youtube.com/watch?v=s7EdQ4FqbhY")

amelie = media.Movie("Amelie",
											"April 25, 2001",
										  "A painfully shy waitress working at a tiny Paris cafe, Amelie makes a surprising discovery and sees her life drastically changed for the better.",
										  "http://upload.wikimedia.org/wikipedia/en/thumb/5/53/Amelie_poster.jpg/220px-Amelie_poster.jpg",
										  "http://www.youtube.com/watch?v=sECzJY07oK4")

crouching_tiger_hidden_dragon = media.Movie("Crouching Tiger, Hidden Dragon",
											"July 6, 2000",
										  "The film is set in the Qing Dynasty during the 43rd year (1779) of the reign of the Qianlong Emperor.",
										  "http://upload.wikimedia.org/wikipedia/en/thumb/9/97/Crouching_tiger_hidden_dragon_poster.jpg/220px-Crouching_tiger_hidden_dragon_poster.jpg",
										  "http://www.youtube.com/watch?v=iv_ed5VmoD8")

""" This sets a list of the instances of Movie """

movies = [blue_jasmine, 
					hunger_games, 
					kill_bill, 
					pulp_fiction, 
					amelie, 
					crouching_tiger_hidden_dragon]

""" This passes the list of instances of Movie to the movie page"""					

fresh_tomatoes.open_movies_page(movies)

