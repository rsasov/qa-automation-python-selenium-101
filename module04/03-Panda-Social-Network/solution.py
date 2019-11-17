import re


class Panda:
    """Panda which is user of :class:`PandaSocialNetwork` and has basic attributes as name,
    email, gender and list of friends"""

    def __init__(self, name, email, gender):
        self._validate_input(name, email, gender)
        self.panda_name = name
        self.panda_email = email
        self.panda_gender = gender

    def __str__(self):
        return "%s panda named %s with email: %s" % (self.panda_gender.capitalize(), self.panda_name, self.panda_email)

    def __eq__(self, other):
        if isinstance(other, Panda):
            return self._key() == other._key()
        return False

    def __hash__(self):
        return hash(self._key())

    def _key(self):
        return self.panda_name, self.panda_email, self.panda_gender

    def _validate_input(self, name, email, gender):
        if not name or not email or not gender:
            raise ValueError("Input not provided")
        if not self._is_valid_email(email):
            raise ValueError("Not valid email provided")

    @staticmethod
    def _is_valid_email(email):
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


class PandaSocialNetwork:
    """ Social network that can handle: adding of new :class:`Panda` users, making pandas friends,
    checking connection level between pandas, checking how many pandas with specified gender
    exist in pandas network"""

    def __init__(self):
        self.network = {}

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise PandaAlreadyThere()
        network_entry = {panda: list()}
        self.network.update(network_entry)

    def has_panda(self, panda):
        return panda in self.network

    def make_friends(self, panda1, panda2):
        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends()
        self._assure_network_presence(panda1, panda2)
        self.add_friend(panda2, panda1)
        self.add_friend(panda1, panda2)

    def add_friend(self, panda, friend):
        friends = self.network.get(panda)
        friends.append(friend)
        updated_entry = {panda: friends}
        self.network.update(updated_entry)

    def _assure_network_presence(self, panda1, panda2):
        if panda1 not in self.network:
            self.add_panda(panda1)
        if panda2 not in self.network:
            self.add_panda(panda2)

    def are_friends(self, panda1, panda2):
        panda1_friends = self.network.get(panda1)
        panda2_friends = self.network.get(panda2)
        if not panda1_friends or not panda2_friends:
            return False
        return panda1 in panda2_friends and panda2 in panda1_friends

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False
        return self.network.get(panda)

    def connection_level(self, panda1, panda2):
        if not self.has_panda(panda1) or not self.has_panda(panda1):
            return False
        if not self.network.get(panda1):
            return -1
        checked_pandas = []
        return self._calculate_connection_level(checked_pandas, panda1, panda2)

    def _calculate_connection_level(self, checked_pandas, panda1, panda2, count=0):
        count += 1
        self._update_checked_pandas(checked_pandas, panda1)
        if self.are_friends(panda1, panda2):
            return count
        for panda in self.friends_of(panda1):
            if panda not in checked_pandas:
                return self._calculate_connection_level(checked_pandas, panda, panda2, count)
        return -1

    @staticmethod
    def _update_checked_pandas(checked_pandas, panda):
        if panda not in checked_pandas:
            checked_pandas.append(panda)

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) > 0

    def how_many_gender_in_network(self, level, panda, gender, count=0, current_level=0, checked_pandas=None):
        if current_level == 0 and checked_pandas is None:
            checked_pandas = list()
            self._update_checked_pandas(checked_pandas, panda)
        if panda not in checked_pandas and panda.gender() == gender:
            count += 1
            self._update_checked_pandas(checked_pandas, panda)
        if current_level == level:
            return count
        current_level += 1
        for panda_friend in self.friends_of(panda):
            if panda_friend not in checked_pandas:
                count = self.how_many_gender_in_network(level, panda_friend, gender, count, current_level, checked_pandas)
        return count


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass
