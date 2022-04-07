class MifareClassic1k:
    """A class to represent a Mifare Classic 1k tag.

    Attributes:
        uid (str): String that contains the UID.
        atqa (str): String that contains the ATQA.
        sak (str): String that contains the SAK.
        blocks (dict): Dictionary that contains the blocks of memory.
        sector_keys (dict): Dictionary that contains the sector_keys.
        date (datetime.datetime): Date and time when the tag was saved.
        files (dict): Dictionary with the name of the files that contain the information of the tag.
        name (str): Custom name given to the tag.

    Methods:
        get_details_short()

    """

    def __init__(self, uid: str, atqa, sak, blocks, sector_keys, date, files, name=""):
        self.uid = uid
        self.atqa = atqa
        self.sak = sak
        self.blocks = blocks
        self.sector_keys = sector_keys
        self.date = date
        self.files = files
        self.__name = name

    def __repr__(self):
        return f"MifareClassic1k(uid={self.uid}, atqa={self.atqa}, sak={self.atqa}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def details_short(self) -> str:
        """Returns a string containing a few details of the tag.

        Returns:
            details (str): String that contains the details.

        """

        formatted_date = self.date.strftime("%d-%m-%Y %H:%M:%S")
        details = f"    Date: {formatted_date}\n    UID: {self.uid}"
        return details

    @property
    def details_long(self) -> str:
        """Returns a string containing many details of the tag.

            Returns:
                details (str): String that contains the details.

        """

        line = " ---------------------------------------"
        details = f"UID: {self.uid}\nATQA: {self.atqa}\nSAK: {self.sak}\n\nMemory:\n{line}\n"
        for n in range(64):
            details += f"| {str(n).rjust(2, ' ')} | {self.blocks[str(n)]} |\n"
            if (n+1)%4 == 0:
                details += f"{line}\n"
        return details
