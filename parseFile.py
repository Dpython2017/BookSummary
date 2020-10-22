import datetime
import logging

from utility import clean

logging.basicConfig(filename="file_manipulator.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class FileParser:
    """
        Implementation pre-processes the file data
        and creates the required Data Structures.
    """

    def __init__(self, filename='stream.txt'):
        """
        Initiates the file_parser implementation once the class is invoked.
        :param filename: filename
        """
        self.file_name = filename
        self._user = {}
        self._chat_groups = {}
        self._messages = []
        self.__file_parser()

    def __file_parser(self) -> None:
        """
         Iterates through the file object and creates mapping
         in the data.
        """
        try:
            file_obj = open(file=self.file_name, mode='r')
            for i in file_obj:
                field = i.split('|')

                if "Applicant\n" in field:
                    d = {
                        field[1]: None
                    }
                    self._user.update(d)
                if "Mentor\n" in field:
                    d = {
                        field[1]: field[2]
                    }
                    self._user.update(d)

                if 'ChatGroup' in field:
                    field[3] = clean(field[3])
                    d = {
                        int(field[1]): (field[2],
                                        field[3])
                    }

                    self._chat_groups.update(d)
                if 'Message' in field:
                    field[4] = clean(field[4])
                    field[4] = datetime.datetime.fromtimestamp(float(field[4]))
                    self._messages.append(field)
        except IOError:
            print("File not accessible")
            logger.error("File not Found")
        finally:
            file_obj.close()

    def get_user(self):
        return self._user

    def get_chat_groups(self):
        return self._chat_groups

    def get_msg(self):
        return self._messages























    #     self.file_obj = open('stream.txt', 'r')
    #
    #     self.mentor_university = {}
    #     self.applicant = {}
    #     self.mentor = {}
    #     self.file_obj = open('stream.txt', 'r')
    #     self.users = []
    #     self.chat_groups = {}
    #     self.messages = []
    #     self.__parse_file()
    #
    #
    #
    #
    # def __parse_file(self):
    #     """ Parsing file and creating individual """
    #     for obj in self.file_obj:
    #         field = obj.split('|')
    #         if field[0] == 'User':
    #             self.users.append(field)
    #         elif field[0] == 'ChatGroup':
    #             field[3] = clean(field[3])
    #             d = {
    #                 int(field[1]): [field[2],
    #                                 field[3]]
    #             }
    #             self.chat_groups.update(d)
    #         elif field[0] == 'Message':
    #             field[4] = clean(field[4])
    #             field[4] = datetime.datetime.fromtimestamp(float(field[4]))
    #             self.messages.append(field)
    #         else:
    #             logger.error("Unexpected data {}".format(field))






