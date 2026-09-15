class Applicant:
    """Класс, представляющий соискателя работы."""

    def __init__(self, applicant_id, last_name, first_name, patronymic,
                 qualification, profession, extra_info=""):
        self._applicant_id = applicant_id
        self._last_name = last_name
        self._first_name = first_name
        self._patronymic = patronymic
        self._qualification = qualification
        self._profession = profession
        self._extra_info = extra_info

    # --- applicant_id ---
    @property
    def applicant_id(self):
        return self._applicant_id

    @applicant_id.setter
    def applicant_id(self, value):
        self._applicant_id = value

    # --- last_name ---
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    # --- first_name ---
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    # --- patronymic ---
    @property
    def patronymic(self):
        return self._patronymic

    @patronymic.setter
    def patronymic(self, value):
        self._patronymic = value

    # --- qualification ---
    @property
    def qualification(self):
        return self._qualification

    @qualification.setter
    def qualification(self, value):
        self._qualification = value

    # --- profession ---
    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, value):
        self._profession = value

    # --- extra_info ---
    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, value):
        self._extra_info = value