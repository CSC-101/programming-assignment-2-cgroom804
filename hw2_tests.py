import data
import hw2
import unittest
from hw2 import create_rectangle, shorter_duration_than, song_shorter_than, running_time, validate_route, \
    longest_repetition


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        point1 = data.Point(2, 4)
        point2 = data.Point(5,5)
        result = create_rectangle(point1, point2)
        expected = data.Rectangle(data.Point(2,5), data.Point(5,4))
        self.assertEqual(result, expected)

    def test_create_rectangle2(self):
        point1 = data.Point(3, 5)
        point2 = data.Point(3,6)
        result = create_rectangle(point1, point2)
        expected = data.Rectangle(data.Point(3,6), data.Point(3,5))
        self.assertEqual(result, expected)
    # Part 2
    def test_shorter_duration_than1(self):
        time1 = data.Duration(2,13)
        time2 = data.Duration(2,40)
        result = shorter_duration_than(time1, time2)
        expected = True
        self.assertEqual(result,expected)

    def test_shorter_duration_than2(self):
        time1 = data.Duration(3,23)
        time2 = data.Duration(2,47)
        result = shorter_duration_than(time1, time2)
        expected = False
        self.assertEqual(result,expected)
    # Part 3
    def test_song_shorter_than1(self):
        song_list = [data.Song("Heman", "HeeHee", data.Duration(2, 45)),
                     data.Song("Michael Jackson", "Heal the World", data.Duration(3,32))]
        result = song_shorter_than(song_list, data.Duration(3,00))
        expected = [data.Song("Heman", "HeeHee", data.Duration(2, 45))]
        self.assertEqual(result, expected)

    def test_song_shorter_than2(self):
        song_list = [data.Song("Heman", "HeeHee", data.Duration(2, 45)),
                     data.Song("Michael Jackson", "Heal the World", data.Duration(3, 32)),
                     data.Song("Cole Groom", "Happy Days", data.Duration(1,30))]
        result = song_shorter_than(song_list, data.Duration(3, 00))
        expected = [data.Song("Heman", "HeeHee", data.Duration(2, 45)),
                    data.Song("Cole Groom", "Happy Days", data.Duration(1,30))]
        self.assertEqual(result, expected)

    # Part 4
    def test_running_time1(self):
        song_list = [data.Song("Heman", "HeeHee", data.Duration(2, 45)),
                     data.Song("Michael Jackson", "Heal the World", data.Duration(3, 32)),
                     data.Song("Cole Groom", "Happy Days", data.Duration(1,30))]
        playlist = [0,1,2]
        result = running_time(song_list, playlist)
        expected = data.Duration(7,47)
        self.assertEqual(result, expected)

    def test_running_time2(self):
        song_list = [data.Song("Heman", "HeeHee", data.Duration(2, 45)),
                     data.Song("Michael Jackson", "Heal the World", data.Duration(3, 32)),
                     data.Song("Cole Groom", "Happy Days", data.Duration(1,30)),
                     data.Song("Michael Jackson", "Heal the World", data.Duration(3, 32))]
        playlist = [0,1,2,1]
        result = running_time(song_list, playlist)
        expected = data.Duration(11,19)
        self.assertEqual(result, expected)

    # Part 5
    def test_validate_route1(self):
        city_links =[['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'],
        ['atascadero', 'santa margarita'],['atascadero', 'creston']]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        result = validate_route(city_links, route)
        expected = True
        self.assertEqual(result, expected)

    def test_validate_route2(self):
        city_links =[['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'],
        ['atascadero', 'santa margarita'],['atascadero', 'creston']]
        route = ['san luis obispo', 'atascadero', 'pismo beach']
        result = validate_route(city_links, route)
        expected = False
        self.assertEqual(result, expected)

    # Part 6
    def test_longest_repetition1(self):
        numbers =[0,0,1,2,3,4,4,4,5,6,6,7,8,8]
        result = longest_repetition(numbers)
        expected = 5
        self.assertEqual(result, expected)

    def test_longest_repetition1(self):
        numbers = [1, 1, 2, 2, 1, 1, 1, 3]
        result = longest_repetition(numbers)
        expected = 4
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()

