class Applicant:
    """Класс, представляющий соискателя работы."""

    def __init__(self, applicant_id, last_name, first_name, patronymic,
                 qualification, profession, extra_info=""):
        Applicant._validate_id(applicant_id)
        Applicant._validate_name(last_name, "last_name")
        Applicant._validate_name(first_name, "first_name")
        Applicant._validate_name(patronymic, "patronymic")
        Applicant._validate_non_empty_string(qualification, "qualification")
        Applicant._validate_non_empty_string(profession, "profession")
        Applicant._validate_string(extra_info, "extra_info")

        self._applicant_id = applicant_id
        self._last_name = last_name
        self._first_name = first_name
        self._patronymic = patronymic
        self._qualification = qualification
        self._profession = profession
        self._extra_info = extra_info

    # ------------------- статические методы валидации -------------------

    @staticmethod
    def _validate_id(value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("applicant_id должен быть положительным целым числом")

    @staticmethod
    def _validate_string(value, field_name):
        """Базовая проверка: значение должно быть строкой."""
        if not isinstance(value, str):
            raise ValueError(f"{field_name} должно быть строкой")

    @staticmethod
    def _validate_non_empty_string(value, field_name):
        """Проверка: значение — непустая строка (переиспользует _validate_string)."""
        Applicant._validate_string(value, field_name)
        if not value.strip():
            raise ValueError(f"{field_name} должно быть непустой строкой")

    @staticmethod
    def _validate_name(value, field_name):
        """Проверка ФИО: непустая строка из букв, пробелов и дефисов."""
        Applicant._validate_non_empty_string(value, field_name)
        if not all(ch.isalpha() or ch in "- " for ch in value):
            raise ValueError(f"{field_name} должно содержать только буквы, пробел или дефис")

    # ------------------- applicant_id -------------------
    @property
    def applicant_id(self):
        return self._applicant_id

    @applicant_id.setter
    def applicant_id(self, value):
        Applicant._validate_id(value)
        self._applicant_id = value

    # ------------------- last_name -------------------
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        Applicant._validate_name(value, "last_name")
        self._last_name = value

    # ------------------- first_name -------------------
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        Applicant._validate_name(value, "first_name")
        self._first_name = value

    # ------------------- patronymic -------------------
    @property
    def patronymic(self):
        return self._patronymic

    @patronymic.setter
    def patronymic(self, value):
        Applicant._validate_name(value, "patronymic")
        self._patronymic = value

    # ------------------- qualification -------------------
    @property
    def qualification(self):
        return self._qualification

    @qualification.setter
    def qualification(self, value):
        Applicant._validate_non_empty_string(value, "qualification")
        self._qualification = value

    # ------------------- profession -------------------
    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, value):
        Applicant._validate_non_empty_string(value, "profession")
        self._profession = value

    # ------------------- extra_info -------------------
    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, value):
        Applicant._validate_string(value, "extra_info")
        self._extra_info = value