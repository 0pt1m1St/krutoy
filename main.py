import json
import re


class ApplicantShort:
    """Базовый класс: краткая версия данных соискателя.
    Фамилия И.О., профессия и один контакт (телефон)."""

    def __init__(self, applicant_id, last_name, first_name, patronymic,
                 profession, phone_number):
        ApplicantShort._validate_id(applicant_id)
        ApplicantShort._validate_name(last_name, "last_name")
        ApplicantShort._validate_name(first_name, "first_name")
        ApplicantShort._validate_name(patronymic, "patronymic")
        ApplicantShort._validate_non_empty_string(profession, "profession")
        ApplicantShort._validate_phone(phone_number)

        self._applicant_id = applicant_id
        self._last_name = last_name
        self._first_name = first_name
        self._patronymic = patronymic
        self._profession = profession
        self._phone_number = phone_number

    # ------------------- статические методы валидации (общие для всей иерархии) -------------------

    @staticmethod
    def _validate_id(value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("applicant_id должен быть положительным целым числом")

    @staticmethod
    def _validate_string(value, field_name):
        if not isinstance(value, str):
            raise ValueError(f"{field_name} должно быть строкой")

    @staticmethod
    def _validate_non_empty_string(value, field_name):
        ApplicantShort._validate_string(value, field_name)
        if not value.strip():
            raise ValueError(f"{field_name} должно быть непустой строкой")

    @staticmethod
    def _validate_name(value, field_name):
        ApplicantShort._validate_non_empty_string(value, field_name)
        if not all(ch.isalpha() or ch in "- " for ch in value):
            raise ValueError(f"{field_name} должно содержать только буквы, пробел или дефис")

    @staticmethod
    def _validate_phone(value):
        ApplicantShort._validate_non_empty_string(value, "phone_number")
        cleaned = re.sub(r"[\s\-()]", "", value)
        if not re.fullmatch(r"(\+7|8|7)\d{10}", cleaned):
            raise ValueError(
                "phone_number должен быть в формате +7XXXXXXXXXX или 8XXXXXXXXXX "
                "(10 цифр после кода страны/8)"
            )

    # ------------------- applicant_id -------------------
    @property
    def applicant_id(self):
        return self._applicant_id

    @applicant_id.setter
    def applicant_id(self, value):
        ApplicantShort._validate_id(value)
        self._applicant_id = value

    # ------------------- last_name -------------------
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        ApplicantShort._validate_name(value, "last_name")
        self._last_name = value

    # ------------------- first_name -------------------
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        ApplicantShort._validate_name(value, "first_name")
        self._first_name = value

    # ------------------- patronymic -------------------
    @property
    def patronymic(self):
        return self._patronymic

    @patronymic.setter
    def patronymic(self, value):
        ApplicantShort._validate_name(value, "patronymic")
        self._patronymic = value

    # ------------------- profession -------------------
    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, value):
        ApplicantShort._validate_non_empty_string(value, "profession")
        self._profession = value

    # ------------------- phone_number -------------------
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        ApplicantShort._validate_phone(value)
        self._phone_number = value

    # ------------------- вывод и сравнение -------------------

    def short_info(self) -> str:
        initials = f"{self._first_name[0]}.{self._patronymic[0]}."
        return f"{self._last_name} {initials}, {self._profession}, {self._phone_number}"

    def __str__(self) -> str:
        return self.short_info()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(applicant_id={self._applicant_id!r}, "
            f"last_name={self._last_name!r}, first_name={self._first_name!r}, "
            f"patronymic={self._patronymic!r}, profession={self._profession!r}, "
            f"phone_number={self._phone_number!r})"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, ApplicantShort):
            return NotImplemented
        return (
            self._applicant_id == other._applicant_id
            and self._last_name == other._last_name
            and self._first_name == other._first_name
            and self._patronymic == other._patronymic
            and self._profession == other._profession
            and self._phone_number == other._phone_number
        )


class Applicant(ApplicantShort):
    """Полная версия данных соискателя: наследует ApplicantShort,
    добавляет квалификацию и доп. информацию."""

    def __init__(self, *args, **kwargs):
        # --- Вариант 1: один аргумент - строка (обычная строка или JSON-строка) ---
        if len(args) == 1 and isinstance(args[0], str):
            data = self._parse_string_or_json(args[0])
            self._init_from_dict(data)

        # --- Вариант 2: один аргумент - словарь ---
        elif len(args) == 1 and isinstance(args[0], dict):
            self._init_from_dict(args[0])

        # --- Вариант 3: обычные позиционные/именованные аргументы полей ---
        else:
            self._init_from_fields(*args, **kwargs)

    # ------------------- разбор входных данных -------------------

    @staticmethod
    def _parse_string_or_json(text: str) -> dict:
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            parts = [p.strip() for p in text.split(";")]
            if len(parts) < 7:
                raise ValueError(
                    "Строка должна содержать минимум 7 полей через ';': "
                    "id;фамилия;имя;отчество;квалификация;профессия;телефон[;доп.инфо]"
                )
            return {
                "applicant_id": int(parts[0]),
                "last_name": parts[1],
                "first_name": parts[2],
                "patronymic": parts[3],
                "qualification": parts[4],
                "profession": parts[5],
                "phone_number": parts[6],
                "extra_info": parts[7] if len(parts) > 7 else "",
            }

    def _init_from_dict(self, data: dict):
        try:
            self._init_from_fields(
                applicant_id=data["applicant_id"],
                last_name=data["last_name"],
                first_name=data["first_name"],
                patronymic=data["patronymic"],
                qualification=data["qualification"],
                profession=data["profession"],
                phone_number=data["phone_number"],
                extra_info=data.get("extra_info", ""),
            )
        except KeyError as e:
            raise ValueError(f"Отсутствует обязательное поле: {e}")

    def _init_from_fields(self, applicant_id, last_name, first_name, patronymic,
                           qualification, profession, phone_number, extra_info=""):
        # общие поля и их валидация делегированы базовому классу - без повтора кода
        super().__init__(applicant_id, last_name, first_name, patronymic,
                          profession, phone_number)

        Applicant._validate_non_empty_string(qualification, "qualification")
        Applicant._validate_string(extra_info, "extra_info")

        self._qualification = qualification
        self._extra_info = extra_info

    # ------------------- qualification -------------------
    @property
    def qualification(self):
        return self._qualification

    @qualification.setter
    def qualification(self, value):
        Applicant._validate_non_empty_string(value, "qualification")
        self._qualification = value

    # ------------------- extra_info -------------------
    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, value):
        Applicant._validate_string(value, "extra_info")
        self._extra_info = value

    # ------------------- вывод и сравнение (переопределены) -------------------

    def full_info(self) -> str:
        """Полная версия - переиспользует short_info() базового класса."""
        return (
            f"Соискатель #{self._applicant_id}: "
            f"{self._last_name} {self._first_name} {self._patronymic}, "
            f"квалификация: {self._qualification}, "
            f"профессия: {self._profession}, "
            f"телефон: {self._phone_number}, "
            f"доп. информация: {self._extra_info or '-'}"
        )

    def __str__(self) -> str:
        """Переопределяем: полная версия вместо краткой из базового класса."""
        return self.full_info()

    def __repr__(self) -> str:
        """Переопределяем repr базового класса, добавляя свои поля."""
        base_repr = super().__repr__()[:-1]  # убираем закрывающую скобку базового repr
        return f"{base_repr}, qualification={self._qualification!r}, extra_info={self._extra_info!r})"

    def __eq__(self, other) -> bool:
        """Сначала проверяем равенство общих полей через базовый класс,
        затем - собственные поля."""
        if not isinstance(other, Applicant):
            return NotImplemented
        return (
            super().__eq__(other)
            and self._qualification == other._qualification
            and self._extra_info == other._extra_info
        )