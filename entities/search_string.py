from dataclasses import dataclass

@dataclass
class SearchInfo():
    search_string: str
    until_page: int
    start_page: int
