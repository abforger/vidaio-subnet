from pydantic import BaseModel, Field


class BandwidthConfig(BaseModel):
    total_requests: int = Field(default=64)
    request_interval: int = Field(default=500)
    requests_per_synthetic_interval: int = Field(default=5)
    requests_per_organic_interval: int = Field(default = 10)
    min_stake: int = Field(default=25000)
