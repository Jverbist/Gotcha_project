# A model for a user in the game Gotcha
class Player():
    def __init__(self, name, email, password, image, location, target, alive, kills):
        self.name = name
        self.email = email
        self.password = password
        self.image = image
        self.location = location
        self.target = target
        self.alive = alive
        self.kills = kills
    def __repr__(self):
        return '<Player %r>' % self.name


# A model for a game in the game Gotcha
class Game():
    def __init__(self, name, start_date, end_date, players):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
    def __repr__(self):
        return '<Game %r>' % self.name

