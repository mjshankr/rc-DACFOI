import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SCHOOLS_TO_SCRAPE = ["SEAS"]

SCHOOL_DEPARTMENT_DATA = {
    "SEAS": {
        "base_url": "https://engineering.virginia.edu",
        "departments": {
            "Biomedical Engineering": {
                "people_url": "https://engineering.virginia.edu/department/biomedical-engineering/people?keyword=&position=2&impact_area=All&research_area=All",
            },
            "Chemical Engineering": {
                "people_url": "https://engineering.virginia.edu/department/chemical-engineering/people?keyword=&position=2&impact_area=All&research_area=All",
            },
            "Civil and Environmental Engineering": {
                "people_url": "https://engineering.virginia.edu/department/civil-and-environmental-engineering/people?keyword=&position=2&impact_area=All&research_area=All",
            },
            "Computer Engineering": {
                "people_url": "https://engineering.virginia.edu/department/civil-and-environmental-engineering/people?keyword=&position=2&impact_area=All&research_area=All",
            },
            "Computer Science": {
                "people_url": "https://engineering.virginia.edu/department/computer-science/people?keyword=&position=2&impact_area=All&research_area=All"
            },
            "Electrical and Computer Engineering": {
                "people_url": "https://engineering.virginia.edu/department/electrical-and-computer-engineering/faculty?keyword=&position=2&impact_area=All&research_area=All"
            },
            "Engineering and Society": {
                "people_url": "https://engineering.virginia.edu/department/engineering-and-society/people?keyword=&position=2&impact_area=All&research_area=All",
            },
            "Materials Science and Engineering": {
                "people_url": "https://engineering.virginia.edu/department/materials-science-and-engineering/people?impact_area=All&keyword=&position=2&research_area=All",
            },
            "Mechanical and Aerospace Engineering": {
                "people_url": "https://engineering.virginia.edu/department/mechanical-and-aerospace-engineering/people?keyword=&position=2&impact_area=All&research_area=All"
            },
            "Systems and Information Engineering": {
                "people_url": "https://engineering.virginia.edu/department/systems-and-information-engineering/people?keyword=&position=2&impact_area=All&research_area=All",
            },
        },
    },
}

DEFAULT_FISCAL_YEARS = [2020 + i for i in range(6)]

NIH_REPORTER_PAYLOAD = {
    "criteria": {
        "use_relevance": True,
        "fiscal_years": [],
        "include_active_projects": True,
        "pi_names": [
            {
                "first_name": "",
                "last_name": "",
            }
        ],
        "org_names": [
            "UNIVERSITY OF VIRGINIA",
            "University of Virginia"
        ],
    },
}

OPENAI_CONFIG = {
    "EMBEDDING_MODEL": "text-embedding-ada-002",
    "MAX_TOKENS": 8192,
    "EMBEDDING_DIMENSIONS": 1536,
}

INDEX_PATH = os.path.join(BASE_DIR, "../../instance/index.faiss")