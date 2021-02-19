import sqlite3 as sql

con = sql.connect('test.db')


class GameClass:

    def __init__(self, usersValue):
        self.usersValue = usersValue

    def citiesGame(self):
        with con:
            cur = con.cursor()
            self.usersValue = str(input("> "))
            self.usersValue = self.usersValue[0].upper() + self.usersValue[1:].lower()
            cur.execute(f"SELECT field1, field5,field6 from '_cities' WHERE field5 = '{self.usersValue}';")
            self.rows = cur.fetchone()

            try:
                if self.usersValue.lower() == self.rows[1].lower() and self.rows[2] == 'false':
                    cur.execute(f"UPDATE _cities SET field6 = 'true' WHERE field5 LIKE '{self.usersValue}';")
                    cur.execute(f"SELECT field1, field5,field6 from '_cities' WHERE field5 LIKE '{self.usersValue[-1:].upper()}%' AND field6 = 'false';")
                    self.answer = cur.fetchone()
                    cur.execute(f"UPDATE _cities SET field6 = 'true' WHERE field5 LIKE '{self.answer[1]}';")
                    print("Nice:")
                    return print(self.answer[1])
                else:
                    return print("Город уже использовался")
            except TypeError:
                return print("Looser")


game = GameClass(1)
game.citiesGame()
