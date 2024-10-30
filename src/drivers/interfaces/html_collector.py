from abc import ABC, abstractmethod
from typing import List, Dict

class HtmlCollectorInterface:
    
    """No more an abstract class method, so we use self instead of cls"""
    @abstractmethod
    def collect_essential_information(self, html:str) -> List[Dict[str, str]]:
        pass