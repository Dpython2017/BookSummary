from parseFile import FileParser
import logging

logger = logging.getLogger()


class MessageManipulator(FileParser):
    def __init__(self):
        super().__init__()

    def is_applicant(self, user) -> bool:
        """
            Check if the user is a candidate
            :param user: username
            :type user:str
            :rtype: bool
        """
        users = self.get_user()
        if user in users:
            if users[user] is None:
                return True
        return False

    def is_mentor(self, user) -> bool:
        """
            Check if the user is a metor
            :param user: username
            :type user:str
            :rtype: bool
        """
        users = self.get_user()
        if user in users:
            if users[user] is not None:
                return True
        return False












    # def __applicant_list(self):
    #     """ Implementation creates a list of Applicants """
    #     for i in self.users:
    #         if i[3] == 'Applicant\n':
    #             self.applicant.update({i[1]: None})
    #     logger.info("Created applicant's list")
    #
    # def __mentor_list(self):
    #     """ Implementation creates a list of Mentors """
    #     for i in self.users:
    #         if i[3] == 'Mentor\n':
    #             self.mentor.update({i[1]: None})
    #
    #     logger.info("Created mentor's list")
    #
    # def __map_mentor(self):
    #     """ Implementation maps mentor to university """
    #     for user in self.users:
    #         if 'Mentor\n' in user:
    #             d = {
    #                 user[1]: user[2]
    #             }
    #             self.mentor_university.update(d)
    #
    #     logger.info("Created mentor's and university mapping")
    #
    # def __service(self):
    #     """ Utility that calls all implementations """
    #     logger.info("Initiating internal apis")
    #     self.__applicant_list()
    #     self.__mentor_list()
    #     self.__map_mentor()
    #
    # def is_applicant(self, user):
    #     return self.__is_applicant(user)
    #
    # def is_mentor(self, user):
    #     return self.__is_mentor(user)
    #
    # def __is_applicant(self, user):
    #     """
    #     Implementation that checks is user is an applicant
    #         :param user: username
    #         :type user: str
    #         :rtype: bool
    #     """
    #     if user in self.applicant:
    #         return True
    #     return False
    #
    # def __is_mentor(self, user):
    #     """
    #     Implementation that checks is user is mentor
    #         :param user: username
    #         :type user: str
    #         :rtype: bool
    #     """
    #     if user in self.mentor:
    #         return True
    #     return False
