import unittest
import datetime
from UniversityResponse import UniversityResponse
from utility import difference, average
from message_reader import MessageManipulator
from parseFile import FileParser


class ModuleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.file = "stream.txt"
        self.msg = MessageManipulator()
        self.parser = FileParser()

    def test_response(self):
        result = UniversityResponse()
        response = result.response_time()
        expected = {'UCL': datetime.timedelta(seconds=300), 'Edinburgh':
            datetime.timedelta(seconds=16114, microseconds=428571)}

        self.assertEqual(expected, response)

    def test_average(self):
        date_list = [datetime.timedelta(seconds=1800), datetime.timedelta(seconds=1800),
                     datetime.timedelta(seconds=7200), datetime.timedelta(seconds=1),
                     datetime.timedelta(seconds=1000), datetime.timedelta(seconds=1000),
                     datetime.timedelta(days=1, seconds=13600)]

        result = average(date_list)
        expected = date_list[0]

        self.assertEqual(type(expected), type(result))

    def test_difference(self):
        d1 = datetime.timedelta(seconds=1800)
        d2 = datetime.timedelta(seconds=1800)
        result = difference(d1, d2)
        self.assertEqual('0:00:00', str(result))

    def test_mentor_negative(self):
        user = 'Emma'
        result = self.msg.is_mentor(user)
        self.assertEqual(False, result)

    def test_mentor(self):
        user = 'Joe'
        result = self.msg.is_mentor(user)
        self.assertEqual(True, result)

    def test_applicant_negative(self):
        user = 'Joe'
        result = self.msg.is_applicant(user)
        self.assertEqual(False, result)

    def test_applicant(self):
        user = 'Emma'
        result = self.msg.is_applicant(user)
        self.assertEqual(True, result)

    def test_file_parser_user(self):
        user = {'Emma': None, 'Maria': None, 'Sam': 'UCL', 'Joe': 'Edinburgh',
                'Yannis': 'Edinburgh', 'Tom': None, 'Dave': 'Glasgow'}

        result = self.parser.get_user()
        self.assertEqual(user,result)

    def test_file_parser_chat(self):
        chat = {1: ('Emma', 'Sam'), 2: ('Emma', 'Joe'), 3: ('Emma', 'Dave'),
                4: ('Maria', 'Yannis')}

        result = self.parser.get_chat_groups()
        self.assertEqual(chat, result)

    def test_file_parser_message(self):
        msg = [['Message', 'Emma', '1', 'Hello', datetime.datetime(2015, 1, 1, 15, 30)],
         ['Message', 'Sam', '1', 'Hello', datetime.datetime(2015, 1, 1, 15, 31, 40)],
         ['Message', 'Sam', '1', 'Hello', datetime.datetime(2015, 1, 1, 15, 33, 20)],
         ['Message', 'Emma', '1', 'Hello', datetime.datetime(2015, 1, 1, 15, 38, 20)],
         ['Message', 'Sam', '1', 'Hello', datetime.datetime(2015, 1, 1, 15, 46, 40)],
         ['Message', 'Emma', '2', 'Hey how are you', datetime.datetime(2015, 1, 1, 16, 30)],
         ['Message', 'Emma', '2', 'Could you tell me about the university?', datetime.datetime(2015, 1, 1, 17, 0)],
         ['Message', 'Joe', '2', 'Welcome', datetime.datetime(2015, 1, 1, 17, 30)],
         ['Message', 'Joe', '2', 'I am Joe', datetime.datetime(2015, 1, 1, 18, 0)],
         ['Message', 'Emma', '2', "That's great", datetime.datetime(2015, 1, 1, 18, 30)],
         ['Message', 'Joe', '2', 'I know', datetime.datetime(2015, 1, 1, 20, 30)],
         ['Message', 'Emma', '2', 'Speak another time', datetime.datetime(2015, 1, 2, 1, 0)],
         ['Message', 'Dave', '3', 'Hey', datetime.datetime(2015, 1, 2, 1, 0, 1)],
         ['Message', 'Maria', '4', 'Hey Yannis', datetime.datetime(2015, 1, 2, 1, 0, 1)],
         ['Message', 'Yannis', '4', 'Hey Maria', datetime.datetime(2015, 1, 2, 1, 16, 41)],
         ['Message', 'Yannis', '4', 'Welcome to uni', datetime.datetime(2015, 1, 2, 1, 33, 21)],
         ['Message', 'Yannis', '4', 'I hope u are doing great', datetime.datetime(2015, 1, 2, 1, 50, 1)],
         ['Message', 'Yannis', '4', 'let me know if you nees something', datetime.datetime(2015, 1, 2, 2, 6, 41)],
         ['Message', 'Maria', '4', 'Thanks, really appreciated', datetime.datetime(2015, 1, 2, 2, 23, 21)],
         ['Message', 'Yannis', '4', 'no worries', datetime.datetime(2015, 1, 2, 2, 40, 1)],
         ['Message', 'Maria', '4', 'Can i join the uni', datetime.datetime(2015, 1, 2, 2, 40, 1)],
         ['Message', 'Yannis', '4', 'Whats your statement', datetime.datetime(2015, 1, 3, 6, 26, 41)]]

        result = self.parser.get_msg()
        self.assertEqual(msg, result)



