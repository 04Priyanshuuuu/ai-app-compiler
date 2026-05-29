from pydantic import BaseModel
from typing import Dict, Any


class AppSchema(BaseModel):

    ui: Dict[str, Any]

    api: Dict[str, Any]

    database: Dict[str, Any]

    auth: Dict[str, Any]

    business_logic: Dict[str, Any]