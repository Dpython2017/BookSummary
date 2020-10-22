from message_reader import MessageManipulator
from utility import difference, average
import logging

logger = logging.getLogger()


class UniversityResponse(MessageManipulator):
    def __init__(self):
        super().__init__()
        self.cache = {}

    def response_time(self) -> dict:
        """
        Calculates the average response time per college
            :return: dictionary of university and average time mapping
            :rtype: dict
        """
        response = {}
        university_response = {}
        # Calling private member data from the parent class
        messages = self.get_msg()
        chat_groups = self.get_chat_groups()
        user = self.get_user()

        for msg in range(len(messages)):
            # checks for the current and next message if first user is
            # applicant and another is mentor then the difference of the time stamp is
            # calculated.
            c_id = messages[msg][2]
            mentor = chat_groups[int(c_id)][1]

            if self.is_applicant(messages[msg][1]):
                if self.is_applicant(messages[msg + 1][1]):
                    logger.info('Both are applicants')
                    pass
                if self.is_mentor(mentor):
                    diff = difference(messages[msg][4], messages[msg + 1][4])
                    if user[mentor] not in response:
                        response[user[mentor]] = []
                    response[user[mentor]].append(diff)

        for i in response:
            avg = average(response[i])
            university_response.update({i: avg})
            print("Average response time for university ({}) is: {}".format(i, avg))
            logger.info("Average response time for university ({}) is: {}".format(i, avg))

        return university_response

