import re


class Panda:
    """Panda which is user of :class:`PandaSocialNetwork` and has basic attributes as name,
    email, gender and list of friends"""

    def __init__(self, name, email, gender):
        self.validate_input(name, email, gender)
        self.panda_name = name
        self.panda_email = email
        self.panda_gender = gender
        self.friend_list = []

    def __str__(self):
        return "%s panda named %s with email: %s" % (self.panda_gender.capitalize(), self.panda_name, self.panda_email)

    def __eq__(self, other):
        if isinstance(other, Panda):
            return self.__key() == other.__key()
        raise NotImplemented

    def __hash__(self):
        return hash(self.__key())

    def __key(self):
        return self.panda_name, self.panda_email, self.panda_gender

    def validate_input(self, name, email, gender):
        if not name or not email or not gender:
            raise ValueError("Input not provided")
        if not self.is_valid_email(email):
            raise ValueError("Not valid email provided")

    @staticmethod
    def is_valid_email(email):
        email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        return re.search(email_regex, email)

    def name(self):
        return self.panda_name

    def email(self):
        return self.panda_email

    def gender(self):
        return self.panda_gender

    def is_male(self):
        return self.panda_gender == "male"

    def is_female(self):
        return self.panda_gender == "female"

    def add_friend(self, panda):
        self.friend_list.append(panda)

    def friends(self):
        return self.friend_list


class PandaSocialNetwork:
    """ Social network that can handle: adding of new :class:`Panda` users, making pandas friends,
    checking connection level between pandas, checking how many pandas with specified gender
    exist in pandas network"""

    def __init__(self):
        self.network = []

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise PandaAlreadyThere()
        self.network.append(panda)

    def has_panda(self, panda):
        return panda in self.network

    def make_friends(self, panda1, panda2):
        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends
        self.add_pandas_to_network_if_absent(panda1, panda2)
        panda1.add_friend(panda2)
        panda2.add_friend(panda1)

    def add_pandas_to_network_if_absent(self, panda1, panda2):
        if panda1 not in self.network:
            self.add_panda(panda1)
        if panda2 not in self.network:
            self.add_panda(panda2)

    @staticmethod
    def are_friends(panda1, panda2):
        if not panda1.friends() or not panda2.friends():
            return False
        return panda1 in panda2.friends() and panda2 in panda1.friends()

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False
        return panda.friends()

    def connection_level(self, panda1, panda2):
        if not self.has_panda(panda1) or not self.has_panda(panda1):
            return False
        if not panda1.friends():
            return -1
        checked_pandas = []
        return self.__calculate_connection_level(checked_pandas, panda1, panda2)

    def __calculate_connection_level(self, checked_pandas, panda1, panda2, count=0):
        count += 1
        self.update_checked_pandas(checked_pandas, panda1)
        if self.are_friends(panda1, panda2):
            return count
        for panda in self.friends_of(panda1):
            if panda in checked_pandas:
                continue
            return self.__calculate_connection_level(checked_pandas, panda, panda2, count)
        return -1

    @staticmethod
    def update_checked_pandas(checked_pandas, panda):
        if panda not in checked_pandas:
            checked_pandas.append(panda)

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) > 0

    def how_many_gender_in_network(self, level, panda, gender, count=0, current_level=0, checked_pandas=None):
        if current_level == 0 and checked_pandas is None:
            checked_pandas = list()
            self.update_checked_pandas(checked_pandas, panda)
        if panda not in checked_pandas and panda.gender() == gender:
            count += 1
            self.update_checked_pandas(checked_pandas, panda)
        if current_level == level:
            return count
        current_level += 1
        for panda_friend in self.friends_of(panda):
            if panda_friend in checked_pandas:
                continue
            count = self.how_many_gender_in_network(level, panda_friend, gender, count, current_level, checked_pandas)
        return count


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass
